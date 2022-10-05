# Generated by Django 4.1.1 on 2022-10-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('admin', 'администратор'), ('member', 'пользователь'), ('moderator', 'модератор')], default='member', max_length=10)),
                ('age', models.SmallIntegerField()),
                ('location', models.ManyToManyField(to='ads.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['username'],
            },
        ),
    ]
