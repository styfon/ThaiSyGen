import streamlit as st
import json
import os

# streamlit run ToneRulesSL.py
# source LangOnline/bin/activate

# Assuming gen1 and gen2 functions are defined elsewhere and imported here
def gen1(*args):
    # Example implementation of gen1
    return "Gen1 Result"

def gen2():
    # Example implementation of gen2
    return "Gen2 Result"

# JSON file paths
realsy_file = "realsy.json"
fakesy_file = "fakesy.json"

# Ensure JSON files exist
if not os.path.exists(realsy_file):
    with open(realsy_file, 'w') as f:
        json.dump([], f)

if not os.path.exists(fakesy_file):
    with open(fakesy_file, 'w') as f:
        json.dump([], f)

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to save data to JSON
def save_to_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

# Streamlit app
def main():
    st.title("Syllable Generator")

    if 'generated_string' not in st.session_state:
        st.session_state.generated_string = ""

    def generate_string(gen_func, *args):
        st.session_state.generated_string = gen_func(*args)

    def add_to_json(file_path):
        data = load_json(file_path)
        data.append(st.session_state.generated_string)
        save_to_json(file_path, data)
        st.session_state.generated_string = gen_func()

    # Home screen
    choice = st.selectbox("Choose an option", ["Home", "Standard Rules", "Special Rules"])

    if choice == "Home":
        st.header("Home")
        st.button("Standard Rules", on_click=lambda: st.experimental_rerun())
        st.button("Special Rules", on_click=lambda: st.experimental_rerun())

    elif choice == "Standard Rules":
        st.header("Standard Rules")

        # Checkboxes
        checkboxes = [st.checkbox(f"Option {i+1}") for i in range(5)]
        input_vars = [cb for cb in checkboxes]

        if st.button("Generate"):
            generate_string(gen1, *input_vars)

        st.write(st.session_state.generated_string)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Actual Syllable"):
                add_to_json(realsy_file)
        with col2:
            if st.button("Not a Syllable"):
                add_to_json(fakesy_file)

    elif choice == "Special Rules":
        st.header("Special Rules")

        if st.button("Generate"):
            generate_string(gen2)

        st.write(st.session_state.generated_string)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Actual Syllable"):
                add_to_json(realsy_file)
        with col2:
            if st.button("Not a Syllable"):
                add_to_json(fakesy_file)

if __name__ == "__main__":
    main()


#Features
#open up and there are check boxes of all the things
# you can practice. 
#You check as many as you want and it will randomly
# generate syllables to practice
#Ongoing do not use list