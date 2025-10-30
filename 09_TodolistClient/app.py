import streamlit as st
import requests


BASE_URL="http://localhost:8000"


def login():
    st.title("Login")
    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password",type="password")
        submit = st.form_submit_button("Login")
        if submit:
            #  POST http://127.0.0.1:8000/users/authenticate
            response = requests.post(BASE_URL+"/users/authenticate", json={
                "name":username,
                "password":password
            })
            if response.status_code==200:
                user_data= response.json()
                st.session_state["user"]=user_data
                st.success(f"Wilkommen, {user_data['name']}")
                st.session_state['logged_in']=True
                st.rerun()
            else:
                st.error("Name oder Passwort falsch!")

def welcome():
    user = st.session_state.get('user')
    st.title(f"Wilkommen, {user['name']}")


def main():
    if "logged_in" not in st.session_state:
        st.session_state['logged_in']=False
    if st.session_state['logged_in']:
        welcome()
    else:
        login()
if __name__=="__main__":
    main()