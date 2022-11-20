# Generated by Django 4.1.3 on 2022-11-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Price')),
            ],
        ),
    ]