#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'sql check code'
import mysql.connector

conn=mysql.connector.connect(user='root', password='password', database='awesome')
cursor=conn.cursor()
cursor.execute('select * from users')
data=cursor.fetchall()
print(data)