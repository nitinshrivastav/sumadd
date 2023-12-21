from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/add',methods=['GET'])
def jkfjk():
    try:
        a=int(request.args.get('num1'))
        b=int(request.args.get('num2'))
        t=a-b
    except:
        return jsonify({'Error':'invalid Data'})
    return jsonify({'Answer':t})