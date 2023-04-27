
def r(vpath, npath):
    """read metadata of note (npath - path to note) in vault (vpath - path to vault)"""
    fpath = f'{vpath}/{npath}'
    d = {}
    with open(fpath, encoding='utf-8') as f:
        for l in f: 
            if l == '---\n': break
        for l in f:
            if l == '---\n': break
            k, v = l[:-1].split(': ')
            d[k] = v
    return d
