class script(object):
    START_TXT = """<b>𝗛𝗶 {},</b>

<b>ɪ ᴀᴍ ᴊᴜꜱᴛ ᴀ ꜱɪᴍᴩʟᴇ ᴩʀᴇ ꜰᴜɴᴄᴛɪᴏɴᴇᴅ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ʙᴏᴛ ɪᴛꜱ ꜱɪᴍᴩʟᴇ ᴛᴏ ᴜꜱᴇ ᴍᴇ...</b>
𝗝𝘂𝘀𝘁 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝘀 𝗔𝗱𝗺𝗶𝗻
<b>ᴛʜᴀᴛꜱ ᴀʟʟ ɪ ᴡɪʟʟ ᴩʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ ᴛʜᴇʀᴇ..🥰</b>"""
    HELP_TXT = """<b>𝐻𝑒𝑦 {} 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑇𝑜 𝐻𝑒𝑙𝑝 𝑀𝑜𝑑𝑢𝑙𝑒 ☺️"""
    ABOUT_TXT = """                      
•<b> ᴍʏ ɴᴀᴍᴇ </b>: {}
•<b> ᴄʀᴇᴀᴛᴏʀ </b>: <a href="https://t.me/DARKWEBLOAD">𝑡ℎ𝑖𝑠 𝑝𝑒𝑟𝑠𝑜𝑛</a>
•<b> ʟᴀɴɢᴜᴀɢᴇ </b>: 𝑝𝑦𝑡ℎ𝑜𝑛
•<b> ʟɪʙʀᴀʀʏ </b>: 𝑝𝑦𝑟𝑜𝑔𝑟𝑎𝑚
•<b> ꜱᴇʀᴠᴇʀ </b>: ℎ𝑒𝑟𝑜𝑘𝑢
•<b> ᴅᴀᴛᴀʙᴀꜱᴇ </b>: 𝑚𝑜𝑛𝑔𝑜 𝑑𝑏
•<b> ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ </b>: 𝑉9.8 [𝐵𝑒𝑇𝑎]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝖳ʜɪs 𝖡ᴏᴛ 𝖭ᴏᴛ 𝖠 𝖮ᴘᴇɴ 𝖲ᴏᴜʀᴄᴇ 𝖯ʀᴏᴊᴇᴄᴛ 🤧</a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

•/whois :-give a user full details"""
    ALIVE_TXT ="""<b>ALIVE MODULE</b>
• /alive - check me alive or dead🤧
Just for a rasam😂"""
    ZOMBIES_TXT = """𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖪𝗂𝖼𝗄 𝖴𝗌𝖾𝗋

<b>𝖪𝗂𝖼𝗄 𝖨𝗇𝖺𝖼𝗍𝗂𝗏𝖾 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 𝖥𝗋𝗈𝗆 𝖦𝗋𝗈𝗎𝗉. 𝖠𝖽𝖽 𝖬𝖾 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇 𝖶𝗂𝗍𝗁 𝖡𝖺𝗇 𝖴𝗌𝖾𝗋𝗌 𝖯𝖾𝗋𝗆𝗂𝗌𝗎𝗈𝗇 𝖨𝗇 𝖦𝗋𝗈𝗎𝗉.</b>
<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""
    IMAGE_TXT = """• Help : Image

• This Command Help You To Edit Image Very Easly 😇

• Command And Usage :
• Just Send Me A Image To Edit ✨

➪ Made By : <a href=https://t.me/DARKWEBLOAD>Dᴀʀᴋ ᴡᴇʙʟᴏᴀᴅ🇮🇳</a>"""
    SONG_TXT ="""<b>SONG MODULE</b>
Song Download
Song Download Module, For Those Who Love Music

🎈 Command

- /song [Song Name] - To Download Music

Usage
- working pm and groups"""
    JSON_TXT ="""<b>JSON MODULE</b>
JSON:
Bot returns json for all replied messages with /json

Features:
Message Editting JSON
Pm Support
Group Support

Note:
Everyone can use this command , if spaming happens bot will automatically ban you from the group"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>📚 Commands & Usage:</b>

◉ /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

◉ /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
  /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

  <b>example</b> : - /covid India"""
    STICKER_TXT ="""<b>Command</b> /stickerid If you need telegram sticker id click /stickerid to get sticker id (Replay with sticker)"""
    YTTHUMB_TXT = """Help to download any youtube video thumbnail

• How to Use
Type /ytthumb and video link
• Example

<code>/ytthumb https://youtu.be/OWqbMNrVt5s</code>"""
    REPORT_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖱𝖾𝗉𝗈𝗋𝗍 ⚠️

𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖱𝖾𝗉𝗈𝗋𝗍 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖮𝗋 𝖠 𝖴𝗌𝖾𝗋 𝖳𝗈 𝖳𝗁𝖾 𝖠𝖽𝗆𝗂𝗇 𝖮𝖿 𝖳𝗁𝖾 𝖱𝖾𝗌𝗉𝖾𝖼𝗍𝗂𝗏𝖾 𝖦𝗋𝗈𝗎𝗉. 𝖣𝗈𝗇'𝗍 𝖬𝗂𝗌𝗎𝗌𝖾 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽.
➤ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:
➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""
    ABOOK_TXT = """•<b> Help : Audiobook</b>

You Can Convert A Pdf File To A Video File With This Command.

• Command And Usage:
➪ /audiobook : Replay This Command To Any Pdf To Generate The Audio"""
    URLSHORT_TXT = """• Help : Url shortner

This command help you to short a url.
• /short : use this command with your link to get shorted links
• Example :
/short https://youtu.be/IF_qoYnCLjs"""
    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝖳𝖾𝗑𝗍 𝖳𝗈 𝖲𝗉𝖾𝖾𝖼𝗁
<b>Commands and Usage:</b>
• /tts <text> : 𝖢𝗈𝗇𝗏𝖾𝗋𝗍 𝖳𝖾𝗑𝗍 𝖳𝗈 𝖲𝗉𝖾𝖾𝖼𝗁
<b>NOTE:</b>
• 𝖨𝗆𝖽𝖻 𝖲𝗁𝗈𝗎𝗅𝖽 𝖧𝖺𝗏𝖾 𝖠𝖽𝗆𝗂𝗇 𝖯𝗋𝖾𝗏𝗂𝗅𝖺𝗀𝖾.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>🎲 NOTHING MUCH JUST SOME FUN THINGS</b>
t𝗋𝗒 𝗍𝗁𝗂𝗌 𝖮𝗎𝗍: 
𝟣. /dice - Roll The Dice 
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - add a filter in chat.
• /filters - list all the filters of a chat.
• /del - delete a specific filter in chat.
• /delall - delete the whole filters in a chat (chat owner only)."""
    FILE_TXT = """• Help : file store module

• By using this module you can store files in my database and i will give you a permenent link to access the saved files.if you want to add files from a private channel you must make me admin on the channel to access files...

• <b>Commands And Usage</b> :

➪ /plink : replay to any media to get link.

➪ /pbatch : use your meadia link to this command.

➪ /batch : to creat links for multiple files. 
• Example :
/batch https://t.me/+Rc9TK3wIf6xjODE9

Credits : <a href=https://t.me/DARKWEBLOAD><b>Dᴀʀᴋ ᴡᴇʙʟᴏᴀᴅ🇮🇳</b></a>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - connect a particular chat to your PM.
• /disconnect  - disconnect from a chat.
• /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
• /id - get id of a specifed user.
• /info  - get information about a user.
• /json - get the json details of a message.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<b>NOTE:</b>
• IMDb should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
• /ban - ban a user.
• /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>📂 𝖳ᴏᴛᴀʟ 𝖥ɪʟᴇs:</b> <code>{}</code>
<b>👥 𝖳ᴏᴛᴀʟ 𝖴sᴇʀs :</b> <code>{}</code>
<b>🎎 𝖳ᴏᴛᴀʟ 𝖢ʜᴀᴛs :</b> <code>{}</code>
<b>🗃️ 𝖴sᴇᴅ 𝖲ᴛᴏʀᴀɢᴇ :</b> <code>{}</code> MiB
<b>🆓 𝖥ʀᴇᴇ 𝖲ᴛᴏʀᴀɢᴇ :</b> <code>{}</code> MiB""" 
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
