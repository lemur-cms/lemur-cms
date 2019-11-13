


class Default(object):

    core = ['cms']

    @property
    def apps(self):
        return [
            # feincms defaults
            'feincms',
            'feincms.module.medialibrary',
            'feincms.module.page',
            # django defaults
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.sitemaps',
            # rest and filters
            'corsheaders',
            'rest_framework',
            'django_filters',
            # django extensions
            'django_extensions',
        ]

    @property
    def middlewares(self):
        MIDDLEWARE = [
            'corsheaders.middleware.CorsMiddleware',
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

        # Add locale after session and before common
        MIDDLEWARE += ['django.middleware.locale.LocaleMiddleware']
        MIDDLEWARE += ['django.middleware.common.CommonMiddleware']

        return MIDDLEWARE

    @property
    def context_processors(self):
        """return CORE Conent Type Processors
        """
        cp = [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]

        return cp
