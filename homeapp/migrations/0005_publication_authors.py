# Generated by Django 2.2.5 on 2019-11-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_auto_20191110_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]