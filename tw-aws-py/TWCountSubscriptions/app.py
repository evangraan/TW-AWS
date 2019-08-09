import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    conn = connect()


    sql = 'SELECT COUNT("uID") FROM "PlayerGalaxy" WHERE "IGEA"=1 OR "Painter"=1;'
        
    cur = execute(conn,sql)

    ReturnData=""
    row = curr.fetchone()
    if row!=None:
        ReturnData += str(row[0]
            
    conn.commit()

    return ReturnData;



