
"""cmd : .sguide """

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 1)

    input_str = event.pattern_match.group(1)

    if input_str == "sguide":

        await event.edit(input_str)

        animation_chars = [

            "[BotHub's Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-06)",
            
            "[BotHub's README.md file](https://github.com/mkaraniya/BotHub/blob/master/README.md)"
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 3])
