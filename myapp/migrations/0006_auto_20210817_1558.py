# Generated by Django 3.2.6 on 2021-08-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210817_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='datadetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('mail_id', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='details',
        ),
    ]
