# Generated by Django 3.1.4 on 2020-12-29 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('uni', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('timezone', models.CharField(choices=[(1, 'UTC -4 through UTC -5 AKA Eastern (EST) or Central (CST)'), (2, 'UTC -6 through UTC -7 AKA Mountain (MST) or Pacific (PST)'), (3, 'UTC -8 through UTC -12 or UTC +12 through UTC +9'), (4, 'UTC +8 through UTC -3')], max_length=128, verbose_name='Timezone')),
                ('time_management', models.IntegerField(choices=[(1, 'Finish far before the deadline (days before the deadline)'), (2, 'Finish early (a day or two before the deadline)'), (3, 'Finish with a little bit of time left over (several hours before the deadline)'), (4, 'Finish at the last minute (several minutes before deadline)')], default=0)),
                ('collaborative', models.IntegerField(choices=[(1, 'Prefer minimal talking'), (2, ''), (3, ''), (4, ''), (5, 'Very interactive')], default=0)),
                ('academic_seriousness', models.IntegerField(choices=[(1, 'Not so serious'), (2, ''), (3, ''), (4, ''), (5, 'Very serious student')], default=0)),
                ('extroverted', models.IntegerField(choices=[(1, 'Not extroverted'), (2, ''), (3, ''), (4, ''), (5, 'Very extroverted')], default=0)),
                ('discovery', models.CharField(choices=[('class', 'Class'), ('discord', 'Discord'), ('facebook', 'Facebook'), ('friend', 'Friend'), ('groupme', 'GroupMe'), ('instagram', 'Instagram'), ('slack', 'Slack'), ('snapchat', 'Snapchat'), ('student_council', 'Student Council')], max_length=50)),
                ('fun_facts', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_num', models.CharField(max_length=10)),
                ('students', models.ManyToManyField(to='study.Student')),
            ],
        ),
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_number', models.CharField(max_length=3)),
                ('call_number', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=50)),
                ('num_students', models.IntegerField()),
                ('time', models.CharField(max_length=50)),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='study.professor')),
            ],
        ),
    ]
