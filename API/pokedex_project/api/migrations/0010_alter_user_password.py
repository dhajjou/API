# Generated by Django 4.2.11 on 2024-04-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_egggroup_options_alter_items_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$br3R4fN2FGvnhaX6Fb68DH$0g+FsBSv3T/G8s89FvO3n2XogDRHXXo+3DRPDXA0yho=', max_length=255),
        ),
    ]
