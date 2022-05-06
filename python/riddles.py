from bs4 import BeautifulSoup
import sys
import json
from urllib.request import urlopen


def get_riddle():
	url = 'https://www.riddles.com/riddle-of-the-day'
	page = urlopen(url)
	soup = BeautifulSoup(page)
	riddles = soup.findAll("blockquote", {"class": "orange_dk_blockquote hidden-print"})
	latest_riddle = str(riddles[0])

	answers = soup.findAll("blockquote", {"class": "dark_purple_blockquote"})
	latest_answer = str(answers[0])

	latest_riddle_len = len(latest_riddle)
	latest_answer_len = len(latest_answer)


	riddle_open_tag_len= 57
	answer_open_tag_len = 46
	end_tag_len = 17
	riddle_last_cut = latest_riddle_len - end_tag_len
	answer_last_cut = latest_answer_len - end_tag_len

	riddle = latest_riddle[riddle_open_tag_len:riddle_last_cut]
	answer = latest_answer[answer_open_tag_len:answer_last_cut]

	riddle_object = []
	riddle_object.append(riddle)
	riddle_object.append(answer)

	return riddle_object
	#f = open("riddle.json","w+")
	#json.dump(riddle_object, f)
	#f.close()

	#sys.stdout.flush()



def main():
    get_riddle()

    

if __name__ == "__main__":
    main()