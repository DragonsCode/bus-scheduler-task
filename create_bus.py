from datetime import datetime, time, timedelta

def create_bus(stops, times, start_time, end_time, file_name, interval, buses):
    stop = stops[0]
    b = start_time.seconds//60//60
    k = end_time.seconds//60//60
    print(b)
    print(k)
    d = times[0]
    e = times[0]
    file = open(f"{file_name}.txt", "w")
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
            print(stop, c, dest)
            inter+=interval
            b = c.seconds//60//60
            file.write(f"{c}; {stop}; {dest}\n")
        e += d
    
    file.close()

create_bus(stops=["E", "A", "B", "F"], times=[6, 3, 5], start_time=timedelta(hours=5, minutes=10), end_time=timedelta(days=1, hours=1, minutes=30), file_name="437", interval=5, buses=3)

create_bus(stops=["A", "B", "C", "D"], times=[3, 5, 4], start_time=timedelta(hours=5), end_time=timedelta(days=1, hours=1), file_name="104", interval=10, buses=3)