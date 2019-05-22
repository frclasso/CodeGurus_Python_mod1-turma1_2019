
def functionName(level):
    if level < 1:
        raise Exception(level)
    return level

try:
    l = functionName(-1)
    print('level = ', l)
except Exception as e:
    print('Error in level argument:', e)
