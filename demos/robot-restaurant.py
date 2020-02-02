from bento import Beef, Mackerel, Sushi, Water
from kabukicho import neon


class RobotRestaurant:
    # Come for the robots, stay for the neon
    def make_robots(self):
        self.robots = []

    def make_robots_glow(self, neon):
        self.robots.append(neon.everything)
    
    def add_expensive_bento(self):
        self.beef_bento = Beef()
        self.fish_bento = Mackerel()
        self.robot_sushi = Sushi()
        self.mineral_water = Water()