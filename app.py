from flask import Flask,request ,render_template

app=Flask(__name__)

@app.route("/")
def calculator():
    return render_template("index.html")

@app.route("/calculate",methods=["POST"])
def calculate():
    num1=float(request.form['num1'])
    num2=float(request.form['num2'])

    operation = request.form['operation']

    if operation=='add':
        res=num1+num2
    elif operation=='subtract':
        res=num1-num2
    elif operation=='multiply':
        res=num1*num2
    elif operation=='divide':
        if num2==0:
            return "Division by zero error"
        res=num1/num2
    else:
        return "Invalid Operation"
    return f"Result:{res}"

if __name__=='__main__':
    app.run(debug=True)
    