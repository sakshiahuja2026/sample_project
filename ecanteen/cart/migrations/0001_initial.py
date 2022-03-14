# Generated by Django 4.0.2 on 2022-03-08 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('payment_status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=50)),
                ('fruit', models.CharField(choices=[('apple', 'apple'), ('banana', 'banana'), ('orange', 'orange'), ('grapes', 'grapes')], max_length=50)),
            ],
            options={
                'db_table': 'season',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_name', models.CharField(max_length=50)),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.payment')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]