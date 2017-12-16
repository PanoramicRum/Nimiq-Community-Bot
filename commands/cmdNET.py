def get_net(bot, update, args):
	import json
	import requests
	import yaml
	import re
	args = [re.sub(r'[^a-zA-Z0-9_\-$]', r'', arg)[:100] for arg in args]
	dontknow = "Sorry. I don't know that information." 
	ethdiv = 1000000000000000000
	answer = dontknow
	if len(args) <= 2:
		net_file = 'config/net.yml'
		with open(net_file, 'r') as ymlfile:
			net = yaml.load(ymlfile)
		conf_file = 'config/botcfg.yml'
		with open(conf_file, 'r') as ymlcfgfile:
			cfg = yaml.load(ymlcfgfile)	
		#### No arguments	
		if len(args) == 0:	
			answer = net['info']
		#### Commands with no second argument
		elif len(args)==1:
			if args[0] == 'contributors':
				txList = requests.get('http://api.etherscan.io/api?module=account&action=txlist&address=' + net['contract'] + '&startblock=0&endblock=999999999&sort=asc&apikey=' + cfg['etherscan_token'] ).json()['result']
				cont_dict = {'':''}	
				for tx in txList:
					if tx['isError'] == '0':
						cont_dict[tx['from']]=int(tx['value'])/ethdiv
				answer = str(len(cont_dict)) + " different contributors participated in the Token Sale."		
			elif args[0] == 'supply':
#				totalSupply = requests.get('https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=' + net['contract'] + '&apikey=' + cfg['etherscan_token'] ).json()['result']
				txList = requests.get('http://api.etherscan.io/api?module=account&action=txlist&address=' + net['contract'] + '&startblock=0&endblock=999999999&sort=asc&apikey=' + cfg['etherscan_token'] ).json()['result']
				netcount = 0
				for tx in txList:
					if tx['isError'] == '0':
						netcount += int(tx['value'])/int(ethdiv)
				answer = "The total Circulating Supply of NET is " + str(netcount*175) + " NET."
			elif args[0] == 'whales':
				txList = requests.get('http://api.etherscan.io/api?module=account&action=txlist&address=' + net['contract'] + '&startblock=0&endblock=999999999&sort=asc&apikey=' + cfg['etherscan_token'] ).json()['result']
				cont_dict = {'': 0 }	
				whalecount = 0
				answer = 'These are the current NET holders sorted by balance:\n'	
				for tx in txList:
					if tx['isError'] == '0':
						cont_dict[tx['from']] = int(tx['value'])/int(ethdiv)
				orderdict = [(k, cont_dict[k]) for k in sorted(cont_dict, key=cont_dict.get, reverse=True)]
				for k, v in orderdict:
					if whalecount<5:
						answer = answer + "%s: %.2f ether\n" % (k, v)
					whalecount += 1
				
		#### Commands with a second argument
		elif len(args)==2:
			if args[0] == 'balance':
				totalBalance = requests.get('https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=' + net['contract'] + '&address=' + args[1] + '&tag=latest&apikey='+ cfg['etherscan_token'] ).json()['result']
				answer =  args[1] + ' : ' + str(int(totalBalance)/ethdiv)	+ " NET."	
			if args[0] == 'tokensale':
				txList = requests.get('http://api.etherscan.io/api?module=account&action=txlist&address=' + net['contract'] + '&startblock=0&endblock=999999999&sort=asc&apikey=' + cfg['etherscan_token'] ).json()['result']
				ethcount = 0
				count = 0	
				for tx in txList:	
			#		if count <50:
			#			answer = answer+ tx['from'] + '-'
			#		count += 1
					if tx['isError'] == '1':
						if args[1] in tx['from']:
							ethcount += int(tx['value'])/int(ethdiv)
				answer = "This address contributed " + str(ethcount) + "(" + str(ethcount*175) + " NET) to the Nimiq Token Generation Event."
		### Commands with too many arguments
		elif len(args)>2:
			answer='Too Many Arguments. /help for help' 

	bot.sendMessage(update.message.chat_id, text=answer, parse_mode='Markdown')
