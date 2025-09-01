from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from app.models import Model3D, User
from werkzeug.utils import secure_filename
import io
from bson.objectid import ObjectId

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    try:
        print("🔄 Loading homepage...")
        
        # Get recent public models
        recent_models, total_public = Model3D.get_public_models(page=1, per_page=6)
        
        print(f"📋 Found {total_public} public models for homepage")
        for i, model in enumerate(recent_models[:3]):
            print(f"   Recent Model {i+1}: {model.name} (Public: {model.is_public})")
        
        # Get statistics
        stats = Model3D.get_stats()
        print(f"📊 Stats: {stats}")
        
        return render_template('index.html', 
                             recent_models=recent_models,
                             total_models=stats['public_models'],
                             total_users=stats['total_users'],
                             total_downloads=stats['total_downloads'])
    except Exception as e:
        print(f"Index page error: {e}")
        import traceback
        traceback.print_exc()
        # Fallback values if database query fails
        return render_template('index.html', 
                             recent_models=[],
                             total_models=0,
                             total_users=0,
                             total_downloads=0)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    try:
        print(f"🔄 Dashboard for user: {current_user.id} ({current_user.username})")
        
        user_models, total_user_models = Model3D.get_user_models(current_user.id, page=1, per_page=10)
        
        print(f"📋 Found {total_user_models} models for user {current_user.id}")
        for i, model in enumerate(user_models[:3]):
            print(f"   Model {i+1}: {model.name} (Public: {model.is_public})")
        
        # Calculate user stats
        total_downloads = sum(model.download_count for model in user_models)
        public_models = sum(1 for model in user_models if model.is_public)
        
        return render_template('dashboard.html', 
                             user_models=user_models,
                             total_models=total_user_models,
                             total_downloads=total_downloads,
                             public_models=public_models)
    except Exception as e:
        print(f"Dashboard error: {e}")
        import traceback
        traceback.print_exc()
        return render_template('dashboard.html', 
                             user_models=[],
                             total_models=0,
                             total_downloads=0,
                             public_models=0,
                             error=str(e))

@main_bp.route('/browse')
def browse():
    """Browse public models"""
    try:
        print("🔄 Loading browse page...")
        
        search = request.args.get('search', '').strip()
        page = request.args.get('page', 1, type=int)
        
        print(f"📋 Browse params - Page: {page}, Search: '{search}'")
        
        # Get public models with pagination
        models, total = Model3D.get_public_models(page=page, per_page=12, search=search if search else None)
        
        print(f"📋 Found {total} public models")
        for i, model in enumerate(models[:3]):
            print(f"   Public Model {i+1}: {model.name} (ID: {model.id})")
        
        # Calculate pagination info
        total_pages = (total + 11) // 12  # Ceiling division
        has_prev = page > 1
        has_next = page < total_pages
        
        # Create pagination object-like structure
        class Pagination:
            def __init__(self, items, total, page, per_page):
                self.items = items
                self.total = total
                self.page = page
                self.per_page = per_page
                self.pages = (total + per_page - 1) // per_page
                self.has_prev = page > 1
                self.has_next = page < self.pages
                self.prev_num = page - 1 if self.has_prev else None
                self.next_num = page + 1 if self.has_next else None
        
        pagination = Pagination(models, total, page, 12)
        
        return render_template('browse.html', models=pagination, search=search)
        
    except Exception as e:
        print(f"❌ Browse error: {e}")
        import traceback
        traceback.print_exc()
        # Return empty pagination on error
        class EmptyPagination:
            items = []
            total = 0
            pages = 0
            page = 1
            has_prev = False
            has_next = False
            prev_num = None
            next_num = None
        
        return render_template('browse.html', models=EmptyPagination(), search='')

@main_bp.route('/model/<model_id>')
def model_detail(model_id):
    """View model details"""
    try:
        print(f"🔄 Loading model detail for ID: {model_id}")
        
        model = Model3D.get_by_id(model_id)
        if not model:
            print(f"❌ Model not found: {model_id}")
            flash('Model not found.', 'error')
            return redirect(url_for('main.browse'))
        
        print(f"✅ Model found: {model.name} (Public: {model.is_public})")
        
        # Check access permissions
        if not model.is_public:
            if not current_user.is_authenticated or model.user_id != current_user.id:
                print(f"❌ Access denied for model: {model_id}")
                flash('You do not have permission to view this model.', 'error')
                return redirect(url_for('main.browse'))
        
        # Get model owner info
        owner = User.get_by_id(model.user_id)
        print(f"✅ Owner found: {owner.username if owner else 'Unknown'}")
        
        return render_template('model_detail.html', model=model, owner=owner)
        
    except Exception as e:
        print(f"❌ Model detail error: {e}")
        import traceback
        traceback.print_exc()
        flash('Error loading model details.', 'error')
        return redirect(url_for('main.browse'))

@main_bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    """Upload 3D model"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name', '').strip()
            description = request.form.get('description', '').strip()
            is_public = request.form.get('is_public') == 'on'
            
            # Get uploaded file
            file = request.files.get('file')
            
            if not file or file.filename == '':
                flash('Please select a file to upload.', 'error')
                return render_template('upload.html')
            
            if not name:
                flash('Please provide a name for your model.', 'error')
                return render_template('upload.html')
            
            # Validate file extension
            filename = secure_filename(file.filename)
            file_extension = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
            
            allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']
            if file_extension not in allowed_extensions:
                flash(f'File type not supported. Allowed: {", ".join(allowed_extensions)}', 'error')
                return render_template('upload.html')
            
            # Read file content
            file_content = file.read()
            file_size = len(file_content)
            
            # Check file size (100MB limit)
            if file_size > current_app.config['MAX_CONTENT_LENGTH']:
                flash('File too large. Maximum size is 100MB.', 'error')
                return render_template('upload.html')
            
            # Store file in GridFS
            fs = current_app.config['GRIDFS']
            gridfs_file_id = fs.put(
                file_content,
                filename=filename,
                content_type=file.content_type,
                metadata={
                    'original_filename': file.filename,
                    'uploaded_by': current_user.id,
                    'upload_date': Model3D().upload_date
                }
            )
            
            # Create model record
            model = Model3D(
                name=name,
                description=description,
                file_format=file_extension,
                file_size=file_size,
                original_filename=file.filename,
                user_id=current_user.id,
                is_public=is_public,
                gridfs_file_id=str(gridfs_file_id)
            )
            
            model.save()
            
            flash(f'Model "{name}" uploaded successfully!', 'success')
            return redirect(url_for('main.model_detail', model_id=model.id))
            
        except Exception as e:
            print(f"Upload error: {e}")
            flash('Upload failed. Please try again.', 'error')
            return render_template('upload.html')
    
    return render_template('upload.html')

@main_bp.route('/profile')
@login_required
def profile():
    """User profile page"""
    try:
        user_models, total = Model3D.get_user_models(current_user.id)
        stats = {
            'total_models': total,
            'public_models': sum(1 for model in user_models if model.is_public),
            'total_downloads': sum(model.download_count for model in user_models)
        }
        
        return render_template('profile.html', user=current_user, stats=stats)
        
    except Exception as e:
        print(f"Profile error: {e}")
        return render_template('profile.html', user=current_user, stats={
            'total_models': 0,
            'public_models': 0,
            'total_downloads': 0
        })
