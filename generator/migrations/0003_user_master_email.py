# Generated by Django 4.1.5 on 2023-01-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_user_master_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_master',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
