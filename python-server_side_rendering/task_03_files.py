import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products_list = read_json('products.json')
    elif source == 'csv':
        products_list = read_csv('products.csv')

    if product_id:
        product_id = int(product_id)
        filtered_products = [product for product in products_list if int(product['id']) == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products_list = filtered_products

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
