# Generated by Django 4.1.6 on 2023-03-05 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("items_list", "0007_alter_shoppinglist_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shoppinglist",
            name="created_at",
        ),
    ]
