# Generated by Django 2.2 on 2019-10-12 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.IntegerField(choices=[(1, 'Normal'), (2, 'VIP'), (3, 'SVIP')])),
                ('userName', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='API.UserInfo')),
            ],
            options={
                'db_table': 'usertoken',
            },
        ),
    ]
