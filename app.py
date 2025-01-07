from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Row

# running flask app
app = Flask(__name__)

#creating engine to read SQL database
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/Newyork_Airbnb_prices_db')

#creating function to connect to database , run the query , storing the results and converting into a json file 
def query_db(query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(query), params or {})
        return [dict(row._mapping) for row in result]
    
# creating home page
# Home page listing all routes
@app.route('/')
def home():
    """Home page that lists all available routes."""
    routes = {
        "/api/room_types": "Get all room types",
        "/api/prices": "Get all prices",
        "/api/prices/borough/<borough>": "Get prices by borough (ex, /api/prices/borough/Brooklyn)",
        "/api/prices/neighborhood/<neighborhood>": "Get prices by neighborhood (ex, /api/prices/neighborhood/Williamsburg)",
        "/api/prices/filter?min_price=<min>&max_price=<max>": "Filter prices by range (ex, /api/prices/filter?min_price=100&max_price=500)"
    }
    return jsonify(routes)

# creating route to get all room types
@app.route('/api/room_types', methods=['GET'])
def get_room_type():
    query = """
    SELECT room_type.listing_id, room_type.room_type, prices.listing_price
    FROM room_type
    JOIN prices ON room_type.listing_id = prices.listing_id
    """
    results = query_db(query)
    return jsonify(results)

#route to get all prices
@app.route('/api/prices', methods=['GET'])
def get_prices():
    query = """
    SELECT prices.listing_id, prices.listing_price, prices.borough, prices.neighborhood, room_type.room_type
    FROM prices
    JOIN room_type ON prices.listing_id = room_type.listing_id
    """
    results = query_db(query)
    return jsonify(results)

# route to filter prices by borough 
@app.route('/api/prices/borough/<borough>', methods=['GET'])
def prices_by_borough(borough):
    query = """
    SELECT prices.listing_id, prices.listing_price, prices.borough, prices.neighborhood, room_type.room_type
    FROM prices
    JOIN room_type ON prices.listing_id = room_type.listing_id
    WHERE prices.borough = :borough
    """
    results = query_db(query, {'borough': borough})
    return jsonify(results)

# route to filter prices by neighborhood
@app.route('/api/prices/neighborhood/<neighborhood>', methods=['GET'])
def prices_by_neighborhood(neighborhood):
    query = "SELECT * FROM prices WHERE neighborhood = :neighborhood"
    results = query_db(query, {'neighborhood': neighborhood})
    return jsonify(results)

# route to filter prices by provided range
@app.route('/api/prices/filter', methods=['GET'])
def filter_prices():
    min_price = request.args.get('min_price', 0, type=int)
    max_price = request.args.get('max_price', 10000, type=int)
    query = """
    SELECT prices.listing_id, prices.listing_price, prices.borough, prices.neighborhood, room_type.room_type
    FROM prices
    JOIN room_type ON prices.listing_id = room_type.listing_id
    WHERE CAST(TRIM(TRANSLATE(prices.listing_price, '$ ', '')) AS INT) BETWEEN :min_price AND :max_price
    """
    results = query_db(query, {'min_price': min_price, 'max_price': max_price})
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)