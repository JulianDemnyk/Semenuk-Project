# Generated by Django 5.0.4 on 2024-05-09 18:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='table_text',
            new_name='question_text',
        ),
        migrations.RenameModel(
            old_name='Table',
            new_name='Question',
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
