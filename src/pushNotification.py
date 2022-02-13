import os
from pushbullet import Pushbullet
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("PUSHBULLET_API_KEY")
pb = Pushbullet(API_KEY)


def sendNotification(title, message):
    pb.push_note(title, message)
