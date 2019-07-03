# Generated by Django 2.2.2 on 2019-06-30 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20190630_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flights.Airport'),
        ),
    ]