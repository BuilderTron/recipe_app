# Generated by Django 3.0.4 on 2020-03-18 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200318_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='meal',
            field=models.ForeignKey(choices=[('Breakfast', 'Breakfast'), ('Brunch', 'Brunch'), ('Elevenses', 'Elevenses'), ('Lunch', 'Lunch'), ('Tea', 'Tea'), ('Supper', 'Supper'), ('Dinner', 'Dinner')], on_delete=django.db.models.deletion.CASCADE, to='recipes.Meal'),
        ),
    ]