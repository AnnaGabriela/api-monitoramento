from database.settings import db

def getTotalDomes():
    domes = db.lrange("cupulas", 0, -1)
    totalDomes = db.llen("cupulas")
    return {
        "totalDomes": totalDomes,
        "domes": domes
    }

def getAttributes(dome):
    attributes = db.hgetall('{}'.format(dome))
    return attributes

def setDome(dome):
    domes = db.lrange("cupulas", 0, -1)
    if dome not in domes:
        id = db.lpush("cupulas", dome)
        return "id: " + str(id)
    else:
        return "Already signed up."

def setAttribute(dome, attribute, value):
    id = db.hset(dome, attribute, value)
    return "id: " + str(id)