# Generated by Django 2.2.4 on 2020-03-09 21:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_demographics', '0009_auto_20200309_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='other_relationship',
            field=otree.db.models.StringField(blank=True, default='', max_length=10000, null=True, verbose_name=''),
        ),
    ]