import streamlit as st
import requests

st.set_page_config(
    page_title="Wine Quality Prediction",
    layout="centered"
)


st.title("Wine Quality Prediction")
st.write(
    "Prédisez la qualité d'un vin à partir de ses caractéristiques."
)



st.subheader("Caractéristiques du vin")

with st.form("wine_form"):

    col1, col2 = st.columns(2)

    with col1:

        fixed_acidity = st.number_input(
            "Fixed Acidity",
            min_value=0.0,
            value=7.4
        )

        volatile_acidity = st.number_input(
            "Volatile Acidity",
            min_value=0.0,
            value=0.70
        )

        citric_acid = st.number_input(
            "Citric Acid",
            min_value=0.0,
            value=0.0
        )

        residual_sugar = st.number_input(
            "Residual Sugar",
            min_value=0.0,
            value=1.9
        )

        chlorides = st.number_input(
            "Chlorides",
            min_value=0.0,
            value=0.076
        )

        free_sulfur_dioxide = st.number_input(
            "Free Sulfur Dioxide",
            min_value=0.0,
            value=11.0
        )

    with col2:

        total_sulfur_dioxide = st.number_input(
            "Total Sulfur Dioxide",
            min_value=0.0,
            value=34.0
        )

        density = st.number_input(
            "Density",
            min_value=0.0,
            value=0.9978
        )

        ph = st.number_input(
            "ph",
            min_value=0.0,
            max_value=14.0,
            value=3.51
        )

        sulphates = st.number_input(
            "Sulphates",
            min_value=0.0,
            value=0.56
        )

        alcohol = st.number_input(
            "Alcohol",
            min_value=0.0,
            value=9.4
        )

        wine_type = st.selectbox(
            "Wine Type",
            ["red", "white"]
        )

    submitted = st.form_submit_button(
        "Predict Wine Quality"
    )



if submitted:

    data = {
        "fixed_acidity": fixed_acidity,
        "volatile_acidity": volatile_acidity,
        "citric_acid": citric_acid,
        "residual_sugar": residual_sugar,
        "chlorides": chlorides,
        "free_sulfur_dioxide": free_sulfur_dioxide,
        "total_sulfur_dioxide": total_sulfur_dioxide,
        "density": density,
        "ph": ph,
        "sulphates": sulphates,
        "alcohol": alcohol,
        "type": wine_type
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"]

            st.success(
                f" Qualité prédite : **{prediction}**"
            )

        else:

            st.error(
                f"Erreur API : {response.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Impossible de contacter FastAPI. "
            "Vérifiez que le serveur FastAPI est lancé."
        )