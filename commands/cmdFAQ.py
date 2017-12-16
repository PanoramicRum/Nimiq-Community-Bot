def get_faq(bot, update, args):
	import yaml
	import re
	args = [re.sub(r'[^a-zA-Z0-9_\-$]', r'', arg)[:100] for arg in args]
	key_max = 0
	faq_file = 'config/faq.yml'
	score_dict = {'':''}
	with open(faq_file, 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
		for id in cfg:
			wordcount = 0
			for item in args:
				word = item.replace("?", "")
				loword = word.lower()
				if loword in cfg[id]['words']:
					wordcount += 1
			score_dict[cfg[id]['id']] = wordcount
		max = 0
		for key, value in score_dict.items():
			if value != '':
				if int(value) > max:
					max = int(value)
					key_max = int(key)
		answer=cfg[key_max]['answer'] if  key_max > 0 else "Sorry. I don't know"
	bot.sendMessage(update.message.chat_id, text=answer, parse_mode='Markdown')
