from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x:x[item] == name,items),None)
        return {"item":item} ,200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x[item] == name, items), None) not None :
            return {"message": "item with {} already exists".format(name)},400
        data = request.get_jsion()
        item = {"name": data["name"], "price": data["price"]}
        items.append(item)
        return {"student": name}
class Itemlist(Resource):
    def get(self):
        return {"items": items}

api.add_resource(Item, "/item/<string:name>")
api.add_resource(Itemlist,"/item")
app.run(debug=True)
