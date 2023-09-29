# Preparation
pip install -r requirements.txt

# Run the function locally
In VS Code, install the Azure Functions extension.
In the terminal, run:
`func host start`
(Do NOT use the VS Code UI to run it, it always fails...)

# Current status
When running, the function does every minute:
- get credentials from azure vault for google spreadsheet-access
- get spreadsheet-data to dataframe and print it

Currently, a dummy-spreadsheet stored in my (SZE) personal gdrive is used. To use another spreadsheet:
- Share it with the google service-account: g-collection@g-collection-400509.iam.gserviceaccount.com
- Enter the spreadsheet-id in function_app.py

# Todo
- Write the dataframe to DB
- Evtl.: Automate deployment with github actions

# Deploy to azure
VS Code --> Azure Extension --> Resources --> Function App --> rightclick geniuscollection-gsheet-ingest --> Deploy to Function App...

# Used resources:
## Azure:
- geniuscollection-gsheet-ingest (Function App)
- geniuscollectiongsheetin (Resource Group)
- geniuscollection-creds (Vault)
- geniuscollectiongsheetin (Storage account)

## Google
- g-collection (Having Google Sheets and Google Drive API)
- g-collection-sa (Service Account), with email g-collection@g-collection-400509.iam.gserviceaccount.com