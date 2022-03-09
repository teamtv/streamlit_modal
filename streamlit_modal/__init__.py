from uuid import uuid4
from contextlib import contextmanager

from deprecation import deprecated
import streamlit as st
import streamlit.components.v1 as components


class Modal:

    def __init__(self, title, padding=100, max_width=None, key=None):
        self.title = title
        self.padding = padding
        self.max_width = max_width
        self.key = key or f'streamlit-modal-{uuid4().hex}'

    def is_open(self):
        return st.session_state.get(f'{self.key}-opened', False)

    def open(self):
        st.session_state[f'{self.key}-opened'] = True
        st.experimental_rerun()

    def close(self):
        st.session_state[f'{self.key}-opened'] = False
        st.experimental_rerun()

    @contextmanager
    def container(self):
        if self.max_width:
            max_width = str(self.max_width) + "px"
        else:
            max_width = 'unset'

        st.markdown(
            f"""
            <style>
            div[data-modal-container='true'][key='{self.key}'] {{
                position: fixed;
                width: 100vw !important;
                left: 0;
                z-index: 1001;
            }}

            div[data-modal-container='true'][key='{self.key}'] > div:first-child {{
                margin: auto;
            }}

            div[data-modal-container='true'][key='{self.key}'] h1 a {{
                display: none
            }}

            div[data-modal-container='true'][key='{self.key}']::before {{
                    position: fixed;
                    content: ' ';
                    left: 0;
                    right: 0;
                    top: 0;
                    bottom: 0;
                    z-index: 1000;
                    background-color: rgba(0, 0, 0, 0.5);
            }}
            div[data-modal-container='true'][key='{self.key}'] > div:first-child {{
                max-width: {max_width};
            }}

            div[data-modal-container='true'][key='{self.key}'] > div:first-child > div:first-child {{
                width: unset !important;
                background-color: #fff;     
                padding: {self.padding}px;
                margin-top: -{self.padding}px;
                margin-left: -{self.padding}px;
                margin-bottom: -{2*self.padding}px;
                z-index: 1001;
                border-radius: 5px;
            }}
            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2)  {{
                z-index: 1003;
                position: absolute;
            }}
            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2) > div {{
                text-align: right;
                padding-right: {self.padding}px;
                max-width: {max_width};
            }}

            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2) > div > button {{
                right: 0;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        with st.container():
            _container = st.container()
            if self.title:
                _container.markdown(
                    f"<h1>{self.title}</h1>", unsafe_allow_html=True)

            close_ = st.button('X', key=f'{self.key}-close')
            if close_:
                self.close()

        components.html(
            f"""
            <script>
            // STREAMLIT-MODAL-IFRAME-{self.key} <- Don't remove this comment. It's used to find our iframe
            const iframes = parent.document.body.getElementsByTagName('iframe');
            let container
            for(const iframe of iframes)
            {{
            if (iframe.srcdoc.indexOf("STREAMLIT-MODAL-IFRAME-{self.key}") !== -1) {{
                container = iframe.parentNode.previousSibling;
                container.setAttribute('data-modal-container', 'true');
                container.setAttribute('key', '{self.key}');
            }}
            }}
            </script>
            """,
            height=0, width=0
        )

        with _container:
            yield _container


# keep compatible with old api

_default_modal = Modal('', key='streamlit-modal-default')

@deprecated(deprecated_in="0.1.0", removed_in="1.0.0",
                        current_version='0.1.0',
                        details="Use the `Modal().is_open()` instead")
def is_open():
    return _default_modal.is_open()

@deprecated(deprecated_in="0.1.0", removed_in="1.0.0",
                        current_version='0.1.0',
                        details="Use the `Modal().open()` instead")
def open():  # pylint: disable=redefined-builtin
    return _default_modal.open()

@deprecated(deprecated_in="0.1.0", removed_in="1.0.0",
                        current_version='0.1.0',
                        details="Use the `Modal().close()` instead")
def close():
    return _default_modal.close()


@contextmanager
@deprecated(deprecated_in="0.1.0", removed_in="1.0.0",
                        current_version='0.1.0',
                        details="Use the `Modal().container()` instead")
def container(title=None, padding=100, max_width=None):
    _default_modal.title = title
    _default_modal.padding = padding
    _default_modal.max_width = max_width
    with _default_modal.container() as _container:
        yield [_container]
