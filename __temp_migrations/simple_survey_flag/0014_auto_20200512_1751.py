# Generated by Django 2.2.4 on 2020-05-12 21:51

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_survey_flag', '0013_auto_20200512_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chooseID',
            field=otree.db.models.StringField(choices=[('rzxw4', 'rzxw4'), ('wxzr4', 'wxzr4'), ('zrwx4', 'zrwx4')], max_length=10000, null=True, verbose_name='Please choose one of the following IDs.'),
        ),
    ]
