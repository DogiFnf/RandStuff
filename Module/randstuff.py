from pyrogram.addons.PyroArgs.utils.DataHolder import PyroArgsObj as app
from pyrogram.addons.PyroArgs.types import Message
import Libs.utils as ub
import aiohttp
import json

category = '▫️ Рандомное'


async def get_rand(string: str) -> dict:
    async with aiohttp.ClientSession() as session:
        headers = {
            'x-requested-with': 'XMLHttpRequest'
        }
        async with session.get(
            f'https://randstuff.ru/{string}/generate',
            headers=headers
        ) as res:
            res.raise_for_status()
            response = json.loads(await res.text())
    return response


@app.command(
     description='Случайная шутка',
     usage='.joke',
     example='.joke',
     command_meta_data='◼️',
     category=category
)
async def joke(ctx: Message):
    response = await get_rand('joke')
    await ub.answer(ctx, response['joke']['text'])


@app.command(
     description='Случайный факт',
     usage='.fact',
     example='.fact',
     command_meta_data='◼️',
     category=category
)
async def fact(ctx: Message):
    response = await get_rand('fact')
    await ub.answer(ctx, response['fact']['text'])


@app.command(
     description='Случайная мудрость',
     usage='.saying',
     example='.saying',
     command_meta_data='◼️',
     category=category
)
async def saying(ctx: Message):
    response = await get_rand('saying')
    await ub.answer(ctx, response['saying']['text'])


@app.command(
    description='Генератор паролей',
    usage='.password [длина] [использовать цыфры] [использовать спецсимволы]',
    example='.password 12 y n',
    command_meta_data='◼️',
    category=category
)
async def password(
    ctx: Message,
    length: int = 6,
    use_numbers: str = 'n',
    use_special: str = 'n'
):
    def generate(length, use_numbers, use_special):
        import random
        import string
        chars = string.ascii_lowercase
        chars += string.ascii_uppercase
        if use_numbers == 'y':
            chars += string.digits
        if use_special == 'y':
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    await ub.answer(ctx, generate(length, use_numbers, use_special))
