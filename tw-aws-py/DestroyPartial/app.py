import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    
    GalaxyID = event['body-json']['GalaxyID']

    sql = 'DELETE From "PlayerSystems" WHERE "uID" = ' 
    sql+= "'" + GalaxyID + "';"

    curr = execute(conn,sql )

    sql = 'DELETE From "PlayerPlanets" WHERE "uID" = ' 
    sql+= "'" + GalaxyID + "';"

    curr = execute(conn,sql )

    sql = 'UPDATE "PlayerGalaxy" set "SystemBuildState" = 1 WHERE "uID" = ' 
    sql+= "'" + GalaxyID + "';"

    curr = execute(conn,sql )
    

    finish(conn)

    return "Destroyed";

