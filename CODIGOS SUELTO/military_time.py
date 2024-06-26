time = '11 : 00 PM'
time = time.replace(' ', '')

if time[-2:]=='AM':
    print(time[:-2])
if time[-2:]=='PM':
    hour = time[:2]
    hour = int(hour)
    hour += 12
    hour=str(hour)
    minut = time[3:5]
    print(hour+':'+minut)