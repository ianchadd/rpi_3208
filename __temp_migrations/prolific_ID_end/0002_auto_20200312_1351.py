# Generated by Django 2.2.4 on 2020-03-12 17:51

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prolific_ID_end', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='p_ID',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]