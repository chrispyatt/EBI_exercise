from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Release',
            fields=[
                ('data_release_id', models.AutoField(primary_key=True)),
                ('ensembl_version', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('organism_id', models.AutoField(primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('scientific_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('genome_id', models.AutoField(primary_key=True)),
                ('data_release_id', models.ForeignKey(on_delete=models.deletion.PROTECT, to='quickstart.Data_Release')),
                ('organism_id', models.ForeignKey(on_delete=models.deletion.PROTECT, to='quickstart.Organism')),
            ],
        ),
        migrations.CreateModel(
            name='Genome_Database',
            fields=[
                ('genome_database_id', models.AutoField(primary_key=True)),
                ('genome_id', models.ForeignKey(on_delete=models.deletion.PROTECT, to='quickstart.Genome')),
                ('dbname', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=64)),
            ],
        ),
    ]
