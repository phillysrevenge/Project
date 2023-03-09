# Generated by Django 4.1.6 on 2023-03-08 13:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0002_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('content', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='stackbase.question')),
            ],
        ),
    ]
