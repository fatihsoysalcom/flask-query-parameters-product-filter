from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data
products_data = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200},
    {"id": 2, "name": "Mouse", "category": "Electronics", "price": 25},
    {"id": 3, "name": "Python Book", "category": "Books", "price": 50},
    {"id": 4, "name": "Chair", "category": "Furniture", "price": 150},
    {"id": 5, "name": "Keyboard", "category": "Electronics", "price": 75},
    {"id": 6, "name": "Cookbook", "category": "Books", "price": 30}
]

@app.route('/products', methods=['GET'])
def get_products():
    # HTTP sorgu parametrelerini (query parameters) request.args ile alıyoruz.
    # Bu, URL'deki '?' işaretinden sonra gelen anahtar-değer çiftlerini bir sözlük olarak sağlar.
    category = request.args.get('category') # 'category' parametresini al
    sort_by = request.args.get('sort_by')   # 'sort_by' parametresini al

    filtered_products = list(products_data)

    # Kategoriye göre filtreleme yapıyoruz
    if category:
        # Eğer 'category' parametresi varsa, ürünleri bu kategoriye göre filtrele
        filtered_products = [p for p in filtered_products if p['category'].lower() == category.lower()]

    # Sıralama yapıyoruz
    if sort_by:
        if sort_by == 'price_asc':
            # 'price_asc' parametresi varsa, fiyatı artan sıraya göre sırala
            filtered_products.sort(key=lambda p: p['price'])
        elif sort_by == 'price_desc':
            # 'price_desc' parametresi varsa, fiyatı azalan sıraya göre sırala
            filtered_products.sort(key=lambda p: p['price'], reverse=True)
        # Diğer sıralama seçenekleri buraya eklenebilir

    # Filtrelenmiş ve sıralanmış ürünleri JSON formatında geri döndürüyoruz
    return jsonify(filtered_products)

@app.route('/')
def index():
    return (
        "<h1>Welcome to the Product API Example!</h1>"
        "<p>Try these URLs to see query parameters in action:</p>"
        "<ul>"
        "<li><a href='/products'>/products</a> - All products</li>"
        "<li><a href='/products?category=Electronics'>/products?category=Electronics</a> - Filter by category</li>"
        "<li><a href='/products?sort_by=price_asc'>/products?sort_by=price_asc</a> - Sort by price ascending</li>"
        "<li><a href='/products?category=Books&sort_by=price_desc'>/products?category=Books&sort_by=price_desc</a> - Filter and sort</li>"
        "</ul>"
    )

if __name__ == '__main__':
    app.run(debug=True)
