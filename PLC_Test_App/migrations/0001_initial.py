# Generated by Django 2.1 on 2018-09-07 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name test', max_length=30)),
                ('plc_type', models.CharField(choices=[('u', 'Unitronics'), ('a', 'Allen Bradley'), ('s', 'Siemens')], max_length=1)),
                ('input_names', models.TextField(default="['Input 0','Input 1','Input 2','Input 3','Input 4','Input 5','Input 6','Input 7','Input 8','Input 9','Input 10','Input 11','Input 12','Input 13','Input 14','Input 15','Input 16','Input 17','Input 18','Input 19','Input 20','Input 21','Input 22','Input 23','Input 24','Input 25','Input 26','Input 27','Input 28','Input 29','Input 30','Input 31']")),
                ('output_names', models.TextField(default="['Output 0','Output 1','Output 2','Output 3','Output 4','Output 5','Output 6','Output 7','Output 8','Output 9','Output 10','Output 11','Output 12','Output 13','Output 14','Output 15','Output 16','Output 17','Output 18','Output 19','Output 20','Output 21','Output 22','Output 23','Output 24','Output 25','Output 26','Output 27','Output 28','Output 29','Output 30','Output 31']")),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name test case', max_length=30)),
                ('input', models.TextField(default='[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]')),
                ('result', models.TextField(default='[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PLC_Test_App.Test')),
            ],
        ),
    ]
