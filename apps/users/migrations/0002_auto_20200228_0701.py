# Generated by Django 3.0 on 2020-02-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, help_text='电话号码', max_length=11, null=True, verbose_name='电话'),
        ),
    ]
