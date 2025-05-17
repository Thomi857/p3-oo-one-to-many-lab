class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        """Initialize the Pet object with name, pet_type, and optional owner."""
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")

        self.pet_type = pet_type
        self.owner = owner

        # Add this Pet instance to the all list
        Pet.all.append(self)

        if owner:
            owner.add_pet(self)


class Owner:
    def __init__(self, name):
        """Initialize the Owner object with a name."""
        self.name = name
        self._pets = []  # Renamed to avoid conflict with method name

    def pets(self):
        """Return a full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner's collection if it is of type Pet."""
        if not isinstance(pet, Pet):  
            raise Exception("The pet must be an instance of the Pet class.")

        # Set the pet's owner if not already set
        if pet.owner is None:
            pet.owner = self
        self._pets.append(pet)  # Use '_pets' instead of 'pets'

    def get_sorted_pets(self):
        """Return a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)
