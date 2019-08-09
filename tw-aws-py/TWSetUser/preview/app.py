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

    logger.info(event)

    uID = event['body-json']['uID']
    UserName = event['body-json']['Username']
    TweeterName = event['body-json']['TweeterName']
    AIHandle = event['body-json']['AIHandle']
    PlayerXP = event['body-json']['PlayerXP']
    IGEA = event['body-json']['IGEA']
    CreateID = event['body-json']['CreateID']
    PlayerIcon = event['body-json']['PlayerIcon']
    SystemBuildState = event['body-json']['SystemBuildState']
    Upsert = event['body-json']['Upsert']
    
    if (Upsert != 1):
        CreateID = ""
        
    sql = "INSERT INTO PlayerGalaxy " + \
    "(uID , UserName , TweeterName , AIHandle , PlayerXP , IGEA , CreateID , SystemBuildState , PlayerIcon )" + \
    " VALUES (" + \
    "'" + uID + "'," + \
    "'" + UserName + "'," + \
    "'" + TweeterName + "'," + \
    "'" + AIHandle + "'," + \
    "" + str(PlayerXP) + "," + \
    "" + str(IGEA) + "," + \
    "'" + CreateID + "'," + \
    "" + str(SystemBuildState) + "," + \
    "'" + PlayerIcon + "'" + \
    ");"
    #+ \
    #" ON DUPLICATE KEY UPDATE " + \
    #" UserName = VALUES( UserName )" + \
    #", TweeterName = VALUES( TweeterName  )" + \
    #", AIHandle = VALUES( AIHandle )" + \
    #", PlayerXP = VALUES( PlayerXP )" + \
    #", IGEA = VALUES( IGEA )" + \
    #", CreateID = VALUES( CreateID )" + \
    #", SystemBuildState = VALUES( SystemBuildState )" + \
    #", PlayerIcon = VALUES( PlayerIcon );" 

    if (Upsert == 1):
        execute(conn, "DELETE FROM PlayerGalaxy WHERE AIHandle='" + AIHandle + "';")
    
    execute(conn, sql)
    
    finish(conn)
    
    return "OK" 

