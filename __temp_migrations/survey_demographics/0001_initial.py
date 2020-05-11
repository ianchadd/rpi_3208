# Generated by Django 2.2.4 on 2020-05-11 20:01

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_demographics_group', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_demographics_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_demographics_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_demographics_subsession',
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
                ('age', otree.db.models.IntegerField(null=True, verbose_name='What is your age?')),
                ('yob', otree.db.models.IntegerField(null=True, verbose_name='What is your year of birth?')),
                ('sex', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10000, null=True, verbose_name='What sex were you assigned at birth, on your original birth certificate?')),
                ('male', otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Male')),
                ('female', otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True, verbose_name='Female')),
                ('t_male', otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True, verbose_name='Trans male / Trans man')),
                ('t_female', otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True, verbose_name='Trans female / Trans woman')),
                ('gnc', otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True, verbose_name='Genderqueer / Gender non-conforming')),
                ('other_g', otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True, verbose_name='Other (please state below)')),
                ('diff_gend', otree.db.models.StringField(blank=True, default='', max_length=10000, null=True, verbose_name='')),
                ('orientation', otree.db.models.StringField(choices=[('Heterosexual or straight', 'Heterosexual or straight'), ('Gay or lesbian', 'Gay or lesbian'), ('Bisexual', 'Bisexual'), ('Other (please state below)', 'Other (please state below)')], max_length=10000, null=True, verbose_name='Which do you consider yourself to be:')),
                ('other_orientation', otree.db.models.StringField(blank=True, default='', max_length=10000, null=True, verbose_name='')),
                ('sex_hist', otree.db.models.StringField(choices=[('Men only', 'Men only'), ('Women only', 'Women only'), ('Both men and women', 'Both men and women'), ('I have not had sex', 'I have not had sex'), ('I prefer not to say', 'I prefer not to say')], max_length=10000, null=True, verbose_name='In the past year, who have you had sex with?')),
                ('attracted_men', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Are you sexually attracted to men?')),
                ('attracted_women', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Are you sexually attracted to women?')),
                ('relationship', otree.db.models.StringField(choices=[('Single', 'Single'), ('Partnership (not living in the same home)', 'Partnership (not living in the same home)'), ('Domestic Partnership (living in the same home)', 'Domestic Partnership (living in the same home)'), ('Married', 'Married'), ('Other (please state below)', 'Other (please state below)')], max_length=10000, null=True, verbose_name='Please indicate your current relationship status')),
                ('other_relationship', otree.db.models.StringField(blank=True, default='', max_length=10000, null=True, verbose_name='')),
                ('primary_earner', otree.db.models.StringField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Multiple primary earners in household', 'Multiple primary earners in household')], max_length=10000, null=True, verbose_name='Are you the primary earner in the household?')),
                ('income', otree.db.models.StringField(choices=[('less than $20,000', 'less than $20,000'), ('$20,000 - $39,999', '$20,000 - $39,999'), ('$40,000 - $59,999', '$40,000 - $59,999'), ('$60,000 - $79,999', '$60,000 - $79,999'), ('$80,000 - $99,999', '$80,000 - $99,999'), ('$100,000 or more', '$100,000 or more')], max_length=10000, null=True, verbose_name='Please select your household annual income from the options below')),
                ('ethnicity', otree.db.models.StringField(choices=[('White', 'White'), ('Black or African American', 'Black or African American'), ('American Indian and Alaskan Native', 'American Indian and Alaskan Native'), ('Asian', 'Asian'), ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander'), ('Hispanic or Latino', 'Hispanic or Latino'), ('Middle Eastern or Arab', 'Middle Eastern or Arab'), ('Other (please state below)', 'Other (please state below)')], max_length=10000, null=True, verbose_name='What is your ethnicity?')),
                ('other_ethnicity', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='')),
                ('religion', otree.db.models.StringField(choices=[('Christian (any denomination)', 'Christian (any denomination)'), ('Hindu', 'Hindu'), ('Buddhist', 'Buddhist'), ('Jewish', 'Jewish'), ('Muslim', 'Muslim'), ('Asian Folk Religion (e.g. Taoist, Confucian)', 'Asian Folk Religion (e.g. Taoist, Confucian)'), ('I am not religious', 'I am not religious'), ('Some other religious affiliation (please specify below)', 'Some other religious affiliation (please specify below)')], max_length=10000, null=True, verbose_name='What is your religious affiliation?')),
                ('other_religion', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='')),
                ('econ_politics', otree.db.models.StringField(choices=[('More conservative than liberal', 'More conservative than liberal'), ('Equally conservative and liberal', 'Equally conservative and liberal'), ('More liberal than conservative', 'More liberal than conservative')], max_length=10000, null=True, verbose_name='')),
                ('social_politics', otree.db.models.StringField(choices=[('More conservative than liberal', 'More conservative than liberal'), ('Equally conservative and liberal', 'Equally conservative and liberal'), ('More liberal than conservative', 'More liberal than conservative')], max_length=10000, null=True, verbose_name='')),
                ('lgbt_free', otree.db.models.IntegerField(choices=[[5, 'Strongly Agree'], [4, 'Agree'], [3, 'Neither Agree nor Disagree'], [2, 'Disagree'], [1, 'Strongly Disagree']], null=True, verbose_name='Do you believe that gay men and lesbians should be free to live their own lives as they wish?')),
                ('live_in', otree.db.models.StringField(choices=[('AK (Alaska)', 'AK (Alaska)'), ('AL (Alabama)', 'AL (Alabama)'), ('AR (Arkansas)', 'AR (Arkansas)'), ('AS (American Samoa)', 'AS (American Samoa)'), ('AZ (Arizona)', 'AZ (Arizona)'), ('CA (California)', 'CA (California)'), ('CO (Colorado)', 'CO (Colorado)'), ('CT (Connecticut)', 'CT (Connecticut)'), ('DC (District of Columbia)', 'DC (District of Columbia)'), ('DE (Delaware)', 'DE (Delaware)'), ('FL (Florida)', 'FL (Florida)'), ('GA (Georgia)', 'GA (Georgia)'), ('GU (Guam)', 'GU (Guam)'), ('HI (Hawaii)', 'HI (Hawaii)'), ('IA (Iowa)', 'IA (Iowa)'), ('ID (Idaho)', 'ID (Idaho)'), ('IL (Illinois)', 'IL (Illinois)'), ('IN (Indiana)', 'IN (Indiana)'), ('KS (Kansas)', 'KS (Kansas)'), ('KY (Kentucky)', 'KY (Kentucky)'), ('LA (Louisiana)', 'LA (Louisiana)'), ('MA (Massachusetts)', 'MA (Massachusetts)'), ('MD (Maryland)', 'MD (Maryland)'), ('ME (Maine)', 'ME (Maine)'), ('MI (Michigan)', 'MI (Michigan)'), ('MN (Minnesota)', 'MN (Minnesota)'), ('MO (Missouri)', 'MO (Missouri)'), ('MP (Northern Mariana Islands)', 'MP (Northern Mariana Islands)'), ('MS (Mississippi)', 'MS (Mississippi)'), ('MT (Montana)', 'MT (Montana)'), ('NC (North Carolina)', 'NC (North Carolina)'), ('ND (North Dakota)', 'ND (North Dakota)'), ('NE (Nebraska)', 'NE (Nebraska)'), ('NH (New Hampshire)', 'NH (New Hampshire)'), ('NJ (New Jersey)', 'NJ (New Jersey)'), ('NM (New Mexico)', 'NM (New Mexico)'), ('NV (Nevada)', 'NV (Nevada)'), ('NY (New York)', 'NY (New York)'), ('OH (Ohio)', 'OH (Ohio)'), ('OK (Oklahoma)', 'OK (Oklahoma)'), ('OR (Oregon)', 'OR (Oregon)'), ('PA (Pennsylvania)', 'PA (Pennsylvania)'), ('PR (Puerto Rico)', 'PR (Puerto Rico)'), ('RI (Rhode Island)', 'RI (Rhode Island)'), ('SC (South Carolina)', 'SC (South Carolina)'), ('SD (South Dakota)', 'SD (South Dakota)'), ('TN (Tennessee)', 'TN (Tennessee)'), ('TX (Texas)', 'TX (Texas)'), ('UT (Utah)', 'UT (Utah)'), ('VA (Virginia)', 'VA (Virginia)'), ('VI (Virgin Islands)', 'VI (Virgin Islands)'), ('VT (Vermont)', 'VT (Vermont)'), ('WA (Washington)', 'WA (Washington)'), ('WI (Wisconsin)', 'WI (Wisconsin)'), ('WV (West Virginia)', 'WV (West Virginia)'), ('WY (Wyoming)', 'WY (Wyoming)'), ('Other (please state below)', 'Other (please state below)')], max_length=10000, null=True, verbose_name='In which US state/territory do you currently live?')),
                ('grew_up_in', otree.db.models.StringField(choices=[('AK (Alaska)', 'AK (Alaska)'), ('AL (Alabama)', 'AL (Alabama)'), ('AR (Arkansas)', 'AR (Arkansas)'), ('AS (American Samoa)', 'AS (American Samoa)'), ('AZ (Arizona)', 'AZ (Arizona)'), ('CA (California)', 'CA (California)'), ('CO (Colorado)', 'CO (Colorado)'), ('CT (Connecticut)', 'CT (Connecticut)'), ('DC (District of Columbia)', 'DC (District of Columbia)'), ('DE (Delaware)', 'DE (Delaware)'), ('FL (Florida)', 'FL (Florida)'), ('GA (Georgia)', 'GA (Georgia)'), ('GU (Guam)', 'GU (Guam)'), ('HI (Hawaii)', 'HI (Hawaii)'), ('IA (Iowa)', 'IA (Iowa)'), ('ID (Idaho)', 'ID (Idaho)'), ('IL (Illinois)', 'IL (Illinois)'), ('IN (Indiana)', 'IN (Indiana)'), ('KS (Kansas)', 'KS (Kansas)'), ('KY (Kentucky)', 'KY (Kentucky)'), ('LA (Louisiana)', 'LA (Louisiana)'), ('MA (Massachusetts)', 'MA (Massachusetts)'), ('MD (Maryland)', 'MD (Maryland)'), ('ME (Maine)', 'ME (Maine)'), ('MI (Michigan)', 'MI (Michigan)'), ('MN (Minnesota)', 'MN (Minnesota)'), ('MO (Missouri)', 'MO (Missouri)'), ('MP (Northern Mariana Islands)', 'MP (Northern Mariana Islands)'), ('MS (Mississippi)', 'MS (Mississippi)'), ('MT (Montana)', 'MT (Montana)'), ('NC (North Carolina)', 'NC (North Carolina)'), ('ND (North Dakota)', 'ND (North Dakota)'), ('NE (Nebraska)', 'NE (Nebraska)'), ('NH (New Hampshire)', 'NH (New Hampshire)'), ('NJ (New Jersey)', 'NJ (New Jersey)'), ('NM (New Mexico)', 'NM (New Mexico)'), ('NV (Nevada)', 'NV (Nevada)'), ('NY (New York)', 'NY (New York)'), ('OH (Ohio)', 'OH (Ohio)'), ('OK (Oklahoma)', 'OK (Oklahoma)'), ('OR (Oregon)', 'OR (Oregon)'), ('PA (Pennsylvania)', 'PA (Pennsylvania)'), ('PR (Puerto Rico)', 'PR (Puerto Rico)'), ('RI (Rhode Island)', 'RI (Rhode Island)'), ('SC (South Carolina)', 'SC (South Carolina)'), ('SD (South Dakota)', 'SD (South Dakota)'), ('TN (Tennessee)', 'TN (Tennessee)'), ('TX (Texas)', 'TX (Texas)'), ('UT (Utah)', 'UT (Utah)'), ('VA (Virginia)', 'VA (Virginia)'), ('VI (Virgin Islands)', 'VI (Virgin Islands)'), ('VT (Vermont)', 'VT (Vermont)'), ('WA (Washington)', 'WA (Washington)'), ('WI (Wisconsin)', 'WI (Wisconsin)'), ('WV (West Virginia)', 'WV (West Virginia)'), ('WY (Wyoming)', 'WY (Wyoming)'), ('Other (please state below)', 'Other (please state below)')], max_length=10000, null=True, verbose_name='In which US state/territory did you spend the most time in for the first 18 years of your life?')),
                ('other_live_location', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='')),
                ('other_grew_up_location', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='')),
                ('attn_check_1', otree.db.models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='(Attention Check) Please select 1 in the list below.')),
                ('consider_lgbt_ally', otree.db.models.IntegerField(choices=[[1, 'Yes'], [0, 'No']], null=True, verbose_name='Do you consider yourself to be an ally to the LGBTQ+ community?')),
                ('program_lgbt_ally', otree.db.models.IntegerField(choices=[[1, 'Yes'], [0, 'No']], null=True, verbose_name='Are you formally registered as an LGBTQ+ ally (e.g. Safe Zone Training, Campus Ally programs, etc.) in your workplace, school, university, or other institution?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey_demographics.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_demographics_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_demographics_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_demographics.Subsession')),
            ],
            options={
                'db_table': 'survey_demographics_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_demographics.Subsession'),
        ),
    ]
