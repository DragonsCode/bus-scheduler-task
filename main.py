import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import *
from functions import predict, get_routes
from routes import create_routes


# Диспетчер для хендлеров
dp = Dispatcher()


@dp.message(CommandStart())
@dp.message(Command(commands=['help']))
async def help_handler(message: Message) -> None:
    """
    Отправляет пользователю сообщение с инструкцией
    """
    await message.answer(help_msg)


@dp.message(Command(commands=['routes']))
async def routes_handler(message: Message) -> None:
    """
    Отправляет пользователю список маршрутов
    """
    routes = get_routes()
    await message.answer(routes_msg.format(routes=', '.join(routes)))


@dp.message()
async def bus_handler(message: Message) -> None:
    """
    Отправляет пользователю информацию о ближайшем автобусе к указанной станции в указанном маршруте
    """
    args = message.text.split(' ')

    if len(args) < 2:
        await message.answer(args_error_msg)
        return
    
    if not args[0].isdigit():
        await message.answer(route_error_msg)
        return
    
    try:
        predicted = predict(args[0], ' '.join(args[1:]))
    except:
        await message.answer(no_file_error_msg.format(route=args[0]))
        return
    
    if not predicted:
        await message.answer(no_station_error_msg.format(station=' '.join(args[1:])))
        return
    
    await message.answer(predicted)


async def main() -> None:
    # Инициализация объекта бота с настройками по умолчанию
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Создание тестовых маршрутов
    create_routes()

    # Запуск обработки событий
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())