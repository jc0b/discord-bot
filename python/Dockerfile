FROM python:3-slim-buster
LABEL Author="Jacob Burley <j@jc0b.computer>"

RUN pip3 install python-dotenv nextcord beautifulsoup4 requests

COPY ./ /discordBot
WORKDIR /discordBot
CMD ["python3", "bot.py"]