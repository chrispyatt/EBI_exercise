# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Genome(models.Model):
    genome_id = models.AutoField(primary_key=True)
    data_release_id = models.PositiveIntegerField()
    assembly_id = models.PositiveIntegerField()
    organism_id = models.PositiveIntegerField()
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


