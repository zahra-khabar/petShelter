from animals import Dog, Cat, Bird, Dinosaur
from people import Adopter
from fileactions import load_shelter, save_shelter


ANIMAL_CLASSES = {
    "dog": Dog,
    "cat": Cat,
    "bird": Bird,
    "dinosaur": Dinosaur,
}


def read_animal_input():
    animal_type = input("Animal type (dog/cat/bird/dinosaur): ").strip().lower()
    cls = ANIMAL_CLASSES.get(animal_type)
    if cls is None:
        print("Invalid animal type.")
        return None

    name = input("Name: ").strip()
    age = int(input("Age: ").strip())
    gender = input("Gender (male/female): ").strip().lower()
    breed = input("Breed: ").strip()
    return cls(name=name, age=age, gender=gender, breed=breed)


def read_adopter_input():
    name = input("Adopter name: ").strip()
    phone = input("Phone number: ").strip()
    national_id = input("National ID: ").strip()
    Adopter.validate_phone(phone)
    Adopter.validate_national_id(national_id)
    return name, phone, national_id


def main():
    shelter = load_shelter()

    while True:
        print("===== Pet Shelter program=====")
        print("1. Add Animal")
        print("2. Remove Animal")
        print("3. Show Animals")
        print("4. Search Animal")
        print("5. Adopt Animal")
        print("6. Return Animal")
        print("7. Show Available Animals")
        print("8. Show Adopted Animals")
        print("9. Exit")

        choice = input("Choice: ").strip()

        try:
            match choice:
                case "1":
                    animal = read_animal_input()
                    if animal is not None:
                        shelter.add_animal(animal)
                        print(f"Animal {animal.name} added.")

                case "2":
                    animal_name = input("Animal name: ").strip()
                    animal = shelter.remove_animal(animal_name)
                    print(f"Animal {animal.name} removed.")

                case "3":
                    shelter.show_all()

                case "4":
                    keyword = input("Search keyword (name/breed): ").strip()
                    shelter.show_search_results(keyword)

                case "5":
                    animal_name = input("Animal name: ").strip()
                    name, phone, national_id = read_adopter_input()
                    adopter = shelter.find_or_create_adopter(name, phone, national_id)
                    animal = shelter.adopt_animal(animal_name, adopter)
                    print(f"Animal {animal.name} adopted by {adopter.name}.")

                case "6":
                    animal_name = input("Animal name: ").strip()
                    animal = shelter.return_animal(animal_name)
                    print(f"Animal {animal.name} returned to the shelter.")

                case "7":
                    shelter.show_available()

                case "8":
                    shelter.show_adopted()

                case "9":
                    save_shelter(shelter)
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid choice.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

