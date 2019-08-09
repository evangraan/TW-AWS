import sys
import logging
import json

from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    uID = event['body-json']['uID']
    SystemID = event['body-json']['SystemID']
    SystemData = json.dumps(event['body-json']['SystemData'])


    conn = connect()
    findSQL = 'SELECT "uID" FROM "PlayerSystems" WHERE "SystemID" = ' + "'" + SystemID + "';"
    findcur = execute(conn, findSQL);
    
    sql=""
    if(findcur.rowcount==0):
        sql = 'INSERT INTO "PlayerSystems" ("uID","SystemID","SolarSystemData") VALUES ('
        sql+= "'" + uID + "','" + SystemID + "','" + SystemData + "');"
    else:
        sql = 'UPDATE "PlayerSystems" SET "SolarSystemData"'
        sql+= " = '" + SystemData + "'"
        sql+= ' WHERE "SystemID" = ' + "'" + SystemID + "';"

    execute(conn,sql)
    
    conn.commit
    
    finish(conn)
    
    logger.info("SUCCESS: System Saved OK"  )
    
    return "OK"

