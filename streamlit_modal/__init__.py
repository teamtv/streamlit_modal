from contextlib import contextmanager

import streamlit as st
import streamlit.components.v1 as components


def is_open():
    return st.session_state.get('modal_is_open', False)


def open():
    st.session_state.modal_is_open = True
    st.experimental_rerun()


def close():
    st.session_state.modal_is_open = False
    st.experimental_rerun()


@contextmanager
def container(title=None, padding=100):
    st.markdown(
        """
        <style>
        div[data-modal-container='true'] {
            position: fixed;
        }

        div[data-modal-container='true'] h1 a {
            display: none
        }

        div[data-modal-container='true']::before {
                position: fixed;
                content: ' ';
                left: 0;
                right: 0;
                top: 0;
                bottom: 0;
                z-index: 1000;
                background-color: rgba(0, 0, 0, 0.5);
        }

        div[data-modal-container='true'] > div:first-child > div:first-child {
            width: unset !important;
            background-color: #f0f0f0;     
            margin: auto;
            padding: """ + str(padding) + """px;
            margin-top: -""" + str(padding) + """px;
            margin-left: -""" + str(padding) + """px;
            margin-bottom: -""" + str(2 * padding) + """px;
            z-index: 1001;
            border-radius: 5px;
        }
        div[data-modal-container='true'] > div > div:nth-child(2)  {
            z-index: 1003;
            position: absolute;
        }
        div[data-modal-container='true'] > div > div:nth-child(2) > div {
            text-align: right;
        }
        div[data-modal-container='true'] > div > div:nth-child(2) > div > button {
            right: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        _container = st.container()
        if title:
            _container.markdown(f"<h1>{title}</h1>", unsafe_allow_html=True)

        close_ = st.button('X')
        if close_:
            close()

    components.html(
        """
        <script>
        // MODAL
        const iframes = parent.document.body.getElementsByTagName('iframe');
        let container
        for(const iframe of iframes)
        {
          if (iframe.srcdoc.indexOf("MODAL") !== -1) {
            container = iframe.parentNode.previousSibling;
            container.setAttribute('data-modal-container', 'true');
          }
        }
        </script>
        """,
        height=0, width=0
    )

    with _container:
        yield _container
