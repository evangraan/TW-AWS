import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    SystemID = event["params"]["querystring"]["SystemID"]
    D = chr(34)

    curr = execute(conn, 'SELECT "PlanetID", "PlanetData" From "PlayerPlanets" WHERE "SystemID" = ' + "'" + SystemID + "';")

    ReturnData = "{\"Planets\" : [" 

    baselength = len(ReturnData)
    
    for row in curr.fetchall():
        if len(ReturnData)>baselength:
            ReturnData+=","
        ReturnData += "" + row[1]  + ""  #[1:-1]
        
    ReturnData += "]}"

    finish(conn)

    return ReturnData;




