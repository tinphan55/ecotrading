# Generated by Django 4.1.5 on 2023-04-12 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa')),
                ('description', models.TextField(blank=True, max_length=255)),
                ('ratio_risk', models.IntegerField(default=0.03)),
                ('transaction_fee', models.IntegerField(default=0.0015)),
                ('tax', models.IntegerField(default=0.001)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tài khoản',
                'verbose_name_plural': 'Tài khoản',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa')),
                ('stock', models.CharField(blank=True, choices=[], max_length=6, null=True)),
                ('position', models.CharField(blank=True, choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=4, null=True)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('cut_loss_price', models.IntegerField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.account')),
            ],
        ),
        migrations.CreateModel(
            name='CashTrasfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa')),
                ('amount', models.FloatField()),
                ('description', models.TextField(blank=True, max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.account')),
            ],
        ),
    ]
