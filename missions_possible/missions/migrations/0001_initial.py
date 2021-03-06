# Generated by Django 2.1.2 on 2018-10-09 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OpenEndedQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='missions.Question')),
            ],
            bases=('missions.question',),
        ),
        migrations.CreateModel(
            name='RatingQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='missions.Question')),
            ],
            bases=('missions.question',),
        ),
        migrations.AddField(
            model_name='question',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.Mission'),
        ),
    ]
