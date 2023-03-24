class Martian:
    """Someone who lives on Mars."""
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
      if name == 'full_name':
          return f"{self.first_name} {self.last_name}"
      else:
          raise AttributeError(f"No attribute named {name}.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __lt__(self, other):
        print(f">>> Comparing {self.full_name} & {other.full_name}")
        if self.last_name != other.last_name:
            return (self.last_name < other.last_name)
        else:
            return (self.first_name < other.first_name)


m1 = Martian("Cyrille", "Collin")
m2 = Martian("Len", "Klein")
m3 = Martian("Matthias", "Stein")
m4 = Martian("Mike", "Lenox")
m5 = Martian("Bob", "Hillier")
m6 = Martian("Olwyn", "Meek")
m7 = Martian("Andy", "Taylor")
m8 = Martian("Halbert", "Stone")
m9 = Martian("Marvin", "Meek")

martians = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
martians.sort()
for m in martians:
    print(m)