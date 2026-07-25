def main():
    time = input("Enter time: ")
    return_time = convert(time)
    if return_time >= 7 and return_time <= 8:
        print("breakfast time")
    elif return_time >= 12 and return_time <= 13:
        print("lunch time")
    elif return_time >= 18 and return_time <= 19:
        print("dinner time")
    else :
        return 0
def convert(time):
    hour,minute = time.split(":")
    hour = float(hour)
    minute = float(minute) / 60
    return hour + minute
if __name__ == "__main__":
    main()