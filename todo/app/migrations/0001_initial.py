# Generated by Django 4.1.3 on 2022-11-20 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=1000)),
                ('Due_Date', models.DateField(blank=True, null=True)),
                ('Status', models.CharField(choices=[('open', 'OPEN'), ('working', 'WORKING'), ('done', 'DONE'), ('overdue', 'OVERDUE')], default='open', max_length=20)),
                ('Tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tag')),
            ],
        ),
    ]