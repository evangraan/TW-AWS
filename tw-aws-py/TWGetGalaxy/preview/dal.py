import sys
import logging
import pymysql

rds_host  = "hostname"
name = "user"
password = "password"
db_name = "TW"
cursors = []

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def connect():
    try:
        cc = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=10)
        logger.info("Connection to RDS mysql instance succeeded")
        return cc
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

def cur(conn):
    if (conn is None):
        conn = connect()
    if (not conn.open):
        conn = connect()
    return conn.cursor()

def exec(conn, sql):
    logger.info("Query:" + sql)
    curr = cur(conn)
    curr.execute(sql)
    cursors.append(curr)
    return curr

def finish(conn):
    for curr in cursors:
        if curr is not None:
            del curr
    if (conn is not None) and (conn.open):
        conn.commit()
        conn.close()


