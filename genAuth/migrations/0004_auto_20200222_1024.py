# Generated by Django 3.0.3 on 2020-02-22 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import genAuth.codeGenerators


class Migration(migrations.Migration):

    dependencies = [
        ('genAuth', '0003_auto_20200221_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userverificationtoken',
            name='token',
            field=models.CharField(default='81a370960c5ba33d6123cca269a3720fe67379445a14b18efa012268a2a13963', editable=False, max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='SSOCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=genAuth.codeGenerators.loginCode, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
