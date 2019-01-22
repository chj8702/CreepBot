"""
App.py, Connor Jackson
Used for routing requests
"""

from flask import Flask, request, make_response
import json
import bot

app = Flask(__name__)

def event_handler(type, slack_event):
    # If file shared, bot.react
    # If emoticon react, bot.log_reaction
    # If @creepbot (probably for leaderboard), bot.respond
    # Else, event not found error
    if type == "file_shared":
        ts = slack_event["event"]["event_ts"]
        channel = slack_event["event"]["channel_id"]
        bot.react(ts, channel)

    if type == "reaction_added":
        if slack_event["event"]["item"]["type"] == "message":
            ts = slack_event["event"]["event_ts"]
            file = slack_event["event"]["item"]["file"]
            reaction = slack_event["event"]["reaction"]
            bot.log_reaction(ts, file, reaction)

    if type == "reaction_removed":
        if slack_event["event"]["item"]["type"] == "file":
            ts = slack_event["event"]["event_ts"]
            file = slack_event["event"]["item"]["file"]
            reaction = slack_event["event"]["reaction"]
            bot.reaction_redact(ts, file, reaction)

    if type == "app_mention":
        channel = slack_event["event"]["channel"]
        bot.respond(channel)

    else:
        return make_response("[NOT SUBSCRIBED EVENT] Sorry, I don't know that event", 404, {"X-Slack-No_Retry": 1})


@app.route("/", methods=["GET", "POST"])
def listen():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

    if "event" in slack_event:
        type = slack_event["event"]["type"]
        return event_handler(type, slack_event)

    if bot.verification != slack_event.token("token"):
        message = "Invalid Slack verification token: %s \npyBot has: %s\n\n" % (
            slack_event["token"], bot.verification)
        make_response(message, 403, {"X-Slack_No_Retry": 1})

    return make_response("[NO EVENT IN SLACK REQUEST] I don't know how to deal with that", 404, {"X-Slack-No_Retry": 1})


if __name__ == '__main__':
    app.run(debug=True)