# Bhavcopy 
This Web Application will update the Bhavcopy of Equity segment daily and show it on the home page . the source of bhavcopy is src:https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx . Only one day is avaliable .


This web application uses Django for backend and Vuejs for Frontend default database of django and cache memory of redis .

first create virtual environment using pipenv or virtualenv and install the following python packages .

## Requirements
asgiref==3.3.4
DateTime==4.3
Django==3.2
numpy==1.20.2
pandas==1.2.4
python-dateutil==2.8.1
pytz==2021.1
redis==3.5.3
schedule==1.1.0
six==1.15.0
sqlparse==0.4.1
zope.interface==5.4.0


after configuration 

start django server first and  Vuejs server because vuejs is dependent on the django server to serve pages 
it won't throw error if did start it first .

on backend we wrote basic python script on_loop to fetch data bhavcopy daily at 6:00pm and clean database daily  on_loop it's scheduled .
run it once on other terminal and let it run .

## Deployment 

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
