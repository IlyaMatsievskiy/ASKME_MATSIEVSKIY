# Generated by Django 4.2.16 on 2024-12-03 12:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_answer_options_alter_question_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="question",
            options={"ordering": ["-created_at"]},
        ),
    ]
