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
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'creds/credentials.json'
    credentials = service_account.Credentials.from_service_account_file(
        filename=SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    return credentials

# Principal
def main():
    creds = spreadsheetApi()
    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    rangeName = 'Test'
    result = sheet.values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    return values

if __name__ == '__main__':
    print(main())