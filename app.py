import streamlit as st
view=[100,150,30] # 동영상 조회수를 웹으로 출력하고 싶음
st.write('# youtube view')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview=pd.Series(view)
sview