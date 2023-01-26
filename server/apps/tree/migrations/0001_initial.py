# Generated by Django 3.2.16 on 2023-01-26 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название элемента')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tree.menu', verbose_name='Меню')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree.menuitem', verbose_name='Родительский элемент')),
            ],
            options={
                'verbose_name': 'Элемент Меню',
                'verbose_name_plural': 'Элементы Меню',
            },
        ),
        migrations.AddIndex(
            model_name='menu',
            index=models.Index(fields=['name'], name='tree_menu_name_6c0b5f_idx'),
        ),
    ]
