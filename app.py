from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('loan_model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            features = [float(request.form.get(key)) for key in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                                                                 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
                                                                 'Credit_History', 'Property_Area']]
            prediction = model.predict([features])
            result = 'Loan Approved' if prediction[0] == 1 else 'Loan Rejected'
            return render_template('index.html', prediction_text=result)
        except:
            return render_template('index.html', prediction_text='Error in input. Please check your values.')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
