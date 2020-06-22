# Generated by Django 2.2.4 on 2020-06-22 13:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('qsp_dg_dict_id', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='attn_check_1',
            field=otree.db.models.IntegerField(choices=[[1, 'Cat'], [2, 'Dog'], [3, 'Bird']], null=True, verbose_name='Please select the word "Dog"'),
        ),
    ]
