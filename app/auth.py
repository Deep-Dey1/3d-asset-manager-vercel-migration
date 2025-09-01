from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if not all([username, email, password]):
            flash('All fields are required.', 'error')
            return render_template('auth/register.html')
        
        # Check if user already exists
        if User.get_by_username(username):
            flash('Username already exists.', 'error')
            return render_template('auth/register.html')
        
        if User.get_by_email(email):
            flash('Email already registered.', 'error')
            return render_template('auth/register.html')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        try:
            user.save()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            print(f"Registration error: {e}")
            flash('Registration failed. Please try again.', 'error')
            return render_template('auth/register.html')
    
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_field = request.form.get('login_field')  # Updated to match template
        password = request.form.get('password')
        
        if not all([login_field, password]):
            flash('Please provide login credentials.', 'error')
            return render_template('auth/login.html')
        
        # Try to find user by username first, then email
        user = User.get_by_username(login_field)
        if not user:
            user = User.get_by_email(login_field)
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Invalid credentials.', 'error')
            return render_template('auth/login.html')
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
