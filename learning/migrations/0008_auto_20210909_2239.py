# Generated by Django 3.2.7 on 2021-09-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_auto_20210909_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motiveType', models.CharField(blank=True, max_length=200, null=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('imagelink', models.CharField(blank=True, max_length=10000, null=True)),
                ('lifetime', models.CharField(blank=True, max_length=200, null=True)),
                ('quote', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='questionpaper',
            old_name='questionPaper',
            new_name='name',
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='link',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
