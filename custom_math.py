def clamp(v, min, max):
    if v > max:
        return max
    if v < min:
        return min
    return v