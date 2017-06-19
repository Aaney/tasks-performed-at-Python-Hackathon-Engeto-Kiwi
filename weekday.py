# task from: http://hack.engeto.com/weekday

from datetime import date
import re

def tell_weekday(ymd):
    indexedWeekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # weekday names not used in the end
    try:
        matchObject = re.search(r"\(\d{4},\d\d?,\d\d?\)", ymd)
        datum = matchObject.group(0)
        a, b, c = datum.split(",")
        y, m, d = int(a[1:]), int(b), int(c[:len(c)-1])

        if date(y,m,d)<date(1970,1,1):
            return -1
        else:
            try:
                weekIndex = date(y, m, d).isoweekday()
                weekdayName = indexedWeekdays[weekIndex-1]
                # return weekdayName
                return weekIndex
            except ValueError:
                print("Non-existent date")
                return 0
    except ValueError:
        print("Non-existent date")
        return 0


def tell_weekday_test():
    print(tell_weekday("(1969,12,31)") == -1)
    print(tell_weekday("(2017,6,17)") == 6)
    print(tell_weekday("(2015,2,29)") == 0)
    print(tell_weekday("(1970,1,1)") == 4)
# tell_weekday_test()

print(tell_weekday("(1966,5,13)"))
