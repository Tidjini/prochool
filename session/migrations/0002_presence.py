# Generated by Django 3.2.16 on 2022-11-02 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_membership'),
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('absent', models.BooleanField(default=True)),
                ('by_admin', models.BooleanField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presences', to='session.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_presences', to='student.student')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]