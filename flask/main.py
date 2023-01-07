from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY']='32q3428rewp0hjnq288Q28Q28Q2N7J32018R3vcnvcxnx2'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(15), nullable=False)
    price=db.Column(db.Integer, nullable=False)
    discription=db.Column(db.String(100), nullable=False)
    image=db.Column(db.String(100), nullable=False)
@app.route('/', methods=['POST', 'GET'])
def index():
    item=Item.query.order_by(Item.price).all()
    return render_template('index.html', data=item)
    if 'cart' not in session:
        session['cart'] = []
    if request.method=='POST':
        session['cart'] += [{
            'title':request.form['title'],
            'price':request.form['price'],
            'cout':1,
        }]
        cart=session['cart'](title=title, price=price) 
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/cart')
def cart():
    return render_template('cart.html', cart=session['cart'])
@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method=='POST':
        title=request.form['title']
        price=request.form['price']
        discription=request.form['discription']
        image=request.form['image']
        item=Item(title=title, price=price, discription=discription, image=image)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'АСИПКА'
    else: 
        return render_template('create.html')   
if __name__ == '__main__':
    app.run(debug=True)