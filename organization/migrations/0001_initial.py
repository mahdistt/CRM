# Generated by Django 3.2.5 on 2021-07-28 18:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام سازمان')),
                ('city', models.CharField(max_length=20, verbose_name='نام استان')),
                ('number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='شماره وارد شده صحیح نیست!', regex='^0[0-9]{2,}[0-9]{7,}$')], verbose_name='شماره تلفن')),
                ('number_of_employees', models.IntegerField(verbose_name='تعداد کارمندان')),
                ('email', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('introducer_name', models.CharField(max_length=100, verbose_name='نام معرف')),
                ('introducer_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='شماره وارد شده صحیح نیست!', regex='^0[0-9]{2,}[0-9]{7,}$')], verbose_name='شماره معرف')),
                ('created_info', models.DateTimeField(auto_now_add=True)),
                ('operator_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
