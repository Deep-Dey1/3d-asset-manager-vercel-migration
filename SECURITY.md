# Security Guidelines

## Environment Variables Protection

### ✅ What's Protected
- All sensitive data is stored in environment variables
- `.env` files are in `.gitignore` 
- Example files only contain placeholder values
- Production secrets are set in Vercel dashboard

### 🔒 Critical Environment Variables

| Variable | Description | Security Level |
|----------|-------------|----------------|
| `MONGODB_URI` | Database connection string with credentials | **CRITICAL** |
| `SECRET_KEY` | Flask session encryption key | **CRITICAL** |
| `FLASK_ENV` | Application environment | Medium |

### 🚨 Never Commit These
- `.env` files
- Database passwords
- API keys
- Secret keys
- Connection strings with credentials

### ✅ Safe to Commit
- `.env.example` with placeholder values
- Documentation with example formats
- Configuration templates

## Setting Up Environment Variables

### Local Development
1. Copy the example file:
   ```bash
   cp .env.example .env
   ```
2. Fill in your actual values in `.env`
3. Never commit the `.env` file

### Production (Vercel)
1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add each variable individually
3. Use "Production" environment for live deployment

## MongoDB Security

### Database Access
- Enable IP allowlisting in MongoDB Atlas
- Use strong passwords (12+ characters)
- URL-encode special characters in connection strings
- Rotate credentials regularly

### Network Security
- Restrict database access to specific IPs when possible
- Use MongoDB Atlas security features
- Enable audit logging for production

## Flask Security

### Secret Key
- Generate random 32+ character secret keys
- Use different keys for development/production
- Rotate keys periodically

Example generation:
```python
import secrets
print(secrets.token_hex(32))
```

### Session Security
- Set secure cookie flags in production
- Use HTTPS for all production traffic
- Implement proper session timeout

## Best Practices

### Development
- Use `.env.example` for documentation
- Never hardcode credentials in source code
- Use environment-specific configurations
- Test with dummy data when possible

### Production
- Set environment variables through hosting platform
- Enable all security headers
- Use HTTPS exclusively
- Monitor for security vulnerabilities
- Regular security audits

### Version Control
- Always use `.gitignore` for sensitive files
- Review commits for accidental credential exposure
- Use commit hooks to prevent sensitive data commits
- Consider using git-secrets or similar tools

## Incident Response

If credentials are accidentally committed:
1. **Immediately** rotate all exposed credentials
2. Force push to remove from history if recent
3. Check logs for any unauthorized access
4. Update documentation and team
5. Review security practices

## Contact

For security issues or questions, please review this documentation first, then consult with your development team.
