from django.db import models

# Create your models here.

class Results(models.Model):
    organism_id = models.ForeignKey(organism, on_delete=models.CASCADE)
    result_id = models.AutoField(primary_key=True)
    genome_database_id = models.ForeignKey(genome_database, on_delete=models.CASCADE)
    data_release_id = models.ForeignKey(data_release, on_delete=models.CASCADE)
    genome_id = models.ForeignKey(Genome, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'results'


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

