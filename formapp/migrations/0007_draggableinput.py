# Generated by Django 4.2.5 on 2024-02-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0006_alter_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DraggableInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('x_axis', models.IntegerField()),
                ('y_axis', models.IntegerField()),
            ],
        ),
    ]