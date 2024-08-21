from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)

@app.route('/create_tag', methods=['POST'])
def create_tag():
    body = request.json
    product_code = body.get('product_code')

    if not product_code:
        return jsonify({"error": "Product code is required"}), 400

    if not isinstance(product_code, str):
        return jsonify({"error": "Product code must be a string number"}), 400
    
    tag = Code128(product_code, ImageWriter)
    path_from_tag = f'{product_code}'
    tag.save(path_from_tag)
    
    return jsonify({"tag_path": path_from_tag})
 
