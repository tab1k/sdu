# Generated by Django 5.0 on 2023-12-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_customuser_student_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="balance",
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="ent_score",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
