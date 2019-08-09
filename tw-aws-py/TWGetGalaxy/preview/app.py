import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)
conn = connect()

def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    D = chr(34)
    
    uID = event['params']['querystring']['uID']
    curr = execute(conn, "SELECT UserName, TweeterName, PlayerIcon, PlayerXP, IGEA, AIHandle, SystemBuildState FROM PlayerGalaxy WHERE uID='" + uID  + "';")
     
    ReturnData = "{"
    for row in curr:
        row = cur.fetchone()
        
        if row!=None:
            
            ReturnData += D + "UserName" + D + ":" + D + row[0] + D + " , "
            ReturnData += D + "TweeterName" + D + ":" + D + row[1] + D + " , "
            ReturnData += D + "PlayerIcon" + D + ":" + D + row[2] + D + " , "
            ReturnData += D + "PlayerXP" + D + ":"  + str(row[3])  + " , "
            ReturnData += D + "IGEA" + D + ":"  + str(row[4])  + " , "
            ReturnData += D + "AIHandle" + D + ":" + D + row[5] + D + ", " 
            ReturnData += D + "SystemBuildState" + D + ":" + str(row[6]) + ""
            
    ReturnData += "}"
        
    finish(conn)

    logger.info("SUCCESS:" + ReturnData)    
    return ReturnData
