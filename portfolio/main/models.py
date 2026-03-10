from django.db import models


class SiteProfile(models.Model):
    name = models.CharField(max_length=100, default="Dhanunjaya Reddy")
    role = models.CharField(max_length=200, default="Software Developer | Machine Learning Enthusiast")
    about_text = models.TextField(default="I am a Computer Science student passionate about Artificial Intelligence, Machine Learning, and Software Development. I love building intelligent systems and elegant web applications that solve real-world problems.")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    twitter_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Site Profile"
        verbose_name_plural = "Site Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('web', 'Web Development'),
        ('ml', 'Machine Learning'),
        ('tools', 'Tools & Others'),
        ('Core', 'Core Computer Science'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='programming')
    percentage = models.IntegerField(default=80, help_text="Skill level (0-100)")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    screenshot = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags, e.g. Python,Django,ML")
    category = models.CharField(max_length=100, blank=True, default='All')
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} - {self.email} ({self.submitted_at.strftime('%Y-%m-%d')})"
