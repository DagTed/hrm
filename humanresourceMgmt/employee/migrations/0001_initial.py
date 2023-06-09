# Generated by Django 3.0 on 2023-03-30 06:21

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
            name='EmployeeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeID', models.CharField(max_length=50)),
                ('employeeDEPT', models.CharField(max_length=50, null=True)),
                ('designation', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('joiningdate', models.DateField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
