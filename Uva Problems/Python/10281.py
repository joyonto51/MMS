def Time(x):
    h, m, s = map(int, x.split(':'))
    s = int(s)
    m = int(m * 60)
    h = int(h * 60 * 60)
    sum = h + m + s
    return sum
def sp(w):
    return int(w)

speed_1 = 0
speed_2 = 0
time_1 = 0
time_2 = 0
dist = 0
while True:
    try:
        T = input()
    except:
        break
    if len(T.split()) == 2:
        string_time, speed = T.split()
        speed_2 = float(speed)
        time_2 = float(Time(string_time))
        dist += float((speed_1/3600)*(time_2-time_1))
        speed_1 = speed_2
        time_1 = time_2

    else:
        d = float(Time(T))
        e = float((d-time_1)*(speed_1/3600))
        f = float(dist+e)
        print("{} {:.2f} km".format(T,f))
