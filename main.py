# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import pymysql.cursors
import views

app = Flask(__name__,
            static_url_path='', 
            static_folder='./static',
            template_folder='./templates')

#database connection

cnt = pymysql.connect(host='localhost',user='root',password='',db='flaskcommerce',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

#bassic data

with cnt.cursor() as cursor:
        main_data = {}
        sql = "select * from settings"
        cursor.execute(sql)
        result = cursor.fetchone()
        main_data['name'] = result['main_name']
        main_data['desc'] = result['desciption']
        main_data['head_tags'] = result['head_tags']
        main_data['footer_tags'] = result['footer_tags']
        main_data['maintance'] = result['maintance']
        main_data['extra'] = result['extra']
        main_data['currency'] = 'PLN'

@app.route('/')
def init_index():
    main_data['route'] = '/'
    return render_template('index.html',main_data = main_data)

@app.route('/categories')
def init_category():
    main_data['route'] = '/categories'
    return views.categories_page(main_data)

@app.route('/categories/<path:subpath>')
def init_subpath(subpath):
    
        return views.categories_sub(main_data,subpath)

@app.route('/products/<path:subpath>')
def init_prodpage(subpath):

        return views.product_page(main_data,subpath)
