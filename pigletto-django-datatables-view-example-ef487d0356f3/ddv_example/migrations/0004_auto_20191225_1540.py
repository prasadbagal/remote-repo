# Generated by Django 2.1 on 2019-12-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddv_example', '0003_auto_20191225_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='first',
            field=models.CharField(max_length=10, verbose_name='First'),
        ),
    ]