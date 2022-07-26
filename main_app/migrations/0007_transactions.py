# Generated by Django 4.0.6 on 2022-07-24 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_merge_20220722_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(default='be3f8c', max_length=100)),
                ('date', models.DateField(verbose_name='transaction date')),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('P', 'In Progress'), ('C', 'Completed')], default='I', max_length=1)),
                ('price', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.account')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
