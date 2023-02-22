SECRET_KEY = "IDONTLIKESPAM"

USE_TZ = True

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

INSTALLED_APPS = [
    "django_bootstrap5",
    "django_bootstrap_input_group",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    }
]

BOOTSTRAP5 = {
    'wrapper_class': 'test-wrapper-class',
    'inline_wrapper_class': 'test-inline-class',
    'horizontal_label_class': 'test-horizontal-label',
    'horizontal_field_class': 'test-horizontal-field',
}
