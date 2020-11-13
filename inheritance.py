class SpaceObject:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

class Planet(SpaceObject):
    def __init__(self, name,  population=None):
        super().__init__(name)
        self.population = population or []
       

    def __repr__(self):
        if len(self.population) != 0:
            names = ''
            for i in self.population:
                names += str(i) + ', '
            names = names[:-2]
            return f'The planet {self.name} is populated by {names}.'
        else:
            return f'The planet {self.name} is not populated yet.'

    def get_populated(self, *args):
        for i in args:
            if isinstance(i, Animal):
                self.population.append(i)    


class Animal:
    # n_animals = 0

    def __init__(self, species_name, habitat):
        self.habitat = habitat
        self.species_name = species_name
        # Animal.n_animals += 1

class Birds(Animal):
    def __init__(self, species_name, habitat, wingspan, feathers_colour):
        super().__init__(species_name, habitat)
        self.wingspan = wingspan
        self.feather_colour = feathers_colour

    def __repr__(self):
        return f'{self.species_name}'

    def info_about_this_bird(self):
        return f'{self.species_name} is a bird. '\
                f'It lives in the {self.habitat}. The colour of its feathers is {self.feather_colour} '\
                f'and its wingspan is {self.wingspan} meters.'

class Mammals(Animal):
    def __init__(self, species_name, habitat, duration_pregnancy, hair_colour):
        super().__init__(species_name, habitat)
        self.duration_pregnancy = duration_pregnancy
        self.hair_colour = hair_colour

    def __repr__(self):
        return f'{self.species_name}'
        
    def info_about_this_mammal(self):
        return f'{self.species_name} is a mammal. '\
                f'It lives in the {self.habitat}. '\
                f'The colour of its hair\\fur is {self.hair_colour}. '\
                f'The pregnancy of this species usually lasts {self.duration_pregnancy} days.'
    
class Reptiles(Animal):
    def __init__(self, species_name, habitat, n_heart_chambers, skin_colour):
        super().__init__(species_name, habitat)
        self.n_heart_chambers = n_heart_chambers
        self.skin_colour = skin_colour

    def __repr__(self):
        return f'{self.species_name}'
    
    def info_about_this_reptile(self):
        return f'{self.species_name} is a reptile. '\
                f'It lives in the {self.habitat}. '\
               f'The colour of its skin is {self.skin_colour}. '\
               f'The number of heart chambers is {self.n_heart_chambers}.'

def main():
                                                                                                                                             
    bird = Birds('chicken', 'farms',  0.5, 'yellow')
    print(bird.info_about_this_bird())
    
    mammal = Mammals('bear', 'forest', 245, 'brown')
    print(mammal.info_about_this_mammal())
    
    reptile = Reptiles('crocodile', 'water', 4, 'green')
    print(isinstance(reptile, Animal))
    print(reptile)
    print(reptile.info_about_this_reptile())
    
    star = SpaceObject('Ringo Star')
    
    earth = Planet('Earth')
    earth.get_populated(bird, mammal, reptile, star)
    print(earth)
    print(isinstance(earth, Planet), isinstance(earth, SpaceObject))

if __name__ == '__main__':
    main()
