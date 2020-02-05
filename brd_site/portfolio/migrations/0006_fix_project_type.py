# Generated by Django 3.0.2 on 2020-02-04 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_add_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('Personal', 'Personal'), ('OpenSource', 'Open Source')], default='Personal', max_length=16),
        ),
    ]
