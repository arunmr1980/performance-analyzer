import streamlit as st

left_column, right_column = st.columns(2)

with left_column:
    json_file = st.file_uploader("Upload the performance JSON")

if xml_file is not None:
    json_string = json_file.read()
    print("Reading xml file")
    print(xml_string)

    with left_column:
        st.json(json_string)
    mt7xx_txt = ""
    with right_column:
        st.write("MT7XX text file")
        st.download_button("Download File", mt7xx_txt, file_name="mt700.txt")
        st.write(mt7xx_txt)
