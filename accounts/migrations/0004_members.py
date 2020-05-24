# Generated by Django 3.0.6 on 2020-05-24 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200308_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('surname', models.CharField(max_length=30, null=True)),
                ('student_id', models.CharField(blank=True, max_length=30, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_in', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_out', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]