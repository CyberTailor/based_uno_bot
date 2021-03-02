# UNO Bot

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](./LICENSE)

Telegram Bot that allows you to play the popular card game UNO via inline
queries. The bot currently runs as [@unleftbot](https://t.me/unleftbot).

To run the bot yourself, you will need: 
- Python (tested with 3.4+)
- The [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) module
- [Pony ORM](https://ponyorm.com/)

## Extra features/fixes in this fork
- Queer leftist redesign of UNO cards
    - black "choose color" cards → anarcho-communism flag
    - blue cards → transgender pride flag
    - green cards → nonbinary pride flag
    - red cards → rainbow flag
    - yellow cards → pansexual pride flag
- Added white stroke to some option stickers

## Setup
- Get a bot token from [@BotFather](https://t.me/BotFather) and change
  configurations in `config.json`.
- Convert all language files from `.po` files to `.mo` by executing the bash
  script `compile.sh` located in the `locales` folder. Another option is:
  `find . -maxdepth 2 -type d -name 'LC_MESSAGES' -exec bash -c 'msgfmt {}/unobot.po -o {}/unobot.mo' \;`.
- Enable `/setinline` and `/setinlinefeedback` via BotFather for your bot.
- Use `/setcommands` and submit the list of commands in commandlist.txt
- Install requirements (using a `virtualenv` is recommended):
  `pip install -r requirements.txt`

You can change some gameplay parameters like turn times, minimum amount of
players and default gamemode in `config.json`.

Current gamemodes available: classic, fast, wild and text. Check the details
with the `/modes` command.

Then run the bot with `python3 bot.py`.

Code documentation is minimal but there.

## Contributing
Patches and pull requests are welcome. Please use either
[git-send-email(1)](https://git-send-email.io/) or
[git-request-pull(1)](https://git-scm.com/docs/git-request-pull), addressed to
cybertailor@gmail.com.
