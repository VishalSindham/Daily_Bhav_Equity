# importing required modules
import urllib.request 
import schedule
import time 
from zipfile import ZipFile
from datetime import datetime
import csv 
import os 
def dataFetch():
    print('i was here fetch')
    try:
        today ='EQ'+ datetime.today().strftime('%d%m%y')+'_CSV.ZIP'
        # today = 'EQ040521_CSV.ZIP'
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'whatever')
        url = 'https://www.bseindia.com/download/BhavCopy/Equity/'+today
        todays_data = today
        # print(url,todays_data,sep='\n')
        opener.retrieve(url, todays_data)
        # opener.retrieve('https://www.bseindia.com/download/BhavCopy/Equity/EQ030521_CSV.ZIP', 'EQ030521_CSV.ZIP')
        # https://www.bseindia.com/download/BhavCopy/Equity/EQ030521_CSV.ZIP sample url 
    
        # specifying the zip file name
        file_name = todays_data

        # opening the zip file in READ mode
        with ZipFile(file_name, 'r') as zip:
            # printing all the contents of the zip file
            # zip.printdir()

            # extracting all the files
            # print('Extracting all the files now...')
            zip.extractall()
            print('Done!')
    except :
        pass
def flush_data():
    try:
        os.system('python manage.py flush --no-input')
        print('data flused')
    except:
        pass
def enter_data():
    print('i was here ')
    try:
        ample_data = open('data_fetch.py')
        ramp = ample_data.read()
        exec(ramp)
        print('data entry done')
    except:
        pass

    

schedule.every().day.at('18:00').do(dataFetch)
schedule.every().day.at('18:05').do(enter_data)
schedule.every().day.at('17:50').do(flush_data)
while True :
    schedule.run_pending()
    time.sleep(1)
    