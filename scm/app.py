from flask import Flask, render_template, request, jsonify
from orderquery import OrderQuery
from materialquery import MaterialQuery
from deliveryquery import DeliverQuery
from surplusquery import SurplusQuery
from contractquery import ContractQuery

app = Flask(__name__)


@app.route('/')
def show_index_page():
    return render_template('orderyquery.html')


@app.route('/orderPage')
def show_order_page():
    return render_template('orderyquery.html')


@app.route('/deliveryPage')
def show_delivery_page():
    return render_template('deliverquery.html')


@app.route('/surplusPage')
def show_surplus_page():
    return render_template('surplusquery.html')


@app.route('/contractPage')
def show_contract_page():
    return render_template('contractquery.html')


@app.route('/materialPage')
def show_material_page():
    return render_template('materialquery.html')


@app.route('/orderQuery', methods=['POST', 'GET'])
def order_query():
    query = OrderQuery(request)
    return query.get_response_json()


@app.route('/materialQuery', methods=['POST', 'GET'])
def material_query():
    query = MaterialQuery(request)
    return query.get_response_json()


@app.route('/deliveryQuery', methods=['POST', 'GET'])
def delivery_query():
    query = DeliverQuery(request)
    return query.get_response_json()


@app.route('/surplusQuery', methods=['POST', 'GET'])
def surplus_query():
    query = SurplusQuery(request)
    return query.get_response_json()


@app.route('/contractQuery', methods=['POST', 'GET'])
def contract_query():
    query = ContractQuery(request)
    return query.get_response_json()

if __name__ == '__main__':
    app.run()
