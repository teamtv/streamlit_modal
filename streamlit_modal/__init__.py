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
def container():
    with st.container():
        _container = st.container()

    components.html(
        """

        <script>

        // MODAL

        const styles = `
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

                div[data-modal-container='true'] > div:first-child > div {
                    position: fixed !important;
                    background-color: #f0f0f0;
                    padding: 100px;
                    margin: auto;
                    top: 120px;
                    left: 0;
                    right: 0;
                    z-index: 1001;
                    border-radius: 5px;
                }
        `;


        const exists = !!parent.document.querySelector("style[data-modal-css='true']");
        if (!exists) {
        var head = parent.document.head || parent.document.getElementsByTagName('head')[0],
    styleTag = parent.document.createElement('style')

    styleTag.type = 'text/css'
    styleTag.setAttribute("data-modal-css", "true");

    if (styleTag.styleSheet) {
        styleTag.styleSheet.cssText = styles;
    } else {
        styleTag.appendChild(parent.document.createTextNode(styles))
    }

    head.appendChild(styleTag)
}
        //const sheet = parent.document.styleSheets[0];
        //console.log("sheet", sheet);
        //sheet.insertRule(styles, sheet.cssRules.length);

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

        window.addEventListener('unload', () => {
        //   parent.document.body.removeChild(elm);
        });
        </script>
        <body style='background-color: red'>asdsad</body>
        """,
        height=10, width=10
    )

    yield _container

