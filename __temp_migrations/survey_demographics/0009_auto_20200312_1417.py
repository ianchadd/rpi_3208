# Generated by Django 2.2.4 on 2020-03-12 18:17

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_demographics', '0008_auto_20200312_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='male',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Male'),
        ),
    ]