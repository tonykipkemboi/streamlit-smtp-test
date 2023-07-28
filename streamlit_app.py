""" 
If you've two-step verification enabled, your regular password won't work. Instead, generate an app-specific password:

- Go to your Google Account.
- On the left navigation panel, click on "Security."
- Under "Signing in to Google," select "App Passwords." You might need to sign in again.
- At the bottom, choose the app and device you want the app password for, then select "Generate."
- Use this app password in your Streamlit app.

"""

import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Taking inputs
email_sender = st.text_input('From')
email_receiver = st.text_input('To')
subject = st.text_input('Subject')
body = st.text_area('Body')

# Hide the password input
password = st.text_input('Password', type="password")  

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")
