# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import pymysql.cursors

cnt = pymysql.connect(host='localhost',user='root',password='',db='flaskcommerce',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

def error_page():

    return render_template('error.html')

def categories_page(md):

        with cnt.cursor() as cursor:
        
            sql = 'select * from categories'
            cursor.execute(sql)
            
            result = cursor.fetchall()


            return render_template('categories.html',categories = result, main_data = md)

def subpath_page(md,sp):

        return render_template('subpath.html',main_data = md, lol = sp)