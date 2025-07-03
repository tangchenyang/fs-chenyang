import os

import streamlit as st

from pathlib import Path
HOME_PATH = Path.home()

MARKDOWN_TEMPLATE = """```{format}
{content}
"""
if __name__ == '__main__':
    # User
    st.markdown(f"# Configurations")
    username = st.text_input("Username", placeholder="Enter your username")
    user_home = f"{HOME_PATH}/fs-users/{username}"

    #
    input_text = st.text_area("Enter your text", placeholder="Enter your text")
    file_name = "temp.txt"
    file_full_path = f"{user_home}/{file_name}"

    col1, col2 = st.columns(2)
    btn = col1.button("Save Content", use_container_width=True)

    if btn:
        os.makedirs(os.path.dirname(file_full_path), exist_ok=True)
        with open(file_full_path, 'w') as f:
            f.write(input_text)
            st.success(f"Saved content to '{file_full_path}' successfully.")

    refresh_btn = col2.button("Refresh Content", use_container_width=True)

    if os.path.exists(file_full_path):
        with open(file_full_path, 'r') as f:
            st.markdown("### File Content")
            file_content = f.read()
            st.markdown(MARKDOWN_TEMPLATE.format(format="text", content=file_content))



