# Generated by Django 3.2.5 on 2021-07-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.TextField()),
            ],
        ),
    ]