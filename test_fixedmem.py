#!/usr/bin/env python3
"""Test script to make sure the fixedmem player behave correctly"""
# All the "simpleplayers" can be implemented as depth 0 or 1 fixedmem players
from ast import literal_eval
from fixedmem import FixedMemPlayer, imp_simple_player
from tournament import Tournament

if __name__ == '__main__':
    tourn = Tournament(rounds=8)
    tourn.verbosity = 3
    player = imp_simple_player('male', 'contrary')
    tourn.add_player(player)
    print('name {} hist_params {} action_params {}'.format(player.name, player.hist_params, player.action_params))
    player = imp_simple_player('male', 'alt')
    #tourn.add_player(player)
    player = imp_simple_player('male', 'titfortat')
    #tourn.add_player(player)
    player = imp_simple_player('male', 'coop')
    #tourn.add_player(player)
    player = imp_simple_player('female', 'dom')
    #tourn.add_player(player)
    player = imp_simple_player('female', 'random')
    #tourn.add_player(player)
    player = imp_simple_player('female', 'random')
    tourn.add_player(player)
    player = imp_simple_player('female', 'coop')
    #tourn.add_player(player)
    print('name {} hist_params {} action_params {}'.format(player.name, player.hist_params, player.action_params))
    tourn.resolve()

