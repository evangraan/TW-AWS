import sys
import logging
import json
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    conn = connect()

    uID = event['body-json']['uID']
    SystemID = event['body-json']['SystemID']
    PlanetID = event['body-json']['PlanetID']
    PlanetData = event['body-json']['PlanetData'] 

    findSQL = 'SELECT "uID" FROM "PlayerPlanets" WHERE "PlanetID" = ' + "'" + PlanetID + "';"
    
    findcur = execute(conn, findSQL)

    sql=""
    
    if(findcur.rowcount==0):
        sql = 'INSERT INTO "PlayerPlanets" ("uID","SystemID","PlanetID","PlanetData") VALUES (' + \
        "'" + uID + "'," + \
        "'" + SystemID + "'," + \
        "'" + PlanetID + "'," + \
        "'" + PlanetData + "');"  
    else:
        sql = 'UPDATE "PlayerPlanets" SET "PlanetData"'
        sql+= " = '" + PlanetData + "'"
        sql+= ' WHERE "PlanetID" = ' + "'" + PlanetID + "';"

    #sql = 'INSERT INTO "PlayerPlanets" ("uID","SystemID","PlanetID","PlanetData") VALUES (' + \
    #"'" + uID + "'," + \
    #"'" + SystemID + "'," + \
    #"'" + PlanetID + "'," + \
    #"'" + PlanetData + "')"  + \
    #' ON CONFLICT ("PlanetID") DO UPDATE SET "PlanetData"' + \
    #" = '" + PlanetData + "';"

    execute(conn, sql)

    finish(conn)

    logger.info("Saved Planet Reached End Gold")

    return "OK"
