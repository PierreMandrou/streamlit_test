import streamlit as st

def session():
    st.header("Streamlit Session tutorial")
    # Initialization
    if 'counter' not in st.session_state:
        st.session_state['counter'] = 0
    not_a_session_value = 0

    if st.button('click on me'):
        st.session_state['counter'] += 1
        not_a_session_value += 1
    
    st.write(st.session_state.counter, ' : This a session state value !')
    st.write(not_a_session_value, ' : This is not a session state value !')

if __name__ == "__main__":
    
    st.set_page_config(
        page_title="streamlit advanced features",
        layout="centered"
    )
    st.title("Pierre Mandrou was here.")

    st.title("Streamlit advanced features")

    session()
