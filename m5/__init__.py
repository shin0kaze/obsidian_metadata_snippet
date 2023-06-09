import ruamel.yaml
from io import StringIO
yaml = ruamel.yaml.YAML()


def r(vpath, npath):
    """read metadata of note (npath - path to note) in vault (vpath - path to vault)"""
    fpath = f'{vpath}/{npath}'
    with open(fpath, encoding='utf-8') as f:
        # Check if file has any metadata
        for i, l in enumerate(f):
            if l == '---\n' and i == 0:
                break
            else:
                return {}
        lst = []
        for l in f:
            if l == '---\n':
                break
            lst.append(l)
            # k, v = l[:-1].split(': ')
            # d[k] = v[1:-1]
    chunk = "".join(lst)
    dct = yaml.load(chunk)
    return dct if dct is not None else {}


def w(vpath, npath, dct):
    orig_dct = r(vpath, npath)
    sio = StringIO()
    yaml.dump(dct, sio)
    new_meta = sio.getvalue()
    sio.close()
    fpath = f'{vpath}/{npath}'
    until_line = line_count(orig_dct)
    with open(fpath, 'r', encoding='utf-8') as fi:
        with open(fpath, 'r+', encoding='utf-8') as fo:
            # not implemented yet
            if not is_meta_exists():
                add_empty_meta()
            # first line is ---
            cur_lineno = 1
            fi.readline()
            seek_pos = fi.tell()
            fo.seek(seek_pos, 0)
            # skip old meta
            while cur_lineno <= until_line:
                cur_lineno += 1
                fi.readline()

            # insert our new meta
            fo.writelines(new_meta)

            # insert rest of the file
            cur_line = fi.readline()
            while cur_line:
                fo.writelines(cur_line)
                cur_line = fi.readline()
            fo.truncate()


def line_count(dct):
    count = 0
    for v in list(dct.values()):

        # check multiline
        ml_count = v.count('\n')
        ml_count = ml_count + 1 if ml_count > 0 else 0

        count += 1 + ml_count
    return count


def is_meta_exists():
    return True


def add_empty_meta():
    pass


if __name__ == '__main__' and True:
    v = r('.', 'test.txt')
    print(v)

    v['c'] = 'bbb'
    v['d'] = 'bbb'
    del v['a']
    w('.', 'test2.txt', v)
    v2 = r('.', 'test2.txt')
    print(v2)
