##The functionality of this bot comes out-of-the-box with reddit now (without reddit gold), so it has been made obselete.

This bot will parse through comments to check if you the `searched_username` you define in `config.py` has been mentioned using Reddit.com's '/u/' + config.searched_username format.
In order to use this bot, you must clone it, install pip and install PRAW using `pip install praw`.
You must then create a new reddit account, register an application at https://ssl.reddit.com/prefs/apps and place the app's credentials in the `config.py` folder.  You can define the amount of submissions that you check through each iteration, the subreddits you check in, and the amount of time that your bot sleeps between each iteration in the `config.py` file.
