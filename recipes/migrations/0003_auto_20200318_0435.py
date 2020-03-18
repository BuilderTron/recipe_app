# Generated by Django 3.0.4 on 2020-03-18 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20200318_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'meal',
                'verbose_name_plural': 'meals',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='recipe',
            name='meal',
            field=models.ForeignKey(choices=[('Breakfast', 'Breakfast'), ('Brunch', 'Brunch'), ('Elevenses', 'Elevenses'), ('Lunch', 'Lunch'), ('Tea', 'Tea'), ('Supper', 'Supper'), ('Dinner', 'Dinner')], on_delete=django.db.models.deletion.CASCADE, to='recipes.Meal'),
        ),
    ]