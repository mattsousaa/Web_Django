# Generated by Django 2.2.1 on 2019-05-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bio', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='clients_photos')),
            ],
        ),
    ]