# Generated by Django 3.2.18 on 2023-04-10 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EVotingApp.constituency')),
            ],
        ),
    ]
