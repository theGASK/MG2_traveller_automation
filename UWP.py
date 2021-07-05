import dice

class POI(object):

    def _size_standard(self):
        return dice.roll(2,6,-2)


    def _atmosphere_standard(self):
        if self.size == 0:
            return 0
        else:
            return dice.roll(2,6,-7) + self.size

    def _temperature_standard(self):
        return dice.roll(2,6,0) + self.UWP_temp_mod[self.atmosphere]


    def _hydrography_standard(self):

        if self.size <= 1:
            return 0
        
        hydrography = dice.roll(2,6,-7) + self.atmosphere

        if self.atmosphere in (0, 1, 10, 11, 12):
            hydrography -= 4

        if self.atmosphere != 13:
            if self.atmosphere in (10, 11):
                hydrography -= 2            
            elif self.temperature >= 12:
                hydrography -= 6

        return hydrography


    def _population_standard(self):
        return dice.roll(2,6,-2)


    def _government_standard(self):
        
        if self.population == 0:
            return 0    
        else:
            return dice.roll(2,6,-7) + self._population


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