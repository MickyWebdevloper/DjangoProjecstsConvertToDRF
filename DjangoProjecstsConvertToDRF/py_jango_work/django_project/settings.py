from pathlib import Path
# made me.
import os
# productions
# import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6c69ff091ed68422654c48fda47fd8feab163368cfa3e76f4f'
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# Deployments
# DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')
DEBUG = '6c69ff091ed68422654c48fda47fd8feab163368cfa3e76f4f'

# ALLOWED_HOSTS = ['py-djngo.herokuapp.com']
ALLOWED_HOSTS = ['http://127.0.0.1:8000', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # made by me.
    'crispy_forms',
    'blog',
    'users',
    # 'api',
    'rest_framework',

    'django_filters',

    # "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "corsheaders.middleware.CorsMiddleware",  # made me corsheaders
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# production
STATIC_URL = '/static/'
# made me.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# made by me.
CRISPY_TEMPLATE_PACK = "bootstrap4"
# made by me.
LOGIN_REDIRECT_URL = 'blog-home'

LOGIN_URL = 'login'
# # email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
# EMAIL_HOST_USER = 'alirofikr@gmail.com'
# EMAIL_HOST_PASSWORD = 'Hacker@#@#1123***'

# Activate Django-Heroku.
# django_heroku.settings(locals())



# DEFAULT_RENDERER_CLASSES
# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
# 'rest_framework.renderers.BrowsableAPIRenderer',
#     ]
# }

# corsepolicy headers 
# CORS_ALLOWED_ORIGINS = [
#     # "https://example.com",
#     # "https://sub.example.com",
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]
