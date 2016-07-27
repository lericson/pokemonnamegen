# Deep Learning Techniques for Naming Pokémons

![pkm](http://vignette2.wikia.nocookie.net/es.pokemon/images/4/46/Pokémon_Gotta_catch_em_all_logo.png/revision/latest?cb=20130917005914)

# Idea & Inspiration

- Generate new Pokémon names using deep learning

- A guy holding a talk said he'd tried, but was unsatisfied

# Model

- Two-layer LSTM with 256 and 128 units
- Learn character transitions, B → u etc.
- Sample from posterior, feed back into network

![supermodel](https://realbuzz4.s3.amazonaws.com/photo_field_photos/600x450/9d412134b16e164ba5386f876758a466537d.jpg)

How to use:

```python
from pokemon.names import sample
sample(n=10)
sample(root='Guido')
```
