# Generated by Django 4.0.4 on 2022-05-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_cartorder_order_status_useraddressbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddressbook',
            name='mobile',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
