import pickle

class Animal ():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает")


class Bird(Animal):
    birds = []
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type
        Bird.birds.append(self)

    def make_sound(self):
        print(f"{self.name} говорит Чирик")

class Mammal(Animal):
    mammals = []
    def __init__(self, name, age, type_of_eating):
        super().__init__(name, age)
        self.type_of_eating = type_of_eating
        Mammal.mammals.append(self)

    def make_sound(self):
        print(f"{self.name} зовет друга покушать")

class Reptile(Animal):
    reptiles = []
    def __init__(self, name, age, new_skin):
        super().__init__(name, age)
        self.new_skin = new_skin
        Reptile.reptiles.append(self)

    def make_sound(self):
        print(f"{self.name} говорит Шшшшш")

class ZooKeeper():
    zookeepers = []
    def __init__(self, name, spec):
        self.name = name
        self.spec = spec
        ZooKeeper.zookeepers.append(self)

    def feed_animal(self, animal):
        print(f"Смотритель {self.name} кормит животное - {animal}")

class Vet():
    vets = []
    def __init__(self, name, spec):
        self.name = name
        self.spec = spec
        Vet.vets.append(self)

    def heat_animal(self, animal):
        print(f"Ветеринар {self.name} лечит животное - {animal}")

class Zoo():
    zoos = []
    def __init__(self, name, birds, mammals , reptiles , zookeepers , vets):
        self.name = name
        self.birds = birds
        self.mammals = mammals
        self.reptiles = reptiles
        self.zookeepers = zookeepers
        self.vets = vets
        Zoo.zoos.append(self)

    def add_animals(self):
        class_animal = int(input("Введите класс животного, добавляемого в зоопарк (выберите номер):\n"
                             "1 - птицы\n"
                             "2 - млекопитающие\n"
                             "3 - рептилии\n"))
        name = input("Введите наименование животного: ").lower()
        age = input("Введите возраст животного: ")
        if class_animal == 1:
            type = input("Введите разновидность птицы: ").lower()
            bird = Bird(name, age, type)
            self.birds = Bird.birds
            print(f"Птица - {bird.name}, возраст - {bird.age}, вид - {bird.type} ДОБАВЛЕНА в зоопарк")
        if class_animal == 2:
            type_of_eating = input("Введите тип млекопитающего(х - хищник/т - травоядный): ").lower()
            mam = Mammal(name, age, type_of_eating)
            self.mammals = Mammal.mammals
            print(f"Млекопитающее - {mam.name}, возраст - {mam.age}, тип - {mam.type_of_eating} ДОБАВЛЕНО в зоопарк")
        if class_animal == 3:
            new_skin = input("Введите сбросил ли недавно кожу (нк - новая кожа/ск - старая кожа): ").lower()
            rep = Reptile(name, age, new_skin)
            self.reptiles = Reptile.reptiles
            print(f"Рептилия - {rep.name}, возраст - {rep.age}, тип - {rep.new_skin} ДОБАВЛЕНА в зоопарк")

    def add_staff(self):
        class_staff = int(input("Введите должность, добавляемого в зоопарк сотрудника (выберите номер):\n"
                             "1 - ветеринар\n"
                             "2 - смотритель\n"))
        name = input("Введите имя сотрудника: ").title()
        spec = input("Введите специализацию (п - птицы/ м - млекопитающие/р - рептилии/у - универсал): ").lower()
        if class_staff == 1:
            vet = Vet(name, spec)
            self.vets = Vet.vets
            print(f"Ветеринар - {vet.name}, специализация -  {vet.spec} ВЗЯТ на работу в зоопарк")
        if class_staff == 2:
            zk = ZooKeeper(name, spec)
            self.zookeepers = ZooKeeper.zookeepers
            print(f"Смотритель - {zk.name}, специализация -  {zk.spec} ВЗЯТ на работу в зоопарк")

    def output_staff_zoo(self):
        for i, man in enumerate(self.vets):
            print(f'Ветеринар {i}: {man.name} Специализация: {man.spec}')
        for i, man in enumerate(self.zookeepers):
            print(f'Служащий {i}: {man.name} Специализация: {man.spec}')

    def output_animals_zoo(self):
        print('Птицы:')
        for i, item in enumerate(self.birds):
            print(f'{i}: {item.name} Возраст: {item.age} Вид: {item.type}')
        print('Млекопитающие:')
        for i, item in enumerate(self.mammals):
            print(f'{i}: {item.name} Возраст: {item.age} Тип: {item.type_of_eating}')
        print('Рептилии:')
        for i, item in enumerate(self.reptiles):
            print(f'{i}: {item.name} Возраст: {item.age} Тип: {item.new_skin}')

    def update_classes(self):
        Bird.birds = self.birds
        Mammal.mammals = self.mammals
        Reptile.reptiles = self.reptiles
        ZooKeeper.zookeepers = self.zookeepers
        Vet.vets = self.vets


def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()

def menu():
    act = input("Выберите действие:\n"
            "1. Узнать что говорят животные\n"
            "2. Добавить сотрудника\n"
            "3. Добавить животное\n"
            "4. Сохранить данные зоопарка\n"
            "5. Открыть данные зоопарка\n"
            "0 - Завершение работы\n")
    return act

print("Приветствуем в менеджере зоопарка!\n")
zoo_name = input("Введите название зоопарка: ")
b = Bird("тетерев", 2, "курообразные")
r = Reptile("черепаха",100,"нк")
m = Mammal("волк",5,"х")
z = ZooKeeper("Ростовцев","у")
v = Vet("Иванов","у")
v.heat_animal(b.name)
z.feed_animal(r.name)
zoo = Zoo(zoo_name, Bird.birds, Mammal.mammals, Reptile.reptiles,ZooKeeper.zookeepers,Vet.vets)
act = 10
animals = []
while act != 0:
    act = int(menu())
    if act == 1:
        animals.extend(Bird.birds)
        animals.extend(Mammal.mammals)
        animals.extend(Reptile.reptiles)
        animal_sounds(animals)
        animals = []
    if act == 2:
        while True:
            zoo.add_staff()
            choice = input("Вы хотите добавить еще сотрудника? (да/нет):  ").lower()
            if choice != "да":
                zoo.output_staff_zoo()
                break
    if act == 3:
        while True:
            zoo.add_animals()
            choice = input("Вы хотите добавить еще животное? (да/нет):  ").lower()
            if choice != "да":
                zoo.output_animals_zoo()
                break
    if act == 4:
        with open('zoos.pkl','wb') as file:
            pickle.dump(Zoo.zoos,file)
    if act == 5:
        with open('zoos.pkl','rb') as file:
            Zoo.zoos = pickle.load(file)
        zoo.output_staff_zoo()
        zoo.output_animals_zoo()
        zoo.update_classes()
        animals.extend(Bird.birds)
        animals.extend(Mammal.mammals)
        animals.extend(Reptile.reptiles)
        for animal in animals:
            print(animal.name,animal.age)
        animals = []









