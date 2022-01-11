# Streamlit modal

Modal support for streamlit. The hackish way.

## Example

```python
import streamlit as st
import streamlit_modal as modal

import streamlit.components.v1 as components


open_modal = st.button("Open")
if open_modal:
    modal.open()
    st.session_state.modal_open = True

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
        st.write(value)
        close = st.button("Close modal")
        if close:
            modal.close()

```

## Install

```shell script
pip install streamlit-modal
```
