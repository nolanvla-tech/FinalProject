# Nolan La - Portfolio Website

A professional portfolio website built with Django showcasing projects, skills, experience, and professional background.

## Features

- **Professional Portfolio**: Showcase your projects with detailed descriptions
- **Skills Management**: Organize technical, business, soft skills, and languages
- **Experience Timeline**: Display work history, education, and leadership roles
- **Project Showcase**: Individual project pages with full details
- **Contact Form**: Easy way for visitors to get in touch
- **Responsive Design**: Beautiful white professional theme with blue accents
- **Admin Interface**: Easy content management through Django admin

## Live Demo

Visit the website at: [Your Render URL will go here]

## Project Pages

- **Home**: Hero section with featured projects
- **About**: Professional bio and experience timeline  
- **Projects**: Gallery of all projects with category filtering
- **Project Detail**: Individual project showcase pages
- **Skills**: Organized skills by category
- **Resume**: Education, work experience, and leadership
- **Contact**: Contact form and information

## Technology Stack

- **Backend**: Django 6.0.4
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3
- **Image Processing**: Pillow
- **Deployment**: Gunicorn + Render

## Local Development

### Prerequisites

- Python 3.11+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser (admin):
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000/ in your browser

### Accessing Admin Panel

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Add/edit projects, skills, experiences, and site profile information

## Database Setup

### Populate Initial Data

Run the population script to add initial projects, skills, and experiences:

```bash
python populate_db.py
```

### Manual Setup via Admin

1. Create Site Profile: Add your name, bio, contact info, and profile picture
2. Add Projects: Create projects with details, images, and links
3. Add Skills: Organize skills by category and proficiency level
4. Add Experiences: Add education, work history, and leadership roles

## Project Structure

```
PortfolioProject/
├── ai_portfolio/           # Django settings & configuration
│   ├── settings.py         # Django configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── projects/               # Main app
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Admin customization
│   └── templates/         # HTML templates
├── media/                  # User uploaded files
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment configuration
└── runtime.txt            # Python version
```

## Deployment to Render

### Prerequisites

- GitHub account with repository created and code pushed
- Render account (free tier available at render.com)

### Deployment Steps

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub account

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository

3. **Configure Service**
   - **Name**: `nolan-portfolio` (or your preferred name)
   - **Environment**: Select Python 3.11
   - **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input`
   - **Start Command**: `gunicorn ai_portfolio.wsgi`

4. **Set Environment Variables**
   - Click "Environment"
   - Add the following variables:
     ```
     DEBUG=False
     ALLOWED_HOSTS=yourdomain.onrender.com
     SECRET_KEY=your-secret-key-here
     ```

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy your application
   - Your site will be live at: `https://yourdomain.onrender.com`

### Production Settings

Update `ai_portfolio/settings.py` for production:

```python
# Set DEBUG to False
DEBUG = False

# Add your Render domain
ALLOWED_HOSTS = ['yourdomain.onrender.com']

# Use environment variables
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

### Database Migration on Deploy

Render automatically runs the build command which includes:
- Installing dependencies
- Running migrations
- Collecting static files

After first deploy, populate data:
1. SSH into Render service
2. Run: `python manage.py shell < populate_db.py`
3. Or add data through Django admin

## Custom Domain

1. Go to your Render service settings
2. Click "Custom Domain"
3. Enter your domain (e.g., nolanla.com)
4. Follow DNS configuration instructions
5. Point domain nameservers to Render

## Environment Variables

Create `.env` file locally (not committed to git):

```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Troubleshooting

### Static Files Not Displaying
- Ensure `STATIC_URL` and `STATIC_ROOT` are configured in settings.py
- Run `python manage.py collectstatic` locally
- Check Render logs for errors

### Database Issues
- Verify migrations ran: `python manage.py migrate`
- Check database is accessible from Render environment
- Use PostgreSQL for production (more reliable than SQLite)

### Image Upload Issues
- Ensure `media/` directory exists
- Check file permissions
- Verify `MEDIA_URL` and `MEDIA_ROOT` settings

## Support & Contribution

For issues or improvements, please:
1. Check existing issues
2. Create new issue with detailed description
3. Submit pull requests for improvements

## License

This project is open source and available under the MIT License.

## Contact

- **Email**: nolan_la1@baylor.edu
- **LinkedIn**: https://linkedin.com/in/nolanla
- **GitHub**: https://github.com/nolanvla-tech

---

Built with Django 🎉
