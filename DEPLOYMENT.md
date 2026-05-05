# Deployment Guide

Your portfolio project is ready for deployment! Follow these steps to get it live.

## Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com) and sign in (create account if needed)
2. Click **New** (top left) to create a new repository
3. Name it: `portfolio` (or similar)
4. Set to **Public** (so it's visible)
5. Click **Create repository**

## Step 2: Push Code to GitHub

After creating the repository, GitHub will show you commands. Use these:

```powershell
cd c:\Users\nolan\Downloads\AdvPython4v98\PortfolioProject

# Set your GitHub username and email (if not already set)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Add remote (replace with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/portfolio.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Set Up Render Deployment

1. Go to [render.com](https://render.com) and sign up (free account)
2. Click **New** → **Web Service**
3. Connect your GitHub account and select the `portfolio` repository
4. Fill in the settings:
   - **Name**: `portfolio` (or similar)
   - **Environment**: `Python 3`
   - **Build Command**: 
     ```
     pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
     ```
   - **Start Command**: 
     ```
     gunicorn ai_portfolio.wsgi
     ```

5. Click **Advanced** and add Environment Variables:
   - `DEBUG=False`
   - `SECRET_KEY=` (generate a new secure key - see below)
   - `ALLOWED_HOSTS=your-app-name.onrender.com`

### Generate Secure SECRET_KEY

In PowerShell:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and paste it as the `SECRET_KEY` environment variable value.

6. Click **Create Web Service** and Render will deploy your app!

## Step 4: Test Your Live Site

- Render will provide a URL like `https://portfolio-xxx.onrender.com`
- Click the link to view your live portfolio
- Test all pages and features

## Troubleshooting

### Check Logs
In Render dashboard, click your service and view the **Logs** tab to see any errors.

### Common Issues

**Static files not loading**: 
- Ensure `DEBUG=False` is set
- Check that `collectstatic` ran successfully in build logs

**Image/Media not displaying**:
- Media files don't persist on Render's free tier
- For persistent uploads, you'd need to configure cloud storage (S3, etc.)
- For now, the profile image and other media uploaded before deployment should work

**Page crashes**:
- Check the Logs tab in Render dashboard
- Usually database migration or settings issues

## Next Steps

- Set up a custom domain (Render → Settings → Custom Domain)
- Configure email backend for contact form
- Add CI/CD with GitHub Actions for auto-deploy on push
- Upgrade database to PostgreSQL for production (instead of SQLite)

---

**Your portfolio is ready to share!** 🎉

Current live features:
- ✅ Professional home page with profile image
- ✅ About page with full bio and experience
- ✅ Project showcase (3 featured projects)
- ✅ Skills organized by category
- ✅ Resume/CV display
- ✅ Contact form (submissions stored in database)
- ✅ Mobile-responsive design with white professional theme
