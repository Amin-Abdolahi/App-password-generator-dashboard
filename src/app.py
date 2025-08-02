import streamlit as st
from password_generators import RandomPasswordGenerator,MemorablePasswordGenerator, PinCodeGenerator
import base64




def set_background(image_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            color: white;
        }}
        .main {{
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 10px;
            margin: 5% 20%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.2);


        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_background("../image/background.jpg")

def main():
    st.title("Password Generator")
    st.write("Select the type of password you want to generate:")
    password_type = st.radio("Password Type", ["Random Password", "Memorable Password", "PIN Code"], horizontal=True)

    if password_type == "Random Password":
        length = st.slider("Length", 8, 32, 16)
        include_symbols = st.checkbox("Include Symbols", True)
        include_numbers = st.checkbox("Include Numbers", True)
        include_uppercase = st.checkbox("Include Uppercase", True)
        include_lowercase = st.checkbox("Include Lowercase", True)

        if st.button("Generate"):
            generator = RandomPasswordGenerator(int(length), include_numbers, include_symbols, include_uppercase, include_lowercase)
            password = generator.generate()
            st.write("Generated Password:")
            st.code(password, language="bash")


    elif password_type == "Memorable Password":
        no_of_words = st.slider("Number of Words", 3, 30, 4)
        separator = st.text_input("Separator", "-")
        capitalization = st.checkbox("Capitalization", False)
        vocabulary = st.text_area("Vocabulary (one word per line), leave empty to use default", height=150)

        if st.button("Generate"):
            generator = MemorablePasswordGenerator(no_of_words, separator, capitalization, vocabulary.splitlines() if vocabulary else None)
            password = generator.generate()
            st.write("Generated Password:")
            st.code(password, language="bash")

    elif password_type == "PIN Code":
        length = st.slider("Length", 4, 16, 6)

        if st.button("Generate"):
            generator = PinCodeGenerator(length)
            pin_code = generator.generate()
            st.write("Generated PIN Code:")
            st.code(pin_code, language="bash")




if __name__ == "__main__":
    main()