# Generated by Django 3.2.16 on 2022-11-03 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('birthdate', models.DateField()),
                ('type', models.CharField(choices=[('f', 'Father'), ('m', 'Mother'), ('o', 'Other')], max_length=1)),
                ('profession', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('birthdate', models.DateField()),
                ('barre_code', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('branch', models.CharField(choices=[('math', 'Math'), ('science', 'Science'), ('science', 'Science')], max_length=30)),
                ('year_of_study', models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year')], max_length=1)),
                ('level_of_study', models.CharField(choices=[('vl', 'Very Low'), ('l', 'Low'), ('a', 'Avrage'), ('g', 'Good'), ('e', 'Excelent')], max_length=2)),
                ('observation', models.CharField(max_length=255)),
                ('establishment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='students.establishment')),
                ('parents', models.ManyToManyField(to='students.Parent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remain_sessions', models.IntegerField()),
                ('sessions', models.IntegerField()),
                ('amount', models.FloatField()),
                ('debit', models.FloatField()),
                ('credit', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_memberships', to='students.student')),
            ],
        ),
    ]
