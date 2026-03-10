# Dhanunjaya Reddy — Portfolio Website

A futuristic dark-themed developer portfolio built with **Django**, featuring a glassmorphism UI, animated skill bars, project filtering, and a full admin panel.

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Apply Migrations
```bash
python manage.py migrate
```

### 3. Create Admin Superuser
```bash
python manage.py createsuperuser
```

### 4. Run the Development Server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** to see your portfolio.  
Visit **http://127.0.0.1:8000/admin** to manage content.

---

## 🎛️ Admin Panel Guide

### Setting Up Your Profile
1. Go to **Admin > Site Profile > Add/Edit**
2. Fill in your name, role, about text, email
3. Upload your **profile picture** (square image recommended)
4. Upload your **resume PDF**
5. Add your GitHub, LinkedIn, Twitter URLs

### Adding Skills
1. Go to **Admin > Skills > Add Skill**
2. Set the skill name (e.g. `Python`)
3. Choose a category: `Programming`, `Web Development`, `Machine Learning`, `Tools & Others`
4. Set percentage (0–100)
5. Use the `order` field to control display order

### Adding Projects
1. Go to **Admin > Projects > Add Project**
2. Fill in title, description, short description
3. Upload a **project screenshot**
4. Add GitHub URL and/or live demo URL
5. Add comma-separated **tags** (e.g. `Python,Django,ML`)
6. Set a **category** for filtering (e.g. `Web`, `ML`, `Full Stack`)
7. Check **Featured** to highlight important projects

### Viewing Contact Messages
1. Go to **Admin > Contact Messages**
2. All form submissions appear here
3. Mark messages as read using the checkbox

---

## 📁 Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3              ← Auto-created after migrate
├── media/                  ← Uploaded files (profile pic, resume, screenshots)
│   ├── profile/
│   ├── resume/
│   └── projects/
├── portfolio/              ← Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── main/                   ← Main app
    ├── models.py           ← SiteProfile, Skill, Project, ContactMessage
    ├── views.py            ← Page views + AJAX endpoints
    ├── forms.py            ← Validated contact form
    ├── admin.py            ← Rich admin interface
    ├── urls.py             ← URL routing
    ├── migrations/
    └── templates/main/
        └── index.html      ← Full single-page portfolio
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎨 Dark Theme | Futuristic `#0f172a` base with cyan + indigo accents |
| 🖱️ Custom Cursor | Smooth trailing ring cursor (desktop only) |
| ⌨️ Typing Animation | Cycles through developer roles |
| 📊 Animated Skill Bars | Bars animate on scroll into view |
| 🗂️ Project Filtering | Client-side filter by category |
| 📝 Contact Form | AJAX submission with validation |
| 📥 Resume Download | Served from Django media |
| 🔒 CSRF Protection | All forms are CSRF-protected |
| 📱 Responsive | Mobile-first, works on all screen sizes |
| 🔍 SEO-Friendly | Meta tags, semantic HTML |
| ⚡ Fast Loading | Minimal dependencies, lazy images |

---

## 🔧 Production Deployment

For production, update `settings.py`:

```python
DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']  # Use env variable
ALLOWED_HOSTS = ['yourdomain.com']

# Use PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Then run:
```bash
python manage.py collectstatic
```

---

## 🎨 Customization

- **Colors**: Edit CSS variables in `index.html` (`:root` block)
- **Typing Phrases**: Edit the `phrases` array in the `<script>` section
- **Stats**: Update the About section stat cards in `index.html`
- **Fonts**: Change Google Fonts import at the top of `index.html`

---

Built with ❤️ by Dhanunjaya Reddy
