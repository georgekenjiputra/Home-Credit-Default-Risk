import streamlit as st
import pandas as pd
import pickle

st.title("Default Risk Prediction for Customer")

# Import model
model = pickle.load(open("model.pkl", "rb"))

st.write('Please choose how to input your information:')

input_option = st.radio('Input Option', ('Manual Input', 'Upload File'))

if input_option == 'Manual Input':
    st.write('Please fill in your information:')
    
    # User input
    nit = st.selectbox(label='From where is your source of income?', options=['Working', 'State servant', 'Commercial associate',
                                                                             'Pensioner', 'Unemployed', 'Student', 'Businessman',
                                                                             'Maternity leave'])
    org = st.selectbox(label='What is your organization type?', options=
        ['Business Entity Type 3', 'School', 'Government', 'Religion', 'XNA', 'Electricity', 'Medicine',
       'Business Entity Type 2', 'Self-employed', 'Transport: type 2', 'Construction', 'Housing', 'Kindergarten',
       'Trade: type 7', 'Industry: type 11', 'Military', 'Services', 'Security Ministries', 'Transport: type 4',
       'Industry: type 1', 'Emergency', 'Security', 'Trade: type 2', 'University', 'Transport: type 3', 'Police',
       'Business Entity Type 1', 'Postal', 'Industry: type 4', 'Agriculture', 'Restaurant', 'Culture', 'Hotel',
       'Industry: type 7', 'Trade: type 3', 'Industry: type 3', 'Bank', 'Industry: type 9', 'Insurance', 'Trade: type 6',
       'Industry: type 2', 'Transport: type 1', 'Industry: type 12', 'Mobile', 'Trade: type 1', 'Industry: type 5',
       'Industry: type 10', 'Legal Services', 'Advertising', 'Trade: type 5', 'Cleaning', 'Industry: type 13',
       'Trade: type 4', 'Telecom', 'Industry: type 8', 'Realtor', 'Industry: type 6', 'Other'])
    occ = st.selectbox(label='What is your occupation type?', options=
        ['Laborers', 'Core staff', 'Accountants', 'Managers', 'Drivers', 'Sales staff', 'Cleaning staff', 'Cooking staff',
       'Private service staff', 'Medicine staff', 'Security staff', 'High skill tech staff', 'Waiters/barmen staff',
       'Low-skill Laborers', 'Realty agents', 'Secretaries', 'IT staff','HR staff', 'Others'])
    xs3 = st.number_input(label='Enter your third external source:', min_value=0.00000, max_value=0.99999, value=0.00000, step=0.00001)
    xs2 = st.number_input(label='Enter your second external source:', min_value=0.00000, max_value=0.99999, value=0.00000, step=0.00001)
    dbh = st.number_input(label='How old are you in days?:', min_value=-99999, max_value=0, value=-10000, step=1)
    acr = st.number_input(label='How much is your amount credit?:', min_value=0, max_value=9999999, value=100000, step=1)
    ait = st.number_input(label='How much is your amount income in total?:', min_value=0, max_value=999999999, value=1000000, step=1)
    cip = acr / ait
    ama = st.number_input(label='How much is your amount annuity?:', min_value=0.0, max_value=999999.9, value=10000.0, step=0.1)
    aip = ama / ait
    crt = ama / acr
    dem = st.number_input(label='How long have you been working in days?:', value=10000, step=1)
    dep = dem / dbh

    # Convert into dataframe
    data = pd.DataFrame({'name_income_type': [nit],
                         'organization_type': [org],
                         'occupation_type': [occ],
                         'ext_source_3': [xs3],
                         'ext_source_2': [xs2],
                         'days_birth': [dbh],
                         'credit_income_percent': [cip],
                         'annuity_income_percent': [aip],
                         'credit_term': [crt],
                         'days_employed_percent': [dep]
                         })

    # Prediction
    if st.button('Predict'):
        prediction = model.predict(data).tolist()[0]

        if prediction == 0:
            prediction = 'Congratulations, this person is most likely to pay!'
        else:
            prediction = 'Too bad, this person may not be able to pay!'

        st.write('Prediction result:')
        st.write(prediction)

else:
    uploaded_file = st.file_uploader('Upload CSV file', type='csv')

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write('Data uploaded successfully!')

        if st.button('Predict'):
            predictions = model.predict(data)
            result_data = pd.DataFrame({'SK_ID_CURR': data['sk_id_curr'], 'TARGET': predictions})
            st.write('Prediction result:')
            st.dataframe(result_data)