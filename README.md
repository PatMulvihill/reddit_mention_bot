###Reddit Mention Bot
<br />

This Reddit Mention Bot will parse through comments in user-defined subreddits to check if the `searched_username` you define in the `config.py` file has been mentioned using Reddit.com's '/u/' + config.searched_username format.
In order to use this bot, you must clone it, install pip and install PRAW using `pip install praw`.
You also have to rename `config.py.example` to `config.py` and edit the variables in that file to your liking.
You must then create a new reddit account, register an application at https://ssl.reddit.com/prefs/apps and place the app's credentials (`username`, `password`, `client_id`, `client_secret`) in the `config.py` folder.  You can define the amount of submissions that the bot parses in each iteration (`lim`), the subreddits the bot checks for your username in (`subs`), and the amount of time that your bot sleeps between each iteration (sleep_time) in the `config.py` file.
<br />
This bot will also create a `comments_replied_to.txt` file in the installation directory that keeps track of the comment ID's of comments that the bot has already handled.
The bot will not respond to itself and is case insensitive.
