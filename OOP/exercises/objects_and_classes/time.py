class Time:
    max_seconds = 59
    max_minutes = 59
    max_hours = 23

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        s_leading_zero = '0' if self.seconds < 10 else ''
        m_leading_zero = '0' if self.minutes < 10 else ''
        h_leading_zero = '0' if self.hours < 10 else ''

        return (f"{h_leading_zero}{self.hours}:{m_leading_zero}"
                f"{self.minutes}:{s_leading_zero}{self.seconds}")

    def next_second(self):
        increment = 0

        self.seconds += 1
        if self.seconds > self.__class__.max_seconds:
            self.seconds = 0
            increment = 1

        self.minutes += increment
        if self.minutes > self.__class__.max_minutes:
            self.minutes = 0
            increment = 1
        else:
            increment = 0

        self.hours += increment
        if self.hours > self.__class__.max_hours:
            self.hours = 0

        return self.get_time()


time = Time(9, 30, 59)
print(time.get_time())
print(time.next_second())

time = Time(10, 59, 59)

print(time.next_second())

time = Time(23, 59, 59)

print(time.next_second())