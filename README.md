# EBI_exercise


This application is intended to be a REST API endpoint allowing queries of the ensembl_metadata_106 database

The application can be run via the manage.py runserver command, and searches performed either by using the search boxes on the main page or via constructing a URL search string.

The application will return a list of databases matching your search criteria, in JSON format.






NOTE: needs routers (I think) to fix the foreign key issue (looks for non-existent _id_id field when searching for genome_id)