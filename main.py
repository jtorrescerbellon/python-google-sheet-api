# Librerias a importar
import os
from dotenv import load_dotenv

from httplib2 import Http
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

# Lectura archivo .env
load_dotenv()
spreadsheetId = os.getenv('SPREADSHEET_ID')

# Funcion para conectarse con Google sheet API
def spreadsheetApi():
    pass

# Principal
def main():
    pass

if __name__ == '__main__':
    print(spreadsheetId)