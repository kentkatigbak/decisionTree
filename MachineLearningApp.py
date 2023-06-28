# Import Libraries

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import webbrowser

# Page configurations

st.set_page_config(page_title="ML-DT KentKatigbak", layout="wide", initial_sidebar_state="expanded")

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("""
        <style>
            .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
            .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

# App
st.title("Machine Learning Web Application")
choice = option_menu(
    menu_title=None,
    options=["About App", "Decision Tree", "Developer"],
    #icons=["None" ,"linkedin", "facebook", "instagram", "twitter", "stickies"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "lightgray"},
        "icon": {"color": "black", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "darkgray"},
        "nav-link-selected": {"background-color": "#c1502e"},
    }
)

# About App
if choice == "About App":
    st.title("Machine Learning Web Application")
    st.header("Decision Tree Model")

# Developer
if choice == "Developer":
    devCol1, devCol2 = st.columns([1.5, 2])

    with devCol1:
        st.image("logo_kent.png")
    with devCol2:
        st.markdown("""
                    <h1 class = title1>
                        Kent Jym B. Katigbak
                    </h1>
                    <h4 class = subtitle1>
                        - Industrial Engineer
                    </h4>
                    <h4 class = subtitle1>
                        - Certified Lean Six Sigma Yellow Belt
                    </h4>
                    <h4 class = subtitle1>
                        - Safety Officer 2
                    </h4>
                    <h4 class = subtitle1>
                        - Planning Management Fundamentals Certified
                    </h4>
                    <h4 class = subtitle1>
                        - Continuous Improvement Fundamentals Certified
                    </h4>
                    <h4 class = subtitle1>
                        - Data Science Fundamentals Certified
                    </h4>
                    <h4 class = subtitle1>
                        - Data Analyst
                    </h4>
                    <h4 class = subtitle1>
                        - Python Programmer
                    </h4>
                    <style>
                        .title1 {
                        padding-bottom: 3rem;
                    }
                        .subtitle1 {
                        padding-top: 0rem;
                        padding-right: 0rem;
                        padding-bottom: 1rem;
                        font-style: italic;
                    }
            </style>
            """, unsafe_allow_html=True)
    
    linkedin = "https://www.linkedin.com/in/kentjk/"
    facebok = "https://www.facebook.com/kntktgbk"
    instagram = "https://www.instagram.com/kentjk_/"
    twitter = "https://twitter.com/kentjk_"
    
    socials = option_menu(
        menu_title=None,
        options=["Let's Connect!", "Linkedin", "Facebook", "Instagram", "Twitter"],
        icons=["person-plus-fill", "linkedin", "facebook", "instagram", "twitter"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "lightgray"},
            "icon": {"color": "black", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "darkgray"},
            "nav-link-selected": {"background-color": "#c1502e"},
        }
    )
    
    if socials == "Linkedin":
        webbrowser.open_new_tab(linkedin)
    if socials == "Facebook":
        webbrowser.open_new_tab(facebok)
    if socials == "Instagram":
        webbrowser.open_new_tab(instagram)
    if socials == "Twitter":
        webbrowser.open_new_tab(twitter)
    if socials == "Download Resume":
        st.subheader("You are about to save a PDF copy of my resume")
        resume = open("Resume - Katigbak, Kent Jym.pdf", "rb")
        st.download_button("Proceed to download", resume, file_name="KentJymKatigbak_Resume.pdf", mime="pdf")


# Machine Learning

if choice == "Decision Tree":
    st.title("Machine Learning Using Decision Tree Algorithm")
    st.write("__________________________________")
    st.subheader("Start by uploading a dataframe.")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Display uploaded dataframe
        st.subheader("Preview of uploaded dataframe")
        st.dataframe(df)
        st.write("__________________________________")
        
        # Selecting number of desired inputs
        st.subheader("Separate dataframe into INPUTS and OUTPUT")
        input_qty = st.slider("Select number of inputs",
                            min_value=1,
                            max_value=5,
                            step=1)
        
        if input_qty == 1:
            
            # Seperate dataframe into INPUTS and OUTPUT
            input_column = st.multiselect("Select input columns", df.columns)
            output_column = st.selectbox("Select output column", df.columns)
            X = df[input_column]
            y = df[output_column]
            
            # Display input and output dataframes
            colA1, spaceA, colA2 = st.columns([5,1,5])
            with colA1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
            with colA2:
                st.subheader("Dataframe of OUTPUT")
                st.dataframe(y)
                
            st.write("__________________________________")
            
            st.subheader("Fill in valid values for all INPUTS")
            
            colB1, spaceB, colB2 = st.columns([5,1,5])
            with colB1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
                # # Creating model using DECISION TREE algorithm and displaying model accuracy
                # size = st.slider("Select your desired test size",
                #                 min_value=0.00,
                #                 max_value=1.00,
                #                 step=0.01)
                # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=size)
                # model = DecisionTreeClassifier()
                # model.fit(X_train, y_train)
                # predictions2 = model.predict(X_test)
                # score = accuracy_score(y_test, predictions2)
                # st.subheader(f"The model has a {score*100}% accuracy.")
            
            with colB2:
                # Start predictions
                input1 = st.number_input("Add value for input 1")
                model = DecisionTreeClassifier()
                model.fit(X, y)
                prediction = model.predict([[input1]])
                st.subheader(f"For the given input, the value of the output is {prediction}.")
            
        if input_qty == 2:
            
            # Seperate dataframe into INPUTS and OUTPUT
            input_column = st.multiselect("Select input columns", df.columns)
            output_column = st.selectbox("Select output column", df.columns)
            X = df[input_column]
            y = df[output_column]
            
            # Display input and output dataframes
            colA1, spaceA, colA2 = st.columns([5,1,5])
            with colA1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
            with colA2:
                st.subheader("Dataframe of OUTPUT")
                st.dataframe(y)
            
            st.subheader("Fill in valid values for all INPUTS")
            
            colB1, spaceB, colB2 = st.columns([5,1,5])
            with colB1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
                # # Creating model using DECISION TREE algorithm and displaying model accuracy
                # size = st.slider("Select your desired test size",
                #                 min_value=0.00,
                #                 max_value=1.00,
                #                 step=0.01)
                # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=size)
                # model = DecisionTreeClassifier()
                # model.fit(X_train, y_train)
                # predictions2 = model.predict(X_test)
                # score = accuracy_score(y_test, predictions2)
                # st.subheader(f"The model has a {score*100}% accuracy.")
            
            with colB2:
                # Start predictions
                input1 = st.number_input("Add value for input 1")
                input2 = st.number_input("Add value for input 2")
                model = DecisionTreeClassifier()
                model.fit(X, y)
                prediction = model.predict([[input1, input2]])
                st.subheader(f"For the given inputs, the value of the output is {prediction}.")
            
        if input_qty == 3:
            
            # Seperate dataframe into INPUTS and OUTPUT
            input_column = st.multiselect("Select input columns", df.columns)
            output_column = st.selectbox("Select output column", df.columns)
            X = df[input_column]
            y = df[output_column]
            
            # Display input and output dataframes
            colA1, spaceA, colA2 = st.columns([5,1,5])
            with colA1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
            with colA2:
                st.subheader("Dataframe of OUTPUT")
                st.dataframe(y)
            
            st.subheader("Fill in valid values for all INPUTS")
            
            colB1, spaceB, colB2 = st.columns([5,1,5])
            with colB1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
                # # Creating model using DECISION TREE algorithm and displaying model accuracy
                # size = st.slider("Select your desired test size",
                #                 min_value=0.00,
                #                 max_value=1.00,
                #                 step=0.01)
                # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=size)
                # model = DecisionTreeClassifier()
                # model.fit(X_train, y_train)
                # predictions2 = model.predict(X_test)
                # score = accuracy_score(y_test, predictions2)
                # st.subheader(f"The model has a {score*100}% accuracy.")
            
            with colB2:
                # Start predictions
                input1 = st.number_input("Add value for input 1")
                input2 = st.number_input("Add value for input 2")
                input3 = st.number_input("Add value for input 3")
                model = DecisionTreeClassifier()
                model.fit(X, y)
                prediction = model.predict([[input1, input2, input3]])
                st.subheader(f"For the given inputs, the value of the output is {prediction}.")            
            
        if input_qty == 4:
            
            # Seperate dataframe into INPUTS and OUTPUT
            input_column = st.multiselect("Select input columns", df.columns)
            output_column = st.selectbox("Select output column", df.columns)
            X = df[input_column]
            y = df[output_column]
            
            # Display input and output dataframes
            colA1, spaceA, colA2 = st.columns([5,1,5])
            with colA1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
            with colA2:
                st.subheader("Dataframe of OUTPUT")
                st.dataframe(y)
            
            st.subheader("Fill in valid values for all INPUTS")
            
            colB1, spaceB, colB2 = st.columns([5,1,5])
            with colB1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
                # # Creating model using DECISION TREE algorithm and displaying model accuracy
                # size = st.slider("Select your desired test size",
                #                 min_value=0.00,
                #                 max_value=1.00,
                #                 step=0.01)
                # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=size)
                # model = DecisionTreeClassifier()
                # model.fit(X_train, y_train)
                # predictions2 = model.predict(X_test)
                # score = accuracy_score(y_test, predictions2)
                # st.subheader(f"The model has a {score*100}% accuracy.")
            
            with colB2:
                # Start predictions
                input1 = st.number_input("Add value for input 1")
                input2 = st.number_input("Add value for input 2")
                input3 = st.number_input("Add value for input 3")
                input4 = st.number_input("Add value for input 4")
                model = DecisionTreeClassifier()
                model.fit(X, y)
                prediction = model.predict([[input1, input2, input3, input4]])
                st.subheader(f"For the given inputs, the value of the output is {prediction}.")

        if input_qty == 5:
            
            # Seperate dataframe into INPUTS and OUTPUT
            input_column = st.multiselect("Select input columns", df.columns)
            output_column = st.selectbox("Select output column", df.columns)
            X = df[input_column]
            y = df[output_column]
            
            # Display input and output dataframes
            colA1, spaceA, colA2 = st.columns([5,1,5])
            with colA1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
            with colA2:
                st.subheader("Dataframe of OUTPUT")
                st.dataframe(y)
            
            st.subheader("Fill in valid values for all INPUTS")
            
            colB1, spaceB, colB2 = st.columns([5,1,5])
            with colB1:
                st.subheader("Dataframe of INPUTS")
                st.dataframe(X)
                # # Creating model using DECISION TREE algorithm and displaying model accuracy
                # size = st.slider("Select your desired test size",
                #                 min_value=0.00,
                #                 max_value=1.00,
                #                 step=0.01)
                # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=size)
                # model = DecisionTreeClassifier()
                # model.fit(X_train, y_train)
                # predictions2 = model.predict(X_test)
                # score = accuracy_score(y_test, predictions2)
                # st.subheader(f"The model has a {score*100}% accuracy.")
            
            with colB2:
                # Start predictions
                input1 = st.number_input("Add value for input 1")
                input2 = st.number_input("Add value for input 2")
                input3 = st.number_input("Add value for input 3")
                input4 = st.number_input("Add value for input 4")
                input5 = st.number_input("Add value for input 5")
                model = DecisionTreeClassifier()
                model.fit(X, y)
                prediction = model.predict([[input1, input2, input3, input4, input5]])
                st.subheader(f"For the given inputs, the value of the output is {prediction}.")            
