# Generated by Django 4.2.1 on 2023-05-31 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_game_id_alter_notice_id_alter_player_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='status',
        ),
    ]