# Discord Math Bot :x: :heavy_division_sign:
A discord bot that generates math questions and keeps track of each users # of correct and incorrect answers

## Adding To Your Server :factory:
To add the bot to your server use this link:
* [Discord Math Bot](https://discord.com/api/oauth2/authorize?client_id=831777759184289799&permissions=8&scope=bot)

## Usage :newspaper:
To use this bot type in a channel that give the bot permission to read and write.

Commands:

* `$math` - generates and prints math question, then waits for a response

## Program Flow :alien:
This program starts at `bot.py` and uses `equation_generator.py` to generate equations and `database.py` to inteface with out PostgreSQL database

## Running This Program :running:
If you are trying to run this program on your machine then you need
a bot `token` from discord. Once you get one, go to the bottom of `bot.py` and paste your token there in the `token` variable

## Dependencies :milky_way:
discord

`pip install discord`


psycopg2

`pip install psycopg2`


PyYAML

`pip install pyyaml`

