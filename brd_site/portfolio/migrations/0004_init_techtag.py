# Generated by Django 3.0.2 on 2020-02-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_fix_blank_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechTag',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('projects', models.ManyToManyField(to='portfolio.Project')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
