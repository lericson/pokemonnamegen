# coding: utf-8

from __future__ import print_function, unicode_literals

pokemanz = [
    'Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon',
    'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod',
    'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto',
    'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok',
    'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran♀', 'Nidorina',
    'Nidoqueen', 'Nidoran♂', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable',
    'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat',
    'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat',
    'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck',
    'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag',
    'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop',
    'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel',
    'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta',
    'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', "Farfetch'd",
    'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder',
    'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno',
    'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor',
    'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing',
    'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan',
    'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime',
    'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp',
    'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon',
    'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl',
    'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair',
    'Dragonite', 'Mewtwo', 'Mew', 'Chikorita', 'Bayleef', 'Meganium',
    'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw',
    'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba',
    'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu',
    'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep',
    'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo',
    'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern',
    'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow',
    'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco',
    'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull',
    'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa',
    'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola',
    'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour',
    'Houndoom', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler',
    'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby',
    'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar',
    'Tyranitar', 'Lugia', 'Ho-Oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile',
    'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert',
    'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon',
    'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot',
    'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper',
    'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish',
    'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask',
    'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama',
    'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron',
    'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric',
    'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot',
    'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt',
    'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon',
    'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper',
    'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt',
    'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas',
    'Milotic', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'Duskull',
    'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie',
    'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss',
    'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum',
    'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias',
    'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys', 'Turtwig',
    'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup',
    'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof',
    'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew',
    'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy',
    'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel',
    'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom',
    'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow',
    'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor',
    'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb',
    'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario',
    'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak',
    'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow',
    'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth',
    'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon',
    'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir',
    'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia',
    'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy',
    'Darkrai', 'Shaymin', 'Arceus', 'Victini', 'Snivy', 'Servine',
    'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott',
    'Samurott', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland',
    'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear', 'Simisear',
    'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill',
    'Unfezant', 'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith',
    'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino', 'Timburr',
    'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh',
    'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede',
    'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Basculin',
    'Sandile', 'Krokorok', 'Krookodile', 'Darumaka', 'Darmanitan', 'Maractus',
    'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask',
    'Cofagrigus', 'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish',
    'Garbodor', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Gothita',
    'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett',
    'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling', 'Sawsbuck',
    'Emolga', 'Karrablast', 'Escavalier', 'Foongus', 'Amoonguss', 'Frillish',
    'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed',
    'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik',
    'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure',
    'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal',
    'Shelmet', 'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon',
    'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet',
    'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino',
    'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion',
    'Virizion', 'Tornadus', 'Thundurus', 'Reshiram', 'Zekrom', 'Landorus',
    'Kyurem', 'Keldeo', 'Meloetta', 'Genesect', 'Chespin', 'Quilladin',
    'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie', 'Frogadier',
    'Greninja', 'Bunnelby', 'Diggersby', 'Fletchling', 'Fletchinder',
    'Talonflame', 'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo', 'Pyroar',
    'Flabébé', 'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Pangoro', 'Furfrou',
    'Espurr', 'Meowstic', 'Honedge', 'Doublade', 'Aegislash', 'Spritzee',
    'Aromatisse', 'Swirlix', 'Slurpuff', 'Inkay', 'Malamar', 'Binacle',
    'Barbaracle', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer',
    'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus',
    'Sylveon', 'Hawlucha', 'Dedenne', 'Carbink', 'Sliggoo', 'Goodra',
    'Klefki', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Gourgeist', 'Bergmite',
    'Avalugg', 'Noibat', 'Noivern', 'Xerneas', 'Yveltal', 'Zygarde',
    'Diancie', 'Hoopa', 'Volcanion', 'Rowlet', 'Litten', 'Popplio', 'Pikipek',
    'Yungoos', 'Grubbin', 'Charjabug', 'Vikavolt', 'Drampa', 'Bruxish',
    'Cutiefly', 'Togedemaru', 'Rockruff', 'Komala', 'Salandit', 'Mimikkyu',
    'Bewear', 'Tapu Koko', 'Solgaleo', 'Lunala', 'Magearna'
]

pokemanz_lower = {n.lower() for n in pokemanz}

pokemanz = list(map('^{}$'.format, pokemanz))


import sys
import numpy as np
from os import environ
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, Embedding
from keras.preprocessing.text import Tokenizer
from keras.utils import np_utils


x, y = [], []
tok = Tokenizer(char_level=True)
tok.fit_on_texts(pokemanz)

"""
# detta är för att göra något i likhet med word2vec men på bokstavsnivå
#
#for seq in tok.texts_to_sequences(pokemanz):
#    print(seq)
#    (couples, labels) = skipgrams(seq, vocsize)
#    x.extend(couples)
#    y.extend(labels)
#    print(couples, labels)
"""

cw = {v: k for k, v in tok.word_index.items()}
for seq in tok.texts_to_sequences(pokemanz):
    x.extend(seq[:-1])
    y.extend(seq[1:])

x = np.array(x, dtype=np.uint)
y = np.array(y, dtype=np.uint)

word_index = {k: v for k, v in tok.word_index.items()}
char_index = {v: k for k, v in tok.word_index.items()}
vocsize = len(word_index)

assert np.count_nonzero(y == word_index['$']) == len(pokemanz)
assert (char_index[x[1]], char_index[y[1]]) == tuple('Bu')
assert len(x) == len(y)

batch_size, num_batches = 10000, 5000
batches_per_it = 50
sizes = 256, 128
seq_length = int(environ.get('SEQ_LENGTH', '20'))

# Pad with zeroes
x = np.array([([0]*seq_length + list(x[max(0, i-seq_length):i]))[-seq_length:]
             for i in range(1, len(x) + 1)])
y = np_utils.to_categorical(y - 1, vocsize)


def main(args=sys.argv[1:]):
    model = Sequential()
    model.add(Embedding(vocsize + 1, sizes[0], mask_zero=True,
                        input_length=seq_length))
    for size in sizes[:-1]:
        model.add(LSTM(128, return_sequences=True))
    model.add(LSTM(sizes[-1]))
    model.add(Dense(vocsize))
    model.add(Activation('softmax'))

    print('x.shape:', x.shape)
    print('y.shape:', y.shape)

    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop')

    with open('topology.json', 'w') as f:
        f.write(model.to_json())

    for iteration in range(1, num_batches//batches_per_it):
        print()
        print('-' * 50)
        print('Iteration', iteration)

        model.fit(x, y, batch_size=batch_size,
                  nb_epoch=batches_per_it, verbose=True)
        model.save_weights('brain-{}.h5'.format(iteration))


if __name__ == "__main__":
    main()
