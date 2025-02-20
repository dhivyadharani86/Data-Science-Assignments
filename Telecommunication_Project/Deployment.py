import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image


# Load the model
# loading in the model to predict on the data 
pickle_in = open("D:\OneDrive - Excelra Knowledge Solutions Pvt Ltd\Desktop\Data Science Assignments\Telecommunication_Project\lgb_clf.pkl", "rb")
lgb_clf = pickle.load(pickle_in)
pickle_in.close()


# Streamlit App
st.header("Telecommunication churn project")


def welcome(): 
        return 'welcome all'


# Sidebar for input values
with st.sidebar:
    st.header("Input Parameters")
    account_length = st.slider("Account length (Customers)",0,250,65)
    voice_mail_plan = st.slider ("Voice mail plan (Status)",0,1,0)
    voice_mail_messages = st.slider ("Voice mail messages (Text messages)",0,60,0)
    day_mins = st.slider ("Day mins (Chit-chat)",0.0,360.0,129.1)
    evening_mins = st.slider ("Evening mins (Breakfree)",0.0,363.7,185.5)
    night_mins = st.slider ("Night mins (Booring)",23.2,395.0,154.1)
    international_mins = st.slider ("Internatioanl mins (Moodsetting)",0.0,20.0,15.4)
    customer_service_calls = st.slider ("customer service calls (Torture)",0,9,5)
    international_plan = st.slider ("International plan (Expensive)",0,1,1)
    day_calls = st.slider ("Day calls (morning masala)",0,165,145)
    day_charge = st.slider ("Day charge",0.00,59.64,25.50)
    evening_calls = st.slider("Evening calls (Soothy snacks)",0,170,150)
    evening_charge = st.slider ("Evening charge",0.00,30.91,29.00)
    night_calls = st.slider ("Night calls (Naughty drinks)",33,175,155)
    night_charge = st.slider ("Night charge",1.04,17.77,16.50)
    international_calls = st.slider ("International calls (Foreign site)",0,20,15)
    international_charge = st.slider ("International charge",0.0,5.4,2.5)
    total_charge = st.slider ("Total charge (Budget branch)",22.93,96.15,30.00)
result =""




# Create an input array for the model
input_data = np.array([[
    account_length,
    voice_mail_plan,
    voice_mail_messages,
    day_mins,
    evening_mins,
    night_mins,
    international_mins, 
    customer_service_calls,
    international_plan,
    day_calls,
    day_charge, 
    evening_calls,
    evening_charge, 
    night_calls,
    night_charge, 
    international_calls, 
    international_charge, 
    total_charge ]])




# Prediction button
# defining the function which will make the prediction using 
# the data which the user inputs 
def prediction (account_length, voice_mail_plan,voice_mail_messages,day_mins,evening_mins,night_mins,international_mins, customer_service_calls,international_plan,day_calls,day_charge, evening_calls,evening_charge, night_calls,night_charge, international_calls, international_charge, total_charge
                                        ):
        prediction = lgb_clf.predict (
                    [[account_length, voice_mail_plan, voice_mail_messages,day_mins,evening_mins,night_mins,international_mins, customer_service_calls,international_plan,day_calls,day_charge, evening_calls,evening_charge, night_calls,night_charge, international_calls, international_charge, total_charge
                    ]]) 
        print(prediction) 
        return prediction 


        
# this is the main function in which we define our webpage 
def main(): 
        # giving the webpage a title 
        st.subheader("Customer churn team 3") 
        
        # here we define some of the front end elements of the web page like 
        # the font and background color, the padding and the text to be displayed 
html_temp = """ 
        <marquee><div style ="background-color:white;padding:3px"> 
        <h3 style ="color:green;text-align:center;">Churn classification ML app </h3> 
        </div></marquee> 
        """
        


        # this line allows us to display the front end aspects we have 
        # defined in the above code 
st.markdown(html_temp, unsafe_allow_html = True) 
    
        # the below line ensures that when the button called 'Predict' is clicked, 
        # the prediction function defined above is called to make the prediction 
        # and store it in the variable result 
if st.button("Predict"): 
                result = prediction(account_length,voice_mail_plan,voice_mail_messages,day_mins,evening_mins,night_mins,international_mins, customer_service_calls,international_plan,day_calls,day_charge, evening_calls,evening_charge, night_calls,night_charge, international_calls, international_charge, total_charge) 
st.success('The client is still in the company or not (1-Churn, 0-No Churn) === {}'
                   .format(result)) 
        
if __name__=='__main__': 
        main()