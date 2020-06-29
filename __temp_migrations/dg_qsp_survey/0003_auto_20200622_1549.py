# Generated by Django 2.2.4 on 2020-06-22 19:49

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('dg_qsp_survey', '0002_auto_20200622_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age_confidence',
            field=otree.db.models.IntegerField(choices=[[1, 'I chose randomly'], [2, 'A little confident'], [3, 'Fairly confident'], [4, 'Highly confident']], null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='gender_confidence',
            field=otree.db.models.IntegerField(choices=[[1, 'I chose randomly'], [2, 'A little confident'], [3, 'Fairly confident'], [4, 'Highly confident']], null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='orientation_confidence',
            field=otree.db.models.IntegerField(choices=[[1, 'I chose randomly'], [2, 'A little confident'], [3, 'Fairly confident'], [4, 'Highly confident']], null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='politics_confidence',
            field=otree.db.models.IntegerField(choices=[[1, 'I chose randomly'], [2, 'A little confident'], [3, 'Fairly confident'], [4, 'Highly confident']], null=True, verbose_name=''),
        ),
    ]
