# Generated by Django 3.2.7 on 2021-09-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0009_alter_motivation_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='grade',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
