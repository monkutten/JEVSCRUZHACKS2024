import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
# Importing user information variables to avoid extra API Calls
from googlemapstest import userData, addressList, vacancyList, rentList, vacancyTimesList, distanceList, drivetimeList, bustimeList, walktimeList

# Description text
st.header("SlugShack: Your Friend in Housing")
st.text("Press the blue button to talk to a housing expert!")
st.text("Note: The information in the table is randomized as a proof of concept for SlugShack")
# Create two columns on Streamlit
col1, col2= st.columns([5,5])

# Implements Sheets API in Column 1
with col1:
    st.subheader("Available housing positions")
    df = pd.DataFrame({
    'Address': addressList,
    'Vacancies': vacancyList,
    'Estimated Rent' : rentList,
    'Time Until Vacancy' : vacancyTimesList,
    'Distance (km)' : distanceList,
    'Driving Time (mins)' : drivetimeList,
    'Bus Time (mins)' : bustimeList,
    'Walk Time (mins)' : walktimeList,
    })

    # User input to view housing contact information
    row = st.text_input("Please enter the row number of the address you're interested in")
    if st.button('Enter'):
        valid_row = int(row) in range(len(userData))
        f"Looks like you're interested in this property! The name of the vacating resident is {userData[int(row)][2]}. You can contact them by emailing them at {userData[int(row)][1]}, or calling them at {userData[int(row)][3]}!" if valid_row else "Enter a valid row number!"


# Implements Vectara Chatbot using Flowise HTML Embed in Column 2
with col2:
    st.subheader("Santa Cruz Housing Expert")
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <script type="module">
            import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
            Chatbot.init({
                chatflowid: "6a355a02-f85b-4120-8c90-c38745b772ba",
                apiHost: "http://localhost:3000",
            })
        </script>
        """,
        height=500,
    )

    df



