# Generated by Django 5.0 on 2023-12-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0002_visitor_number_of_people_alter_visitor_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='mobile_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='number_of_people',
            field=models.IntegerField(),
        ),
    ]
