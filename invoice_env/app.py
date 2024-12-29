from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route to render the invoice template
@app.route("/")
def home():
    return render_template("invoice.html")  # Ensure your HTML file is in the templates folder

# API endpoint to handle user input and generate data
@app.route("/generate_invoice", methods=["POST"])
def generate_invoice():
    data = request.json
    # Example: Process incoming data (client info, items, totals, etc.)
    client_name = data.get("client_name")
    invoice_number = data.get("invoice_number")
    items = data.get("items", [])
    total = sum(item["quantity"] * item["unit_price"] for item in items)
    
    # Return the processed data
    return jsonify({
        "client_name": client_name,
        "invoice_number": invoice_number,
        "items": items,
        "total": total
    })

if __name__ == "__main__":
    app.run(debug=True)
