import data
import random


#  may need to fix name output for non-binary

class Character:
    #  Base Character Traits
    race = ''
    subrace = ''
    name = ''
    age = 4
    height = 5
    weight = 8
    size = ''
    features = []
    languages = []

    #  Additional Character Traits
    distinct_ft = ''
    hi_ability = ''
    lo_ability = ''
    talent = ''
    mannerism = ''
    interaction_style = ''
    ideal = ''
    bond = ''
    flaw = ''

    def __str__(self):
        pass


#  Create new character -- heavy lifting

def create_new_char():
    new_character = Character()

    #  Our name and age depends on race, so we're going to decide that first.
    races = []
    for race in data.races:
        races.append(race)
    new_character.race = random.choice(races)

    #  After race is decided, we can choose a name & age, but we need some user input...

    print(f'We need a little help naming your {new_character.race}')

    done = False
    while not done:
        gender_selection = input('Does your character identify as male, female, or non-binary? ')
        if gender_selection == 'male':
            new_character.name = random.choice(data.races[new_character.race]['names']['male'])
            done = True
        elif gender_selection == 'female':
            new_character.name = random.choice(data.races[new_character.race]['names']['female'])
            done = True
        elif gender_selection == 'non-binary':
            new_character.name = random.choice(data.races[new_character.race]['names'])
            done = True
        else:
            print('Sorry, I didn\'t catch that. Please enter \"male\", \"female\", or \"non-binary\".')

    print('Thanks. Alright, last thing -- I promise.')

    done = False
    while not done:

        ages = []

        age_selection = input('Would you like to make a child or an adult? ')
        if age_selection == 'child':
            for age in data.races[new_character.race]['Child Age']:
                ages.append(age)
            new_character.age = random.choice(ages)
            done = True
        elif age_selection == 'adult':
            for age in data.races[new_character.race]['Adult Age']:
                ages.append(age)
            new_character.age = random.choice(ages)
            done = True
        else:
            print('Sorry, I didn\'t catch that. Please enter either \"child\" or \"adult\".')

    #  These features are unique to each character regardless of race.
    new_character.distinct_ft = random.choice(data.distinct_ft['Clothing'])

    new_character.hi_ability = random.choice(data.hi_ability)

    new_character.lo_ability = random.choice(data.lo_ability)

    new_character.talent = random.choice(data.talent)

    new_character.mannerism = random.choice(data.mannerism)

    new_character.interaction_style = random.choice(data.interaction_style)

    new_character.ideal = random.choice(data.ideal)

    new_character.bond = random.choice(data.bond)

    new_character.flaw = random.choice(data.flaw)

    #  These features are specific to race and DO need randomly selected.
    subraces = []
    heights = []
    weights = []

    for subrace in data.races[new_character.race]['Subrace']:
        subraces.append(subrace)
    new_character.subrace = random.choice(subraces)

    for height in data.races[new_character.race]['Height']:
        heights.append(height)
    new_character.height = random.choice(heights)

    for weight in data.races[new_character.race]['Weight']:
        weights.append(weight)
    new_character.weight = random.choice(weights)

    #  These features are specific to the race but DON'T need randomly selected.
    new_character.feature = data.races[new_character.race]['Features']

    new_character.language = data.races[new_character.race]['Languages']

    new_character.size = data.races[new_character.race]['Size']

    #  Time to print out our character!
    print(f'Your new character, {new_character.name} has finished generating.')

    done = False
    while not done:
        desired_format = input('Would you like the character output as a text block or as a list?')

        if desired_format == 'text block':
            pass

        elif desired_format == 'list':
            print('Character Key information')
            print('-------------------------------------')
            print(f'Name: {new_character.name}')
            print(f'Race: {new_character.race}')
            print(f'Subrace: {new_character.subrace}')
            print(f'Age: {new_character.age}')
            print(f'Height: {new_character.height}')
            print(f'Weight: {new_character.weight}')
            print(f'Size: {new_character.size}')
            print(f'Features: {new_character.feature}')
            print(f'Languages: {new_character.language}')

            print('Memorable Unique Information')
            print('-------------------------------------')
            print(f'Distinct Feature: {new_character.distinct_ft}')
            print(f'Highest Ability: {new_character.hi_ability}')
            print(f'Lowest Ability: {new_character.lo_ability}')
            print(f'Talent: {new_character.talent}')
            print(f'Mannerism: {new_character.mannerism}')
            print(f'Interaction Style: {new_character.interaction_style}')
            print(f'Ideal: {new_character.ideal}')
            print(f'Bond: {new_character.bond}')
            print(f'Flaw: {new_character.flaw}')

        else:
            print('Sorry, I didn\'t catch that. Please enter either \"text block\" or \"list\".')


def save_character():
    pass


create_new_char()
