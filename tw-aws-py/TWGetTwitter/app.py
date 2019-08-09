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
    
    SearchName = event['params']['querystring']['SearchName']
    D = chr(34)
    
    sql = 'SELECT "UserName", "TweeterName", "PlayerIcon", "PlayerXP", "IGEA", "Painter", "AIHandle", "uID" , "SystemBuildState", "CreateID" FROM "PlayerGalaxy" WHERE "TweeterName"= '
    sql += "'" + SearchName + "' OR " +  '"AIHandle"' + "= '" + SearchName + "';"
    
    
    curr = execute(conn, sql)

    ReturnData = " { " + D + "UsersList" + D + " : ["
    baselength = len(ReturnData)
        

    for row in curr.fetchall():
        Painter = 0
        if row[5] != None:
            Painter = row[5]
        if len(ReturnData)>baselength:
            ReturnData+=","
        ReturnData += "{"
        ReturnData += D + "UserName" + D + " : " + D + row[0] + D
        ReturnData += " , " 
        ReturnData += D + "TweeterName" + D + " : " + D + row[1] + D
        ReturnData += " , "  
        ReturnData += D + "PlayerIcon" + D + " : " + D + row[2] + D
        ReturnData += " , " 
        ReturnData += D + "PlayerXP" + D + " : " + str(row[3]) 
        ReturnData += " , " 
        ReturnData += D + "IGEA" + D + " : " + str(row[4]) 
        ReturnData += " , " 
        ReturnData += D + "Painter" + D + " : " + str(Painter) 
        ReturnData += " , " 
        ReturnData += D + "AIHandle" + D + " : " + D + row[6] + D
        ReturnData += " , " 
        ReturnData += D + "uID" + D + " : " + D + row[7] + D
        ReturnData += " , " 
        ReturnData += D + "SystemBuildState" + D + " : " + str(row[8])
        ReturnData += " , " 
        ReturnData += D + "CreateID" + D + " : " + D + row[9] + D
        
        ReturnData += "}"  

    ReturnData += "]}"        

    finish(conn)        

    return ReturnData





