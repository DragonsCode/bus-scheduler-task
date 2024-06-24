import os
import re
from datetime import datetime, time, timedelta


def create_bus(stops: list[str], times: list[int], start_time: timedelta, end_time: timedelta, file_name: str, interval: int = 5, buses: int = 1) -> None:
    """
    Функция для генерацию расписаня для маршрута
    stops - список со станциями
    times - список с интервалами между станциями в минутах
    start_time - время начала работы маршрута
    end_time - время окончания работы маршрута, указывать day=1 если водитель работает и ночью следующего дня
    file_name - название маршрута для названия файла, к примеру если параметр задан "104", то файл будет назван "104.txt"
    interval - интервал между автобусами в минутах
    buses - количество автобусов в маршруте
    """
    stop = stops[0]
    b = start_time.seconds//60//60
    k = end_time.seconds//60//60
    d = times[0]
    e = times[0]

    file = open(f"routes/{file_name}.txt", "w")
    tm3=start_time
    c=timedelta(hours=0)

    while c<end_time:
        try:
            stop = stops[stops.index(stop)+1]
        except IndexError:
            stops.reverse()
            stop = stops[1]
        
        try:
            d = times[times.index(d)+1]
        except IndexError:
            times.reverse()
            d = times[0]
        
        inter=0
        dest=stops[-1]

        for i in range(buses):
            tm4 = timedelta(hours=0, minutes=0+e+inter)
            c=tm3 + tm4
            inter+=interval
            b = c.seconds//60//60
            file.write(f"{c}; {stop}; {dest}\n")
        
        e += d
    file.close()


def predict(route: str, station: str) -> str:
    """
    Функция для вычисления ближайшего автобуса по указанному маршруту route к указанной станции station
    """
    file = open(f"routes/{route}.txt", "r")
    
    data = {}
    
    for line in file:
        i = line.replace("\n", "").split(";")
        data[i[0]] = [i[1], i[2]]
    file.close()
    
    all_times = []
    dests = []
    now = datetime.now()
    tm2 = timedelta(hours=now.hour, minutes=now.minute)

    if now.hour>-1 and now.hour<5:
        tm2 = timedelta(days=1, hours=now.hour, minutes=now.minute)
    
    for i in data:
        tm = None

        if "1 day, " in i:
            l=i.replace("1 day, ", "").split(':')
            d=1
            h, m, s = l[0], l[1], l[2]
            h=int(h)
            m=int(m)
            tm = timedelta(days=d, hours=h, minutes=m)
        else:
            l = i.split(':')
            h, m, s = l[0], l[1], l[2]
            h=int(h)
            m=int(m)
            tm = timedelta(hours=h, minutes=m)
        
        all_times.append(tm)
    all_times.sort()

    for i in all_times:
        if i>tm2:
            if data[str(i)][0]==" "+station and data[str(i)][1] not in dests:
                dests.append(data[str(i)][1])
                return f"Время: {tm2}\n"\
                       f"Станция: {station}\n"\
                       f"Маршрут: {route}\n"\
                       f"Ближайший автобус примерно приедет в: {i}\n"\
                       f"Примерное время ожидания: {i-tm2}\n"\
                       f"Направляется в станцию: {data[str(i)][1]}"


def get_routes(directory = "routes"):
    """
    Функция для получения списка маршрутов из существующих файлов
    """
    files = os.listdir(directory)

    numeric_files = [re.match(r"(\d+)\.txt", file) for file in files]
    numeric_parts = [match.group(1) for match in numeric_files if match]

    return tuple(numeric_parts)