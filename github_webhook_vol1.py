from github_webhook import Webhook
from flask import Flask

application = Flask(__name__)  # Standard Flask application
webhook = Webhook(application) # Defines '/postreceive' endpoint

@application.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=3000)