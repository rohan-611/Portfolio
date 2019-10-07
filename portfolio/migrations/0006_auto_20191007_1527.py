# Generated by Django 2.2.4 on 2019-10-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_researchandpublications_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='Sandeep Raghuwanshi', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Sandeep Raghuwanshi', max_length=50),
            preserve_default=False,
        ),
    ]
