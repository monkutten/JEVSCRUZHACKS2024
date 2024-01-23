# JEVSCRUZHACKS2024

CRUZHACKS 2024 Project: SlugShack  
Created in collaboration by: James Manlangit, Ethan Phan, Vishnu Naroth, Sofia Dang 

Description: 
SlugShack connects graduating/departing students in desperately needed houses with students seeking somewhere to call home. Chatbot coached on SC Housing Crisis studies explains complex housing system. A proof-of-concept of a tool that could alleviate the UCSC student housing crisis. 

How it works:
Website contains the user interface for the database and also the housing chatbot. This configuration allows a user to search through nearby available housing, and sort results by various metrics like distance to campus, # of vacancies, estimated monthly rent, and more. To the right of the intractable database is the chatbot, which can guide users to resources regarding affordable housing, explain some of the main causes of the SC housing crisis, and more. Note: All user information in the Google Sheets database is fictional.

Tools/APIs used:
flowise
github
google-maps
google-places
gspread
open-ai
streamlit
vectara

Credentials Needed:  
Vectara API Key  
Google Project API Key  
Google: credentials.json  
Vectara: token.json  

Usage:  
npx flowise start <- initializes localhost for Chatbot  
streamlit run vectarainterface.py <- initializes localhost for Streamlit Website

