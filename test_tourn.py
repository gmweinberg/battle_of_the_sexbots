#!/usr/bin/env python3

from ast import literal_eval
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
    parser.add_argument('--verbosity', type=int, default=1)
    parser.add_argument('--generations', type=int, default=1)
    parser.add_argument('--mult', type=int, default=1, help='multiplier of distribution')
    parser.add_argument('--dist', help='distribution', default=None)
    args = parser.parse_args()
    if args.dist:
        dist = literal_eval(args.dist)
    tourn = Tournament(rounds=args.rounds)
    tourn.verbosity = args.verbosity
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
            for ii in range(dist[sex][name] * args.mult):
                tourn.add_player(class_(sex=sex, name=name))
    for gen in range(args.generations):
        tourn.resolve()
        tourn.reproduce()
        print()
        tourn.show_distribution()
        print()




