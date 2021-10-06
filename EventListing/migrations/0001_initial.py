# Generated by Django 3.0.8 on 2021-09-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('About_Id', models.AutoField(default='', primary_key=True, serialize=False)),
                ('own_pic', models.ImageField(upload_to='')),
                ('about_urslf', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('query', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name_of_event', models.CharField(default='', max_length=50)),
                ('pic_or_logo', models.ImageField(blank=True, null=True, upload_to='image')),
                ('location', models.CharField(default='', max_length=100)),
                ('duration', models.CharField(default='', max_length=100)),
                ('time', models.CharField(default='', max_length=20)),
                ('venue', models.CharField(default='', max_length=100)),
                ('industry', models.CharField(default='', max_length=20)),
                ('organizer', models.CharField(default='', max_length=50)),
                ('link_to_register', models.CharField(default=' ', max_length=200)),
                ('type_of_event', models.CharField(default='', max_length=50)),
                ('post_or_not', models.BooleanField(default=False)),
            ],
        ),
    ]