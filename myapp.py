import streamlit as st
st.set_page_config(page_title='Hemanth')
st.header('Types of Hemanths')

col1, col2, col3 = st.columns(3)
with col1:
  st.subheader("Meanwhile Audiance")
  st.image("Screenshot_20221215_230406.png",caption="Audiance",width=300,use_column_width=True)
  st.write("hemanth is CR")
with col2:
  st.subheader("Persian Hemanth")
  st.image("Screenshot 2023-09-06 155930.png",caption="Persian Hemanth",width=300,use_column_width=True)
  st.write("Persian hemanth is Rocking")
with col3:
  st.subheader("Ragdoll Hemanth")
  st.image("Screenshot 2023-09-06 160040.png",caption="Ragdoll Hemanth",width=300,use_column_width=True)
  st.write("Ragdoll hemanth is pirate")
