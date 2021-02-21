#!/usr/bin/env python

class Tournament(object):
    def __init__(self, rounds):
        self.males = []
        self.females = []
        self.rounds = rounds # number of times each male interacts with each female
        self.verbosity = 1

    def add_player(self, player):
        player.score = 0
        if player.sex == 'male':
            self.males.append(player)
        else:
            self.females.append(player)

    def resolve(self):
        for male in self.males:
            for female in self.females:
                history = []
                for round in range(self.rounds):
                    male_action = male.get_action(history)
                    female_action = female.get_action(history)
                    score = self.score_actions(male_action, female_action)
                    male.score += score[0]
                    female.score += score[1]
                    history.append((male_action, female_action))
        self.males.sort(key=lambda x: x.score, reverse=True)
        self.females.sort(key=lambda x: x.score, reverse=True)
        if self.verbosity:
            print('male scores')
            for male in self.males:
                print(male.name, male.score)
            print()
            print('female scores')
            for female in self.females:
                print(female.name, female.score)

    def score_actions(self, male_action, female_action):
        if male_action != female_action:
            return (0, 0)
        if male_action == 'MS':
            return (2,1)
        return (1,2)

