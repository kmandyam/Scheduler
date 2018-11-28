from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def main():
    """
    Prints all calendar events for tomorrow
    """
    events = get_events()
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def get_events():
    """
    Returns a list of a calendar events for tomorrow
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    tomorrow_morning = datetime.datetime.utcnow().isoformat() + 'Z'
    tomorrow_evening = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    tomorrow_evening = tomorrow_evening.isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary', timeMin=tomorrow_morning,
                                        timeMax=tomorrow_evening,
                                        maxResults=5, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events

if __name__ == '__main__':
    main()
