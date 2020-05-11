FROM python
MAINTAINER Jacob Burley <j@jc0b.computer>
COPY ./ /discordBot
RUN cd /discordBot \
	&& pip3 install python-dotenv discord.py beautifulsoup4 requests termcolor \
	&& echo "Making sure that .env exists..." \
	&& test -f .env
WORKDIR /discordBot
CMD ["python3", "bot.py"]