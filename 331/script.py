import datetime
import time

with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        ch, cm = map(int, f.readline().strip().split(':'))
        h, m = map(int, f.readline().strip().split(' '))

        # option 1, mathematics:
        # nm = (cm + m) % 60
        # nh = (ch + h + int(cm + m >= 60)) % 24
        #
        # o.write(f'{str(nh).zfill(2)}:{str(nm).zfill(2)}')

        # option 2, library:

        var = datetime.datetime(2000, 1, 1, ch, cm, 0) + datetime.timedelta(hours=h, minutes=m)
        o.write(var.strftime('%H:%M'))
