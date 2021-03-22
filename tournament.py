#!/usr/bin/env python
import random
from collections import defaultdict
from copy import copy

class Tournament(object):
    def __init__(self, rounds):
        self.males = []
        self.females = []
        self.dist_history = []
        self.rounds = rounds # number of times each male interacts with each female
        self.verbosity = 1

    def add_player(self, player):
        player.score = 0
        if player.sex == 'male':
            self.males.append(player)
        else:
            self.females.append(player)

    def resolve(self):
        """Determine results for one generation of a tournament"""
        for male in self.males:
            male.pre_match()
        for female in self.females:
            female.pre_match()
        for male in self.males:
            for female in self.females:
                history = []
                if self.verbosity > 1:
                    print('male {} female {}'.format(male.name, female.name))
                for round in range(self.rounds):
                    male_action = male.get_action(history)
                    female_action = female.get_action(history)
                    score = self.score_actions(male_action, female_action)
                    male.score += score[0]
                    female.score += score[1]
                    history.append((male_action, female_action))
                    if self.verbosity > 1:
                        print('male action {} female action {} male score {} female score {}'.format(male_action, female_action, score[0], score[1]))
            if self.verbosity > 1:
                print()
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

    def reproduce(self):
         self.males = self._reproduce_asex(self.males)
         self.females = self._reproduce_asex(self.females)

    def _reproduce_asex(self, players):
        """For a list of players of a sex, determine the number of decendents each player should have."""
        # For now I'll do this the easy way. firts do guarenteed children, then randomly assign leftover children with a
        # probability proportional to leftover sscores. We will not have exactly the same number of children each round,
        # actual number may slightly go up or doew.
        children = []
        players.sort(key = lambda x: x.name)
        total_score = sum(player.score for player in players)
        num_players = len(players)
        repro_score = total_score // num_players
        #print('repro_score', repro_score)
        # first do guarenteed children
        for player in players:
            while player.score > repro_score:
                children.append(copy(player))
                player.score -= repro_score
                if self.verbosity > 1:
                    print(player.name + ' reproduced (guarantee)')
        # now randomly divvy up the leftover children
        if len(children) == num_players: #somehow things worked out exactly
            return children
        total_score = sum(player.score for player in players)
        extra_children = num_players - len(children)
        required = float(total_score) /  extra_children # amount to gurantee a child.
        # print('required', required)
        for player in players:
            chance = player.score / required
            if random.random() < chance:
                children.append(copy(player))
                if self.verbosity > 1:
                    print(player.name + ' reproduced (chance {}'.format(chance))
            else:
                pass
                #print(player.name + 'failed to reproduce (chance {}'.format(chance))
        return children

    def store_dist_hist(self):
        """Store the current player distribution in dist_history"""
        dist = {'males': self.get_sex_distribution('male'),
                'females': self.get_sex_distribution('female')}
        self.dist_history.append(dist)

    def show_distribution(self):
        print('male distribution', self.get_sex_distribution('male'))
        print('female distribution', self.get_sex_distribution('female'))

    def get_sex_distribution(self, sex):
        """get the number of players of each type for a sex"""
        dist = defaultdict(int)
        if sex == 'male':
            players = self.males
        else:
            players = self.females
        for player in players:
            dist[player.name] += 1
        return dist


    def score_actions(self, male_action, female_action):
        if male_action != female_action:
            return (0, 0)
        if male_action == 'MS':
            return (2,1)
        return (1,2)

