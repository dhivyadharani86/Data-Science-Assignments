import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 
import streamlit.web.cli as stcli


# loading in the model to predict on the data 
# pickle_in = open('D:\OneDrive - Excelra Knowledge Solutions Pvt Ltd\Desktop\Data Science Assignments\SolarPower_Project\lgbm_reg.pkl', 'rb') 
pickle_in = open('SolarPower_Project/classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in) 

def welcome(): 
	return 'welcome all'

# defining the function which will make the prediction using 
# the data which the user inputs 
# distance-to-solar-noon	temperature	wind-direction	wind-speed	sky-cover	visibility	humidity	average-wind-speed-(period)	average-pressure-(period)
def prediction(distance_to_solar_noon, temperature,	wind_direction,wind_speed, sky_cover, visibility,humidity,average_wind_speed_period,average_pressure_period): 

	prediction = classifier.predict( 
		[[distance_to_solar_noon, temperature,	wind_direction,wind_speed, sky_cover, visibility,humidity,average_wind_speed_period,average_pressure_period]]) 
	print(prediction) 
	return prediction 
	

# this is the main function in which we define our webpage 
def main(): 
	# giving the webpage a title 
	st.title("Solar Power Prediction Team 5") 
	
	# here we define some of the front end elements of the web page like 
	# the font and background color, the padding and the text to be displayed 
	html_temp = """ 
	<div style ="background-color:yellow;padding:13px"> 
	<h1 style ="color:black;text-align:center;">Streamlit Solar Power Prediction ML App </h1> 
	</div> 
	"""
	
	# this line allows us to display the front end aspects we have 
	# defined in the above code 
	st.markdown(html_temp, unsafe_allow_html = True) 
	
	# the following lines create text boxes in which the user can enter 
	# the data required to make the prediction
	# st.slider("Please select a rating range", 0, 300)
	# distance_to_solar_noon =st.slider("Please select a rating range", 0, 1)
	distance_to_solar_noon = st.text_input("Distance_to_solar_noon", "Type Here") 
	temperature = st.text_input("Temperature", "Type Here") 
	wind_direction = st.text_input("Wind_direction", "Type Here") 
	wind_speed = st.text_input("Wind speed", "Type Here") 	
	sky_cover = st.text_input("Sky_cover", "Type Here") 
	visibility = st.text_input("Visibility", "Type Here") 
	humidity= st.text_input("Humidity", "Type Here") 
	average_wind_speed_period= st.text_input("Average_wind_speed_period", "Type Here") 
	average_pressure_period= st.text_input("Average_pressure_period", "Type Here") 
	result ="" 
	
	# the below line ensures that when the button called 'Predict' is clicked, 
	# the prediction function defined above is called to make the prediction 
	# and store it in the variable result 
	if st.button("Predict"): 
		result = prediction(distance_to_solar_noon, temperature,	wind_direction,wind_speed, sky_cover, visibility,humidity,average_wind_speed_period,average_pressure_period) 
	st.success('The output is {}'.format(result)) 
	
if __name__=='__main__': 
	main() 
