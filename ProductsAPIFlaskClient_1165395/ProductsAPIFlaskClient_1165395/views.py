from flask import request  
from Models import Product
from ServiceClient import ServiceClient

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ProductsAPIFlaskClient_1165395 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/showproducts',methods=['GET','POST']) 
def showproducts(): 
    sc = ServiceClient() 
    products = sc.get_all_products() 
    catsel = 0 
    if len(request.form) > 0: 
        catsel =  request.form['catddl'] # posted data dropdon value 
        products = sc.get_products_by_category(catsel) 
 
     
    cats = sc.get_categories() 
    return render_template( 
        'showproducts.html', 
        title='Show Products', 
        prods=products, 
        catlist = cats, 
        catselected = int(catsel), 
        message='Your application description page.' 
    ) 
 
@app.route('/addnewproduct',methods=['GET','POST']) 
def addnewproduct(): 
    sc = ServiceClient() 
    catsel = 100 
    res = '' 
    if len(request.form) > 0: 
        prod = Product() 
        prod.product_id = request.form['product_id'] 
        prod.product_name = request.form['product_name'] 
        prod.price = request.form['price'] 
        prod.stock_level = request.form['stock_level'] 
        prod.category_id =  request.form['category_id'] # posted data 
        res = sc.add_new_product(prod) 
        msg = res 
    cats = sc.get_categories() 
    return render_template( 
        'addnewproduct.html', 
        title='Add New Product', 
        catlist = cats, 
        msg=res 
    ) 

