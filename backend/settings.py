from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Media ──────────────────────────────────────────────────────────────────────
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ── Seguridad / Debug ──────────────────────────────────────────────────────────
# Por defecto True en local. En Render pondremos DEBUG=False en variables de entorno.
DEBUG = os.getenv("DEBUG", "True").strip().lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-unsafe")

# ALLOWED_HOSTS: en local permite localhost; en prod usa env.
_hosts_env = os.getenv("ALLOWED_HOSTS", "")
if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = [h.strip() for h in _hosts_env.split(",") if h.strip()] or ["localhost", "127.0.0.1","tu-servicio>.onrender.com"]

# ── Apps ───────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "blog",
]

# ── Middleware (orden correcto) ────────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",      # <- antes que CommonMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ── CORS / CSRF ────────────────────────────────────────────────────────────────
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://dragon-ball-react-psi.vercel.app",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://dragon-ball-react-psi.vercel.app",
    # Cuando tengas Render:
    # "https://<tu-backend>.onrender.com",
]

# ── URLs / WSGI ────────────────────────────────────────────────────────────────
ROOT_URLCONF = "backend.urls"
WSGI_APPLICATION = "backend.wsgi.application"

# ── Base de datos: sqlite en local, Postgres por DATABASE_URL en prod ──────────
default_sqlite = f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
db_url = os.getenv("DATABASE_URL", default_sqlite)
DATABASES = {
    "default": dj_database_url.parse(
        db_url,
        conn_max_age=600,
        ssl_require=db_url.startswith("postgres://") or db_url.startswith("postgresql://dragonball_backend_db_user:bTMkxUObF8wEZyr5HFoyw3hmxct6fcb0@dpg-d2vf6nq4d50c73aa452g-a.frankfurt-postgres.render.com/dragonball_backend_db"),
    )
}

# ── Password validators ────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
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
    }
]
# ── i18n / tz ─────────────────────────────────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ── Static / WhiteNoise ────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ── Default PK ────────────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
