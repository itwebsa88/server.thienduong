# Generated by Django 5.1 on 2024-09-01 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('status', models.IntegerField(null=True)),
                ('money', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount_code', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('paypassword', models.CharField(max_length=100)),
                ('header_img', models.CharField(max_length=50)),
                ('uid', models.IntegerField()),
                ('ip', models.CharField(max_length=50)),
                ('last_time', models.DateTimeField(auto_now_add=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.IntegerField()),
                ('num', models.IntegerField()),
                ('min', models.IntegerField()),
                ('max', models.IntegerField()),
                ('is_online', models.IntegerField()),
                ('role', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('daili', models.CharField(max_length=30)),
            ],
        ),
    ]
