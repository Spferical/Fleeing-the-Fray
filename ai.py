import tcod
import mob
import random
from config import DIAGONAL_MOVEMENT, TORCH_RADIUS
import terrain


class BasicMonster:
    # AI for a basic monster
    target = None
    state = 'resting'

    def update(self):
        # a basic monster takes its turn. If you can see it, it can see you
        if self.target:
            target_dist = self.owner.distance_to(self.target)
        for object in terrain.map.objects:
            if object != self.target:
                if isinstance(object, mob.Mob) and \
                        object.faction != self.owner.faction:
                    dist = self.owner.distance_to(object)
                    if dist < TORCH_RADIUS + 999999999:
                        if not self.target or dist < target_dist:
                            self.target = object
                            self.state = 'chasing'
                            return

        # before chasing, make sure target is not dead
        if self.target:
            if self.target.dead:
                self.target = None
                self.state = 'resting'
            else:
                # move towards target if far away, or fire
                if self.owner.distance_to(self.target) >= 2:
                    if isinstance(self.owner, mob.RangedMob) and random.randint(0, 1) == 0:
                        self.owner.fire_towards(self.target.x, self.target.y)
                    else:
                        self.owner.move_towards(self.target.x, self.target.y)

                # close enough, attack!
                else:
                    self.owner.attack(self.target)


class ConfusedMob:
    confused_turns = 10
    state = 'confused'

    def __init__(self, old_ai):
        self.old_ai = old_ai
        self.owner = self.old_ai.owner

    def update(self):
        if DIAGONAL_MOVEMENT:
            (dx, dy) = (random.randint(-1, 1), random.randint(-1, 1))
        else:
            if random.randint(0, 1):
                (dx, dy) = (random.randint(-1, 1), 0)
            else:
                (dx, dy) = (0, random.randint(-1, 1))
        self.owner.move_or_attack(dx, dy)
        self.confused_turns -= 1
        if self.confused_turns <= 0:
            self.owner.ai = self.old_ai
