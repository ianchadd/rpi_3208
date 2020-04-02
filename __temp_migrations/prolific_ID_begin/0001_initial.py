# Generated by Django 2.2.4 on 2020-03-10 03:01

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prolific_id_begin_group', to='otree.Session')),
            ],
            options={
                'db_table': 'prolific_ID_begin_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prolific_id_begin_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'prolific_ID_begin_subsession',
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
                ('p_ID', otree.db.models.StringField(max_length=10000, null=True, verbose_name='Paste your Prolific ID here')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prolific_ID_begin.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prolific_id_begin_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prolific_id_begin_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prolific_ID_begin.Subsession')),
            ],
            options={
                'db_table': 'prolific_ID_begin_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prolific_ID_begin.Subsession'),
        ),
    ]
