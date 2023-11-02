from flask import render_template, url_for, request, redirect, session
from sqlalchemy import desc
from datetime import datetime
from order.models import Order
from order import app, db
from order.services import *


@app.route('/', methods = ['POST', 'GET'])
def index():
    # print(request.method)
    if request.method == 'POST':
        # new_order = Order(customer_name=request.form['customer_name'], order_items=request.form['order_items'], order_date=request.form['order_date'])
        
        customer = request.form['customer_name'] 
        items = request.form['order_items']
        num_items = request.form['items_number']
        date = request.form['order_date'] if request.form['order_date'] else datetime.utcnow().strftime('%Y-%m-%d')
        
        session['form_data'] = {
            'customer': customer,
            'items': items,
            'num_items': num_items,
            'date': date
        }

        orders = order_precess(items)
        print(f'items = {items}')
        print(f'num_items = {num_items}')
        
        len1 = len(items.strip().split(','))
        len2 = len(num_items.strip().split('.'))
        print(len1, len2)

        # new_order = Order(customer=customer, items=items, date=date)
        # print(new_order.customer, new_order.items, new_order.date)
        try:
            if len1 != len2:
                raise Exception('Number of items not match')
            new_order = Order(customer=customer, item=items, num_item=num_items, date=date)
            db.session.add(new_order)
            db.session.commit()
            # db.session.add(new_order)
            # db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"An error occurred: {e}")
            return 'There was an issue adding your order'
    else:
        orders = Order.query.order_by(desc(Order.date)).all()
        form_data = session.get('form_data', {
            'customer': '',
            'items': '',
            'num_items': '',
            'date': ''
        })
        return render_template('index.html', orders = orders, form_data=form_data)

    
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
        order.customer = request.form['customer_name']
        order.item = request.form['order_item']
        order.num_item = request.form['items_number']
        # print(request.form['order_date'])
        order.date = request.form['order_date']

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
        orders = Order.query.filter(Order.customer.icontains(q) | Order.date.icontains(q)).order_by(Order.date).all()
    else:
        orders = Order.query.order_by(Order.date).all()

    return render_template('search.html', orders = orders)
        