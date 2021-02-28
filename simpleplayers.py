"""Some simple players for battle of the sexes. These simple players can all be male or female."""
import random
from player import Player

class RandomPlayer(Player):
    """Random player plays randomly"""
    def __init__(self, name, sex):
        super(RandomPlayer, self).__init__(name, sex)

    def get_action(self, history):
        return random.choice(['MS', 'WS'])

class NashPlayer(Player):
    """Nash player also plays randomly, but at the nash equilibrium raio of 2/3 preferred action."""
    def __init__(self, name, sex):
        super(NashPlayer, self).__init__(name, sex)

    def get_action(self, history):
        if self.sex == 'male':
            if random.random() < 2.0/3:
                return 'MS'
            return 'WS'
        if random.random() < 2.0/3:
            return 'WS'
        return 'MS'

class DominantPlayer(Player):
    """Dominant player always plays his or her preferred action"""
    def __init__(self, name, sex):
        super(DominantPlayer, self).__init__(name, sex)

    def get_action(self, history):
        if self.sex == 'male':
            return 'MS'
        return 'WS'

class SubmissivePlayer(Player):
    """Submissive player performs the other player's preferred action."""
    def __init__(self, name, sex):
        super(SubmissivePlayer, self).__init__(name, sex)

    def get_action(self, history):
        if self.sex == 'male':
            return 'WS'
        return 'MS'

class CoopPlayer(Player):
    """Coop(erative) player will play randomly on the first round and on all rounds where on the previous
        round the players playes opposite actions. If on the preious round both players played the same action,
        coop will play the same action as the previous round in attempt to "cooperate"."""
    def __init__(self, name, sex):
        super(CoopPlayer, self).__init__(name, sex)

    def get_action(self, history):
        if not history:
            return random.choice(['MS', 'WS'])
        prev = history[-1]
        if prev[0] == prev[1]:
            return prev[0]
        return random.choice(['MS', 'WS'])

class TitForTatPlayer(Player):
    """TitForTat player will play randomly on the first round and on all rounds where on the previous
        round the players playes opposite actions. If on the preious round both players played the same action,
        TitForTat will play the same opposiute as the previous round in attempt to "be fair"."""
    def __init__(self, name, sex):
        super(TitForTatPlayer, self).__init__(name, sex)

    def get_action(self, history):
        if not history:
            return random.choice(['MS', 'WS'])
        prev = history[-1]
        if prev[0] == prev[1]:
            if prev[0] == 'MS':
                return 'WS'
            return 'MS'
        return random.choice(['MS', 'WS'])

class AltPlayer(Player):
    """AltPlayer plays the first round randomly, then in each successive round plays the opposite
       of what it played the previous round."""
    def __init__(self, name, sex):
        super(AltPlayer, self).__init__(name, sex)

    def get_action(self, history):
        if not history:
            return random.choice(['MS', 'WS'])
        prev = history[-1]
        if self.sex == 'male':
            index = 0
        else:
            index = 1
        if prev[index] == 'MS':
            return 'WS'
        return 'MS'

class ContraryPlayer(Player):
    """ContraryPlayer plays the first round randomly, then in each successive round plays the opposite
       of what the other player played the previous round."""
    def __init__(self, name, sex):
        super(ContraryPlayer, self).__init__(name, sex)

    def get_action(self, history):
        if not history:
            return random.choice(['MS', 'WS'])
        prev = history[-1]
        if self.sex == 'male':
            index = 1
        else:
            index = 0
        if prev[index] == 'MS':
            return 'WS'
        return 'MS'

class PigheadPlayer(Player):
    """Pighead player plays randomly the first round, then keeps playing the same thing."""
    def __init__(self, name, sex):
        super(PigheadPlayer, self).__init__(name, sex)

    def get_action(self, history):
        if not history:
            return random.choice(['MS', 'WS'])
        prev = history[-1]
        if self.sex == 'male':
            return prev[0]
        return prev[1]

name_dict = {
              "random":  RandomPlayer,
              "nash": NashPlayer,
              "dom": DominantPlayer,
              "sub": SubmissivePlayer,
              "coop": CoopPlayer,
              "titfortat": TitForTatPlayer,
              "alt": AltPlayer,
              "contrary": ContraryPlayer,
              "pighead": PigheadPlayer,
            }


def create_simple_player(name, sex):
    """Create one of these simpleplayers and return it."""
    if name in name_dict:
         player = name_dict[name](name, sex)
         return player
    # find  best match
    best_chars = 0
    best = None
    for key in name_dict.keys():
        matched = 0
        for ii, char in enumerate(key):
            if ii < len(name) and char == name[ii]:
                matched += 1
                if matched > best_chars:
                     best_chars = matched
                     best = name_dict[key]
            else:
                break

    player = best(name, sex)
    return player

if __name__ == '__main__':
    import sys
    name = sys.argv[1]
    player = create_simple_player(name, 'male')
    print(repr(player))
