import streamlit as st
from prediction import predict


st.set_page_config(page_title="Krishi Kalyaan 🌦️", page_icon=":seedling:")


st.title("🌱 Krishi Kalyaan 🌦️")
st.markdown("Welcome to Krishi Kalyaan! This tool helps farmers predict crop yields based on various factors including location, crop selection, pesticide usage, average rainfall, and average temperature. Simply enter your district name, pesticide usage, and select the crop you're interested in, and click Predict to get the results.")
st.markdown("---")


st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with st.form(key="user_inputs"):
    city = st.text_input("Enter your district name:", "Noida")
    pesticides = st.text_input("Enter pesticide usage (in tonnes):", "21211")
    item = st.selectbox("Select your crop", ['Cassava', 'Maize', 'Plantains and others', 'Potatoes', 'Rice, paddy', 'Sorghum', 'Soybeans', 'Sweet potatoes', 'Wheat', 'Yams'])
    predict_button = st.form_submit_button("Predict")


average_yields = {
    'Cassava': 255000,
    'Maize': 70000,
    'Plantains and others': 200000,
    'Potatoes': 300000,
    'Rice, paddy': 40000,
    'Sorghum': 9000,
    'Soybeans': 15000,
    'Sweet potatoes': 250000,
    'Wheat': 35373,
    'Yams': 90000
}


if predict_button:
    try:
        pesticides = float(pesticides)
    except ValueError:
        st.error("Please enter a valid numeric value for pesticides.")
        st.stop()

    if item not in average_yields:
        st.error("Please select a valid crop from the dropdown list.")
        st.stop()

    predicted_yield = predict(city, item, pesticides)
    average_yield = average_yields[item]
    efficiency = min(round((predicted_yield / average_yield) * 100), 90)

    st.write(f"Predicted yield for {item} in {city} with {pesticides} tonnes of pesticides: {predicted_yield} hg/ha")
    st.write(f"Efficiency (compared to average yield of {item} in India): {efficiency}%")


    st.write("Efficiency:")
    st.progress(efficiency / 100)


    if efficiency >= 80:
        color = "green"
    elif efficiency >= 55:
        color = "yellow"
    else:
        color = "red"

    st.markdown(f'<p style="color:{color};">Efficiency: {efficiency}%</p>', unsafe_allow_html=True)
