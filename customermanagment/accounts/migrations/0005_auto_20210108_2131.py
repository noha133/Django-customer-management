# Generated by Django 3.0.3 on 2021-01-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210108_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='data_created',
        ),
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]