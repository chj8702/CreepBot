"""
bot.py, Connor Jackson
Used for responding to events
"""

import os
from slackclient import SlackClient

slack_token = os.environ["SLACK_BOT_TOKEN"]
oauth_token = os.environ["SLACK_OAUTH_TOKEN"]
sc = SlackClient(slack_token)

def verification():
    return oauth_token

def react(ts, channel):
    print("This is me, reacting")


def log_reaction(ts, file, reaction):
    print("This is me, logging a reaction to a file")
    pass

def reaction_redact(ts, file, reaction):
    print("This is me, taking note that you removed your reaction ")
    pass

def respond(channel):
    print("This is me, recognizing that you said something")
    sc.api_call(
        "chat.postMessage",
        channel=channel,
        text="I hear you, but I dont know what you're saying (yet)"
    )