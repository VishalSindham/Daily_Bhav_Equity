import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bhav.settings")

import django
django.setup()

from django.core.management import call_command
import csv
from page.models import Bhav 
from datetime import datetime
file_name = 'EQ'+datetime.today().strftime('%d%m%y')+'.CSV' #replace this in the filename argument
try:
    with open(file_name) as csvfile: 
        reader = csv.DictReader(csvfile) 
        for row in reader: 
            p = Bhav(SC_CODE = row['SC_CODE'],SC_NAME= row['SC_NAME'],SC_GROUP= row['SC_GROUP'],SC_TYPE = row['SC_TYPE'],OPEN = row['OPEN'],HIGH = row['HIGH'],LOW = row['LOW'],CLOSE = row['CLOSE'],LAST = row['LAST'],PREVCLOSE = row['PREVCLOSE'],NO_TRADES= row['NO_TRADES'],NO_OF_SHRS= row['NO_OF_SHRS'],NET_TURNOV= row['NET_TURNOV'],TDCLOINDI= row['TDCLOINDI'])
            p.save()
except:
    pass