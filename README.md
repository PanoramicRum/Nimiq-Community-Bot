# [Nimiq](https://nimiq.com/) Community Bot

Aid with common questions by the community and queries to the [NET Smart Contract](https://etherscan.io/token/NimiqNetwork).

## Quickstart

The bot has the following commands:
### /question 

Searches for keywords in the user's question and matches it with the most accurate answer found in the [YAML FAQ file](.././config/faq.yml).

### /net 

Queries the NET Smart Contract for useful information (balances, address, number of transactions). The second argument of the command tells the bot the type of query:
 - balance: Asks for the balance of an address. Input the address. Example: `/net balance 0x8d12a197cb00d4747a1fe03395095ce2a5cc6819`
 - whales: Lists the 10 addresses with higher balance of NET.

## Requirements

- Python latest version.
- Python module `telegram`

## Usage

If you want to install your own copy of the bot, test and improve it follow this steps:

- Get an account in [Etherscan](https://etherscan.io/) and copy your API Token.
- Talk to [Telegram's Botfather](https://core.telegram.org/bots) to get a Bot Token.
- git clone https://github.com/PanoramicRum/Nimiq_Bot.git
- Open [config/botcfg.yml](./config/botcfg.yml) and add your Etherscan Token.
- Run the bot using `python ./bot.py`
