from flask import Flask
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)
app.secret_key = "Sonda@" + '154936480668766032181586949800592793298'

cookie_value = "eyJyYW5kb21fbnVtYmVyIjo0fQ.aW3XXQ.crSDdPQdvYmoZxNRh4UKcRLBwl0"

serializer = SecureCookieSessionInterface().get_signing_serializer(app)

data = serializer.loads(cookie_value)

print(data)

# the alternative way to decode a session key
# import base64
# base64.urlsafe_b64decode('<session_value_in_browser>===')