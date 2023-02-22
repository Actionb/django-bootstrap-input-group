SECRET_KEY = "IDONTLIKESPAM"

USE_TZ = True

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

INSTALLED_APPS = [
    "django_bootstrap5",
    "django_bootstrap_input_group",
]

ROOT_URLCONF = "tests.urls"

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # required for django.contrib.admin
    "django.contrib.messages.middleware.MessageMiddleware",  # required for django.contrib.admin
)

STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

BOOTSTRAP5 = {
    'wrapper_class': 'test-wrapper-class',
    'inline_wrapper_class': 'test-inline-class',
    'horizontal_label_class': 'test-horizontal-label',
    'horizontal_field_class': 'test-horizontal-field',
}
