# -*- coding:utf-8 -*-

import logging

from tornado.options import define
from tornado.options import options
from tornado.options import parse_command_line

import pyorient

HOST = 'localhost'
# HOST = '172.28.32.49'
PORT = 2424
USER = 'root'
PASSWORD = 'root'
DB_NAME = 'orientdb'


def main():
    client = pyorient.OrientDB(HOST, PORT)
    session_id = client.connect(USER, PASSWORD)
    
    is_exist = client.db_exists(DB_NAME, pyorient.STORAGE_TYPE_MEMORY)
    if is_exist:
        logging.info("Database: %s has exist, do not creat it again.", DB_NAME)
    else: 
        client.db_create(DB_NAME, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY)
        logging.info("Database: %s is created", DB_NAME)

    db_list = client.db_list()
    logging.info("Database list: %s is created", db_list)

    #db_size = client.db_size()
    #logging.info("The size of the db is: %s", db_size)
    ## NOTE: You must have an opened database to issue this command

    #db_count_records = client.db_count_records()
    #logging.info("Database count of records is: %s", db_count_records)
    ### NOTE: You must have an opened database to issue this command
    

if __name__ == '__main__':
    parse_command_line()
   
    main()
