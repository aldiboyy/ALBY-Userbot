# all plugins are imported from bothub,x-tra-telegram by @heyworld
# Don't edit or you gay
# credits: spechide,ravana69,mkaraniya & me
# Modifikasi sedikit dari @punya_alby
# ░█████╗░██╗░░░░░██████╗░██╗░░░██╗
# ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
# ███████║██║░░░░░██████╦╝░╚████╔╝░
# ██╔══██║██║░░░░░██╔══██╗░░╚██╔╝░░
# ██║░░██║███████╗██████╦╝░░░██║░░░
# ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
# PERSETAN DENGAN ORANG YANG HAPUS CREDIT
from telethon import events

import asyncio

from userbot.events import register
from userbot import CMD_HELP, bot, ALIVE_NAME
from collections import deque
from telethon.errors.rpcerrorlist import MessageIdInvalidError
import random

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "quickheal":

        await event.edit(input_str)

        animation_chars = [
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault: No Virus Found...`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "sqh":

        await event.edit(input_str)

        animation_chars = [
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault: No Virus Found...`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "vquickheal":

        await event.edit(input_str)

        animation_chars = [
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault:⚠️Virus Found⚠️\nMore Info: Torzan, Spyware, Adware`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 19)

    input_str = event.pattern_match.group(1)

    if input_str == "jaralby":

        await event.edit(input_str)

        animation_chars = [

            "`Menghubungkan ke Jaringan ALBY...`",
            "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",
            "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
            "*Mengoptimalkan Jaringan ALBY...*",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
            "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",
            "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▇ █`",
            "**Jaringan ALBY Ditingkatkan....**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 19])


@register(outgoing=True, pattern="^.dump(?: |$)(.*)")
async def _(message):
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = ' '.join(obj)
    except IndexError:
        inp = "🥞 🎂 🍫"
    u, t, g, o, s, n = inp.split(), '🗑', '<(^_^ <)', '(> ^_^)>', '⠀ ', '\n'
    h = [(u[0], u[1], u[2]), (u[0], u[1], ''), (u[0], '', '')]
    for something in reversed([y for y in ([''.join(x) for x in (
            f + (s, g, s + s * f.count(''), t), f + (g, s * 2 + s * f.count(''), t),
            f[:i] + (o, f[i], s * 2 + s * f.count(''), t), f[:i] + (s + s * f.count(''), o, f[i], s, t),
            f[:i] + (s * 2 + s * f.count(''), o, f[i], t), f[:i] + (s * 3 + s * f.count(''), o, t),
            f[:i] + (s * 3 + s * f.count(''), g, t))] for i, f in enumerate(reversed(h)))]):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await message.edit(something_else)
            except MessageIdInvalidError:
                return

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "think":
        await event.edit(input_str)
        animation_chars = [
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING... 🤔"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "wtf":
        await event.edit(input_str)
        animation_chars = [
            "What",
            "What The",
            "What The F",
            "What The F Brah",
            "What The F Brah\nhttps://telegra.ph//file/f3b760e4a99340d331f9b.jpg"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 5])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "music":

        await event.edit(input_str)

        animation_chars = [
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY  Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ALBY Music Player](https://t.me/ruangprojects)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "telepon":

        await event.edit(input_str)

        animation_chars = [
            "`Menyambungkan telfon ke telegram...`",
            "`telfon tersambung.`",
            "`Telegram: Hallo bro,ada afa menelfon ku?`",
            f"`Me: Saya `@{DEFAULTUSER},`Ingin memberitahukan bahwa disini ada babu`",
            "`Babu nya ngeselin`",
            "`Aduh pokok nya babu nya goblok`",
            "`telfon privasi terhubung...`",
            "`Me: Hello Pulici saya ingin melaporkan bahwa disini ada babu`",
            "`Pulici: Siapa ini?`",
            f"`Me: Saya @{DEFAULTUSER} Goblok bgt pulici ",
            "`Pulici: Oo iyah tenang biar saya urus babunya`",
            "`Me: Asiappp Makasih pulici.`",
            "`Pulici: Iya sama sama,telfon saya lagi nanti kalo ada babu`",
            "`Me: Iya pulici, Saya juga lagi gabut aja nelpon anda`",
            "`Pulici: oooooasuuuuuu GOBLOK`",
            "`Me: Awowkwokwkkw Pulici nya goblok`",
            "`Pulici: Dah lah anying Gajelas`",
            "`Telpon Nya terputus.....`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])


@bot.on(events.NewMessage(pattern=r"\.belo", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    await event.edit("Typing...")

    await asyncio.sleep(2)

    x = (random.randrange(1, 96))

    if x == 1:

        await event.edit("`\"Underwater bubbles and raindrops are total opposites of each other.\"`")

    if x == 2:

        await event.edit("`\"If you buy an eraser you are literally paying for your mistakes.\"`")

    if x == 3:

        await event.edit("`\"The Person you care for most has the potential to destroy you the most.\"`")

    if x == 4:

        await event.edit("`\"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger.\"`")

    if x == 5:

        await event.edit("`\"Any video with “wait for it” in the title is simply too long.\"`")

    if x == 6:

        await event.edit("`\"Your age in years is how many times you’ve circled the Sun, but your age in months is how many times the Moon has circled you.\"`")

    if x == 7:

        await event.edit("`\"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience.\"`")

    if x == 8:

        await event.edit("`\"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof.\"`")

    if x == 9:

        await event.edit("`\"The most crushing feeling is when someone smiles at you on the street and you don’t react fast enough to smile back.\"`")

    if x == 10:

        await event.edit("`\"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils.\"`")

    if x == 11:

        await event.edit("`\"A folder is for things that you don't want to fold.\"`")

    if x == 12:

        await event.edit("`\"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching.\"`")

    if x == 13:

        await event.edit("`\"If everything goes smoothly, you probably won't remember today.\"`")

    if x == 14:

        await event.edit("`\"When you meet new people in real life, you unlock more characters for your dream world.\"`")

    if x == 15:

        await event.edit("`\"Maybe if they renamed sunscreen to “anti-cancer cream” more people would wear it.\"`")

    if x == 16:

        await event.edit("`\"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass.\"`")

    if x == 17:

        await event.edit("`\"Parents worry about what their sons download and worry about what their daughters upload.\"`")

    if x == 18:

        await event.edit("`\"It's crazy how you can be the same age as someone, but at a completely different stage in your life.\"`")

    if x == 19:

        await event.edit("`\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"`")

    if x == 20:

        await event.edit("`\"Technically, no one has ever been in an empty room.\"`")

    if x == 21:

        await event.edit("`\"An onion is the bass player of food. You would probably not enjoy it solo, but you’d miss it if it wasn’t there.\"`")

    if x == 22:

        await event.edit("`\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"`")

    if x == 23:

        await event.edit("`\"Every single decision you ever made has brought you to read this sentence.\"`")

    if x == 24:

        await event.edit("`\"The word 'quiet' is often said very loud.\"`")

    if x == 25:

        await event.edit("`\"Everybody wants you to work hard, but nobody wants to hear about how hard you work.\"`")

    if x == 26:

        await event.edit("`\"We brush our teeth with hair on a stick and brush our hair with teeth on a stick.\"`")

    if x == 27:

        await event.edit("`\"No one remembers your awkward moments but they’re too busy remembering their own.\"`")

    if x == 28:

        await event.edit("`\"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible.\"`")

    if x == 29:

        await event.edit("`\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"`")

    if x == 30:

        await event.edit("`\"The biggest irony is that computers & mobiles were invented to save out time!\"`")

    if x == 31:

        await event.edit("`\"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects.\"`")

    if x == 32:

        await event.edit("`\"You know you’re getting old when your parents start disappointing you, instead of you disappointing them.\"`")

    if x == 33:

        await event.edit("`\"Humans are designed to learn through experience yet the education system has made it so we get no experience.\"`")

    if x == 34:

        await event.edit("`\"By focusing on blinking, you blink slower... Same for breathing.\"`")

    if x == 35:

        await event.edit("`\"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid.\"`")

    if x == 36:

        await event.edit("`\"Characters that get married in fiction were literally made for each other.\"`")

    if x == 37:

        await event.edit("`\"Babies are a clean hard drive that can be programmed with any language.\"`")

    if x == 38:

        await event.edit("`\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"`")

    if x == 39:

        await event.edit("`\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"`")

    if x == 40:

        await event.edit("`\"Maybe we don't find time travelers because we all die in 25-50 years.\"`")

    if x == 41:

        await event.edit("`\"Sleep is the trial version of death, It even comes with ads based on your activity.\"`")

    if x == 42:

        await event.edit("`\"The most unrealistic thing about Spy movies is how clean the air ventilation system is!\"`")

    if x == 43:

        await event.edit("`\"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes.\"`")

    if x == 44:

        await event.edit("`\"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves.\"`")

    if x == 45:

        await event.edit("`\"If Greenland actually turns green, we're all screwed.\"`")

    if x == 46:

        await event.edit("`\"If someone says clever things in your dream, it actually shows your own cleverness.\"`")

    if x == 47:

        await event.edit("`\"Famous movie quotes are credited to the actor and not the actual writer who wrote them.\"`")

    if x == 48:

        await event.edit("`\"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out.\"`")

    if x == 49:

        await event.edit("`\"Ask yourself why the the brain ignores the second the.\"`")

    if x == 50:

        await event.edit("`\"You’ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened.\"`")

    if x == 51:

        await event.edit("`\"It will be a lot harder for kids to win against their parents in video games in the future.\"`")

    if x == 52:

        await event.edit("`\"Everyone has flaws, if you don't recognize yours, you have a new one.\"`")

    if x == 53:

        await event.edit("`\"Raising a child is training your replacement.\"`")

    if x == 54:

        await event.edit("`\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"`")

    if x == 55:

        await event.edit("`\"There's always someone who hated you for no reason, and still does.\"`")

    if x == 56:

        await event.edit("`\"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect.\"`")

    if x == 57:

        await event.edit("`\"The more important a good night's sleep is, the harder it is to fall asleep.\"`")

    if x == 58:

        await event.edit("`\"Blessed are those that can properly describe the type of haircut they want to a new stylist.\"`")

    if x == 59:

        await event.edit("`\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"`")

    if x == 60:

        await event.edit("`\"Theme park employees must be good at telling the difference between screams of horror and excitement.\"`")

    if x == 61:

        await event.edit("`\"6 to 6:30 feels more half-an-hour than 5:50 to 6:20\"`")

    if x == 62:

        await event.edit("`\"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience.\"`")

    if x == 63:

        await event.edit("`\"Listening to podcasts before bed is the adult version of story-time.\"`")

    if x == 64:

        await event.edit("`\"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing.\"`")

    if x == 65:

        await event.edit("`\"A ton of whales is really only like half a whale.\"`")

    if x == 66:

        await event.edit("`\"When you get old, the old you is technically the new you, and your young self is the old you.\"`")

    if x == 67:

        await event.edit("`\"You probably won't find many negative reviews of parachutes on the Internet.\"`")

    if x == 68:

        await event.edit("`\"We show the most love and admiration for people when they're no longer around to appreciate it.\"`")

    if x == 69:

        await event.edit("`\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"`")

    if x == 70:

        await event.edit("`\"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for.\"`")

    if x == 71:

        await event.edit("`\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"`")

    if x == 72:

        await event.edit("`\"The most effective alarm clock is a full bladder.\"`")

    if x == 73:

        await event.edit("`\"You probably just synchronized blinks with millions of people.\"`")

    if x == 74:

        await event.edit("`\"Since we test drugs on animals first, rat medicine must be years ahead of human medicine.\"`")

    if x == 75:

        await event.edit("`\"Night before a day off is more satisfying than the actual day off.\"`")

    if x == 76:

        await event.edit("`\"We put paper in a folder to keep it from folding.\"`")

    if x == 77:

        await event.edit("`\"Somewhere, two best friends are meeting for the first time.\"`")

    if x == 78:

        await event.edit("`\"Our brain simultaneously hates us, loves us, doesn't care about us, and micromanages our every move.\"`")

    if x == 79:

        await event.edit("`\"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice.\"`")

    if x == 80:

        await event.edit("`\"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents.\"`")

    if x == 81:

        await event.edit("`\"Wikipedia is what the internet was meant to be.\"`")

    if x == 82:

        await event.edit("`\"A theme park is the only place that you can hear screams in the distance and not be concerned.\"`")

    if x == 83:

        await event.edit("`\"A wireless phone charger offers less freedom of movement than a wired one.\"`")

    if x == 84:

        await event.edit("`\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"`")

    if x == 85:

        await event.edit("`\"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world.\"`")

    if x == 86:

        await event.edit("`\"If someday human teleportation becomes real, people will still be late for work.\"`")

    if x == 87:

        await event.edit("`\"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider\"`")

    if x == 88:

        await event.edit("`\"Doing something alone is kind of sad, but doing it solo is cool af.\"`")

    if x == 89:

        await event.edit("`\"Your brain suddenly becomes perfect at proofreading after you post something.\"`")

    if x == 90:

        await event.edit("`\"There's always that one song in your playlist that you always skip but never remove.\"`")

    if x == 91:

        await event.edit("`\"Kids next century will probably hate us for taking all the good usernames.\"`")

    if x == 92:

        await event.edit("`\"Bubbles are to fish what rain is to humans.\"`")

    if x == 93:

        await event.edit("`\"The more people you meet, the more you realise and appreciate how well your parents raised you.\"`")

    if x == 94:

        await event.edit("`\"A comma is a short pause, a coma is a long pause.\"`")

    if x == 95:

        await event.edit("`\"Someday you will either not wake up or not go to sleep.\"`")

    if x == 96:

        await event.edit("`\"Bermuda Triangle might be the exit portal of this simulation.\"`")

    if x == 97:

        await event.edit("`\"If we put solar panels above parking lots, then our cars wouldn't get hot and we would have a lot of clean energy.\"`")

@bot.on(events.NewMessage(pattern=r"\.qs", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    await event.edit("selecting question...")

    await asyncio.sleep(2)

    x = (random.randrange(1, 60))

    if x == 1:

        await event.edit("`\"Arrange them in descending order of importance – MONEY, LOVE, FAMILY, CAREER, FRIENDS.\"`")

    if x == 2:

        await event.edit("`\"If you had to change your name, what would your new name be, and why would you choose that name?\"`")

    if x == 3:

        await event.edit("`\"What’s the most interesting thing you’ve read or seen this week?\"`")

    if x == 4:

        await event.edit("`\"What scene from a TV show will you never forget?\"`")

    if x == 5:

        await event.edit("`\"If you could become a master in one skill, what skill would you choose?\"`")

    if x == 6:

        await event.edit("`\"What three words can describe you?\"`")

    if x == 7:

        await event.edit("`\"If you had to delete one app from your phone, what would it be?\"`")

    if x == 8:

        await event.edit("`\"Would you go out with me if I was the last person on earth?\"`")

    if x == 9:

        await event.edit("`\"If you switched genders for the day, what would you do?\"`")

    if x == 10:

        await event.edit("`\"If you could eat lunch with someone here. Who would you choose?\"`")

    if x == 11:

        await event.edit("`\"If you were told you only had one week left to live, what would you do?\"`")

    if x == 12:

        await event.edit("`\"What's number one item you would save from your burning house?\"`")

    if x == 13:

        await event.edit("`\"If you could only text one person for the rest of your life, but you could never talk to that person face to face, who would that be?\"`")

    if x == 14:

        await event.edit("`\"How many kids do you want to have in the future?\"`")

    if x == 15:

        await event.edit("`\"Who in this group would be the worst person to date? Why?\"`")

    if x == 16:

        await event.edit("`\"What does your dream boy or girl look like?\"`")

    if x == 17:

        await event.edit("`\"What would be in your web history that you’d be embarrassed if someone saw?\"`")

    if x == 18:

        await event.edit("`\"Do you sing in the shower?\"`")

    if x == 19:

        await event.edit("`\"What’s the right age to get married?\"`")

    if x == 20:

        await event.edit("`\"What are your top 5 rules for life?\"`")

    if x == 21:

        await event.edit("`\"If given an option, would you choose a holiday at the beach or in the mountains?\"`")

    if x == 22:

        await event.edit("`\"If you are made the president of your country, what would be the first thing that you will do?\"`")

    if x == 23:

        await event.edit("`\"If given a chance to meet 3 most famous people on the earth, who would it be, answer in order of preference.\"`")

    if x == 24:

        await event.edit("`\"Have you ever wished to have a superpower, if so, what superpower you would like to have?\"`")

    if x == 25:

        await event.edit("`\"Can you spend an entire day without phone and internet? If yes, what would you do?\"`")

    if x == 26:

        await event.edit("`\"Live-in relation or marriage, what do you prefer?\"`")

    if x == 27:

        await event.edit("`\"What is your favorite cuisine or type of food?\"`")

    if x == 28:

        await event.edit("`\"What are some good and bad things about the education system in your country?\"`")

    if x == 29:

        await event.edit("`\"What do you think of online education?\"`")

    if x == 30:

        await event.edit("`\"What are some goals you have failed to accomplish?\"`")

    if x == 31:

        await event.edit("`\"Will technology save the human race or destroy it?\"`")

    if x == 32:

        await event.edit("`\"What was the best invention of the last 50 years?\"`")

    if x == 33:

        await event.edit("`\"Have you travelled to any different countries? Which ones?\"`")

    if x == 34:

        await event.edit("`\"Which sport is the most exciting to watch? Which is the most boring to watch?\"`")

    if x == 35:

        await event.edit("`\"What’s the most addictive mobile game you have played?\"`")

    if x == 36:

        await event.edit("`\"How many apps do you have on your phone?\"`")

    if x == 37:

        await event.edit("`\"What was the last song you listened to?\"`")

    if x == 38:

        await event.edit("`\"Do you prefer to watch movies in the theater or in the comfort of your own home?\"`")

    if x == 39:

        await event.edit("`\"Do you like horror movies? Why or why not?\"`")

    if x == 40:

        await event.edit("`\"How often do you help others? Who do you help? How do you help?\"`")

    if x == 41:

        await event.edit("`\"What song do you play most often?\"`")

    if x == 42:

        await event.edit("`\"Suggest a new rule that should be added in this group!\"`")

    if x == 43:

        await event.edit("`\"What app on your phone do you think I should get?\"`")

    if x == 44:

        await event.edit("`\"What website or app has completely changed your life for better or for worse?\"`")

    if x == 45:

        await event.edit("`\"What isn’t real but you desperately wish it was?\"`")

    if x == 46:

        await event.edit("`\"What thing do you really wish you could buy right now?\"`")

    if x == 47:

        await event.edit("`\"If you could ban an admin from this group. Who would you prefer ?\"`")

    if x == 48:

        await event.edit("`\"What would you do if someone left a duffle bag filled with $2,000,000 on your back porch?\"`")

    if x == 49:

        await event.edit("`\"Who is the luckiest person you know?\"`")

    if x == 50:

        await event.edit("`\"If you could visit someone's house in this group, who would it be ?\"`")

    if x == 51:

        await event.edit("`\"What are you tired of hearing about?\"`")

    if x == 52:

        await event.edit("`\"If you died today, what would your greatest achievement be?\"`")

    if x == 53:

        await event.edit("`\"What method will you choose to kill yourself?\"`")

    if x == 54:

        await event.edit("`\"What’s the best news you've heard in the last 24 hours?\"`")

    if x == 55:

        await event.edit("`\"What is the most important change that should be made to your country’s education system?\"`")

    if x == 56:

        await event.edit("`\"Send your favourite sticker pack.\"`")

    if x == 57:

        await event.edit("`\"Send your favourite animated sticker pack.\"`")

    if x == 58:

        await event.edit("`\"Send your favourite video or gif.\"`")

    if x == 59:

        await event.edit("`\"Send your favourite emojies\"`")

    if x == 60:

        await event.edit("`\"What’s something you misunderstood as a child and only realized much later was wrong?\"`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "load":

        await event.edit(input_str)

        animation_chars = [

            "▮",

            "▯",

            "▬",

            "▭"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "square":

        await event.edit(input_str)

        animation_chars = [

            "◧",

            "◨",

            "◧",

            "◨"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "up":

        await event.edit(input_str)

        animation_chars = [

            "╹",

            "╻",

            "╹",

            "╻"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "round":

        await event.edit(input_str)

        animation_chars = [

            "⚫",

            "⬤",

            "●",

            "∘"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "heart":

        await event.edit(input_str)

        animation_chars = [

            "🖤",

            "❤️",

            "🖤",

            "❤️"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "anim":

        await event.edit(input_str)

        animation_chars = [

            "😁",

            "😧",

            "😡",

            "😢",



            "😁",

            "😧",

            "😡",

            "😢",



            "__**...BRO oh BRO! i merasa seperti menjadi pahlawan....**__"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "fnl":

        await event.edit(input_str)

        animation_chars = [

            "😁🏿",

            "😁🏾",

            "😁🏽",

            "😁🏼",

            "‎😁",

            "**Fair & Lovely ALBY Is BeHiNd You....**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "monkey":

        await event.edit(input_str)

        animation_chars = [

            "🐵",

            "🙉",

            "🙈",

            "🙊",

            "🖕‎🐵🖕",

            "**OPPA MONEKEYY Style....**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 14)

    input_str = event.pattern_match.group(1)

    if input_str == "hand":

        await event.edit(input_str)

        animation_chars = [

            "👈",

            "👉",

            "☝️",

            "👆",

            "🖕",

            "👇",

            "✌️",

            "🤞",

            "🖖",

            "🤘",

            "🤙",

            "🖐️",

            "👌"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 14])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 13)

    input_str = event.pattern_match.group(1)

    if input_str == "cnt":

        await event.edit(input_str)

        animation_chars = [

            "🔟",

            "9️⃣",

            "8️⃣",

            "7️⃣",

            "6️⃣",

            "5️⃣",

            "4️⃣",

            "3️⃣",

            "2️⃣",

            "1️⃣",

            "0️⃣",

            "🆘"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 13])




@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "admeme":

        await event.edit(input_str)

        animation_chars = [
            "@aaaaaaaaaaaaadddddddddddddmmmmmmmmmmmmmiiiiiiiiiiiiinnnnnnnnnnnnn",
            "@aaaaaaaaaaaaddddddddddddmmmmmmmmmmmmiiiiiiiiiiiinnnnnnnnnnnn",
            "@aaaaaaaaaaadddddddddddmmmmmmmmmmmiiiiiiiiiiinnnnnnnnnnn",
            "@aaaaaaaaaaddddddddddmmmmmmmmmmiiiiiiiiiinnnnnnnnnn",
            "@aaaaaaaaadddddddddmmmmmmmmmiiiiiiiiinnnnnnnnn",
            "@aaaaaaaaddddddddmmmmmmmmiiiiiiiinnnnnnnn",
            "@aaaaaaadddddddmmmmmmmiiiiiiinnnnnnn",
            "@aaaaaaddddddmmmmmmiiiiiinnnnnn",
            "@aaaaadddddmmmmmiiiiinnnnn",
            "@aaaaddddmmmmiiiinnnn",
            "@aaadddmmmiiinnn",
            "@aaddmmiinn",
            "@admin"]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 103])


@register(outgoing=True, pattern="^.gotm(?: |$)(.*)")
async def _(event):

    if event.fwd_from:

        return

    await event.edit("Thinking... 🤔")

    await asyncio.sleep(2)

    x = (random.randrange(1, 30))

    if x == 1:

        await event.edit("[To your teachers on failing you in all your papers confidently, every time...](https://telegra.ph/file/431d178780f9bff353047.jpg)", link_preview=True)

    if x == 2:

        await event.edit("[A shift from the mainstream darling, sweetheart, jaanu, and what not...](https://telegra.ph/file/6bbb86a6c7d2c4a61e102.jpg)", link_preview=True)

    if x == 3:

        await event.edit("[To the guy who's friendzone-ing you...](https://telegra.ph/file/8930b05e9535e9b9b8229.jpg)", link_preview=True)

    if x == 4:

        await event.edit("[When your friend asks for his money back...](https://telegra.ph/file/2df575ab38df5ce9dbf5e.jpg)", link_preview=True)

    if x == 5:

        await event.edit("[A bad-ass reply to who do you think you are?](https://telegra.ph/file/3a35a0c37f4418da9f702.jpg)", link_preview=True)

    if x == 6:

        await event.edit("[When the traffic police stops your car and asks for documents...](https://telegra.ph/file/52612d58d6a61315a4c3a.jpg)", link_preview=True)

    if x == 7:

        await event.edit("[ When your friend asks about the food he/she just cooked and you don't want to break his/her heart...](https://telegra.ph/file/702df36088f5c26fef931.jpg)", link_preview=True)

    if x == 8:

        await event.edit("[When you're out of words...](https://telegra.ph/file/ba748a74bcab4a1135d2a.jpg)", link_preview=True)

    if x == 9:

        await event.edit("[When you realize your wallet is empty...](https://telegra.ph/file/a4508324b496d3d4580df.jpg)", link_preview=True)

    if x == 10:

        await event.edit("[When shit is about to happen...](https://telegra.ph/file/e15d9d64f9f25e8d05f19.jpg)", link_preview=True)

    if x == 11:

        await event.edit("[When that oversmart classmate shouts a wrong answer in class...](https://telegra.ph/file/1a225a2e4b7bfd7f7a809.jpg)", link_preview=True)

    if x == 12:

        await event.edit("[When things go wrong in a big fat Indian wedding...](https://telegra.ph/file/db69e17e85bb444caca32.jpg)", link_preview=True)

    if x == 13:

        await event.edit("[A perfect justification for breaking a promise...](https://telegra.ph/file/0b8fb8fb729d157844ac9.jpg)", link_preview=True)

    if x == 14:

        await event.edit("[When your friend just won't stop LOL-ing on something silly you said...](https://telegra.ph/file/247fa54106c32318797ae.jpg)", link_preview=True)

    if x == 15:

        await event.edit("[When someone makes a joke on you...](https://telegra.ph/file/2ee216651443524eaafcf.jpg)", link_preview=True)

    if x == 16:

        await event.edit("[When your professor insults you in front of the class...](https://telegra.ph/file/a2dc7317627e514a8e180.jpg)", link_preview=True)

    if x == 17:

        await event.edit("[When your job interviewer asks if you're nervous...](https://telegra.ph/file/9cc147d0bf8adbebf164b.jpg)", link_preview=True)

    if x == 18:

        await event.edit("[When you're sick of someone complaining about the heat outside...](https://telegra.ph/file/9248635263c52b968f968.jpg)", link_preview=True)

    if x == 19:

        await event.edit("[When your adda is occupied by outsiders...](https://telegra.ph/file/ef537007ba6d9d4cbd384.jpg)", link_preview=True)

    if x == 20:

        await event.edit("[When you don't have the right words to motivate somebody...](https://telegra.ph/file/2c932d769ae4c5fbed368.jpg)", link_preview=True)

    if x == 21:

        await event.edit("[When the bouncer won't let you and your group of friends in because you're all under-aged...](https://telegra.ph/file/6c8ca79f1e20ebd04391c.jpg)", link_preview=True)

    if x == 22:

        await event.edit("[To the friend who wants you to take the fall for his actions...](https://telegra.ph/file/d4171b9bc9104b5d972d9.jpg)", link_preview=True)

    if x == 23:

        await event.edit("[When that prick of a bully wouldn't take your words seriously...](https://telegra.ph/file/188d73bd24cf866d8d8d0.jpg)", link_preview=True)

    if x == 24:

        await event.edit("[ When you're forced to go shopping/watch a football match with your partner...](https://telegra.ph/file/6e129f138c99c1886cb2b.jpg)", link_preview=True)

    if x == 25:

        await event.edit("[To the large queue behind you after you get the last concert/movie ticket...](https://telegra.ph/file/2423f213dd4e4282a31ea.jpg)", link_preview=True)

    if x == 26:

        await event.edit("[When your parents thought you'd fail but you prove them wrong...](https://telegra.ph/file/39cc5098466f622bf21e3.jpg)", link_preview=True)

    if x == 27:

        await event.edit("[A justification for not voting!](https://telegra.ph/file/87d475a8f9a8350d2450e.jpg)", link_preview=True)

    if x == 28:

        await event.edit("[When your partner expects you to do too many things...](https://telegra.ph/file/68bc768d36e08862bf94e.jpg)", link_preview=True)

    if x == 29:

        await event.edit("[When your friends cancel on the plan you made at the last minute...](https://telegra.ph/file/960b58c8f625b17613307.jpg)", link_preview=True)

    if x == 30:

        await event.edit("[For that friend of yours who does not like loud music and head banging...](https://telegra.ph/file/acbce070d3c52b921b2bd.jpg)", link_preview=True)


@register(outgoing=True, pattern="^.gott(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Typing...")
    await asyncio.sleep(2)
    x = (random.randrange(1, 40))
    if x == 1:
        await event.edit("`\"The man who passes the sentence should swing the sword.\"`")
    if x == 2:
        await event.edit("`\"When the snows fall and the white winds blow, the lone wolf dies but the pack survives!\"`")
    if x == 3:
        await event.edit("`\"The things I do for love!\"`")
    if x == 4:
        await event.edit("`\"I have a tender spot in my heart for cripples, bastards and broken things.\"`")
    if x == 5:
        await event.edit("`\"Death is so terribly final, while life is full of possibilities.\"`")
    if x == 6:
        await event.edit("`\"Once you’ve accepted your flaws, no one can use them against you.\"`")
    if x == 7:
        await event.edit("`\"If I look back I am lost.\"`")
    if x == 8:
        await event.edit("`\"When you play the game of thrones, you win or you die.\"`")
    if x == 9:
        await event.edit("`\"I grew up with soldiers. I learned how to die a long time ago.\"`")
    if x == 10:
        await event.edit("`\"What do we say to the Lord of Death?\nNot Today!\"`")
    if x == 11:
        await event.edit("`\"Every flight begins with a fall.\"`")
    if x == 12:
        await event.edit("`\"Different roads sometimes lead to the same castle.\"`")
    if x == 13:
        await event.edit("`\"Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you.\"`")
    if x == 14:
        await event.edit("`\"The day will come when you think you are safe and happy, and your joy will turn to ashes in your mouth.\"`")
    if x == 15:
        await event.edit("`\"The night is dark and full of terrors.\"`")
    if x == 16:
        await event.edit("`\"You know nothing, Jon Snow.\"`")
    if x == 17:
        await event.edit("`\"Night gathers, and now my watch begins!\"`")
    if x == 18:
        await event.edit("`\"A Lannister always pays his debts.\"`")
    if x == 19:
        await event.edit("`\"Burn them all!\"`")
    if x == 20:
        await event.edit("`\"What do we say to the God of death?\"`")
    if x == 21:
        await event.edit("`\"There's no cure for being a c*nt.\"`")
    if x == 22:
        await event.edit("`\"Winter is coming!\"`")
    if x == 23:
        await event.edit("`\"That's what I do: I drink and I know things.\"`")
    if x == 24:
        await event.edit("`\"I am the dragon's daughter, and I swear to you that those who would harm you will die screaming.\"`")
    if x == 25:
        await event.edit("`\"A lion does not concern himself with the opinion of sheep.\"`")
    if x == 26:
        await event.edit("`\"Chaos isn't a pit. Chaos is a ladder.\"`")
    if x == 27:
        await event.edit("`\"I understand that if any more words come pouring out your c*nt mouth, I'm gonna have to eat every f*cking chicken in this room.\"`")
    if x == 28:
        await event.edit("`\"If you think this has a happy ending, you haven't been paying attention.\"`")
    if x == 29:
        await event.edit("`\"If you ever call me sister again, I'll have you strangled in your sleep.\"`")
    if x == 30:
        await event.edit("`\"A girl is Arya Stark of Winterfell. And I'm going home.\"`")
    if x == 31:
        await event.edit("`\"Any man who must say 'I am the King' is no true King.\"`")
    if x == 32:
        await event.edit("`\"If I fall, don't bring me back.\"`")
    if x == 33:
        await event.edit("`\"Lannister, Targaryen, Baratheon, Stark, Tyrell... they're all just spokes on a wheel. This one's on top, then that one's on top, and on and on it spins, crushing those on the ground.\"`")
    if x == 34:
        await event.edit("`\"Hold the door!`")
    if x == 35:
        await event.edit("`\"When people ask you what happened here, tell them the North remembers. Tell them winter came for House Frey.\"`")
    if x == 36:
        await event.edit("`\"Nothing f*cks you harder than time.\"`")
    if x == 37:
        await event.edit("`\"There is only one war that matters. The Great War. And it is here.\"`")
    if x == 38:
        await event.edit("`\"Power is power!\"`")
    if x == 39:
        await event.edit("`\"I demand a trial by combat!\"`")
    if x == 40:
        await event.edit("`\"I wish I was the monster you think I am!\"`")


@register(outgoing=True, pattern="^.hp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Casting spell...")
    await asyncio.sleep(2)
    x = (random.randrange(1, 76))
    if (x == 1):
        await event.edit("**Halo pulici**")
    if (x == 2):
        await event.edit("**Disini ada babu ngerusuh**")
    if (x == 3):
        await event.edit("**Tolong yah pulici**")
    if (x == 4):
        await event.edit("**Penjara babu ini,dia gila**")
    if (x == 5):
        await event.edit("*ORTU NYA JUGA DAH GANGURUS**")
    if (x == 6):
        await event.edit("**KARNA DIA BEBAN ORTU**")
    if (x == 7):
        await event.edit("**MENDING PENJARA DIA!!**")
    if (x == 8):
        await event.edit("**Bener bener gaguna**")
    if (x == 9):
        await event.edit("**Udah gabut nya jelek**")
    if (x == 10):
        await event.edit("*Tukang ngerusuh**")
    if (x == 11):
        await event.edit("**Mungkin otak nya dah gawaras**")
    if (x == 12):
        await event.edit("**Atau sikis nya dah kena**")
    if (x == 13):
        await event.edit("**ATAU MUNGKIN EFEK BROKEN HOME**")
    if (x == 14):
        await event.edit("**BROKEN HEART**")
    if (x == 15):
        await event.edit("**BROKEN MENTAL**")
    if (x == 16):
        await event.edit("**KASIAN KAN DIA**")
    if (x == 17):
        await event.edit("**MENDING DI PENJARA**")
    if (x == 18):
        await event.edit("**AYO PULICI**")
    if (x == 19):
        await event.edit("**PENJARAKAN DIA**")
    if (x == 20):
        await event.edit("**YO BISA YO**")
    if (x == 21):
        await event.edit("**SUKA WAR DI TELEGRAM**")
    if (x == 22):
        await event.edit("**TAPI KALO KETRIGGER**")
    if (x == 23):
        await event.edit("**MINTA SHARELOK**")
    if (x == 24):
        await event.edit("**TAPI GA DI SAMPERIN**")
    if (x == 25):
        await event.edit("**OWH MUNGKIN GA ADA ONGKOS**")
    if (x == 26):
        await event.edit("**O IYA KAN MISKIN**")
    if (x == 27):
        await event.edit("**PENGANGGURAN**")
    if (x == 28):
        await event.edit("**BEBAN ORTU**")
    if (x == 29):
        await event.edit("**TYDACK BERGUNA**")
    if (x == 30):
        await event.edit("**ALIAS SAMPAH GC**")
    if (x == 31):
        await event.edit("**POKOKNYA**")
    if (x == 32):
        await event.edit("**DIA GA PANTES HIDUP**")
    if (x == 33):
        await event.edit("**UDAH JELEK**")
    if (x == 34):
        await event.edit("**DEKIL**")
    if (x == 35):
        await event.edit("**BAU**")
    if (x == 36):
        await event.edit("**KASIAN KAN**")
    if (x == 37):
        await event.edit("**KASIAN BANGET**")
    if (x == 38):
        await event.edit("**SERIUS DAH**")
    if (x == 39):
        await event.edit("**MAU NGOMONG APA LG YA?**")
    if (x == 40):
        await event.edit("**YA POKOK NYA**")
    if (x == 41):
        await event.edit("**DIA GILA**")
    if (x == 42):
        await event.edit("**IDIHHH**")
    if (x == 43):
        await event.edit("**NGAPAIN DI LIATIN?**")
    if (x == 44):
        await event.edit("**ASTOGEEELL**")
    if (x == 45):
        await event.edit("**INI PANJANG BGT**")
    if (x == 46):
        await event.edit("**GUA MAU NGATA APA LG YA**")
    if (x == 47):
        await event.edit("**PULICI UDH YA**")
    if (x == 48):
        await event.edit("**TAPI PANJANG BGT**")
    if (x == 49):
        await event.edit("**CAPE NGEDIT NYA AJG**")
    if (x == 50):
        await event.edit("**ETT DAH BUSEHHH**")
    if (x == 51):
        await event.edit("**ADDAH**")
    if (x == 52):
        await event.edit("**AYOLAHHH**")
    if (x == 53):
        await event.edit("**PANJANG BANGET BRO**")
    if (x == 54):
        await event.edit("**BENERAN**")
    if (x == 55):
        await event.edit("**GA BOHONG**")
    if (x == 56):
        await event.edit("**DEMI APASI**")
    if (x == 57):
        await event.edit("**TWINGGGG**")
    if (x == 58):
        await event.edit("**BUJUG**")
    if (x == 59):
        await event.edit("*NELPON PULICI LAMA BAT**")
    if (x == 60):
        await event.edit("**ASTAGHFIRULLAH**")
    if (x == 61):
        await event.edit("**GARA GARA BABU**")
    if (x == 62):
        await event.edit("**GUA JADI GEDEG**")
    if (x == 63):
        await event.edit("**BABU PEA**")
    if (x == 64):
        await event.edit("**LAEN KLI JANGAN NGERUSUH**")
    if (x == 65):
        await event.edit("**KALO GABUT**")
    if (x == 66):
        await event.edit("**BUKA CHANNEL BOKEP**")
    if (x == 67):
        await event.edit("**TRUS COLI**")
    if (x == 68):
        await event.edit("**ABIS ITU BOBO**")
    if (x == 69):
        await event.edit("**BESOK NYA MENINGGAL**")
    if (x == 70):
        await event.edit("**PANJANG BGT SERIUS**")
    if (x == 71):
        await event.edit("**CAPE NGEDIT**")
    if (x == 71):
        await event.edit("**ALLAHU AKBAR**")
    if (x == 73):
        await event.edit("**DAH SEGITU AJAH**")
    if (x == 74):
        await event.edit("**JANGAN BANYAK BANYAK**")
    if (x == 75):
        await event.edit("**BABAYY MWAHHH🥰😘**")


@register(outgoing=True, pattern="^.suits(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Typing...")
    await asyncio.sleep(2)
    x = (random.randrange(1, 43))
    if x == 1:
        await event.edit("`\"The only time success comes before work is in the dictionary.\"`")
    if x == 2:
        await event.edit("`\"That’s the difference between you and me, you wanna lose small, I wanna win big.\"`")
    if x == 3:
        await event.edit("`\"When you are backed against the wall, break the goddamn thing down.\"`")
    if x == 4:
        await event.edit("`\"If they think you care, they’ll walk all over you.\"`")
    if x == 5:
        await event.edit("`\"I don’t have dreams, I have goals.\"`")
    if x == 6:
        await event.edit("`\"It’s going to happen, because I am going to make it happen.\"`")
    if x == 7:
        await event.edit("`\"Ever loved someone so much, you would do anything for them? Yeah, well make that someone yourself and do whatever the hell you want.\"`")
    if x == 8:
        await event.edit("`\"I like to smile at people who don’t like me.\"`")
    if x == 9:
        await event.edit("`\"Don’t raise your voice, improve your argument.\"`")
    if x == 10:
        await event.edit("`\"You want to change your life? Change the way you think.\"`")
    if x == 11:
        await event.edit("`\"Have goals so big you get uncomfortable telling small minded people.\"`")
    if x == 12:
        await event.edit("`\"Kill them with success. Bury them with a smile.\"`")
    if x == 13:
        await event.edit("`\"Winners don’t make excuses.\"`")
    if x == 14:
        await event.edit("`\"It's not a problem if you always win.\"`")
    if x == 15:
        await event.edit("`\"I don’t play the odds I play the man.\"`")
    if x == 16:
        await event.edit("`\"You always have a choice.\"`")
    if x == 17:
        await event.edit("`\"Sorry, I can’t hear you over the sound of how awesome I am.\"`")
    if x == 18:
        await event.edit("`\"Anyone can do my job, but no one can be me.\"`")
    if x == 19:
        await event.edit("`\"I believe in work, I don’t fuck with luck.\"`")
    if x == 20:
        await event.edit("`\"It’s not bragging if it’s true.\"`")
    if x == 21:
        await event.edit("`\"Win a no win situation by rewriting the rules.\"`")
    if x == 22:
        await event.edit("`\"Let them hate, just make sure they spell your name right.\"`")
    if x == 23:
        await event.edit("`\"That’s the difference between you and me. You wanna lose small, I wanna win big.\"`")
    if x == 24:
        await event.edit("`\"Oh you have no idea how Donna I am.\"`")
    if x == 25:
        await event.edit("`\"It is so much easier to criticize someone else than it is to acknowledge your own shortcomings.\"`")
    if x == 26:
        await event.edit("`\"And if you think I'm smarter than you? You're damn right I do. But if you think that means I can't kick your ass up and down this floor, take a swing. See what happens.\"`")
    if x == 27:
        await event.edit("`\"If they had did it once, they will do it again.\"`")
    if x == 28:
        await event.edit("`\"He goes, I go.\"`")
    if x == 29:
        await event.edit("`\"First impressions last. You start behind the eight ball, you'll never get in front.\"`")
    if x == 30:
        await event.edit("`\"I don't respond to threats. I make them.\"`")
    if x == 31:
        await event.edit("`\"Nobody does anything as a courtesy. They sent you where they want you to look. Listen, being a lawyer is a lot like being a doctor.\"`")
    if x == 32:
        await event.edit("`\"Sometimes I like to hangout with people that aren't that bright. You know, just to see how the other halves live.\"`")
    if x == 33:
        await event.edit("`\"Never destroy anyone in public when you can accomplish the same result in private.\"`")
    if x == 34:
        await event.edit("`\"You don’t send a puppy to clean up its own mess.\"`")
    if x == 35:
        await event.edit("`\"Gloating is fine, you just not have to suck at it.\"`")
    if x == 36:
        await event.edit("`\"It's not bragging if it's true.\"`")
    if x == 37:
        await event.edit("`\"Sometimes good guys gotta do bad things to make the bad guys pay.\"`")
    if x == 38:
        await event.edit("`\"I don't pave the way for people,people pave the way for me.\"`")
    if x == 39:
        await event.edit("`\"My respect isn't demanded, it's earnt.\"`")
    if x == 40:
        await event.edit("`\"I don't get lucky, I make my own luck.\"`")
    if x == 41:
        await event.edit("`\"This isn't elementary school. This is hard work, long hours, high pressure. I need a grown godamn man.\nYou give me this, and I'll work as hard as it takes to school those Harvard douches and become the best lawyer you have ever seen.\"`")
    if x == 42:
        await event.edit("`\"Love is a terrifying thing\nIt’s not safe. Because when you love someone, you have to face the fact that you can lose them.\nSometimes life throws an unexpected wrench in your way. It might be that you’re in jeopardy of losing your career, your freedom, or worst of all, you might even find out that a loved one has died\nThese things make you realize how precious life is, how important every second we have on this earth is, and how important the people we care about are to us.\"`")
