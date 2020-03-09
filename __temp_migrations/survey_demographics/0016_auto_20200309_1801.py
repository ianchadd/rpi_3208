# Generated by Django 2.2.4 on 2020-03-09 22:01

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_demographics', '0015_auto_20200309_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='politics',
        ),
        migrations.AddField(
            model_name='player',
            name='econ_politics',
            field=otree.db.models.StringField(choices=[('More conservative than liberal', 'More conservative than liberal'), ('Equally conservative and liberal', 'Equally conservative and liberal'), ('More liberal than conservative', 'More liberal than conservative')], max_length=10000, null=True, verbose_name='On economic issues, politically I am'),
        ),
        migrations.AddField(
            model_name='player',
            name='social_politics',
            field=otree.db.models.StringField(choices=[('More conservative than liberal', 'More conservative than liberal'), ('Equally conservative and liberal', 'Equally conservative and liberal'), ('More liberal than conservative', 'More liberal than conservative')], max_length=10000, null=True, verbose_name='On social issues, politically I am'),
        ),
    ]
