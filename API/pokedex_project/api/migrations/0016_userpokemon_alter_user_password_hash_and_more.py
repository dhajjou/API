# Generated by Django 4.2.11 on 2024-04-26 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_rolepermissions_permission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pokemon', to='api.pokemon')),
            ],
            options={
                'db_table': 'user_pokemon',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='password_hash',
            field=models.CharField(default='pbkdf2_sha256$600000$OU3qz15N9E9C7NVNG67ETe$xtyMIaSGdBa01dLa9vZh4K0rIjfiRl86kSYyNFgISvc=', max_length=255),
        ),
        migrations.DeleteModel(
            name='PokemonUser',
        ),
        migrations.AddField(
            model_name='userpokemon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pokemon', to=settings.AUTH_USER_MODEL),
        ),
    ]
