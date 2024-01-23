import gspread
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "15J1Nm-Q3c9vG0Fi-kl-SmiW2cB_UYfn5vKu5EkzUwDQ"
SAMPLE_RANGE_NAME = "A2:H"
#SAMPLE_RANGE_NAME = "Form Responses 3!B2:L"

gc = gspread.service_account()
wks = gc.open_by_key("15J1Nm-Q3c9vG0Fi-kl-SmiW2cB_UYfn5vKu5EkzUwDQ").sheet1

def RetrieveData():
  Data = []
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    # Iterate through rows
    for row in values:
      # Append Data in each row to list.
      rowData = [f"{row[1]}", f"{row[2]}", f"{row[3]}", f"{row[4]}", f"{row[5]}", f"{row[6]}", f"{row[7]}"]
      Data.append(rowData)
    return Data
       
  except HttpError as err:
    print(err)

# Check if cell is empty
def CheckCell(cell):
  if wks.get_values(cell) == []:
    return True
  else:
    return False

# Add data to Google Sheets  
def AddData(cell, data):
    wks.update(cell, data)

# Returns content in a row
def GetRowVals(row):
  return wks.row_values(row)

