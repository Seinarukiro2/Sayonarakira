
import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.adm(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Начинаю процедуру получения админ-доступа...`")
	sleep(1)
	await typew.edit("0%")
	number = 1
	await typew.edit(str(number) + "%   ▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	sleep(1)
	await typew.edit("`Админка взломана успешно, доступ предоставлен!`")
