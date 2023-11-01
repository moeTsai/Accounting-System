from flask import render_template, url_for, request, redirect, session
from datetime import datetime
from order.models import Order
from order import app, db


@app.route('/', methods = ['POST', 'GET'])
def index():
    # print(request.method)
    if request.method == 'POST':
        # new_order = Order(customer_name=request.form['customer_name'], order_items=request.form['order_items'], order_date=request.form['order_date'])
        customer_name = request.form['customer_name'] 
        order_items = request.form['order_items']     
        order_date = request.form['order_date'] if request.form['order_date'] else datetime.utcnow().strftime('%Y-%m-%d')
        
        new_order = Order(customer_name=customer_name, order_items=order_items, order_date=order_date)
        print(new_order.customer_name, new_order.order_items, new_order.order_date)
        try:
            db.session.add(new_order)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"An error occurred: {e}")
            return 'There was an issue adding your order'
    else:
        orders = Order.query.order_by(Order.order_date).all()
        return render_template('index.html', orders = orders)
    
@app.route('/delete/<int:id>')
def delete(id):
    order_to_delete = Order.query.get_or_404(id)
    
    try:
        db.session.delete(order_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that order'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    order = Order.query.get_or_404(id)

    if request.method == 'POST':
        order.customer_name = request.form['customer_name']
        order.order_items = request.form['order_items']
        print(request.form['order_date'])
        order.order_date = request.form['order_date']

        try:
            db.session.commit()
            # print(request.rederrer)
            return redirect('/')
        except:
            return 'There was an issue updating your order'

    else:
        return render_template('update.html', order = order)
    
@app.route('/search', methods=['POST'])
def search():
    
    q = request.form.get('search_query')
    if q:
        orders = Order.query.filter(Order.customer_name.icontains(q)).order_by(Order.order_date).all()
    else:
        orders = Order.query.order_by(Order.order_date).all()

    return render_template('search.html', orders = orders)
        