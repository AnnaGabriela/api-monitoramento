from db.settings import database

def getDomes():
    totalDomes = database.llen("cupulas")
    domes = database.lrange("cupulas", 0, totalDomes)
    return { totalDomes, domes }

def getAttributes(cupula):
    attributes = database.hgetall('{}'.format(cupula))
    return attributes