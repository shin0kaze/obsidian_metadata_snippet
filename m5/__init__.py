from yaml import safe_load, safe_dump


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
    yaml = safe_load(chunk)
    return yaml if yaml is not None else {}


def w(vpath, npath, d):
    orig_d = r(vpath, npath)
    # merge two dics, d has will overwrite
    # new_d = orig_d | d
    new_meta = safe_dump(d)
    fpath = f'{vpath}/{npath}'
    until_line = len(orig_d)
    with open(fpath, 'r', encoding='utf-8') as fi:
        with open(fpath, 'r+', encoding='utf-8') as fo:
            if not is_meta_exists():
                add_empty_meta()
            # first line is ---
            cur_lineno = 1
            fi.readline()
            seek_pos = fi.tell()
            fo.seek(seek_pos, 0)
            # skip not needed lines
            while cur_lineno <= until_line:
                cur_lineno += 1
                fi.readline()

            # insert our text
            fo.writelines(new_meta)

            # insert rest of the file
            cur_line = fi.readline()
            while cur_line:
                fo.writelines(cur_line)
                cur_line = fi.readline()
            fo.truncate()


def is_meta_exists():
    return True


def add_empty_meta():
    pass


if __name__ == '__main__' and False:
    v = r('.', 'test.txt')
    print(v)

    v['c'] = 'bbb'
    v['d'] = 'bbb'
    del v['a']
    w('.', 'test2.txt', v)
    v2 = r('.', 'test.txt')
    print(v)
