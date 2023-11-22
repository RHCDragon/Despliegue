from flask import Flask, jsonify, request
app = Flask (__name__)
from Database import db

@app.route('(ping')
def ping():
    return jsonify({"message":"pong, Hay conexion"})

@app.route ('/iceCreams')
def getProducts():
    return jsonify(["iceCreams": Database])

@app.route ('/iceCreams/<string:name')
def get(name):
    ictotal = [ic for ic in db if ic ['sabor']==name]
    if (len(ictotal)>0):
        return jsonify({"": ictotal[0]})
    return jsonify({"mensaje": "Not found"})

@app.route('/IceCreams', methods = ['POST'])
def addIC():
    newIC = {
        "sabor": request.json['sabor'],
        "precio": request.json['precio'],
        "tamaño": request.json['tamaño'],
        "cantidad": request.json['cantidad']
    }
    db.append(new_product)
    return jsonify("IceCreams": db, "mensaje": "Helado creado")

@app.route('/IceCreams/<string:name>', methods = ['PUT'])
def editIC(ic_name):
    ictotal = [ic for ic in db if ic ['sabor']==name]
    if(len(ictotal)>0):
        ictotal[0]['sabor'] = request.json['sabor']
        ictotal[0]['precio'] = request.json['precio']
        ictotal[0]['tamano'] = request.json['tamano']
        ictotal[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            "mensaje": "Helaso Actualizado",
            "": ictotal[0]
        })
    return jsonify("mesnaje": "Not found")

@app.route('/IceCreams/<string:name>', methods = ['DELETE'])
def deleteIC(ic_name):
    ictotal = [ic for ic in db if ic ['sabor']==name]
    if(len(ictotal)>0):
        db.remove(ictotal[0])
        return jsonify({
            "mensaje": "Helado Eliminado",
            "": db
        })
    return jsonify({"mensaje:" "Not found"})

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8080 )