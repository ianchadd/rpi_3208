# Generated by Django 2.2.4 on 2020-03-09 22:13

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_demographics', '0018_auto_20200309_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='grew_up_in',
            field=otree.db.models.StringField(choices=[('AK (Alaska)', 'AK (Alaska)'), ('AL (Alabama)', 'AL (Alabama)'), ('AR (Arkansas)', 'AR (Arkansas)'), ('AS (American Samoa)', 'AS (American Samoa)'), ('AZ (Arizona)', 'AZ (Arizona)'), ('CA (California)', 'CA (California)'), ('CO (Colorado)', 'CO (Colorado)'), ('CT (Connecticut)', 'CT (Connecticut)'), ('DC (District of Columbia)', 'DC (District of Columbia)'), ('DE (Delaware)', 'DE (Delaware)'), ('FL (Florida)', 'FL (Florida)'), ('GA (Georgia)', 'GA (Georgia)'), ('GU (Guam)', 'GU (Guam)'), ('HI (Hawaii)', 'HI (Hawaii)'), ('IA (Iowa)', 'IA (Iowa)'), ('ID (Idaho)', 'ID (Idaho)'), ('IL (Illinois)', 'IL (Illinois)'), ('IN (Indiana)', 'IN (Indiana)'), ('KS (Kansas)', 'KS (Kansas)'), ('KY (Kentucky)', 'KY (Kentucky)'), ('LA (Louisiana)', 'LA (Louisiana)'), ('MA (Massachusetts)', 'MA (Massachusetts)'), ('MD (Maryland)', 'MD (Maryland)'), ('ME (Maine)', 'ME (Maine)'), ('MI (Michigan)', 'MI (Michigan)'), ('MN (Minnesota)', 'MN (Minnesota)'), ('MO (Missouri)', 'MO (Missouri)'), ('MP (Northern Mariana Islands)', 'MP (Northern Mariana Islands)'), ('MS (Mississippi)', 'MS (Mississippi)'), ('MT (Montana)', 'MT (Montana)'), ('NC (North Carolina)', 'NC (North Carolina)'), ('ND (North Dakota)', 'ND (North Dakota)'), ('NE (Nebraska)', 'NE (Nebraska)'), ('NH (New Hampshire)', 'NH (New Hampshire)'), ('NJ (New Jersey)', 'NJ (New Jersey)'), ('NM (New Mexico)', 'NM (New Mexico)'), ('NV (Nevada)', 'NV (Nevada)'), ('NY (New York)', 'NY (New York)'), ('OH (Ohio)', 'OH (Ohio)'), ('OK (Oklahoma)', 'OK (Oklahoma)'), ('OR (Oregon)', 'OR (Oregon)'), ('PA (Pennsylvania)', 'PA (Pennsylvania)'), ('PR (Puerto Rico)', 'PR (Puerto Rico)'), ('RI (Rhode Island)', 'RI (Rhode Island)'), ('SC (South Carolina)', 'SC (South Carolina)'), ('SD (South Dakota)', 'SD (South Dakota)'), ('TN (Tennessee)', 'TN (Tennessee)'), ('TX (Texas)', 'TX (Texas)'), ('UT (Utah)', 'UT (Utah)'), ('VA (Virginia)', 'VA (Virginia)'), ('VI (Virgin Islands)', 'VI (Virgin Islands)'), ('VT (Vermont)', 'VT (Vermont)'), ('WA (Washington)', 'WA (Washington)'), ('WI (Wisconsin)', 'WI (Wisconsin)'), ('WV (West Virginia)', 'WV (West Virginia)'), ('WY (Wyoming)', 'WY (Wyoming)'), ('Other (please state below)', 'Other (please state below)')], max_length=10000, null=True, verbose_name='In which US state/territory did you spend the most time in for the first 18 years of your life?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='live_in',
            field=otree.db.models.StringField(choices=[('AK (Alaska)', 'AK (Alaska)'), ('AL (Alabama)', 'AL (Alabama)'), ('AR (Arkansas)', 'AR (Arkansas)'), ('AS (American Samoa)', 'AS (American Samoa)'), ('AZ (Arizona)', 'AZ (Arizona)'), ('CA (California)', 'CA (California)'), ('CO (Colorado)', 'CO (Colorado)'), ('CT (Connecticut)', 'CT (Connecticut)'), ('DC (District of Columbia)', 'DC (District of Columbia)'), ('DE (Delaware)', 'DE (Delaware)'), ('FL (Florida)', 'FL (Florida)'), ('GA (Georgia)', 'GA (Georgia)'), ('GU (Guam)', 'GU (Guam)'), ('HI (Hawaii)', 'HI (Hawaii)'), ('IA (Iowa)', 'IA (Iowa)'), ('ID (Idaho)', 'ID (Idaho)'), ('IL (Illinois)', 'IL (Illinois)'), ('IN (Indiana)', 'IN (Indiana)'), ('KS (Kansas)', 'KS (Kansas)'), ('KY (Kentucky)', 'KY (Kentucky)'), ('LA (Louisiana)', 'LA (Louisiana)'), ('MA (Massachusetts)', 'MA (Massachusetts)'), ('MD (Maryland)', 'MD (Maryland)'), ('ME (Maine)', 'ME (Maine)'), ('MI (Michigan)', 'MI (Michigan)'), ('MN (Minnesota)', 'MN (Minnesota)'), ('MO (Missouri)', 'MO (Missouri)'), ('MP (Northern Mariana Islands)', 'MP (Northern Mariana Islands)'), ('MS (Mississippi)', 'MS (Mississippi)'), ('MT (Montana)', 'MT (Montana)'), ('NC (North Carolina)', 'NC (North Carolina)'), ('ND (North Dakota)', 'ND (North Dakota)'), ('NE (Nebraska)', 'NE (Nebraska)'), ('NH (New Hampshire)', 'NH (New Hampshire)'), ('NJ (New Jersey)', 'NJ (New Jersey)'), ('NM (New Mexico)', 'NM (New Mexico)'), ('NV (Nevada)', 'NV (Nevada)'), ('NY (New York)', 'NY (New York)'), ('OH (Ohio)', 'OH (Ohio)'), ('OK (Oklahoma)', 'OK (Oklahoma)'), ('OR (Oregon)', 'OR (Oregon)'), ('PA (Pennsylvania)', 'PA (Pennsylvania)'), ('PR (Puerto Rico)', 'PR (Puerto Rico)'), ('RI (Rhode Island)', 'RI (Rhode Island)'), ('SC (South Carolina)', 'SC (South Carolina)'), ('SD (South Dakota)', 'SD (South Dakota)'), ('TN (Tennessee)', 'TN (Tennessee)'), ('TX (Texas)', 'TX (Texas)'), ('UT (Utah)', 'UT (Utah)'), ('VA (Virginia)', 'VA (Virginia)'), ('VI (Virgin Islands)', 'VI (Virgin Islands)'), ('VT (Vermont)', 'VT (Vermont)'), ('WA (Washington)', 'WA (Washington)'), ('WI (Wisconsin)', 'WI (Wisconsin)'), ('WV (West Virginia)', 'WV (West Virginia)'), ('WY (Wyoming)', 'WY (Wyoming)'), ('Other (please state below)', 'Other (please state below)')], max_length=10000, null=True, verbose_name='In which US state/territory do you currently live?'),
        ),
    ]
