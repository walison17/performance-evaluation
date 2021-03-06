# Generated by Django 2.2.6 on 2019-10-12 16:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import performance_evaluation.evaluations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('year', models.PositiveIntegerField(default=performance_evaluation.evaluations.models.current_year, verbose_name='Ano')),
                ('rated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rated_evaluations', to='employees.Employee', verbose_name='Avaliado')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Habilidade',
                'verbose_name_plural': 'Habilidades',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EvaluationSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField(verbose_name='Nota')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_skills', to='evaluations.Evaluation', verbose_name='Avaliação')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_skills', to='evaluations.Skill', verbose_name='Habilidade')),
            ],
            options={
                'verbose_name': 'Habilidade',
                'verbose_name_plural': 'Habilidades',
                'ordering': ['-skill__name'],
            },
        ),
        migrations.AddField(
            model_name='evaluation',
            name='skills',
            field=models.ManyToManyField(related_name='evaluations', through='evaluations.EvaluationSkill', to='evaluations.Skill'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='valuator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='valuator_evaluations', to='employees.Employee', verbose_name='Avaliador'),
        ),
    ]
