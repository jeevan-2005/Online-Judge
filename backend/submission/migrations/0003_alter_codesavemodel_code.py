# Generated by Django 5.2.3 on 2025-06-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_submissionmodel_verdict_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesavemodel',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
    ]
