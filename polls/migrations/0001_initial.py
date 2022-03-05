# Generated by Django 3.2.5 on 2022-03-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
                ('item_code', models.CharField(max_length=20)),
                ('target2_code', models.CharField(max_length=50)),
                ('addr2', models.CharField(max_length=200)),
                ('lng', models.CharField(max_length=200)),
                ('addr1', models.CharField(max_length=200)),
                ('open_info', models.CharField(max_length=200)),
                ('target2_etc', models.CharField(max_length=200)),
                ('type', models.IntegerField(default=0)),
                ('close_info', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField(default=0)),
                ('img_name', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('target1_code', models.CharField(max_length=200)),
                ('idx', models.CharField(max_length=50)),
                ('item_etc', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200)),
            ],
        ),
    ]
