from flask import Flask,jsonify,request


app=Flask(__name__)

# intitial data in my to-do list
items=[
    {"id":1,"name":"item 1","description":"this is item 1"},
    {"id":2,"name":"item 2","description":"this is item 2"},
]

@app.route("/")
def home():
    return "Welcome to your own personalized To-Do list!"


# get the items
@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)


# get specific items by id
@app.route("/item/<int:item_id>")
def get_item_id(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item==None:
        return jsonify({"Error": "Item not found!"})
    return jsonify(item)


# POST: create a new task
@app.route("/items",methods=["GET","POST"])
def create_item():
    if not request.json or "name" not in request.json:
        return jsonify({"Error":"Missing item"})
    
    new_item={
        "id":items[-1]["id"] + 1 if items else 1,
        "name":request.json["name"],
        "description":request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)


# PUT: updating an existing item
@app.route("/items/<int:item_id>",methods=["PUT"])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id))
    if item==None:
        return jsonify({"Error":"Missing Item entry!"})
    item["name"]=request.json.get("name",item["name"])
    item["description"]=request.json.get("description",item["description"])
    return jsonify(item)


# DELETE: Remove an existing item
@app.route("/items/<int:item_id>",methods=["DELETE"])
def del_item(item_id):
    global items
    items=[item for item in items  if item["id"]!=item_id]
    return jsonify({"Result":"Item Deleted!"})

 
if __name__=="__main__":
    app.run(debug=True)