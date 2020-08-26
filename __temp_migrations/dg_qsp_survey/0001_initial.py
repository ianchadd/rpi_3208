# Generated by Django 2.2.4 on 2020-06-30 18:24

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dg_qsp_survey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'dg_qsp_survey_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dg_qsp_survey_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'dg_qsp_survey_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('inferred_gender', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans/Intersex/Other', 'Trans/Intersex/Other')], max_length=10000, null=True, verbose_name='')),
                ('inferred_age', otree.db.models.StringField(choices=[('Under 18', 'Under 18'), ('18 - 24', '18 - 24'), ('25 - 34', '25 - 34'), ('35 - 44', '35 - 44'), ('45 - 54', '45 - 54'), ('55 - 64', '55 - 64'), ('65 or Older', '65 or Older')], max_length=10000, null=True, verbose_name='')),
                ('inferred_orientation', otree.db.models.StringField(choices=[('Heterosexual or Straight', 'Heterosexual or Straight'), ('Non-heterosexual or Non-straight', 'Non-heterosexual or Non-straight')], max_length=10000, null=True, verbose_name='')),
                ('inferred_politics', otree.db.models.StringField(choices=[('More conservative than liberal', 'More conservative than liberal'), ('Equally conservative and liberal', 'Equally conservative and liberal'), ('More liberal than conservative', 'More liberal than conservative')], max_length=10000, null=True, verbose_name='')),
                ('gender_confidence', otree.db.models.IntegerField(choices=[[1, 'I chose randomly'], [2, 'A little confident'], [3, 'Fairly confident'], [4, 'Highly confident']], null=True, verbose_name='')),
                ('age_confidence', otree.db.models.IntegerField(choices=[[1, 'I chose randomly'], [2, 'A little confident'], [3, 'Fairly confident'], [4, 'Highly confident']], null=True, verbose_name='')),
                ('orientation_confidence', otree.db.models.IntegerField(choices=[[1, 'I chose randomly'], [2, 'A little confident'], [3, 'Fairly confident'], [4, 'Highly confident']], null=True, verbose_name='')),
                ('politics_confidence', otree.db.models.IntegerField(choices=[[1, 'I chose randomly'], [2, 'A little confident'], [3, 'Fairly confident'], [4, 'Highly confident']], null=True, verbose_name='')),
                ('give_explain', otree.db.models.LongStringField(null=True, verbose_name='')),
                ('id_explain', otree.db.models.LongStringField(null=True, verbose_name='')),
                ('icon_explain', otree.db.models.LongStringField(null=True, verbose_name='')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dg_qsp_survey.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dg_qsp_survey_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dg_qsp_survey_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dg_qsp_survey.Subsession')),
            ],
            options={
                'db_table': 'dg_qsp_survey_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dg_qsp_survey.Subsession'),
        ),
    ]
