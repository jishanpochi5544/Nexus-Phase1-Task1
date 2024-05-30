import google.generativeai as genai
import streamlit as st

# Initialize the Gemini API with your specific API key
gemini_api_key = "YOUR-GEMINI-API-KEY"
genai.configure(api_key=gemini_api_key)

def check_symptoms(symptoms):
    """
    Check symptoms using the Gemini API.
    """
    try:
        query = f"Check symptoms: {symptoms}"
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while checking symptoms: {e}")
        return "We're sorry, but we couldn't check the symptoms right now."

def health_tips():
    """
    Provide general health tips using the Gemini API.
    """
    try:
        query = "Give general health tips."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while fetching health tips: {e}")
        return "We're sorry, but we couldn't fetch health tips right now."

def book_appointment(provider, specialty, date_time):
    """
    Schedule an appointment using the Gemini API.
    """
    try:
        query = f"Schedule appointment with {provider}, specialty: {specialty}, on {date_time}"
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while scheduling the appointment: {e}")
        return "We're sorry, but we couldn't schedule the appointment right now."

def emergency_info():
    """
    Provide emergency assistance information using the Gemini API.
    """
    try:
        query = "Provide emergency assistance information."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while fetching emergency assistance: {e}")
        return "We're sorry, but we couldn't fetch emergency assistance information right now."

def main():
    """
    Main function to run the Streamlit app.
    """
    st.title("HealthBot - Your Healthcare Assistant")
    st.write("Hello! I'm HealthBot. How can I assist you today?")

    user_name = st.text_input("Please enter your name:")
    if user_name:
        task = st.selectbox("Select a service:", ["Symptom Checker", "General Health Tips", "Schedule Appointment", "Emergency Assistance"])

        if task == "Symptom Checker":
            symptoms = st.text_area("Describe your symptoms:")
            if symptoms and st.button("Check Symptoms"):
                diagnosis = check_symptoms(symptoms)
                st.write("Based on your symptoms, here's what I found:")
                st.write(diagnosis)

        elif task == "General Health Tips":
            if st.button("Get Health Tips"):
                tips = health_tips()
                st.write("Here are some health tips for you:")
                st.write(tips)

        elif task == "Schedule Appointment":
            provider = st.text_input("Enter the healthcare provider's name:")
            specialty = st.text_input("Enter the required specialty (e.g., Cardiology, Dermatology):")
            date_time = st.text_input("Enter the preferred date and time for the appointment:")
            if provider and specialty and date_time and st.button("Schedule Appointment"):
                confirmation = book_appointment(provider, specialty, date_time)
                st.write("Your appointment details are as follows:")
                st.write(confirmation)

        elif task == "Emergency Assistance":
            if st.button("Get Emergency Assistance"):
                assistance = emergency_info()
                st.write("Emergency assistance details are:")
                st.write(assistance)

    st.write("Thank you for using HealthBot. Stay healthy!")

if __name__ == "__main__":
    main()
