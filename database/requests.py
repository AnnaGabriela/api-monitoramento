from database.settings import db

def getDomes():
    totalDomes = db.llen("cupulas")
    domes = db.lrange("cupulas", 0, totalDomes)
    return {
        "totalDomes": totalDomes,
        "domes": domes
    }

def getAttributes(cupula):
    attributes = db.hgetall('{}'.format(cupula))
    return attributes
