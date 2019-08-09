import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    uID = event['body-json']['uID']
    GalaxyID = event['body-json']['GalaxyID']
    PlanetID = event['body-json']['PlanetID']
    Score = event['body-json']['Score']

    sql = 'INSERT INTO "InvasionScores" ' + \
    '("uID","GalaxyID","PlanetID","Score")' + \
    " VALUES (" + \
    "'" + uID + "'," + \
    "'" + GalaxyID + "'," + \
    "'" + PlanetID + "'," + \
    "" +  str(Score) + ")" 
    execute(conn, sql)    
         
    finish(conn)

    return "OK"


