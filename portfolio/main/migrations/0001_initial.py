from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='SiteProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Dhanunjaya Reddy', max_length=100)),
                ('role', models.CharField(default='Software Developer | Machine Learning Enthusiast', max_length=200)),
                ('about_text', models.TextField(default='I am a Computer Science student passionate about Artificial Intelligence, Machine Learning, and Software Development. I love building intelligent systems and elegant web applications that solve real-world problems.')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('resume_file', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('github_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('twitter_url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Site Profile',
                'verbose_name_plural': 'Site Profile',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(
                    choices=[('programming', 'Programming'), ('web', 'Web Development'), ('ml', 'Machine Learning'), ('tools', 'Tools & Others')],
                    default='programming', max_length=20
                )),
                ('percentage', models.IntegerField(default=80, help_text='Skill level (0-100)')),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['category', 'order']},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('short_description', models.CharField(blank=True, max_length=300)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('github_url', models.URLField(blank=True)),
                ('live_url', models.URLField(blank=True)),
                ('tags', models.CharField(blank=True, help_text='Comma-separated tags, e.g. Python,Django,ML', max_length=300)),
                ('category', models.CharField(blank=True, default='All', max_length=100)),
                ('featured', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['order', '-created_at']},
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-submitted_at']},
        ),
    ]
