import streamlit as st
st.set_page_config(page_title='Hemanth')
st.header('Types of Hemanths')

col1, col2 = st.columns(2)
with col1:
  st.subheader("Persian Hemanth")
  st.image("Screenshot 2023-09-06 155930.png",caption="Persian Hemanth",width=300,use_column_width=True)
  st.write("Persian hemanth is Rocking")
with col2:
  st.subheader("Ragdoll Hemanth")
  st.image("Screenshot 2023-09-06 160040.png",caption="Ragdoll Hemanth",width=300,use_column_width=True)
  st.write("Ragdoll hemanth is pirate")
