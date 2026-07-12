import streamlit as st

from views import login, register, dashboard, admin, upload, search, history


st.set_page_config(
    page_title="AI Legal Risk Analyzer",
    page_icon="⚖️",
    layout="wide",
)

# ---------- Session Initialization ----------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "email" not in st.session_state:
    st.session_state.email = None

if "role" not in st.session_state:
    st.session_state.role = None

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

# ---------- Current Page ----------

page = st.session_state.current_page

# Routing

if page == "login":
    login.show()

elif page == "register":
    register.show()

elif page == "dashboard":
    dashboard.show()
    
elif page == "admin":
    admin.show()
elif page == "upload":
    upload.show()   

elif page == "search":
    search.show()
    
elif page == "history":

    history.show()