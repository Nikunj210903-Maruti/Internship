from flask import *

app=Flask(__name__,template_folder='template')

dict={}
@app.route('/')
def fun1():
    return render_template('index.html')

@app.route('/add',methods=['POST','GET'])
def fun2():
    if request.method=='POST':
        dict[request.form["key"]]=request.form["value"]
        print(dict)
    return render_template('index.html')


@app.route('/print')
def fun3():
    return str(dict)
        
if __name__=="__main__":
    app.run(debug=True)
    