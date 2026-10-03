from animals import Animal
from people import Adopter
from exceptions import (  AnimalNotFoundError, DuplicateAnimalError, AnimalAlreadyAdoptedError,)

class Shelter:
    """Manages animals and adopters in This Class.."""
    
    def __init__(self, name="Shelter"):
        self.name = name
        self.animals = []
        self.adopters = []
    
    def add_animal(self, animal: Animal):
        for animall in self.animals:
            if (
                animall.name == animal.name
                and animall.breed == animal.breed
                and type(animall) is type(animal)
            ):
                raise DuplicateAnimalError(
                    f"An animal named {animal.name} with breed {animal.breed} is already exists."
                )
        self.animals.append(animal)
        return animal
    
    
    def find_animal_by_name(self, animal_name):
        for aa in self.animals:
            if aa.name == animal_name:
                return aa
        raise AnimalNotFoundError(f"No animal found with name {animal_name}")
    
    
    
    def remove_animal(self, animal_name):
        animal = self.find_animal_by_name(animal_name)
        if animal.adopted:
            raise AnimalAlreadyAdoptedError(
                f"You Can not remove {animal.name}. it is adopted before."
            )
        self.animals.remove(animal)
        return animal
    
    def search_animals(self, value):
        """Search by name or breed."""
        value = value.strip().lower()
        results = []
        for aa in self.animals:
            if value in aa.name.lower() or value in aa.breed.lower():
                results.append(aa)
        return results

    
    def list_animals(self):
        return list(self.animals)

    def list_available(self):
        return [animal for animal in self.animals if not animal.adopted]

    def list_adopted(self):
        return [animal for animal in self.animals if animal.adopted]
   
   #main logic
    def adopt_animal(self, animal_name, adopter: Adopter):
        animal = self.find_animal_by_name(animal_name)
        if animal.adopted:
            raise AnimalAlreadyAdoptedError(
                f"Animal: {animal.name} has been adopted."
            )
        adopter.add_adopted_animal(animal.name)

        animal.adopted = True
        if adopter not in self.adopters:
            self.adopters.append(adopter)
        return animal

    def return_animal(self, animal_name):
        animal = self.find_animal_by_name(animal_name)
        if not animal.adopted:
            raise AnimalAlreadyAdoptedError(
                f"Animal {animal.name} is still in the shelter and can not be returned."
            )
        animal.adopted = False
        for adopter in self.adopters:
          adopter.remove_adopted_animal(animal.name)
        return animal
    
    def find_or_create_adopter(self, name, phone, national_id):
      for person in self.adopters:
        if person.national_id == national_id:
            return person
      return Adopter(name=name, phone=phone, national_id=national_id)

   #---------------------------------
    def print_animal(self, animal):
        info = animal.show_info()
        print(
            f"  {info['name']} | "
            f"Age: {info['age']} | Gender: {info['gender']} | Breed: {info['breed']} | "
            f"Status: {info['status']} | Sound: {info['sound']}"
        )

    def print_animals(self, animals):
        if not animals:
            print("  (empty list)")
            return
        for aa in animals:
            self.print_animal(aa)

    def show_all(self):
        print("\n--- All Animals ---")
        self.print_animals(self.list_animals())

    def show_available(self):
        print("\n--- Animals in Shelter ---")
        self.print_animals(self.list_available())

    def show_adopted(self):
        print("\n--- Adopted Animals ---")
        self.print_animals(self.list_adopted())

    def show_search_results(self, value):
        results = self.search_animals(value)
        print(f"\n--- Search results for {value} ---")
        self.print_animals(results)

