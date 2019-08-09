import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    conn = connect()
    uIDs = event['params']['querystring']['Filter']
    
    qStr = ""
    
    D = chr(34)
    
    if len(uIDs)>0:
        if "|" in uIDs:
            xArr = uIDs.split("|")
            for xStr in xArr:
                if len(xStr)>0:
                    if len(qStr)>0:
                        qStr += " OR "
                    qStr += D + "uID" + D + " = '" + xStr + "'"
        else:
            qStr = D + "uID" + D + " = '" + uIDs + "'"
            
    
    logger.info("filter: " + qStr)
        
    
    
    sql = 'SELECT "UserName", "TweeterName", "PlayerIcon", "PlayerXP", "IGEA", "Painter", "AIHandle", "uID", "SystemBuildState" FROM "PlayerGalaxy"'
    
    if len(qStr) > 0:
        sql+= " WHERE " + qStr + ";"
    else:
        sql+= ";"
    
    logger.info("q: " + sql)

    curr = execute(conn, sql)        

    ReturnData = " { " + D + "UsersList" + D + " : ["
    baselength = len(ReturnData)

    for row in curr.fetchall():
        Painter = 0
        if row[5] != None:
            Painter = row[5]
        if len(ReturnData)>baselength:
            ReturnData+=","
        ReturnData += " { " + D + "UserName" + D + " : " + D + row[0] + D + " , " \
                            + D + "TweeterName" + D + " : " + D + row[1] + D + " , " \
                            + D + "PlayerIcon" + D + " : " + D + row[2] + D + " , " \
                            + D + "PlayerXP" + D + " : " + str(row[3]) + " , " \
                            + D + "IGEA" + D + " : " + str(row[4]) + " , " \
                            + D + "Painter" + D + " : " + str(Painter) + " , " \
                            + D + "AIHandle" + D + " : " + D + row[6] + D + " , " \
                            + D + "uID" + D + " : " + D + row[7] + D + " , " \
                            + D + "SystemBuildState" + D + " : " + str(row[8]) + "  } "
        
    ReturnData += " ] } "
    
    conn.commit
    
    finish(conn)        
    
    return ReturnData


