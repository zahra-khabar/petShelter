class Animal:
    """...Base Class For Animals in PetShelter..."""
    
    def __init__(self, name, age, gender, breed, adopted=False):
        self._validate_name(name)
        self._validate_age(age)

        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.adopted = adopted
        
        
    #Validation Methods
    
    @staticmethod
    def _validate_name(name):
        #check name not null & name is str
       if not isinstance(name, str) or not name.strip():
            raise ValueError("Animal Name must be Not Null...")
        
    
    @staticmethod
    def _validate_age(age):
         if not isinstance(age, int) or age < 0:
            raise ValueError ("Age must be positive Number...")
        
    @property
    def status(self):
      return "Adopted" if self.adopted else "In Shelter"
        
    #---------------------------------
    
    def make_sound(self): 
        #this method will be override in subclasses
        return " "
    
    
    def show_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "breed": self.breed,
            "status": self.status,
            "sound": self.make_sound(),
        }
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "breed": self.breed,
            "adopted": self.adopted,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            breed=data["breed"],
            adopted=data.get("adopted", False),
        )

    def __repr__(self):
        return f"Animal(name={self.name})"

    # -----------------Inheritance----------------
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Jik! Jik!"


class Dinosaur(Animal):
    def make_sound(self):
        return "Ouch!"
    
        