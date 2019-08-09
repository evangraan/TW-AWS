import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """
    conn = connect()

    D = chr(34)
    
    uID = event['params']['querystring']['uID']
    
    sql = 'SELECT "UserName", "TweeterName", "PlayerIcon", "PlayerXP", "IGEA", "Painter", "AIHandle", "SystemBuildState" FROM "PlayerGalaxy" WHERE "uID"='
    sql+= "'" + uID  + "';"
    curr = execute(conn, sql)
     
    ReturnData = "{"
    for row in curr.fetchall():        
        if row != None:
            Painter = 0;
            if row[5] != None:
                Painter = row[5]
            ReturnData += D + "UserName" + D + ":" + D + row[0] + D + " , "
            ReturnData += D + "TweeterName" + D + ":" + D + row[1] + D + " , "
            ReturnData += D + "PlayerIcon" + D + ":" + D + row[2] + D + " , "
            ReturnData += D + "PlayerXP" + D + ":"  + str(row[3])  + " , "
            ReturnData += D + "IGEA" + D + ":"  + str(row[4])  + " , "
            ReturnData += D + "Painter" + D + ":"  + str(Painter)  + " , "
            ReturnData += D + "AIHandle" + D + ":" + D + row[6] + D + ", " 
            ReturnData += D + "SystemBuildState" + D + ":" + str(row[7]) + ""
            
    ReturnData += "}"
        
    finish(conn)

    logger.info("SUCCESS:" + ReturnData)    
    return ReturnData



