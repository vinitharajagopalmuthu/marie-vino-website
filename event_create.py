from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

creds = Credentials.from_authorized_user_file("token.json")
service = build("calendar", "v3", credentials=creds)

event = {
    "summary": "Product Demo Webinar",
    "description": "Live demo session",
    "start": {
        "dateTime": "2026-03-20T10:00:00",
        "timeZone": "Asia/Kuala_Lumpur",
    },
    "end": {
        "dateTime": "2026-03-20T11:00:00",
        "timeZone": "Asia/Kuala_Lumpur",
    },
}

created_event = service.events().insert(
    calendarId="primary",
    body=event
).execute()

print(created_event["id"])