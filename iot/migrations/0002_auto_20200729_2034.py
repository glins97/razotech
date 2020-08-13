# Generated by Django 3.0.8 on 2020-07-29 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='person',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='verified',
        ),
        migrations.RemoveField(
            model_name='web',
            name='id',
        ),
        migrations.RemoveField(
            model_name='web',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='web',
            name='person',
        ),
        migrations.RemoveField(
            model_name='web',
            name='verified',
        ),
        migrations.CreateModel(
            name='AccessDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(max_length=255)),
                ('verified', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.Person')),
            ],
        ),
        migrations.AddField(
            model_name='mobile',
            name='accessdevice_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='iot.AccessDevice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='web',
            name='accessdevice_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='iot.AccessDevice'),
            preserve_default=False,
        ),
    ]