# Generated by Django 4.1.5 on 2023-02-18 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_tag_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]