from quickstart.models import Genome, Data_Release, Genome_Database, Organism, Result
from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    class Meta:
        model = Result
        fields = ['species', 'sci_name', 'release', 'dbtype', 'dbname']


class GenomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genome
        fields = ['genome_id', 'data_release_id', 'organism_id']


class DataReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data_Release
        fields = ['ensembl_version', 'data_release_id']


class GenomeDatabaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genome_Database
        fields = ['genome_id', 'genome_database_id', 'dbname', 'type']


class OrganismSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organism
        fields = ['name', 'scientific_name', 'organism_id']
