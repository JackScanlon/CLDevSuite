# Generated by Django 4.1.3 on 2022-11-16 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('codelist', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.BooleanField(default=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codelist.code')),
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
                ('codes', models.ManyToManyField(blank=True, related_name='related_codes', through='concepts.CodeRule', to='codelist.code')),
            ],
            options={
                'ordering': ('source',),
            },
        ),
        migrations.CreateModel(
            name='HistoricalConcept',
            fields=[
                ('id', models.CharField(db_index=True, editable=False, max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('brand', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.brand')),
                ('coding_system', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='codelist.codingsystem')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.publicationstatus')),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical concept',
                'verbose_name_plural': 'historical concepts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_concept_brand', to='core.brand')),
                ('coding_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coding_system_data', to='codelist.codingsystem')),
                ('components', models.ManyToManyField(blank=True, related_name='related_components', to='concepts.component')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='concept_creator', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='concept_publication_status', to='core.publicationstatus')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='concept_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='coderule',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concepts.component'),
        ),
    ]