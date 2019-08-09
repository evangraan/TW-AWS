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
    uID = event['params']['querystring']['uID']
    UserName = event['params']['querystring']['UserName']
    TweeterName = event['params']['querystring']['TweeterName']
    PlayerIcon = event['params']['querystring']['PlayerIcon']
    PlayerXP = event['params']['querystring']['PlayerXP']
    AIHandle = event['params']['querystring']['AIHandle']
    
    sql = "INSERT INTO `PlayerGalaxy` (uID, UserName, TweeterName, PlayerIcon, PlayerXP, AIHandle) VALUES (" + \
          "'" + uID + "', " + \
          "'" + UserName + "', " + \
          "'" + TweeterName + "', " + \
          "'" + PlayerIcon + "', " + \
          PlayerXP + ", " + \
          "'" + AIHandle + \
          "') ON DUPLICATE KEY UPDATE UserName=VALUES(UserName)" + \
          ", TweeterName=VALUES(TweeterName)" + \
          ", PlayerIcon=VALUES(PlayerIcon)" + \
          ", PlayerXP=VALUES(PlayerXP)" + \
          ", AIHandle=VALUES(AIHandle);"
    execute(conn, sql)
    finish(conn)      

    return "OK"




