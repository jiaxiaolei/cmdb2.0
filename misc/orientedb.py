# -*- coding:utf-8 -*-

import logging

from tornado.options import define
from tornado.options import options
from tornado.options import parse_command_line

import pyorient

HOST = 'localhost'
PORT = 2424
USER = 'root'
PASSWORD = 'root'
DB_NAME = 'orientdb'


def main():
    client = pyorient.OrientDB(HOST, PORT)
    session_id = client.connect(USER, PASSWORD)
    
    flag = client.db_exists(DB_NAME, pyorient.STORAGE_TYPE_MEMORY)
    logging.info('flag:%s' % flag)
    
    if flag:
        logging.info("Database: %s has exist, do not creat it again.", DB_NAME)
    else: 
        client.db_create(DB_NAME, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY)


if __name__ == '__main__':
    parse_command_line()
    
   
    main()
