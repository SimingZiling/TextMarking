# Generated by Django 3.0.5 on 2020-04-15 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_entity_symbolsize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_entity', to='common.Entity'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_entity', to='common.Entity'),
        ),
    ]
