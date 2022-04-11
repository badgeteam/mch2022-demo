import random, math

def randomLetter():
    angle  = random.random() * math.pi
    offset = random.random() * math.pi
    start  = random.random() * 0.7
    end    = random.random() * 0.3 + start
    scale  = random.random() * 30 + 20
    return "\ttd_flying_letter({a}, {o}, {s}, {e}, {z});\n".format(a=angle, o=offset, s=start, e=end, z=scale)
