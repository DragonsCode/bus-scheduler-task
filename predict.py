from datetime import datetime, time, timedelta

def predict(route, station):
    file = open(f"{route}.txt", "r")
    
    data = {}
    
    for line in file:
        i = line.replace("\n", "").split(";")
        data[i[0]] = [i[1], i[2]]
    
    all_times = []
    dests = []
    now = datetime.now()
    tm2 = timedelta(hours=now.hour, minutes=now.minute)
    if now.hour>-1 and now.hour<5:
        tm2 = tm2 = timedelta(days=1, hours=now.hour, minutes=now.minute)
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
                print("Время: ", tm2, "\nСтанция: ", station, f"\nМаршрут: {route}","\nБлижайший автобус приедет в: ", i, "\nЖдать нужно: ", i-tm2, "\nНаправляется в станцию: ", data[str(i)][1], "\n")
    
    file.close()
stat=input()
predict(route="437", station=stat)
predict(route="104", station=stat)