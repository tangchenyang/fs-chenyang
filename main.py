import os

import streamlit as st

from pathlib import Path
HOME_PATH = Path.home()

MARKDOWN_TEMPLATE = """```{format}
{content}
"""
if __name__ == '__main__':
    # Left Side Bar
    with st.sidebar:
        st.markdown(f"# Configurations")
        username = st.text_input("Username", placeholder="Enter your username")
        user_home = f"{HOME_PATH}/fs-users/{username}"

    #
    input_text = st.text_area("Enter your text", placeholder="Enter your text")
    file_name = "abc.txt" # todo
    file_full_path = f"{user_home}/{file_name}"

    btn = st.button("Save File")

    if btn:
        os.makedirs(os.path.dirname(file_full_path), exist_ok=True)
        with open(file_full_path, 'w') as f:
            f.write(input_text)
            st.success(f"File '{file_full_path}' has been updated successfully.")

    if os.path.exists(file_full_path):
        with open(file_full_path, 'r') as f:
            st.markdown("### File Content")
            file_content = f.read()
            st.markdown(MARKDOWN_TEMPLATE.format(format="text", content=file_content))



