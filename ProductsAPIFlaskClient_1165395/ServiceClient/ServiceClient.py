import requests 
from requests.auth import HTTPBasicAuth 
import json 
from Models.Product import Product 
from Models.Category import Category 
 
class ServiceClient(): 
    def __init__(self): 
        self.base_url = "http://localhost:7200/" 
 
    def get_all_products(self): 
        url = 'myapi/v1.0/prods' 
        r = requests.get(self.base_url + url) 
        json_data = r.text 
        data = json.loads(json_data) 
        plist = [Product(json.loads(d)['product_id'], 
                         json.loads(d)['product_name'], 
                         json.loads(d)['description'], 
                         json.loads(d)['price'], 
                         json.loads(d)['stock_level'], 
                         json.loads(d)['category_id']) for d in data['prods']] 
        return plist 
 
    def get_products_by_category(self, catid): 
        url = 'myapi/v1.0/prods/' + str(catid) 
        r = requests.get(self.base_url + url) 
        json_data = r.text 
        data = json.loads(json_data) 
        plist = [Product(json.loads(d)['product_id'], 
                         json.loads(d)['product_name'], 
                         json.loads(d)['description'], 
                         json.loads(d)['price'], 
                         json.loads(d)['stock_level'], 
                         json.loads(d)['category_id']) for d in data['prods']] 
        return plist 
 
    def get_categories(self): 
        url = 'myapi/v1.0/categories' 
        r = requests.get(self.base_url + url) 
        json_data = r.text 
        data = json.loads(json_data) 
        clist = [Category(category_id=json.loads(d)['category_id'], category_name=json.loads(d)['category_name']) for d in data['cats']] 
        return clist 
 
    def add_new_product(self, prod): 
        url = 'myapi/v1.0/prods' 
        url2 = self.base_url + url 
        prodjson = json.dumps(prod.__dict__) 
 
        r = requests.post(url=url2, json=json.loads(prodjson)) 
        reply = r.text 
        return reply