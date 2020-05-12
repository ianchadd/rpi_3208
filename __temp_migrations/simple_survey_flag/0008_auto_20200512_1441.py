# Generated by Django 2.2.4 on 2020-05-12 18:41

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_survey_flag', '0007_auto_20200512_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chooseID',
            field=otree.db.models.StringField(choices=[('dqqjs509', 'dqqjs509'), ('gpdhh268', 'gpdhh268'), ('gxgzp209', 'gxgzp209')], max_length=10000, null=True, verbose_name='Please choose one of the following IDs.'),
        ),
    ]