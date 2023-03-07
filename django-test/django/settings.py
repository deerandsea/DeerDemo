import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'das',
        'USER': 'root',
        'PASSWORD': 'dhc123456',
        'HOST': 'localhost',
        'PORT': '13306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'traditional',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASE_ROUTERS = []

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, '../static')]

# mybatis mapper-locations
MAPPER_LOCATIONS = os.path.join(BASE_DIR, 'mapper')

# server port
PORT = 8080
