import streamlit as st
import os
import requests
import json
import tempfile

st.set_page_config(page_title="Data Analyst Agent", layout="wide")
st.title("📊 Data-Analyst Agent UI")

API_URL = st.text_input("API endpoint URL", "http://localhost:8080/api")
uploaded = st.file_uploader("Upload your `question.txt` file", type="txt")
run = st.button("Run Analysis")

if run and uploaded:
    import time
    start_time = time.time()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        tmp.write(uploaded.getvalue())
        tmp.flush()
        tmp_path = tmp.name

    try:
        files = {"file": open(tmp_path, "rb")}
        with st.spinner("Running agent..."):
            resp = requests.post(API_URL, files=files, timeout=180)
            elapsed_time = time.time() - start_time
            resp.raise_for_status()
            response_data = resp.json()
            # Handle both direct result and wrapped result formats
            if isinstance(response_data, dict) and "result" in response_data:
                data = response_data["result"]
            else:
                data = response_data
            question_text = uploaded.getvalue().decode("utf-8").strip()

        st.subheader("📝 Question")
        st.markdown(f"```text\n{question_text}\n```")

        st.subheader("📄 Result Summary")
        import base64
        for i, item in enumerate(data):
            if isinstance(item, str) and item.startswith("data:image/png;base64,"):
                st.subheader("📈 Generated Plot")
                img_bytes = base64.b64decode(item.split(",")[1])
                img_kb = len(img_bytes) / 1024
                st.caption(f"Image size: {img_kb:.1f} KB")
                st.image(item, use_column_width=True)
            else:
                st.markdown(f"**{i+1}.** `{item}`")

        st.success(f"⏱️ Time taken: {elapsed_time:.2f} seconds")

    except Exception as e:
        st.error(f"❌ Error: {e}")

    finally:
        os.unlink(tmp_path)