# Generated by Django 3.0.4 on 2020-03-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200320_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default='static/recipes/default_img.gif', upload_to='recipes/images/'),
        ),
    ]
