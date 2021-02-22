#!/bin/bash

pip3 install discord.py
pip3 install lyricsgenius
pip3 install mal
pip3 install gsearch

python3 -m pip install discord.py
python3 -m pip install lyricsgenius
python3 -m pip install mal-api
python3 -m pip install gsearch

mkdir fw-bot && cd fw-bot
git clone https://github.com/pixdoet/firewall-bot.git
echo "Done"
