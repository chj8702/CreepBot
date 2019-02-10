~SpotBot~
-Written by Connor Jackson (with heavy inspiration from Slack's tutorial)

SpotBot is a Slack bot that is designed to do polling and point tracking for
the CSH #creepshots channel.

It is written in python, using Flask for routing/web stuff. It consists primarily of app.py, which handles incoming JSON, and bot.py, which handles POST requests 

SpotBot utilizes Slack's Event API to listen for and forward events. It's pretty nice because it means that the bot doesn't have to listen to everthing, instead Slack will :)
