import streamlit as st
from pathlib import Path
from PIL import Image

#st.sidebar('Side')
st.sidebar.title('PG INTERVIEW')
st.markdown('''	## Mizan''')
st.markdown('''	### Mizan''')
st.markdown('''	** Mizanur ** _ Rahman _''')
st.write(' ** Mizanur ** _ Rahman _ ')
st.write(' ** Mizanur  _ Rahman _ **')
st.write('__ Mizanur __ _ Rahman _')

st.button('Click Me')
if st.button('Click Me here'):
	st.text('You have clicked!')

name = st.text_input('Name:')
st.write(name)
st.markdown('''Enter your `Address:`''')
st.text_area('')


st.date_input('Enter a Date:')
st.time_input('Enter a Time:')
st.number_input('Enter a value:',  min_value = 20.0, max_value = 50.0, step = 5.0)

if st.checkbox('EE', value = True):
	st.write('EE Division')

radio_button = st.radio('Divisions:', ['EE', 'CT', 'HTC', 'UDL'], index = 0)
st.write(f'{radio_button} Division')

img_path = Path(r"C:\Users\mizan\Documents\MEGA\MEGA _ Academic\PYTHON\Practice\PG_Interview Dashboard\Script\B-001_S-10349_P-01_Q-01.jpg")
img = Image.open(img_path)
st.image(img, width = 600, caption = 'Figure 01')

img = st.file_uploader('Upload a File:')
if img:
	st.image(img) 

box_multi = st.multiselect('Divisions:', ['EE', 'CT', 'HTC', 'UDL'])
st.write(f'{box_multi} Division')

box = st.selectbox('Divisions:', ['EE', 'CT', 'HTC', 'UDL'], index = 0)
st.write(f'{box} Division')

mark_soi = st.slider('SoI Mark', min_value = 0, max_value = 10, step = 1)
st.write(f'SoI:    {mark_soi}')

mark_interview = st.slider('Interview Mark', min_value = 0, max_value = 10, step = 1)
st.write(f'Interview:  {mark_interview}')

mark_portfolio = st.slider('Portfolio Mark', min_value = 0, max_value = 10, step = 1)
st.write(f'Portfolio:    {mark_portfolio}')

cal = (int(mark_soi) + int(mark_portfolio) + int(mark_interview))/3 
cal_round = round(cal, 2)
st.text(f'Total Mark:    {cal_round}')

#st.help(st.button)