from flask import Flask, redirect,flash,get_flashed_messages, render_template, request, make_response, session, abort, jsonify, url_for
import secrets
from functools import wraps
import firebase_admin
from firebase_admin import credentials, firestore, auth
from datetime import timedelta
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2 import service_account

# from dotenv import load_dotenv

# load_dotenv()



app = Flask(__name__)
app.secret_key = 'thisismysuperdupersecretkey'  # Replace with a strong secret key

# # Configure session cookie settings
# app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookies are sent over HTTPS
# app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent JavaScript access to cookies
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)  # Adjust session expiration as needed
# app.config['SESSION_REFRESH_EACH_REQUEST'] = True
# app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Can be 'Strict', 'Lax', or 'None'

CLIENT_SECRETS_FILE = "marie-vinodh-wedding-firebase-adminsdk-fbsvc-1f3278a429.json"
OAUTH_SECRETS_FILE = "client_secret_1072481959116-ueh8o7ppgtaa65mlq0mpnqj9mmittrhr.apps.googleusercontent.com.json"
cred = credentials.Certificate(CLIENT_SECRETS_FILE)
firebase_admin.initialize_app(cred)
db = firestore.client()
print(db.project)
app.config['SECRET_KEY'] = 'hellomynameisvinitharaj' # Replace with a strong secret key


SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = CLIENT_SECRETS_FILE

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build("calendar", "v3", credentials=credentials)

EVENT_ID = "auhq1u1r5aosq6nri1k6aoic10"
CALENDAR_ID = "34ebfe522a3413e10d368bd2981dacd0361fdc91eb0237d9d0ed997370937c35@group.calendar.google.com"
def add_attendee(email):
    
    event = service.events().get(
        calendarId=CALENDAR_ID,
        eventId=EVENT_ID
    ).execute()

    attendees = event.get("attendees", [])

    if email not in [a["email"] for a in attendees]:
        attendees.append({"email": email})

    event["attendees"] = attendees

    service.events().update(
        calendarId=CALENDAR_ID,
        eventId=EVENT_ID,
        body=event,
        sendUpdates="all"
    ).execute()
    
@app.route('/', methods=['GET','POST'])
def home():
    email=None
    if request.is_json:
        data = request.get_json()
        name = data.get('name2')
        email = data.get('email2')
        malaysianceremony = data.get('malaysianceremony')
        canadianceremony = data.get('canadianceremony')
        print(f"Received JSON data: Name: {name}, Email: {email}, Malaysian Ceremony: {malaysianceremony}, Canadian Ceremony: {canadianceremony}")
    name = request.form.get('name2')
    messages = get_flashed_messages(with_categories=True)
    if name:
        print(name)
    # email=None
    # email = request.form.get('email2')
    if email:
        print(f"Received email: {email}")
        add_attendee(email)
        print(f"Added {email} to Google Calendar event attendees.")
    malaysianceremony = request.form.get('malaysianceremony')
    canadianceremony = request.form.get('canadianceremony')
    if malaysianceremony:
        print("Received Malaysian Ceremony attendance",malaysianceremony)
    if canadianceremony:
        print("Received Canadian Ceremony attendance",canadianceremony)
    print(F"Received name: {name}")
    if name:
        doc_ref = db.collection('message').add(
            {
                'name': name,
                'email': email,
                'malaysian_ceremony': malaysianceremony,
                'canadian_ceremony': canadianceremony
            }
            )
        print(f"Document added with ID: {doc_ref[1].id}")
    return render_template('home.html', messages=messages) 

if __name__ == '__main__':
    app.run(debug=True)