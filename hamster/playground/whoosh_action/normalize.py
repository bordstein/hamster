import json

def get_movie_repr():
    with open("movie_repr.json", "r") as f:
        mv = json.loads(f.read())
        mv_repr = u""
        for val in mv.itervalues():
            if isinstance(val, list):
                for sub in val:
                    if isinstance(sub, dict):
                        print 'dict!'
                        for subsub in sub.itervalues():
                            try:
                                mv_repr += unicode(" " + str(subsub))
                            except:
                                pass
                    else:
                        try:
                            mv_repr += unicode(" " + str(sub))
                        except:
                            pass
            else:
                try:
                    mv_repr += unicode(" " + str(val))
                except:
                    pass
    return mv_repr
