import asyncio
import time
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register



@register(outgoing=True, pattern='^.mun(?: |$)(.*)')
async def mun(typew):
    for _ in range(50):
        await typew.edit("๐")
        await asyncio.sleep(0.3)
        await typew.edit("๐")
        await asyncio.sleep(0.3)

@register(outgoing=True, pattern='^.lav(?: |$)(.*)')
async def mun(typew):
    for _ in range(10):
        await typew.edit("๐งก")
        await asyncio.sleep(0.5)
        await typew.edit("๐")
        await asyncio.sleep(0.5)
        await typew.edit("๐")
        await asyncio.sleep(0.5)
        await typew.edit("๐")
        await asyncio.sleep(0.5)
        await typew.edit("๐")
        await asyncio.sleep(0.5)
        await typew.edit("๐ค")
        await asyncio.sleep(0.5)
