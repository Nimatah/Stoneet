# Generated by Django 3.1.3 on 2020-12-09 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('full_name', models.CharField(default='Admin', max_length=255)),
                ('phone_number', models.CharField(db_index=True, default='0999xxxxxxx', max_length=20)),
                ('mobile_number', models.CharField(db_index=True, default='021xxxxxxxx', max_length=20)),
                ('fax_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True, unique=True)),
                ('id_code', models.CharField(db_index=True, default='xxxxxxxxxx', max_length=50)),
                ('region', models.CharField(default='tehran', max_length=255)),
                ('address', models.TextField(default='tehran')),
                ('postal_code', models.CharField(default='1231231231', max_length=15)),
                ('use_type', models.CharField(choices=[('seller', 'Seller'), ('logistic', 'Logistic'), ('buyer', 'Buyer')], default='buyer', max_length=20)),
                ('legal_type', models.CharField(choices=[('individual', 'Individual'), ('legal', 'Legal')], default='individual', max_length=20)),
                ('state', models.CharField(choices=[('draft', 'Draft'), ('pending', 'Waiting For Confirm'), ('accepted', 'Confirmed'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('image', 'Image'), ('document', 'Document')], max_length=20)),
                ('file', models.FileField(upload_to='users')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
