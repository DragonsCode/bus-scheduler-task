from functions import create_bus, get_routes
import logging


def create_routes():
    """
    Функция создает тестовые маршруты 437 и 104 с тестовыми станциями A, B, C, D, E, F
    """
    routes = get_routes()
    if not routes:
        logging.info("Создание тестовых маршрутов 104 и 437")
        create_bus(stops=["E", "A", "B", "F"], times=[6, 3, 5], start_time=timedelta(hours=5, minutes=10), end_time=timedelta(days=1, hours=1, minutes=30), file_name="437", interval=5, buses=3)
        create_bus(stops=["A", "B", "C", "D"], times=[3, 5, 4], start_time=timedelta(hours=5), end_time=timedelta(days=1, hours=1), file_name="104", interval=10, buses=3)
    else:
        logging.info(f"Маршруты уже существуют: {routes}")
