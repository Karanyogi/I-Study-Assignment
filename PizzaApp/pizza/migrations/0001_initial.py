# Generated by Django 2.2.5 on 2020-09-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10, unique=True)),
                ('price', models.TextField(max_length=10)),
                ('discription', models.TextField(max_length=25)),
                ('discription_html', models.TextField(editable=False)),
            ],
            options={
                'ordering': ['-name'],
                'unique_together': {('name', 'discription')},
            },
        ),
    ]