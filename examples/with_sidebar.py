import streamlit as st
from streamlit_modal import Modal

import streamlit.components.v1 as components

modal = Modal("Demo Modal", key="demo-modal")
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        for i in range(100):
            st.write(f"Text goes here {i}")

        html_string = '''
        <h1>HTML string in RED</h1>

        <script language="javascript">
          document.querySelector("h1").style.color = "red";
        </script>
        '''
        components.html(html_string)

        st.write("Some fancy text")
        value = st.checkbox("Check me")
        st.write(f"Checkbox checked: {value}")

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )