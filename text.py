# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import pymysql.cursor
import views

cnt = pymysql.connect(host='localhost',user='root',password='',db='flaskcommerce',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

def categories_page(md):

        with cnt.cursor() as cursor:
        
            sql = 'select * from categories'
            cursor.execute(sql)
            
            result = cursor.fetchone()

            print(result)
