# ANI-Youtube-Comment-Bot
Youtube Comment Bot for Anti-Natalism International 
https://antinatalisminternational.com/

# Introduction

- Adds comments to the youtube videos given a query string

Inspired by the following Youtube Comment Bot : available as a Chrome Plugin
https://chrome.google.com/webstore/detail/youtube-comment-bot/mndnbpgaknbbbahcekcblgnmjmpjgodl?hl=en
but has has NO privileged Limit unlike the above plugin

Also, possible with software like TubeAssistPro but these are paid unless you use the cracked versions.

# Features

- Maintains & Persists a memory for already covered videos
- and Resumes from the last uncovered video when script is restarted

# Requirements

- Python 3.7.4
- Tested on MacOS Catalina 10.15.7

# Instructions

- Open Terminal / Command Line (Preferred Ubuntu / MacOS terminal or Git Bash on Windows)
- pip3 install -r requirements.txt
- Change the following in the youtube_auto_commentor.py script :
	-- Change the video query text in the `search_text`for e.g. "baby delivery birth"
	-- Change the comment to be added the `string in the filename` for e.g. : "youtube_invite_welcome.txt"

- Run python login/save_login_cookies.py 
- Login using email ID and password
- Press ENTER / any other key on Terminal
- Run python youtube_auto_commentor.py 


