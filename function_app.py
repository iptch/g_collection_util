import logging
import azure.functions as func
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = func.FunctionApp()

@app.schedule(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    spreadsheet_id = "1tJqBrGq_GBXwA8KDrJ3gGNHz_Z5EKxtVYbVeBvqtrZg"

    credentials = service_account.Credentials.from_service_account_file("g-collection-400509-fcf0b43151e3.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
    service = build("sheets", "v4", credentials=credentials)

    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range="A:Z")
    sheet_props = request.execute()

    df = pd.DataFrame(sheet_props['values'][1:], columns=sheet_props['values'][0])

    print(df)
