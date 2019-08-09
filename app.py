# Uses tw-aws-py/lib/dal.py

import sys
import logging
import pymysql
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
    curr = exec(conn,  "SELECT * FROM `PlayerGalaxy` WHERE `uID`= '" + galaxyID + "'")
    for row in curr.fetchall():        
        if row != None:
            item_count += 1
            logger.info(row)
    finish(conn)

    return "Found %d galaxies" %(item_count)
