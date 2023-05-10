import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/irchamali.svg?logo=github&style=social)](https://github.com/irchamali)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('tiunusia.png'))

st.header('TI UNUSIA')

st.info('Program Studi Teknik Informatika Universitas Nahdlatul Ulama Indonesia')

icon_size = 20

# st_button('linkedin', 'https://www.linkedin.com/in/ircham-ali/', 'Follow me on LinkedIn', icon_size)
st_button('youtube', 'https://www.youtube.com/@unusialabs', 'YouTube', icon_size)
# st_button('medium', 'https://irchamali.medium.com/', 'Read my Medium Blogs', icon_size)
st_button('instagram', 'https://instagram.com/teknikinformatikaunusia/', 'Instagram', icon_size)
st_button('twitter', 'https://twitter.com/teknikinformatikaunusia/', 'Twitter', icon_size)
st_button('facebook', 'https://facebook.com/teknikinformatikaunusia/', 'Facebook', icon_size)
st_button('github', 'https://github.com/unusialabs/', 'GitHub', icon_size)
