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
    
    ScreenName = event['body-json']['ScreenName']
    IconURL = event['body-json']['IconURL']
   
    sql = 'INSERT INTO "ValidedTwitterHandles" ("ScreenName", "IconURL") VALUES (' + \
          "'" + ScreenName + "', " + \
          "'" + IconURL +  "')" + \
          ' ON CONFLICT ("ScreenName") DO UPDATE SET ' + \
          ' "IconURL" = ' + \
          "'" + IconURL + "';"
          
    execute(conn, sql)
    
    finish(conn)
    
    return "OK"





