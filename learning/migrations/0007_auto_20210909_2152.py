# Generated by Django 3.2.7 on 2021-09-09 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_auto_20210909_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpaper',
            name='retypeSubject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.subject'),
        ),
    ]
