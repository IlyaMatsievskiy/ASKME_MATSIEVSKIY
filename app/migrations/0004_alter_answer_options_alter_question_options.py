# Generated by Django 4.2.16 on 2024-12-03 12:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_rename_content_question_text"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="answer",
            options={"ordering": ["created_at"]},
        ),
        migrations.AlterModelOptions(
            name="question",
            options={"ordering": ["created_at"]},
        ),
    ]