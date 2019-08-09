import sys
import logging
from dal import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)
conn = connect()

def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    item_count = 0
    
    galaxyID = event['params']['querystring']['galaxyID']
    
    sql = 'SELECT * FROM "PlayerGalaxy" WHERE "uID"= '
    sql+= "'" + galaxyID + "';"
    
    curr = execute(conn, sql)
    
    
    for row in curr.fetchall():        
        if row != None:
            item_count += 1
            logger.info(row)

    finish(conn)

    return "Found %d galaxies" %(item_count)



