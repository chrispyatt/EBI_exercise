from django.shortcuts import render
from django.db.models.base import ObjectDoesNotExist
from django.views.generic import ListView
from quickstart.models import Genome, Data_Release, Genome_Database, Organism
from quickstart.serializers import GenomeDatabaseSerializer, GenomeSerializer, OrganismSerializer, DataReleaseSerializer, ResultSerializer
from rest_framework.renderers import JSONRenderer


# Create your views here.


class Result:
    def __init__(self, dbtype, species, sci_name, release, dbname):
        self.dbtype = dbtype
        self.species = species
        self.sci_name = sci_name
        self.release = release
        self.dbname = dbname



class HomePageView(ListView):
    '''Renders home page.'''
    model = Genome_Database
    template_name = 'home.html'

    def get_queryset(self):
        search_dict = {}
        filter_str = ""
        if self.request.GET.get('search'):
            try:
                query = self.request.GET.get('org')
                print(query)
                org_id = Organism.objects.get(name=query).organism_id
                print(f'org_id {org_id}')
                print(type(org_id))
                gen_id = Genome.objects.get(organism_id=org_id).genome_id
                print(gen_id)
                search_dict['org'] = Genome_Database.objects.filter(genome_id=gen_id)
                #print(search_dict)
                filter_str.append('Organism name: ' + query + ', ')
            except ObjectDoesNotExist:
                pass
            try:
                query = self.request.GET.get('dbtype')
                print(query)
                search_dict['db'] = Genome_Database.objects.filter(type=query)
                filter_str.append('Database type: ' + query + ', ')
            except ObjectDoesNotExist:
                pass
            try:
                query = self.request.GET.get('rel')
                print(query)
                rel_id = Data_Release.objects.get(ensembl_version=query).data_release_id
                gen_id = Genome.objects.get(data_release_id=rel_id).genome_id
                search_dict['rel'] = Genome_Database.objects.filter(genome_id=gen_id)
                filter_str.append('Ensembl release: ' + query + ', ')
            except ObjectDoesNotExist:
                pass
        else:
            pass

        serializer = ResultSerializer(search_dict)
        json = JSONRenderer().render(serializer.data)
        return json



def get_db_id():
    pass

def get_org_id():
    pass

def get_release_id():
    pass

