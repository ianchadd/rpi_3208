# Generated by Django 2.2.4 on 2020-05-12 15:26

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_survey_flag', '0005_auto_20200512_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chooseID',
            field=otree.db.models.StringField(choices=[('mmtdc601', 'mmtdc601'), ('lmmhc568', 'lmmhc568'), ('rpsrm732', 'rpsrm732')], max_length=10000, null=True, verbose_name='Please choose one of the following IDs.'),
        ),
    ]
