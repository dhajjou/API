# Generated by Django 4.2.11 on 2024-04-25 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_rename_rolepermission_rolepermissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolepermissions',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_permissions', to='api.permission'),
        ),
        migrations.AlterField(
            model_name='rolepermissions',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_permissions', to='api.role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password_hash',
            field=models.CharField(default='pbkdf2_sha256$600000$7F3gpb6BtUZb66wtrzQKzG$HZMbEw84tpf54phP5n9xnkDvikEJZyQjPJKRdJj+AFM=', max_length=255),
        ),
        migrations.AlterField(
            model_name='userroles',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_roles', to='api.role'),
        ),
        migrations.AlterField(
            model_name='userroles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_roles', to=settings.AUTH_USER_MODEL),
        ),
    ]
