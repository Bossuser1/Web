
# Django add Projet

python3 manage.py startapp Bio

###2 declarer dans setting.py du repertoire Web

# Application definition 
  
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'Bio'
] 

####3 declarer les urls

   path('', include("Bio.urls")), 
] 

# install dependances
pip3 install -r Requiment.txt


