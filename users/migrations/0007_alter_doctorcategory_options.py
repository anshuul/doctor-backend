# Generated by Django 3.2.7 on 2021-10-26 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_doctor_qr_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctorcategory',
            options={'verbose_name': 'Doctor Category', 'verbose_name_plural': 'Doctor Categories'},
        ),
    ]