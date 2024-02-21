# Inheritance
# Polymorphic
# Attribute protocol
# Encapsulation using __setattr__


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if value < 0:
            raise ValueError("only positive values are allowed")
        super().__setattr__(key, value)


class PositivePoint(Point):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Only numbers are allowed")
        super().__setattr__(key, value)


# p1 = PositivePoint('hi', 10)
# p2 = PositivePoint(-1, 5)
p3 = PositivePoint(5, 9)
print(p3.__dict__)


# Abstraction
# Inheritance
# Composition
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)
    # pass


class TextFileLoggger(Logger):
    def __init__(self, file_obj):
        self.file_obj = file_obj

    def log(self, message):
        self.file_obj.write(message)
        self.file_obj.write('\n')
        self.file_obj.flush()


# (HAS-A) relationship
# composition
class MixLogger:
    def __init__(self, logger, pattern):        # dependency injection
        self.logger = logger
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message:
            self.logger.log(message)


cl = ConsoleLogger()
cl.log("this is an INFO message")
file = open("sample.txt", "w")
tfl = TextFileLoggger(file_obj=file)
tfl.log("this is a LOG message")
mcl = MixLogger(cl, "INFO")
mcl.log("this is an INFO message")
mtfl = MixLogger(tfl, "LOG")
mtfl.log("this is a LOG message")


from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        print(message)


class ConsoleLogger(Logger):

    def log(self, message):
        super().log(message)


class TextFileLogger(Logger):

    def __init__(self, file_obj):
        self.file_obj = file_obj

    def log(self, message):
        self.file_obj.write(message)
        self.file_obj.write('\n')
        self.file_obj.flush()


class CSVLogger(Logger):

    def __init__(self, file_obj):
        self.file_obj = file_obj

    def log(self, message):
        from csv import writer
        csv_obj = writer(self.file_obj)
        csv_obj.writerow(message.split())
        self.file_obj.flush()


# SUb class explosion
# IS-A relationship (Inheritance)
class FilterConsoleLogger(ConsoleLogger):

    def __init__(self, pattern):
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message:
            super().log(message)


# IS_A relationship (Inheritance)
class FilterTextFileLogger(TextFileLogger):

    def __init__(self, pattern, file_obj):
        self.pattern = pattern
        super().__init__(file_obj)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


# IS-A relationship (Inheritance)
class FilterCSVLogger(CSVLogger):

    def __init__(self, pattern, file_obj):
        self.pattern = pattern
        super().__init__(file_obj)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


# HAS-A relationship (composition)
class MixFilterLogger:

    def __init__(self, logger, pattern):        # dependency injection
        self.pattern = pattern
        self.logger = logger

    def log(self, message):         # polymorphic behaviour og log method
        if self.pattern in message:
            self.logger.log(message)


# Inheritance
# Encapsulation
# Polymorphism
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, item, value):
        if not isinstance(value, (int, float)):
            raise TypeError("only numbers are allowed")
        super().__setattr__(item, value)


class PositivePoint(Point):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __setattr__(self, item, value):
        if value < 0:
            raise ValueError("only positive values are allowed")
        super().__setattr__(item, value)


# Encapsulation
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("only numbers are allowed")
        if value < 0:
            raise ValueError("only positive values are allowed")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("only numbers are allowed")
        if value < 0:
            raise ValueError("only positive values are allowed")
        self._b = value
