import os
from decouple import config

#MySQL Database setting
DATABASES ={
    'default':{
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'Purdue',
        'USER' : 'root',
        'PASSWORD' : config('DB_PASSWORD'),
        'HOST':'localhost',
        'PORT' : '3306',
    }
}

SECRET_KEY = "django-insecure-97e7xm1m9a%-w@*#=abd+p49d0qcr0o(kfjy#l6nz(+umh7*ai"