import sys
import logging
import psycopg2
import time

rds_host  = "hostname"
name = "user"
password = "password"
db_name = "TW"
db_port = "3306"
cursors = []

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def connect():
    try:
        conn_string = "dbname='" + db_name  + "' port='" + db_port + "' user='" + name + "' password='" + password + "' host='" + rds_host + "'"
        cc = psycopg2.connect(conn_string)
        logger.info("Connection to RDS postgresql instance succeeded")
        return cc
    except:
        logger.error("ERROR: Unexpected error: Could not connect to postgresql instance.")
        sys.exit()

def open(conn):
  return not conn.closed

def cur(conn):
    if (conn is None):
        conn = connect()
    if (not open(conn)):
        conn = connect()
    currr = conn.cursor()
    cursors.append(currr)
    return currr

def execute(conn, sql):
    curr = cur(conn)
    retries = 0
    try:
        logger.info("Query:" + sql)
        curr.execute(sql)
    except:
        retries = retries + 1
        logger.error("ERROR: Unexpected error: retrying " + str(retries))
        if (retries < 10):
            cleanup(conn, curr)
            time.sleep(1)
            curr = cur(conn)
            curr.execute(sql)
        else:
            finish(conn)
            raise e
    return curr

def cleanup(conn, curr):
    if (conn is not None) and (open(conn)):
        conn.commit()
        conn.close()
    if curr is not None:
        curr.close
        del curr

def finish(conn):
    if (conn is not None) and (open(conn)):
        conn.commit()
        conn.close()
    for curr in cursors:
        if curr is not None:
            curr.close
            del curr



