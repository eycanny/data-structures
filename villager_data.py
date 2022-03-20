"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    #Cyrano|Anteater|Cranky|Education|Don't punch your nose to spite your face.

    species = set()

    villager_data = open(filename)

    for line in villager_data:
        line = line.rstrip()
        villager_attributes = line.split("|")
        species.add(villager_attributes[1])

    villager_data.close()

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    #Cyrano|Anteater|Cranky|Education|Don't punch your nose to spite your face.

    villagers = []

    villager_data = open(filename)

    for line in villager_data:
        line = line.rstrip()
        villager_attributes = line.split("|")

        species = villager_attributes[1]
        names = villager_attributes[0]

        if search_string.title() == species:
            villagers.append(names)
        elif search_string.title() == "All" or search_string == "":
            villagers.append(names)


    villager_data.close()

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    #Cyrano|Anteater|Cranky|Education|Don't punch your nose to spite your face.
    #Antonio|Anteater|Jock|Fitness|Always go for the burn!

    # #create a list of a list of names
    # all_names_by_hobby = []
    # #create a list of hobbies
    # names_by_hobbies = []

    # villager_data = open(filename)

    # for line in villager_data:
    #     line = line.rstrip()
    #     villager_attributes = line.split("|")

    #     name = villager_attributes[0]
    #     hobby = villager_attributes[3]

    #     if hobby not in hobbies:
    #         names_by_hobbies = [hobby, name]
    #     else:

    # return all_names_by_hobby


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    #Cyrano|Anteater|Cranky|Education|Don't punch your nose to spite your face.
    all_data = []

    villager_data = open(filename)

    for line in villager_data:
        line = line.rstrip()
        villager_attributes = line.split("|")

        villager = tuple(villager_attributes)

        all_data.append(villager)

    villager_data.close()

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    #Cyrano|Anteater|Cranky|Education|Don't punch your nose to spite your face.

    villager_data = open(filename)

    for line in villager_data:
        line = line.rstrip()
        villager_attributes = line.split("|")

        name = villager_attributes[0]
        motto = villager_attributes[4]

        if villager_name.title() == name:
            return motto


    villager_data.close()
    return None
    
def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
