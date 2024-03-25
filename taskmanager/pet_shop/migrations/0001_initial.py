# Generated by Django 5.0.3 on 2024-03-15 02:25

import django.db.models.deletion
import django.utils.timezone
import pet_shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_name', models.CharField(max_length=255, verbose_name='Назва виду')),
                ('species_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
            ],
            options={
                'verbose_name': 'Вид',
                'verbose_name_plural': 'Види',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('surname', models.CharField(blank=True, default='', max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Ч', 'Чоловічий'), ('Ж', 'Жіночий')], default='M', max_length=1)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Користувач',
                'verbose_name_plural': 'Користувачі',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', pet_shop.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=255, verbose_name='Ім`я тварини')),
                ('pet_age', models.IntegerField(verbose_name='Вік тварини')),
                ('pet_sex', models.CharField(choices=[('Чоловіча', 'Чоловіча'), ('Жіноча', 'Жіноча')], max_length=8, verbose_name='Стать тварини')),
                ('pet_weight', models.FloatField(verbose_name='Вага тварини')),
                ('pet_species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_shop.species')),
            ],
            options={
                'verbose_name': 'Тварина',
                'verbose_name_plural': 'Тварини',
            },
        ),
    ]
