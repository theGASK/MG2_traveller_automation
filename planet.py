import dice

# Tables of modifiers for each UWP value

UWP_max = [
    ('size',          10, True),
    ('atmosphere',    15, True),
    ('temperature',   12, False),
    ('hydrography',   10, True),
    ('population',    12, True),
    ('government',    15, True),
    ('law_level',      9, True),
    ('starport',      12, False),
    ('tech_level',    15, False),
    ('culture',       66, False),
]

valMap = {
    '-': '-',
    0: '0', 
    1: '1', 
    2: '2', 
    3: '3', 
    4: '4', 
    5: '5', 
    6: '6', 
    7: '7', 
    8: '8', 
    9: '9', 
    10: 'A', 
    11: 'B', 
    12: 'C',
    13: 'D',
    14: 'E', 
    15: 'F' 
}



# Planet class generates a new JSON object containing all UWP data

class Planet(object):

    UWP_temp_mod = [0, 0, -2, -2, -1, -1, 0, 0, 1, 1, 1, 6, 6, 1, -1, 1]
    
    UWP_starport_mod = [-2, -2, -2, -1, -1, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2]
    
    UWP_tech_mod = [
        ('size', {
            0:2, 
            1:2, 
            2:1, 
            3:1, 
            4:1
        }),
        ('atmosphere', {
            0:1, 
            1:1, 
            2:1, 
            3:1, 
            10:1, 
            11:1, 
            12:1, 
            13:1, 
            14:1, 
            15:1
        }),
        ('hydrography', {
            0:1, 
            9:1, 
            10:2
        }),
        ('population', {
            1:1, 
            2:1, 
            3:1, 
            4:1, 
            5:1, 
            8:1, 
            9:2, 
            10:4
        }),
        ('government', {
            0:1, 
            5:1, 
            7:2, 
            13:-2, 
            14:-2
        }),
        ('starport', {
            0:-4, 
            1:-4, 
            2:-4, 
            7:2, 
            8:2, 
            9:4, 
            10:4, 
            11:6, 
            12:6, 
            13:6, 
            14:6, 
            15:6
        }),
    ]
    
    def __init__(self, name, *kwargs):
        super().__init__()

        self.name = name

    def _size_standard(self):
        return dice.roll('2d6-2')
    

    def _atmosphere_standard(self):
        if self.size == 0:
            return 0
        else:
            return dice.roll('2d6-7') + self.size


    def _temperature_standard(self):
        return dice.roll('2d6') + self.UWP_temp_mod[self.atmosphere]
    

    def _hydrography_standard(self):

        if self.size <= 1:
            return 0
        
        hydrography = dice.roll('2d6-7') + self.atmosphere

        if self.atmosphere in (0, 1, 10, 11, 12):
            hydrography -= 4

        if self.atmosphere != 13:
            if self.atmosphere in (10, 11):
                hydrography -= 2            
            elif self.temperature >= 12:
                hydrography -= 6

        return hydrography


    def _population_standard(self):
        return dice.roll('2d6-2')

    
    def _government_standard(self):
        
        if self.population == 0:
            return 0    
        else:
            return dice.roll('2d6-7') + self._population

    
    def _culture_standard(self):

        if self.population == 0:
            return 0        
        else:
            return dice.roll('1d6') * (10 + dice.roll('1d6'))
    

    def _law_standard(self):

        if self.population == 0:
            return 0
        else:
            return dice.roll('2d6-7') + self.government

        
    def _starport_standard(self):
        return dice.roll('2d6') + self.UWP_starport_mod[self.population]

    
    def _tech_standard(self):

        if self.population == 0:
            return 0

        tech_level = dice.roll('1d6')

        # UWP_tech_mod is organized as [ 'attribute' { value : modifier } ]

        for attribute, modifier in self.UWP_tech_mod:
            tech_level += modifier.get(getattr(self, attribute), 0)
        return tech_level

    def _culture_standard