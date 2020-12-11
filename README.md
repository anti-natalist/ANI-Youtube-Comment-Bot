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

- Download https://github.com/anti-natalist/ANI-Youtube-Comment-Bot/archive/main.zip
- Open Terminal / Command Line (Preferred Ubuntu / MacOS terminal or Git Bash on Windows)
- Change Directory using command :  `cd ..`
- Run command : `pip3 install -r requirements.txt`
- Change the following in the youtube_auto_commentor.py script :
	-- Change the video query text in the `search_text`for e.g. "baby delivery birth"
	-- Change the comment to be added the `string in the filename` for e.g. : "youtube_invite_welcome.txt"

- Run python script to login using command :  `login/save_login_cookies.py`
- Login using email ID and password
- Press ENTER / any other key on Terminal
- Run python script to start commenting :  `youtube_auto_commentor.py`


# NOTE

Some viewers have reached out to me expressing their concerns over the safety of the script and authentication methods.
I assure you this is completely safe and secure for you to run and the only motivation behind this project is our desire to spread the awareness of Anti-Natalism throughout the globe for a noble cause.

