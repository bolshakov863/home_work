class Animal:
    def speak(self):
        print('Издавать звуки')

class Dog(Animal):
    def speak(self):
        print('Гав-Гав!')

class BigDog(Dog):
    def speak(self):
        print('Вау-вау!')

class SmallDog(Dog):
    def speak(self):
        print('Тяв-Тяв!')

class ToyDog(SmallDog):
    def speak(self):
        print('Я игрушечная собака!')

class RobotDog(ToyDog):
    def speak(self):
        print('Рав-Рав')

class AngryBigDog(BigDog):
    def speak(self):
        super().speak()
        print('Очень злой взгляд!')
        print('хмурится')

class Cat(Animal):
    def _meow(self):
        print('Мяу!')
    def speak(self):
        self._meow()

class Cheshirsky_Cat(Cat):
    def _meow(self):
        print('Мяу-мяу!')

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

big_dog = BigDog()
big_dog.speak()

small_dog = SmallDog()
small_dog.speak()

toy_dog = ToyDog()
toy_dog.speak()

robot_dog = RobotDog()
robot_dog.speak()

angry_big_dog = AngryBigDog()
angry_big_dog.speak()

cat = Cat()
cat.speak()

cheshirsky_cat = Cheshirsky_Cat()
cheshirsky_cat.speak()

def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()

druzok = Cheshirsky_Cat()
say_n_times(druzok, 5)

list_of_animal = [Cat(),Dog(),Cheshirsky_Cat(),AngryBigDog()]
for animal in list_of_animal:
    animal.speak()
    print('--------------------------------')

for animal in list_of_animal:
    say_n_times(animal, 5)
    print('--------------------------------')


