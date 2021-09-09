# Generated by Django 3.2.7 on 2021-09-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_auto_20210909_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=200)),
                ('questionPaper', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='year',
            name='questionPaper',
        ),
    ]