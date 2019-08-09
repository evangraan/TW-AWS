import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()
    
    uID = event['params']['querystring']['uID']
    DoD = event['params']['querystring']['DoD']
    D = chr(34)

    sql =  'SELECT "EventData" From "PlayerEvents" WHERE "uID" = ' + "'" + uID + "'"

    curr = execute(conn,sql)

    ReturnData = " { " + D + "ListOfEvents" + D + ": [" 
    baselength = len(ReturnData)
    for row in curr.fetchall():
        if len(ReturnData)>baselength:
            ReturnData+=","
        ReturnData += " " + row[0][1:-1]  + " "
        
    ReturnData += " ]} " 

    logger.info("SUCCESS: Events Return " + ReturnData)
    
    if DoD=="1":
        delsql = 'DELETE From "PlayerEvents" WHERE "uID" = ' + "'" + uID + "'"
        execute(conn,delsql )
        conn.commit
    
    if DoD=="2":
        # :12, indicates EventData:12, which is ReinforcementsInitiate
        # :14, indicates EventData:14, which is ReinforcementsHit
        delsql = 'DELETE From "PlayerEvents" WHERE ("uID" = ' + "'" + uID + "')" + " AND (" + '"EventData" LIKE ' + "'%:12,%'" + " OR " + '"EventData" LIKE ' + "'%14,%')"
        execute(conn,delsql )
        conn.commit
    
    finish(conn)
    return ReturnData;


