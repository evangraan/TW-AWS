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


    sql = 'SELECT "uID", "GalaxyID", "PlanetID", "Score" FROM "InvasionScores" ORDER BY "Score" DESC LIMIT 10;'
        
    cur = execute(conn,sql)

    ReturnData = " { 'Scores' = [" 
    baselength = len(ReturnData)
    for row in cur:
        if len(ReturnData)>baselength:
            ReturnData+=","
        ReturnData += "{ 'uID' = '" + row[0] +  "' ;  'GalaxyID' = '" + row[1] + "' ; 'PlanetID' = '" + row[2] + "' ; 'Score' = " + str(row[3]) + " }"
            
    ReturnData += " ]} "
        

    conn.commit()

    return ReturnData;



