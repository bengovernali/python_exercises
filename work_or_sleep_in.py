day = int(input('Day (0-6)? '))

def work_or_sleep_in(day):
    if day == 0 or day == 6:
        print("Sleep in")
    else:
        print("Go to work")

work_or_sleep_in(day)