import os

class Config(object):

    TOKEN = os.environ.get("TOKEN", "7257365475:AAEbUPcrpqOjaFBpjgxNLNvLITO0iV1pMWM")

    API_ID = int(os.environ.get("API_ID", "29712556"))

    API_HASH = os.environ.get("API_HASH", "ecfb01f9c3b7f307470afb79d8a6d154")

    DB_NAME = os.environ.get("DB_NAME","cluster0")

    DB_URL = os.environ.get("DB_URL","mongodb+srv://nisanonisano2:<nisanonisano2>@cluster0.p2faypc.mongodb.net/?retryWrites=true&w=majority")

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Vinencoo")
