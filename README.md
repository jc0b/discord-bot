# discord-bot: A framework for writing Discord bots in Python
Based on an implementation co-written with [A-Artemis](https://github.com/A-Artemis).

## Requirements
* Python 3.8 or higher and/or Docker

## Setup
1. Clone or pull the git repository. 
2. Copy the `.env.example` file to a `.env` file, and add the Discord token as well as the Server ID to it: `cp .env.example .env`
3. Install the following Python libraries by typing in in the terminal: `pip3 install python-dotenv nextcord beautifulsoup4 requests`
4. Run the bot with `python3 python/bot.py`, or using Docker which is explained in a later section.

## Commands
* `!flip`: Flip a coin. Decide your fate.
* `!hello`: Hello, world!
* `!pick [choice1, choice2,...,choice999]`: Picks randomly from a set of comma-seperated values.
* `!roll (x)` : Rolls a 6 sided die, or an x side die if used.
* `!riddle`: Lists the riddle of the day scraped from riddles.com.

# Docker
There is also a Dockerfile available for this bot, which makes setup a little easier.
## Docker setup with Dockerfile
1. Make sure you have docker installed
2. Pull this repo: `git clone git@github.com:jc0b/discord-bot.git`
3. Copy the `.env.example` file to a `.env` file, and add the Discord token as well as the Server ID to it: `cp .env.example .env`
4. Run `docker build -t discordbot ./python/` to build the docker image.
5. Run `docker run -d --name discord_bot discordbot` in order to then run a container based off of that image, with the container having the name `discord_bot`

You can then use `docker ps` to obtain a list of all running containers, and use `docker stop <id>` using either the `CONTAINER ID` or `NAME` to specify which container you want to stop.

## Docker setup with docker-compose
1. Make sure you have Docker and Docker Compose installed.
2. Pull this repo: `git clone git@github.com:jc0b/discord-bot.git`
3. Copy the `.env.example` file to a `.env` file, and add the Discord token as well as the Server ID to it: `cp .env.example .env`
4. Run `docker-compose build` to build the docker image, and then `docker-compose up -d` to run the image (detached - omit the `-d` if you want to attach the container to your current terminal session).
5. To terminate the bot, run `docker-compose down`.

Tip: You only have to run build if you make changes to any of the source, otherwise `docker-compose up` will use the last build.
