# Generated by Django 4.2 on 2023-04-17 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_alter_alumni_alumprofilepic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="alumni",
            name="branch",
        ),
        migrations.AddField(
            model_name="alumni",
            name="cgpa",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="batch",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="batch_yr_alum",
                to="users.credits",
            ),
        ),
    ]
