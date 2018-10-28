# Generated by Django 2.1.2 on 2018-10-28 06:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20181028_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 6, 20, 24, 316605, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='ingredientinventory',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Inventory'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='ingredients',
            field=models.ManyToManyField(through='main.IngredientInventory', to='main.Ingredient'),
        ),
    ]
