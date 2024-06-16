import streamlit as st

def about_page() -> None:
    st.title("About Red Wine Quality Prediction App")

    st.markdown("""
    ### Overview
    This application is designed to predict the quality of red wine based on various chemical properties. It utilizes a machine learning model trained on a comprehensive dataset from [Kaggle](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009/data). The primary goal of this application is to provide wine enthusiasts, producers, and industry professionals with a quick and easy way to assess the quality of red wine samples.

    ### Features
    - **Predictive Modeling**: Employs a state-of-the-art machine learning model that has been rigorously trained and validated to accurately predict wine quality as either 'Good' or 'Bad'.
    - **Interactive User Input**: Users can conveniently input the chemical properties of their wine samples, such as alcohol content, acidity, and sugar levels, through an intuitive interface.
    - **User-Friendly Interface**: Designed with Streamlit, a cutting-edge Python library for building data-driven applications, the app offers a clean, modern, and user-friendly interface for seamless interaction.
                
    ### How It Works
    Users input values for various chemical properties of their wine samples, such as alcohol content, acidity, and sugar levels. The application then processes these inputs through a sophisticated machine learning model, which has been trained on a vast dataset of red wine samples. Based on the inputted chemical properties, the model provides an instant prediction of the wine's quality, classifying it as either 'Good' or 'Bad'.

    ### About the Data
    The data used for training and validating the machine learning model comes from a reputable source, the [Kaggle Red Wine Quality Dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009/data). This dataset comprises 1,599 red wine samples, each with 11 features related to the wine's chemical properties, as well as a quality rating from 0 to 10.
    
    ### Built With 
    - Python Libraries 
        - Pandas
        - Scikit-learn
        - Streamlit

    ### Authors
    - [Akshat Jain](https://linkedin.com/in/akshatjain16)
    
    ### Contributions and Support
    All contributions and suggestions are welcomed from the community to further enhance this application. If you encounter any issues or have ideas for improvements, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/jainakki16/Wine-Quality-Prediction).
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    about_page()

