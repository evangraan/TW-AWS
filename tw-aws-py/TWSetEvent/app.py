import sys
import logging
import json
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    
    conn = connect()
    
    uID = event['body-json']['uID']
    EventData = json.dumps(event['body-json']['EventData'])

    sql = 'INSERT INTO "PlayerEvents" ( "uID" , "EventData" ) VALUES ('
    sql += "'" + uID + "' , '" + EventData + "');"

    execute(conn, sql )
    
    conn.commit
    
    finish(conn)
    
    return "OK";


