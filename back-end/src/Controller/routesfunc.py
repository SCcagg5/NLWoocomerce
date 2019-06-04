from Model.basic import check
from Object.call_api import nlbase


def connect(cn, nextc):
    err = check.contain(cn.pr, ["consumer_key", "consumer_secret", "url"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = nlbase(cn.pr["consumer_key"], cn.pr["consumer_secret"], cn.pr["url"])
    err = use.connect()
    cn.private["use"] = use
    
    return cn.call_next(nextc, err)

def input(cn, nextc):
    err = check.contain(cn.private, ["use"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = cn.private["use"]
    err = use.inputnl()

    return cn.call_next(nextc, err)
