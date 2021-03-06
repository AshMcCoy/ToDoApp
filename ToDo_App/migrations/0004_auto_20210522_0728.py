# Generated by Django 2.2 on 2021-05-22 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ToDo_App', '0003_grocery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grocery',
            options={'ordering': ['complete']},
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['paid'],
            },
        ),
    ]
