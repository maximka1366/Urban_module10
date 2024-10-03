import time
from threading import Thread



class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        vragi = 100
        days = 0
        while  vragi > 0:
            days = days  + 1
            vragi = vragi-self.power
            print(f"{self.name} сражается {days} дней(дня)..., осталось {vragi} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")