import re

from exceptions import (InvalidPhoneNumberError, InvalidNationalIdErr, MaximumAdoptionReachedError,)

class Adopter:
    max_adoption_count = 9
    
    PHONE_PATTERN = re.compile(r"^09\d{9}$")
    NATIONAL_ID_PATTERN = re.compile(r"^\d{10}$")
    
    def __init__(self, name, phone, national_id):
        self.name = name
        self.phone = phone
        self.national_id = national_id
        self.adopted_animals = []
    
    
     #Validation Methods 
    @staticmethod
    def validate_phone(phone):
        if not isinstance(phone, str) or not Adopter.PHONE_PATTERN.match(phone):
            raise InvalidPhoneNumberError(
                f"Invalid phone number Format."
            )
        return phone
    
    @staticmethod
    def validate_national_id(national_id):
        if not isinstance(national_id, str) or not Adopter.NATIONAL_ID_PATTERN.match(national_id):
            raise InvalidNationalIdErr(
                f"Invalid national ID: {national_id} (must be exactly 10 digits)"
            )
        return national_id
    
    
    #-----------------------Functions ---------------
    
    def add_adopted_animal(self, animal_name):
       if len(self.adopted_animals) >= self.max_adoption_count:
        raise MaximumAdoptionReachedError(
            f"{self.name} has reached {self.max_adoption_count}, the max adoptions!"
        )
       if animal_name in self.adopted_animals:
        return
       self.adopted_animals.append(animal_name)


    def remove_adopted_animal(self, animal_name):
        if animal_name in self.adopted_animals:
         self.adopted_animals.remove(animal_name)
    
    
    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "national_id": self.national_id,
            "adopted_animals": list(self.adopted_animals),
        }

    def __repr__(self):
        return f"Adopter(name={self.name},  national_id={self.national_id})"