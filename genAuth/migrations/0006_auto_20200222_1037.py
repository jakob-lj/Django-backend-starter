# Generated by Django 3.0.3 on 2020-02-22 10:37

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('genAuth', '0005_auto_20200222_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssocode',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ssocode',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userverificationtoken',
            name='token',
            field=models.CharField(default='ebf2183f546d66eda11a138afd0c1609c53cf36a6d6ed34ac3be3acb49c965ba', editable=False, max_length=200, unique=True),
        ),
    ]
