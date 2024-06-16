import joblib
import pandas as pd
import streamlit as st


# Load ml model
@st.cache_resource
def load_model():
    model = joblib.load("wine_prediction_model.joblib")
    return model


# Function to get user input
def get_user_input() -> None:
    """
    Function to get user input for prediction.
    """

    fixed_acidity = st.number_input("Fixed Acidity", step=0.1, format="%.3f")
    volatile_acidity = st.number_input("Volatile Acidity", step=0.1, format="%.3f")
    citric_acid = st.number_input("Citric Acid", step=0.1, format="%.3f")
    residual_sugar = st.number_input("Residual sugar", step=0.1, format="%.3f")
    chlorides = st.number_input("Chlorides", step=0.1, format="%.3f")
    free_sulfur_dioxide = st.number_input(
        "Free Sulfur Dioxide", step=0.1, format="%.3f"
    )
    total_sulfur_dioxide = st.number_input(
        "Total Dulfur Dioxide", step=0.1, format="%.3f"
    )
    density = st.number_input("Density", step=0.1, format="%.3f")
    pH = st.number_input("pH", step=0.1, format="%.3f")
    sulphates = st.number_input("Sulphates", step=0.1, format="%.3f")
    alcohol = st.number_input("Alcohol", step=0.1, format="%.3f")

    return {
        "fixed_acidity": fixed_acidity,
        "volatile_acidity": volatile_acidity,
        "citric_acid": citric_acid,
        "residual_sugar": residual_sugar,
        "chlorides": chlorides,
        "free_sulfur_dioxide": free_sulfur_dioxide,
        "total_sulfur_dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol,
    }


# Streamlit app layout
def main() -> None:
    st.set_page_config(page_title="Wine Quality", page_icon="🍷")

    st.markdown(
        body="<h2 style='text-align: center;'> 🍷 Red Wine Quality Prediction App 🍷 </h2>",
        unsafe_allow_html=True,
    )

    st.image("images/ui_wine_image.jpg", use_column_width=True, caption="Red Wine")

    st.markdown(
        body="<h4 style='text-align: center;'> Predict the quality of your red wine! </h4>",
        unsafe_allow_html=True,
    )

    model = load_model()
    user_input = get_user_input()

    columns = st.columns((1.5, 2))
    button_pressed = columns[1].button("Predict!")
    if button_pressed:
        with st.spinner("Generating prediction ..."):
            input_df = pd.DataFrame([user_input])
            prediction = model.predict(input_df)

            if prediction[0] == 0:
                output = "Bad"
            else:
                output = "Good"

            with st.container():
                st.markdown(
                    f"""
                <div style="background-color:#f0f2f6; border-radius:10px; padding:10px; margin-top:20px;">
                    <h3 style='text-align: center; color: #333;'>Prediction Result</h3>
                    <h1 style='text-align: center; color: #ff4b4b;'>{output}</h1>
                    <p style='text-align: center;'>The quality of your red wine is predicted to be <strong>{output}</strong>.</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        st.session_state.fixed_acidity = 20


if __name__ == "__main__":
    main()
