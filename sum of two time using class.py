class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour # Private attribute
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        total_seconds = self.__second + other.__second
        total_minutes = self.__minute + other.__minute + (total_seconds // 60)
        total_hours = self.__hour + other.__hour + (total_minutes // 60)

        seconds = total_seconds % 60
        minutes = total_minutes % 60
        hours = total_hours % 24 # Assume a 24-hour clock

        return Time(hours, minutes, seconds)

    def display(self):
        print(f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}")

hour1 = int(input("Enter hours for Time 1: "))
minute1 = int(input("Enter minutes for Time 1: "))
second1 = int(input("Enter seconds for Time 1: "))

hour2 = int(input("Enter hours for Time 2: "))
minute2 = int(input("Enter minutes for Time 2: "))
second2 = int(input("Enter seconds for Time 2: "))

time1 = Time(hour1, minute1, second1)
time2 = Time(hour2, minute2, second2)

time_sum = time1 + time2

print("\nSum of Times:")
time_sum.display()