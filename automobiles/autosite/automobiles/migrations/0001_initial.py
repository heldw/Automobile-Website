# Generated by Django 2.0.4 on 2018-04-29 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=0)),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motorcycle_id', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=0)),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PersonOwnsCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=0)),
                ('Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automobiles.Car')),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automobiles.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonOwnsMotorcycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=0)),
                ('Motorcycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automobiles.Motorcycle')),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automobiles.Person')),
            ],
        ),
    ]
