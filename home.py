import streamlit as st
from pathlib import Path
from helper import get_txt_from_img
import pandas as pd
from PIL import Image



paths = []

st.write("## 1. Upload your Files")
with st.form(key="Form :", clear_on_submit = True):
    files = st.file_uploader(label = "Upload file", type=["png","jpeg","pdf"], accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')


if Submit :
    paths.clear()
    if len(files) > 0:
        for File in files:
            save_folder = './'
            save_path = Path(save_folder, File.name)
            paths.append(save_path)
            with open(save_path, mode='wb') as w:
                w.write(File.getvalue())


        successful = True
        for p in paths:
            if not p.exists():
                successful = False
        if successful:
            st.balloons()
            st.success(f'File {File.name} is successfully saved!')
    else:
        st.warning("You forgot to upload some files")

st.write("## 2. OCR Results")
if len(paths) > 0:
    results = []
    for (i, p) in enumerate(paths):
        cols = st.columns(2)
        cols[0].image(Image.open(p))
        cols[1].text(get_txt_from_img(p))

else:
    st.write("Upload some files first!")