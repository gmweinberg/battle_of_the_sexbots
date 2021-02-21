#!/usr/bin/env python3

from tournament import Tournament
from simpleplayers import (RandomPlayer, DominantPlayer, SubmissivePlayer, CoopPlayer, TitForTatPlayer,
                          AltPlayer, ContraryPlayer)

dist = {"male": { "random":2,
                  "dom": 2,
                  "sub": 2,
                  "coop": 2,
                  "titfortat": 2,
                  "alt": 2, 
                  "contrary": 2
                  }
        }

dist["female"] = dict(dist["male"])
"""Play a test tournament"""
if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--rounds', type=int, default=10)
    args = parser.parse_args()
    tourn = Tournament(rounds=args.rounds)
    for sex in ['male', 'female']:
        for name in dist[sex]:
            if name == "random":
                class_ = RandomPlayer
            elif name == "dom":
                class_ = DominantPlayer
            elif name == "sub":
                class_ = SubmissivePlayer
            elif name == "coop":
                class_ = CoopPlayer
            elif name == "titfortat":
                class_ = TitForTatPlayer
            elif name == "alt":
                class_ = AltPlayer
            elif name == "contrary":
                class_ = ContraryPlayer
            else:
                raise Exception("unsupported player " + name)
            for ii in range(dist[sex][name]):
                tourn.add_player(class_(sex=sex, name=name))

        #player = RandomPlayer(name='random', sex=sex)
        #tourn.add_player(player)
        #player = DominantPlayer(name='dom', sex=sex)
        #tourn.add_player(player)
        #player = SubmissivePlayer(name='sub', sex=sex)
        #tourn.add_player(player)
        #player = CoopPlayer(name='coop', sex=sex)
        #tourn.add_player(player)
        #player = TitForTatPlayer(name='tit', sex=sex)
        #tourn.add_player(player)
    tourn.resolve()




