import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    uID = event['params']['querystring']['uID']
    D = chr(34)
    
    sql = 'SELECT "SystemID", "SolarSystemData" From "PlayerSystems" WHERE "uID" = '
    sql+= "'" + uID + "';"
    
    curr = execute(conn, sql)

    ReturnData = "{" + D + "SolarSystems" + D + " : [" 
    baselength = len(ReturnData)
    for row in curr.fetchall():
        if len(ReturnData)>baselength:
            ReturnData+=","
        ReturnData += " " +  row[1][1:-1] +  " " 
        
        
    ReturnData += "]}"
    logger.info("SUCCESS: " + ReturnData)

    finish(conn)

    return ReturnData;



