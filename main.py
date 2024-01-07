import random

psswd=input("Password Shuffler: ")

def shuffle_any(o):
    is_l=is_t=False
    if isinstance(o, str):
        l = list(o)
    elif isinstance(o, list):
        l = o[:]
        is_l = True
    elif isinstance(o, tuple):
        is_t = True
        l = list(o)
    else:
        raise Exception("o is None!" if o is None \
                else f"Unexpected type: {o.__class__.__name__}")
    random.shuffle(l)
    return l if is_l else tuple(l) if is_t else ''.join(l)

print(f"shuffle_any(psswd): {shuffle_any(psswd)}")