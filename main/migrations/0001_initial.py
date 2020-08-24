# Generated by Django 3.1 on 2020-08-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_email', models.CharField(max_length=100)),
                ('c_password', models.CharField(max_length=255)),
                ('c_name', models.CharField(max_length=100)),
                ('c_phone', models.CharField(max_length=30)),
                ('c_company', models.CharField(max_length=300)),
                ('c_department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_email', models.CharField(max_length=100)),
                ('u_password', models.CharField(max_length=255)),
                ('u_membership', models.CharField(max_length=10)),
                ('u_credit_company', models.CharField(max_length=10)),
                ('u_credit_number', models.CharField(max_length=16)),
                ('u_credit_date', models.DateField(default=0)),
                ('u_name', models.CharField(max_length=100)),
                ('u_birth', models.DateField(default=0)),
            ],
        ),
    ]