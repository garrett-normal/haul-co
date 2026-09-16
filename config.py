import os

from dotenv import find_dotenv, load_dotenv

path = find_dotenv()
load_dotenv(path, override=True)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_ENGINES = {"default": "sqlite:///db.sqlite"}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or "sqlite:///db.sqlite"
    
    RECAPTCHA_PUBLIC_KEY = "6Lf-UmQsAAAAAKbEmMDYdT2FPwHwA-3E8kiLvzp5"
    RECAPTCHA_PRIVATE_KEY = os.environ.get('CAPTCHA_KEY')
    RECAPTCHA_DATA_ATTRS = {'theme': 'light'}

    # MAIL_SERVER = os.environ.get("MAIL_SERVER")
    # MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    # MAIL_USE_TLS = True  # use TLS for most SMTP providers
    # MAIL_USE_SSL = False  # use SSL only if required (never enable both)
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # MAIL_DEFAULT_SENDER = ("Haul Co", "no-reply@notifications.haul-co.org")
    # MAIL_DEBUG = True
    # MAIL_TIMEOUT = 10
    # TESTING = False