# Generated by Django 3.0.2 on 2020-02-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_init_techtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Open Source', 'Open Source')], default='Personal', max_length=16),
        ),
    ]
