# Generated by Django 4.2 on 2023-04-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_alumni_alumprofilepic_company_companypic_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="studprofilepic",
            field=models.TextField(blank=True, null=True),
        ),
    ]