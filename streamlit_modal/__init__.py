from contextlib import contextmanager

from deprecation import deprecated
import streamlit as st
import streamlit.components.v1 as components

try:
    from streamlit import rerun as rerun  # type: ignore
except ImportError:
    # conditional import for streamlit version <1.27
    from streamlit import experimental_rerun as rerun  # type: ignore


class Modal:

    def __init__(self, title, key, padding=20, max_width=744):
        """
        :param title: title of the Modal shown in the h1
        :param key: unique key identifying this modal instance
        :param padding: padding of the content within the modal
        :param max_width: maximum width this modal should use
        """
        self.title = title
        self.padding = padding
        self.max_width = str(max_width) + "px"
        self.key = key

    def is_open(self):
        return st.session_state.get(f'{self.key}-opened', False)

    def open(self):
        st.session_state[f'{self.key}-opened'] = True
        rerun()

    def close(self, rerun_condition=True):
        st.session_state[f'{self.key}-opened'] = False
        if rerun_condition:
            rerun()

    @contextmanager
    def container(self):
        st.markdown(
            f"""
            <style>
            div[data-modal-container='true'][key='{self.key}'] {{
                position: fixed; 
                width: 100vw !important;
                left: 0;
                z-index: 999992;
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
                max-width: {self.max_width};
            }}

            div[data-modal-container='true'][key='{self.key}'] > div:first-child > div:first-child {{
                width: unset !important;
                background-color: #fff;
                padding: {self.padding}px;
                margin-top: {2*self.padding}px;
                margin-left: -{self.padding}px;
                margin-right: -{self.padding}px;
                margin-bottom: -{2*self.padding}px;
                z-index: 1001;
                border-radius: 5px;
            }}
            div[data-modal-container='true'][key='{self.key}'] > div:first-child > div:first-child > div:first-child  {{
                overflow-y: scroll;
                max-height: 80vh;
                overflow-x: hidden;
                max-width: {self.max_width};
            }}
            
            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2)  {{
                z-index: 1003;
                position: absolute;
            }}
            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2) > div {{
                text-align: right;
                padding-right: {self.padding}px;
                max-width: {self.max_width};
            }}

            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2) > div > button {{
                right: 0;
                margin-top: {2*self.padding + 14}px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        with st.container():
            _container = st.container()
            if self.title:
                _container.markdown(
                    f"<h2>{self.title}</h2>", unsafe_allow_html=True)

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
