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

def categories_sub(md,sp):

        with cnt.cursor() as cursor:

            sql = 'select id from categories where path = "/%s"' % (sp)

            cursor.execute(sql)
            
            unique_id = cursor.fetchone()

            if unique_id:

                get_products = 'select * from products where category = %d' %(unique_id['id'])

                cursor.execute(get_products)

                result = cursor.fetchall()

            return render_template('categories_list.html',main_data = md, products = result)

            print(md,sp)

def product_page(md,sp):

    with cnt.cursor() as cursor:

            sql = 'select id from products where path = "/%s"' % (sp)

            cursor.execute(sql)
            
            unique_id = cursor.fetchone()

            if unique_id:

                get_products = 'select * from products where id = %d' %(unique_id['id'])

                cursor.execute(get_products)

                result = cursor.fetchall()

            return render_template('product_details.html',main_data = md, products = result)