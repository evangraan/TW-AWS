import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    uID = event['params']['querystring']['uID']
 
    sql = 'SELECT "UserName", "TweeterName", "PlayerIcon", "PlayerXP", "IGEA", "Painter", "AIHandle", "SystemBuildState" FROM "PlayerGalaxy" WHERE "uID"='
    sql+= "'" + uID  + "';"
 
    curr = execute(conn, sql)

    ReturnData = ""
    ReturnData += "{"

    row = curr.fetchone()
    if row!=None:
        Painter = 0;
        if row[5] != None:
            Painter = row[5]        
        ReturnData += "'UserName' = '" + row[0]
        ReturnData += "', 'TweeterName' : '" + row[1]
        ReturnData += "','PlayerIcon' : '" + row[2]
        ReturnData += "','PlayerXP' : " + str(row[3])
        ReturnData += ",'IGEA' : " + str(row[4])
        ReturnData += ",'Painter' : " + str(Painter)
        ReturnData += ",'AIHandle' : '" + row[6] + "'"
        ReturnData += "','SystemBuildState' : " + row[7]

    ReturnData += "}"

    finish(conn)
        
    return ReturnData


