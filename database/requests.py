from database.settings import db

def getDomes():
    totalDomes = db.llen("cupulas")
    domes = db.lrange("cupulas", 0, totalDomes)
    return {
        "totalDomes": totalDomes,
        "domes": domes
    }

def getAttributes(dome):
    attributes = db.hgetall('{}'.format(dome))
    return attributes

def setDome(dome):
    res = db.lpush("cupulas", dome)
    return "id: {}".format(str(res))

def setAttribute(dome, attribute, value):
    res = db.hset(dome, attribute, value)
    return "id: {}".format(str(res))