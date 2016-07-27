# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import sys
import numpy as np
from keras.models import model_from_json

from train import pokemanz_lower, word_index, char_index, seq_length


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def main(args=sys.argv[1:]):
    model_fn, names = args[0], args[1:]
    model = load_lstm(model_fn)
    if names:
        for name in names:
            print_names(model, name)
    else:
        name = True
        while name:
            name = raw_input('Name: ')
            print_names(model, name, diversities=[1.0])


def load_lstm(fn):
    model = model_from_json(open('topology.json').read())
    model.load_weights(fn)
    return model


def gen_names(model, n=100, max_iter=1000, root='', diversity=1.0):
    names = set()
    root = '^' + root

    for i in range(max_iter):
        name, next_char = root[:-1], root[-1:]
        xp = ([0]*seq_length + map(word_index.get, name))[-seq_length:]

        while next_char != '$':
            name += next_char
            xp[:-1] = xp[1:]
            xp[-1] = word_index[next_char]
            preds = model.predict(np.array([xp]), verbose=0)[0]
            if next_char == '^':
                preds[word_index['$']] = 0
            next_char = char_index[1 + sample(preds, diversity)]

        if name[1:].lower().strip() not in pokemanz_lower:
            names.add(name[1:])
            if len(names) >= n:
                break

    return names


def print_names(model, root='^', diversities=[0.2, 0.5, 1.0, 1.2]):
    for diversity in diversities:
        if len(diversities) > 1:
            print()
            print('----- diversity:', diversity)
        print(', '.join(gen_names(model, root=root, diversity=diversity)))


if __name__ == "__main__":
    main()
