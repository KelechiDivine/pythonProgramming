class Knight(object):
    def __init__(self, life, speed,
                 attack_power, attack_range,
                 weapon):
        
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon
        
    def __str__(self):
        return "Life: {0}\n"\
                "Speed: {1}\n"\
                "Attack Power: {2}\n"\
                "Attack Range: {3}\n"\
                "Weapon: {4}".format(
           
            self.life,
            self.speed,
            self.attack_power,
            self.attack_range,
        )