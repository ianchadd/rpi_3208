# Generated by Django 2.2.4 on 2020-03-04 22:12

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_survey_flag', '0002_auto_20200304_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='adj_10',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='adj_4',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='adj_5',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='adj_6',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='adj_7',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='adj_8',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='adj_9',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True),
        ),
    ]