# Generated by Django 2.2.4 on 2020-03-12 17:51

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_demographics', '0004_auto_20200312_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='attn_check_1',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='(Attention Check) Please select 1 in the list below.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='lgbt_free',
            field=otree.db.models.IntegerField(choices=[[5, 'Strongly Agree'], [4, 'Agree'], [3, 'Neither Agree nor Disagree'], [2, 'Disagree'], [1, 'Strongly Disagree']], null=True, verbose_name='Do you believe that gay men and lesbians should be free to live their own lives as they wish?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='male',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True, verbose_name='Male'),
        ),
    ]