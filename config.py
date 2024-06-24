TOKEN = "TELEGRAM BOT TOKEN" # Токен бота из Телеграм


# Определение текста для сообщений
help_msg = "Этот бот подскажет когда приедет автобус в указанную станцию. Для этого просто введите номер маршрута и станцию через пробел\n"\
    "Например: 437 A\n"\
    "Для получения списка маршрутов введите /routes\n"\
    "Для получения справки введите /help"

routes_msg = "Маршруты: {routes}"

args_error_msg = "Не хватает аргументов. Пример ввода: 104 A"

route_error_msg = "Номер маршрута должен быть числом. Пример ввода: 104 A"

no_file_error_msg = "Указанный маршрут \"{route}\" не найден"

no_station_error_msg = "Указанная станция \"{station}\" не найдена"