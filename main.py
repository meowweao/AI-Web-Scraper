import streamlit as st
from scrape import scrape_website, clean_body_content, extract_body_content, split_dom_content
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter the url:")

if st.button("Scrap Website"):
    st.write("Scraping the given website")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    print(body_content)
    clean_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", clean_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_input("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)

            st.write(result)