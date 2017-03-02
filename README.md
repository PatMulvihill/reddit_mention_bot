###The functionality of this bot comes out-of-the-box with reddit now (without reddit gold), so it has been made obselete.

This bot will parse through comments to check if you the `searched_username` you define in `config.py` has been mentioned using Reddit.com's '/u/' + config.searched_username format.
In order to use this bot, you must clone it, install pip and install PRAW using `pip install praw`.
You also have to rename `config.py.example` to `config.py`.
You must then create a new reddit account, register an application at https://ssl.reddit.com/prefs/apps and place the app's credentials in the `config.py` folder.  You can define the amount of submissions that you check through each iteration, the subreddits you check in, and the amount of time that your bot sleeps between each iteration in the `config.py` file.
This bot will also create a `comments_replied_to.txt` file in the installation directory that keeps track of the comment ID's of comments the bot has already handled.
The bot will not respond to itself and is case insensitive.
