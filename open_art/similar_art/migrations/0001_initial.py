# Generated by Django 3.2.5 on 2021-07-02 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date uploaded')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_responses', models.CharField(max_length=200)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='similar_art.query')),
            ],
        ),
    ]
