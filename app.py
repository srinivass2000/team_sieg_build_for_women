from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('investment_pred_model.pkl', 'rb'))
ct = pickle.load(open('investment_pred_model_ct.pkl', 'rb'))
model2 = pickle.load(open('model2.pkl', 'rb'))
ct2 = pickle.load(open('model2_ct.pkl', 'rb'))


# Flask constructor 
app = Flask(__name__)    


@app.route('/')
def main():
    return render_template('investment.html')

@app.route('/register')
def register():
    return render_template('form.html')

@app.route('/investment')
def invest():
    return render_template('investment.html')
    
@app.route('/salary')
def salary():
    return render_template('salary.html')

@app.route('/joinus')
def joinus():
    return render_template('joining.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form.get("a") 
    print(data1)
    data2 = request.form.get("b") 
    print(data2)
    data3 = request.form.get("c")
    print(data3)
    arr = np.array([[data1, data2, data3]])
    arre=ct.transform(arr)
    pred = model.predict(arre)
    print(pred)
    # print(type(pred))
    print(pred[0])
    p=round(pred[0],2)
    print(p)
    k="Looks like you will need a investment of"
    return render_template('after.html',p=p*4000,k=k);

@app.route('/predict2', methods=['POST'])
def home2():
    data1 = request.form.get("a") 
    data2 = request.form.get("b") 
    data3 = request.form.get("c")
    data4=request.form.get("d")
    arr = np.array([[data1, data2, data3,data4]])
    arre=ct2.transform(arr)
    pred = model2.predict(arre)
    print(pred)
    # print(type(pred))
    print(pred[0])
    p=round(pred[0],2)
    print(p)
    print(p*7)
    p=round(p*7,1)
    k="Your estimated Annual salary is :"
    return render_template('after.html',p=p,k=k)



@app.route('/reg', methods=['POST'])
def reg():
    name = request.form.get("name")  
    email = request.form.get("email")  
    return render_template("success.html",name=name,email=email) 
  

if __name__ == "__main__":
    app.run(debug=True)















