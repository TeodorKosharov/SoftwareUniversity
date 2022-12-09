class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        result = ''
        if self.hours < 10:
            result += '0' + str(self.hours) + ':'
        else:
            result += str(self.hours) + ':'

        if self.minutes < 10:
            result += '0' + str(self.minutes) + ':'
        else:
            result += str(self.minutes) + ':'

        if self.seconds < 10:
            result += '0' + str(self.seconds)
        else:
            result += str(self.seconds)

        return result

    def next_second(self):
        self.seconds += 1

        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1

                if self.hours > Time.max_hours:
                    self.hours = 0

        return self.get_time()


# Test code:

time = Time(9, 30, 59)
print(time.next_second())

time1 = Time(10, 59, 59)
print(time1.next_second())

time2 = Time(23, 59, 59)
print(time2.next_second())
