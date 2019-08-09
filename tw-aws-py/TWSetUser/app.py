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
    
    if(open(conn)):
        logger.info(event)
    else:
        logger.info("Couldnot connect to database");
    
    uID = event['body-json']['uID']
    UserName = event['body-json']['Username']
    TweeterName = event['body-json']['TweeterName']
    AIHandle = event['body-json']['AIHandle']
    PlayerXP = event['body-json']['PlayerXP']
    IGEA = event['body-json']['IGEA']
    Painter = event['body-json']['Painter']
    CreateID = event['body-json']['CreateID']
    PlayerIcon = event['body-json']['PlayerIcon']
    SystemBuildState = event['body-json']['SystemBuildState']
    Upsert = event['body-json']['Upsert']
    
    if (Upsert != 1):
        CreateID = ""
    
    findSQL = 'SELECT "uID" FROM "PlayerGalaxy" WHERE "uID" = ' + "'" + uID + "';"
    
    findcur = execute(conn, findSQL)
    

    sql=""
    
    if(findcur.rowcount==0):
        sql = 'INSERT INTO "PlayerGalaxy" ("uID" , "UserName" , "TweeterName" , "AIHandle" , "PlayerXP" , "IGEA" , "Painter", "CreateID" , "SystemBuildState" , "PlayerIcon" )' 
        sql+=" VALUES ('" + uID + "' , '" + UserName + "' , '" + TweeterName + "' , '" + AIHandle + "' , " + str(PlayerXP) + " , " + str(IGEA) + " , " + str(Painter) + " , '"  + CreateID + "' , " + str(SystemBuildState) + " , '" + PlayerIcon + "');"
    else:
        sql= 'UPDATE "PlayerGalaxy" SET ' 
        sql+=' "UserName" = '
        sql+="'" + UserName + "',"
        sql+=' "TweeterName" = '
        sql+="'" + TweeterName + "',"
        sql+='"AIHandle" = ' 
        sql+="'" + AIHandle + "'," 
        sql+=' "PlayerXP" = ' 
        sql+="" + str(PlayerXP) + "," 
        sql+=' "IGEA" = ' 
        sql+="" + str(IGEA) + "," 
        sql+=' "Painter" = ' 
        sql+="" + str(Painter) + "," 
        sql+=' "CreateID" = ' 
        sql+="'" + CreateID + "'," 
        sql+=' "SystemBuildState" = ' 
        sql+="" + str(SystemBuildState) + "," 
        sql+=' "PlayerIcon" = ' 
        sql+="'" + PlayerIcon + "' WHERE " + '"uID" = ' + "'" + uID + "';" 
    
#    sql = 'INSERT INTO "PlayerGalaxy" ' + \
#    '("uID" , "UserName" , "TweeterName" , "AIHandle" , "PlayerXP" , "IGEA" , "Painter" , "CreateID" , "SystemBuildState" , "PlayerIcon" )' 
#    sql+=" VALUES ('" + uID + "' , '" + UserName + "' , '" + TweeterName + "' , '" + AIHandle + "' , " + str(PlayerXP) + " , " + str(IGEA) + " , " + str(Painter) + " , '"  + CreateID + "' , " + \
#     str(SystemBuildState) + " , '" + PlayerIcon + "' )" + \
#    ' ON CONFLICT  ON CONSTRAINT "PlayerGalaxy_pkey" DO UPDATE SET ' 
#    sql+=' "UserName" = '
#    sql+="'" + UserName + "',"
#    sql+=' "TweeterName" = '
#    sql+="'" + TweeterName + "',"
#    sql+='"AIHandle" = ' 
#    sql+="'" + AIHandle + "'," 
#    sql+=' "PlayerXP" = ' 
#    sql+="" + str(PlayerXP) + "," 
#    sql+=' "IGEA" = ' 
#    sql+="" + str(IGEA) + "," 
#    sql+=' "Painter" = ' 
#    sql+="" + str(Painter) + "," 
#    sql+=' "CreateID" = ' 
#    sql+="'" + CreateID + "'," 
#    sql+=' "SystemBuildState" = ' 
#    sql+="" + str(SystemBuildState) + "," 
#    sql+=' "PlayerIcon" = ' 
#    sql+="'" + PlayerIcon + "';" 
    
    logger.info(sql)

    if (Upsert == 1):
        execute(conn, 'DELETE FROM "PlayerGalaxy" WHERE "AIHandle" = '  +   "'" + AIHandle + "' ; ")
        
        
    curr = execute(conn, sql)
    

    conn.commit
    
    finish(conn)
    
    logger.info("SUCCESS: Set User Exited With OK.")
    
    return "OK" 


