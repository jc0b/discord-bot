FROM python:3.9.5-slim-buster
LABEL Author="Jacob Burley <j@jc0b.computer>"

RUN pip3 install python-dotenv discord.py beautifulsoup4 requests termcolor

COPY ./ /discordBot
WORKDIR /discordBot
CMD ["python3", "bot.py"]