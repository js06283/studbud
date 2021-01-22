# Generated by Django 3.1.4 on 2021-01-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_auto_20210120_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='timezone',
            field=models.IntegerField(choices=[(1, 'UTC -4 through UTC -5 AKA Eastern (EST) or Central (CST)'), (2, 'UTC -6 through UTC -7 AKA Mountain (MST) or Pacific (PST)'), (3, 'UTC -8 through UTC -12 or UTC +12 through UTC +9'), (4, 'UTC +8 through UTC -3')], default=0),
        ),
    ]