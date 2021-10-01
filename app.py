from typing import List
from flask import Flask,jsonify,request
app=Flask(__name__)
List=[
    {
        'id':1,
        'name':u'aadi',
        'contact':u'9857891010',
        'done':False
    },
    {
        'id':2,
        'name':u'rahul',
        'contact':u'7655456676 ',
        'done':False
    }
]
@app.route("/")
def helloworld():
    return "hello world!"
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!!!"
        },400)
        
    contact={
        'id':List[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }
    List.append(contact)
    return jsonify({
            "status":"success",
            "message":"Task added successfully!!!"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":List
    })
    
if( __name__=="__main__"):
    app.run(debug=True)
 