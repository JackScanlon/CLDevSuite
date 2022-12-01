# Generated by Django 4.1.3 on 2022-11-30 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codelist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.BooleanField(default=True, null=True)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('source',),
            },
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('coding_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coding_system_data', to='codelist.codingsystem')),
                ('components', models.ManyToManyField(blank=True, related_name='related_components', to='concepts.component')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='concept_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
