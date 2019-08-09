import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    uID = event["params"]["querystring"]["uID"]

    curr = execute(conn,'SELECT "UserName", "TweeterName", "AIHandle",  "PlayerIcon", "PlayerXP", "IGEA", "Painter", "SystemBuildState" FROM "PlayerGalaxy" WHERE "uID" = ' + "'" + uID + "';")
        
    row = curr.fetchone()
            
    ReturnData = ""        
    if(row):      
        Painter = 0
        if row[6] != None:
            Painter = row[6]
        ReturnData = "{ " + \
        "'Username' : '" + row[0] + "' , " + \
        "'TweeterName' : '" + row[1] + "' , " + \
        "'AIHandle' : '" + row[2] + "', " + \
        "'PlayerIcon' : '" + row[3] + "' , " + \
        "'SystemBuildState' : " + str(row[7]) + ", " + \
        "'IGEA' : " + str(row[5]) + " , " + \
        "'Painter' : " + str(Painter) + " , " + \
        "'PlayerXP' : " + str(row[4]) + " } "

    finish(conn)
    
    return ReturnData;





