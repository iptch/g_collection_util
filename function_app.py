import logging
import azure.functions as func
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import json

app = func.FunctionApp()

@app.schedule(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


    vault_url = "https://geniuscollection-creds.vault.azure.net/"
    secret_name = "google-api-access-key"

    # Create a secret client
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=vault_url, credential=credential)

    # Get the secret
    secret_value = secret_client.get_secret(secret_name).value



    spreadsheet_id = "1tJqBrGq_GBXwA8KDrJ3gGNHz_Z5EKxtVYbVeBvqtrZg"

    credentials = service_account.Credentials.from_service_account_info(json.loads(secret_value), scopes=["https://www.googleapis.com/auth/spreadsheets"])
    service = build("sheets", "v4", credentials=credentials)

    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range="A:Z")
    sheet_props = request.execute()

    df = pd.DataFrame(sheet_props['values'][1:], columns=sheet_props['values'][0])

    print(df)
    logging.info(df)
