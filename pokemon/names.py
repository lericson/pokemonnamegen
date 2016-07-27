import printa
from .brain import model


def sample(**kw):
    return printa.gen_names(model, **kw)
