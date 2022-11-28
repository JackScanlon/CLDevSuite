import os
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

# CORS
ALLOWED_HOSTS = ['localhost', 'localhost:8008', '127.0.0.1', '127.0.0.1:8008', 'nginx', 'nginx:8008', 'app']
CSRF_TRUSTED_ORIGINS = ['http://localhost', 'http://localhost:8008', 'http://127.0.0.1', 'http://127.0.0.1:8008', 'http://nginx', 'http://nginx:8008', 'http://app']

# Crumb map
BREADCRUMB_MAP = {
    'home': {
        'url': 'pages:home',
        'title': 'Home'
    },
    'phenotypes': {
        'url': 'phenotypes:phenotypes',
        'title': 'Phenotypes'
    },
    'create-phenotypes': {
        'url': 'phenotypes:create_phenotypes',
        'title': 'Create Phenotypes'
    },
    'login': {
        'url': 'account_login',
        'title': 'Login'
    }
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Version control
    'simple_history',

    # Include local Apps
    'apps.accounts.apps.AccountsConfig',
    'apps.core.apps.CoreConfig',
    'apps.organisation.apps.OrganisationConfig',
    'apps.codelist.apps.CodelistConfig',
    'apps.concepts.apps.ConceptsConfig',
    'apps.phenotypes.apps.PhenotypesConfig',
    'apps.tasks.apps.TasksConfig',

    # Allauth package
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # SCSS processor package
    'sass_processor',

    # ElasticSearch
    'django_elasticsearch_dsl',

    # Celery
    'celery',
    'django_celery_results',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'breadcrumbs': 'apps.core.templatetags.breadcrumbs',
                'tooling': 'apps.core.templatetags.tooling',
            },
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', ''),
        'NAME': os.environ.get('DB_NAME', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
    }
}


# Password validation
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


# Internationalisation
LANGUAGE_CODE = os.environ.get('BASE_LANG_CODE', 'en-gb')

LANGUAGES = (
    ('en-gb', _('English')),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

TIME_ZONE = os.environ.get('BASE_TIME_ZONE', 'GMT')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (SCSS, CSS, JavaScript)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, os.environ.get('STATICFILES', 'static'))
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'shared/static'),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    # SCSS compilation
    'sass_processor.finders.CssFinder',
]

# Media (Images, videos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, os.environ.get('MEDIAFILES', 'static'))
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, 'shared/media'),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SCSS processor config
SASS_PROCESSOR_ENABLED = bool(int(os.environ.get('SASS_ENABLED', 1)))
SASS_PROCESSOR_AUTO_INCLUDE = True
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
SASS_OUTPUT_STYLE = 'compact'

# Authentication config
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_USER_MODEL = 'accounts.UserAccount'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# User Accounts config
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none' # Change to 'mandatory' if you want email verification
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Concept Library'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
SOCIALACCOUNT_AUTO_SIGNUP = False

# User Accounts limits
ACCOUNT_LOGIN_ATTEMPTS_LIMIT   = 5     # Max login attempts
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300   # Timeout for 300s after 5 failed login attempts
ACCOUNT_PASSWORD_MIN_LENGTH    = 12    # Min password len

ACCOUNT_RATE_LIMITS = {
    # Change password view (for users already logged in)
    'change_password': '5/m',
    # Email management (e.g. add, remove, change primary)
    'manage_email': '10/m',
    # Request a password reset, global rate limit per IP
    'reset_password': '20/m',
    # Rate limit measured per individual email address
    'reset_password_email': '5/m',
    # Password reset (the view the password reset email links to).
    'reset_password_from_key': '20/m',
    # Signups.
    'signup': '20/m',
}

ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 180  # User can only request a new email for verification every 180s
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3 # Verification emails expire after 3 days

# JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(os.environ.get('ACCESS_TOKEN_LIFETIME', 5))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.environ.get('REFRESH_TOKEN_LIFETIME', 1))),
}

# ElasticSearch config
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': os.getenv('ELASTICSEARCH_DSL_HOSTS', 'localhost:9200')
    },
}

# Redis and Celery configuration
CELERY_ENABLED = True
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'default'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TASK_TRACK_STARTED = True
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'