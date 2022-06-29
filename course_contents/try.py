from flask import Flask ,jsonify,request,render_template

app=Flask(__name__,template_folder='templates')
app.config['JSONIFY_PRETTYPRINT_REGULAR']=True

stores=[
           {
                'name':'saibaba',
                'items': [
                     
                      { 'name' :'chips',
                       'price': 5.99
                     }
                     ]
              
            }
       ]

@app.route('/')
def home():
    return render_template('index.html')
#post for store {name}


@app.route('/store',methods=['POST'])
def create_store():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'item':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#get store
@app.route('/store/<string:name>')#method of flask 
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({"message":"not founds" })

@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})

#post /store/<string:name>/item{name,prise}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_itemin_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'prise':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'not found'})
   
#get store
@app.route('/store/<string:name>/item')#method of flask 
def get_itemin_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})


app.run(port=4999)