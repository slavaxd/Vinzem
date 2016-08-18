#!/bin/bash
clear
cd /var/www/vinzem.tk/finalzem/  #path to your virtual environment
. bin/activate  #Activate your virtual environment
cd /var/www/vinzem.tk/finalzem/finalzem   #After that go to your project directory
python manage.py runserver 127.0.0.1:8001  #run django server

