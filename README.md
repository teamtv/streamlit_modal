# Streamlit modal

Modal support for streamlit. The hackish way.

## Example

```python
import time

import streamlit as st
import streamlit.components.v1 as components

import streamlit_modal as modal


open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")
        st.video("https://youtu.be/_T8LGqJtuGc")
        components.html("<h1>HTML string in RED</h1>")
        st.write("Some fancy text")
        value = st.checkbox("blaat")
        st.write(value)
        close = st.button("Close modal")
        if close:
            modal.close()

```

## Install

```shell script
pip install streamlit-modal
```
