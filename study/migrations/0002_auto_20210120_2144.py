# Generated by Django 3.2 on 2021-01-21 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(default='00000', max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='call_number',
            field=models.CharField(default='00000', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='course',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='course_name',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='course_query',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='course_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='professor',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='section_number',
            field=models.CharField(default='000', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='semester',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='discovery',
            field=models.CharField(choices=[('class', 'Class'), ('discord', 'Discord'), ('facebook', 'Facebook'), ('friend', 'Friend'), ('groupme', 'GroupMe'), ('instagram', 'Instagram'), ('slack', 'Slack'), ('snapchat', 'Snapchat'), ('student_council', 'Student Council')], max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='fun_facts',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(default='0000000000', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='timezone',
            field=models.CharField(choices=[(1, 'UTC -4 through UTC -5 AKA Eastern (EST) or Central (CST)'), (2, 'UTC -6 through UTC -7 AKA Mountain (MST) or Pacific (PST)'), (3, 'UTC -8 through UTC -12 or UTC +12 through UTC +9'), (4, 'UTC +8 through UTC -3')], max_length=255, verbose_name='Timezone'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uni',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='group_num',
            field=models.CharField(default='0000', max_length=255),
        ),
    ]
