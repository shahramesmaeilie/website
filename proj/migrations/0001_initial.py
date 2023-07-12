# Generated by Django 4.2.2 on 2023-06-26 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TITLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PROJECT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('nam', models.CharField(max_length=30)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=15)),
                ('duration', models.DurationField()),
                ('modir', models.CharField(max_length=30)),
                ('place', models.TextField()),
                ('pic', models.ImageField(default='', null=True, upload_to='proj/images')),
                ('status', models.BooleanField(default=False)),
                ('desc', models.TextField()),
                ('teedadnafar', models.IntegerField()),
                ('title', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='proj.title')),
            ],
        ),
    ]
