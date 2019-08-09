import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    PlanetID = event["params"]["querystring"]["PlanetID"]

    sql = 'SELECT "PlanetData" From "PlayerPlanets" WHERE "PlanetID" = ' 
    sql+= "'" + PlanetID + "';"

    curr = execute(conn,sql )
    row = curr.fetchone()
            
    ReturnData = "{ 'PlanetData' = '" + row[0] + "' }"
        
    finish(conn)

    return ReturnData;




