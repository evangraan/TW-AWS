import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    uID = event["params"]["querystring"]["uID"]
    D = chr(34)

    curr = execute(conn, 'SELECT "SystemID", "PlanetID", "PlanetData" From "PlayerPlanets" WHERE "uID" = ' + "'" + uID + "';")

    ReturnData = " { " + D + "Planets" + D + " : [" 
    baselength = len(ReturnData)
    for row in curr.fetchall():
        if len(ReturnData)>baselength:
            ReturnData+=","
        ReturnData += " " + row[2] + " "
        
    ReturnData += " ]} " 

    finish(conn)

    return ReturnData;




