# Generated by Django 2.2.1 on 2019-05-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos'),
        ),
    ]