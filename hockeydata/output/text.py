def dumps(plays):
    return plays.to_string()

def dump(plays, fobj):
    fobj.write(dumps(plays))