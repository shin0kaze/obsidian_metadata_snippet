
def read_md(npath = None):
    npath = npath if npath else @note_path
    fpath = f'{@vault_path}/{npath}'
    d = {}
    with open(fpath, encoding="utf-8") as f:
        for l in f: 
            if l == '---\n': break
        for l in f:
            if l == '---\n': break
            k, v = l[:-1].split(': ')
            d[k] = v

ob_dict = read_md()