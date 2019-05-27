# Discord-Mining-Bot---Eve-Online
This is a simple, yet stable bot that can be used to mark different anomalies as depleted and ping @here when they have re-spawned. It currently supports Enormous, Colossal & Ice.

EXAMPLE:

    You enter: !ice depleted xyz
    Bot Replies: Ice marked depleted for xyz
    Bot Replies in 4 hours: @here Ice has respawned xyz

More features will be added soon, but the basic functionality is there and I wanted to share.

# Supported Commands

    !ice depleted system
    !eno depleted system
    !col depleted system
    !list
    !status {ice, eno, col}
    !status {ice, eno, col} Region
    !delete id

Example: !ice depleted jita

# Download the bot to your server:

Save main.py where you wish to execute the bot from.

# Setting the Bot up:
Create application at discordapp.com/developers/applications.
Add a bot to your application by selecting add bot.
Update main.py with Bot Token given by your application you just created.

# To Host the Bot on your server:
Prerequisites:
Python 3.6+
PIP

Run the following after prerequisites are installed.

    pip install discord

On some distro's you will get permission error when running the above command. If so, try the following:

    pip install --user discord

Run the bot with:

    python main.py

Don't forget to set an icon and name your bot! Goodluck! To keep the bot running after you exit your server, there are many ways to do this. Be creative :) But for a simple solution, use screen.
