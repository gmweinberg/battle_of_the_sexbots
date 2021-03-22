class Player(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex # 'male' or 'female'
        self.score = 0

    def get_action(self, history):
        """Based on history, return an action ('MS' or'WS')"""
        raise Exception('not implemented')

    def pre_match(self):
        """Do whatver must be done before each match."""
        self.score = 0

    def mutate(self):
        """Randomly adjust internal paramaters"""
        pass
