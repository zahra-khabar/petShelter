class PetShelterErr(Exception):
    """General Pet Shelter Errors"""
    pass

class AnimalNotFoundError(PetShelterErr):
    """Any Found Animals"""
    pass

class DuplicateAnimalError(PetShelterErr):
    """Register any Duplicate Animals err"""
    pass

class AnimalAlreadyAdoptedError(PetShelterErr):
    """This Animal Assigned To Others"""
    pass

class MaximumAdoptionReachedError(PetShelterErr):
    """You Reached to Max adoption """
    pass

class InvalidPhoneNumberError(PetShelterErr):
    """Phone Number is incorrect!"""
    pass

class InvalidNationalIdErr(PetShelterErr):
    """national Id is invalid !"""
    pass