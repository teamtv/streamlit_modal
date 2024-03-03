# Streamlit modal

Modal support for streamlit. The hackish way.

## Example

### With default close button

```python
import streamlit as st
from streamlit_modal import Modal

import streamlit.components.v1 as components


modal = Modal(
    "Demo Modal", 
    key="demo-modal",
    
    # Optional
    padding=20,    # default value
    max_width=744,  # default value
    include_close=True
)
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")

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
```

### With own close button

```python
modal = Modal(
    "Demo Modal", 
    key="demo-modal",
    include_close=False
)
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")
        
        exit = st.button("Exit", key="demo-modal-close-button")
        if test:
            st.session_state[f'demo-modal'] = False
            st.rerun()
```

## Install

```shell script
pip install streamlit-modal
```
