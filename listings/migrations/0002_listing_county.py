# Generated by Django 3.1.2 on 2020-11-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='county',
            field=models.CharField(default='kiambu', max_length=200),
            preserve_default=False,
        ),
    ]