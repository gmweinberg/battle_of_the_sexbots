import random
from player import Player

class FixedMemPlayer(Player):
    """FixedMemPlayer has probabilities of actions based on a fixed memory depth e.g. a memory depth 2 player will
       have a probability of MS/WS for each of the 4 possile actions of the previous 2 interactions. A FixedMemPlayer
       with memory depth n must start each match with a bogus "memory" of what happened for the previous n interactions."""
    def __init__(self, name, sex, depth, params=None):
        self.name = name
        self.sex = sex
        self.depth = depth
        self.hist_params = []
        self.action_params = []
        num_params = 2 * depth + 2 ** ( 2 * depth)
        if params:
            if len(params) != num_params:
                raise ValueError('number of parameters should be {}'.format(num_params))
            for param in params:
                if param < 0 or param > 1:
                    raise ValueError("params must all be in interval [0,1]")
            self.hist_params = params[0: 2 * depth]
            self.action_params = params[2 * depth:]
        else:
            for ii in range(2 ** (2 * depth)):
                self.action_params.append(random.random())


    def pre_match(self):
        super(FixedMemPlayer, self).pre_match()
        self.gen_fake_history()

    def gen_fake_history(self):
        """Generate a fake hsitory based on hist_params."""
        self.fake_history  = []
        for ii in range(self.depth):
            fr = []
            for iii in range(2):
                if random.random() < 0.5:
                    fr.append('MS')
                else:
                    fr.append('WS')
            self.fake_history.append(fr)
        


    def get_action(self, history):
        if self.depth:
            if len(history) >= self.depth:
                temp_history = list(history)[-self.depth:]
            else:
                temp_history = list(history)
            ii = 1
            while len(temp_history) < self.depth:
                temp_history.insert(0, self.fake_history[-1 * ii])
        else:
            temp_history = []
        # We use the parameter at position "pos" for determining actions e.g if we had a memory 3
        # bot and the past 3 rounds (real or fake) were (MS, MS), (WS, WS), (MS, WS)
        # the pos is 001101 = 13.
        ii = 0
        pos = 0
        while ii < self.depth:
            then = temp_history[-ii]
            if then[0] == 'WS':
                pos += 2 ** (2 * ii)
            if then[1] == 'WS':
                pos += 2 ** ( 2 * ii + 1)
            ii += 1
        rand = random.random()
        param = self.action_params[pos]
        print('player {} history {} pos {} rand {} param {}'.format(self.name, temp_history, pos, rand, param))
        if random.random() < self.action_params[pos]:
            return 'MS'
        return 'WS'

def imp_simple_player(sex, type_, name=None):
    """Create a fixedmem player that acts like a simpleplayer of the appropriate sex and type.
       Returns theplayer."""
    if not name:
        name = str(sex) + str(type_)
    if type_ == 'dom':
        depth = 0
        if sex == 'male':
            params = [1.0]
        else:
            params = [0.0]
        return FixedMemPlayer(name, sex, depth, params)
    if type_ == "random":
        depth = 0
        params = [0.5]
        return FixedMemPlayer(name, sex, depth, params)
    if type_ == "titfortat":
        depth = 1
        params = [0.5, 0.5, 0, 0.5, 0.5, 1]
        return FixedMemPlayer(name, sex, depth, params)
    if type_ == "coop":
        depth = 1
        params = [0.5, 0.5, 1, 0.5, 0.5, 0]
        return FixedMemPlayer(name, sex, depth, params)
    raise ValueError('unsupported type {}'.format(type_))

