# Generated by Django 4.2.1 on 2023-06-10 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0006_contactus"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ordermodel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("orderDate", models.DateTimeField(auto_created=True, auto_now=True)),
                ("productid", models.CharField(default="0", max_length=200)),
                ("productqty", models.CharField(default="0", max_length=200)),
                ("userId", models.CharField(max_length=200)),
                ("userName", models.CharField(max_length=200)),
                ("userEmail", models.EmailField(max_length=254)),
                ("userContact", models.IntegerField()),
                ("address", models.CharField(max_length=200)),
                ("orderAmount", models.IntegerField()),
                ("paymentMethod", models.CharField(max_length=200)),
                ("transactionId", models.CharField(max_length=200)),
            ],
        ),
    ]
