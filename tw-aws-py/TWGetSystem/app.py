import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    
    conn = connect()    
    
    SystemID = event['params']['querystring']['SystemID']
    
    sql = 'SELECT "SolarSystemData" FROM "PlayerSystems" WHERE "SystemID" = '
    sql += "'" + SystemID + "';"
    
    Acur=execute(conn, sql  )

    row = Acur.fetchone()
        
    ReturnData = "{"
    if row!=None:
        ReturnData += " 'SystemData' = '" + row[0]
    ReturnData += "}"    
        
    finish(conn)
    
    return ReturnData




