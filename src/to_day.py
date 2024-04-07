import datetime

def main():
    # Get today's date
    today = datetime.datetime.now()
    # Get the name of the day
    day_name = today.strftime("%A")
    return day_name

if __name__ == "__main__":
    main()