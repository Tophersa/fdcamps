# Generated by Django 3.2.7 on 2021-09-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='questionPaper',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='QuestionPaper',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
