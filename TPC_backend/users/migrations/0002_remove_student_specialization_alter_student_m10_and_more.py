# Generated by Django 4.2 on 2023-04-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="specialization",
        ),
        migrations.AlterField(
            model_name="student",
            name="m10",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="m11",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="m12",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="msem1",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="msem2",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="msem3",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="msem4",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="msem5",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="msem6",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="msem7",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="msem8",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
