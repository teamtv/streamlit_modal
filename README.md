# Streamlit modal

Modal support for streamlit. The hackish way.

## Example

```python
import streamlit as st
import streamlit_modal as modal


open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container() as container:
        container.write("Text goes here")
        container.video("https://youtu.be/_T8LGqJtuGc")
        container.write("Some fancy text")
        value = container.checkbox("blaat")
        container.write(value)
        close = container.button("Close modal")
        if close:
            modal.close()

```

## Install

```shell script
pip install streamlit-modal
```