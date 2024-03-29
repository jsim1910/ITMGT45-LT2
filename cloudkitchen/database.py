import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]
order_management_db = myclient["order_management"]


products = {
    100: {"name":"Beef Tapa","price":110},
    200: {"name":"Pork Sisig","price":100},
    300: {"name":"Garlic Chicken","price":100},
    400: {"name":"Pork Liempo","price":100},
}

def get_product(code):
    return products[code]

def get_products():
    product_list = []

    for i,v in products.items():
        product = v
        product.setdefault("code",i)
        product_list.append(product)

    return product_list


def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user

    
