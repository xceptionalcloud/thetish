https://developers.google.com/calendar/quickstart/python

Authorizing requests with OAuth 2.0
All requests to the Google Calendar API must be authorized by an authenticated user.

The details of the authorization process, or "flow," for OAuth 2.0 vary somewhat depending on what kind 
of application you're writing. The following general process applies to all application types:

When you create your application, you register it using the Google API Console. Google then provides 
information you'll need later, such as a client ID and a client secret.

Activate the Google Calendar API in the Google API Console. (If the API isn't listed in the API Console, 
then skip this step.)

When your application needs access to user data, it asks Google for a particular scope of access.

Google displays a consent screen to the user, asking them to authorize your application to request some of their data.

If the user approves, then Google gives your application a short-lived access token.

Your application requests user data, attaching the access token to the request.

If Google determines that your request and the token are valid, it returns the requested data.

Some flows include additional steps, such as using refresh tokens to acquire new access tokens. For 
detailed information about flows for various types of applications, see Google's OAuth 2.0 documentation.

Here's the OAuth 2.0 scope information for the Google Calendar API:

https://www.googleapis.com/auth/calendar	read/write access to Calendars -----
https://www.googleapis.com/auth/calendar.readonly	read-only access to Calendars
https://www.googleapis.com/auth/calendar.events	read/write access to Events
https://www.googleapis.com/auth/calendar.events.readonly	read-only access to Events
https://www.googleapis.com/auth/calendar.settings.readonly	read-only access to Settings
https://www.googleapis.com/auth/calendar.addons.execute	run as a Calendar add-on

To request access using OAuth 2.0, your application needs the scope information, as well as information 
that Google supplies when you register your application (such as the client ID and the client secret).

Tip: The Google APIs client libraries can handle some of the authorization process for you. They are 
available for a variety of programming languages; check the page with libraries and samples for more details.
