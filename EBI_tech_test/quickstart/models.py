from django.db import models

# Create your models here.

class Result(models.Model):
    species = models.CharField(max_length=200)
    sci_name = models.CharField(max_length=200)
    release = models.IntegerField()
    dbtype = models.CharField(max_length=200)
    dbname = models.CharField(max_length=200)


class Data_Release(models.Model):
    ensembl_version = models.PositiveIntegerField()
    data_release_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'data_release'


class Organism(models.Model):
    name = models.CharField(max_length=128)
    scientific_name = models.CharField(max_length=128)
    organism_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'organism'


class Genome(models.Model):
    genome_id = models.AutoField(primary_key=True)
    data_release_id = models.ForeignKey(Data_Release, on_delete=models.PROTECT)
    assembly_id = models.PositiveIntegerField()
    organism_id = models.ForeignKey(Organism, on_delete=models.PROTECT)
    genebuild = models.CharField(max_length=255)
    division_id = models.PositiveIntegerField()
    has_pan_compara = models.PositiveIntegerField()
    has_variations = models.PositiveIntegerField()
    has_peptide_compara = models.PositiveIntegerField()
    has_genome_alignments = models.PositiveIntegerField()
    has_synteny = models.PositiveIntegerField()
    has_other_alignments = models.PositiveIntegerField()
    has_microarray = models.PositiveIntegerField()
    website_packed = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'genome'
        unique_together = (('data_release_id', 'genome_id', 'division_id'),)


class Genome_Database(models.Model):
    genome_id = models.ForeignKey(Genome, on_delete=models.PROTECT)
    genome_database_id = models.AutoField(primary_key=True)
    dbname = models.CharField(max_length=64)
    type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'genome_database'
