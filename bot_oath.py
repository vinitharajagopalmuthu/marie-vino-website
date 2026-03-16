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

CLIENT_SECRETS_FILE = "marie-vinodh-wedding-firebase-adminsdk-fbsvc-1f3278a429.json"
OAUTH_SECRETS_FILE = "client_secret_1072481959116-ueh8o7ppgtaa65mlq0mpnqj9mmittrhr.apps.googleusercontent.com.json"


SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = CLIENT_SECRETS_FILE

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build("calendar", "v3", credentials=credentials)

CALENDAR_ID = "34ebfe522a3413e10d368bd2981dacd0361fdc91eb0237d9d0ed997370937c35@group.calendar.google.com"

event = {
    "summary": "Marie & Vinodh Wedding",
    "description": "We;re getting married! Please join us for the celebration.",
    "start": {
        "dateTime": "2026-06-27T09:00:00",
        "timeZone": "Asia/Kuala_Lumpur",
    },
    "end": {
        "dateTime": "2026-06-27T09:30:00",
        "timeZone": "Asia/Kuala_Lumpur",
    },
}

created = service.events().insert(
    calendarId=CALENDAR_ID,
    body=event
).execute()

print(created["id"])