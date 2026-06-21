import streamlit as st
import joblib
from urllib.parse import urlparse
import re



model = joblib.load("model.pkl")

FEATURES = model.feature_names_in_


def extract_features(url):
    parsed = urlparse(url)

    def count_digits(s):
        return sum(c.isdigit() for c in s)

    features = {
        'NumDots': url.count('.'),
        'UrlLength': len(url),
        'NumDash': url.count('-'),
        'AtSymbol': url.count('@'),
        'IpAddress': int(bool(re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url))),
        'HttpsInHostname': int("https" in parsed.netloc),
        'PathLevel': parsed.path.count('/'),
        'PathLength': len(parsed.path),
        'NumNumericChars': count_digits(url)
    }

    return [features[col] for col in FEATURES]


st.set_page_config(page_title="Phishing Detector")

st.title(" Phishing URL Detector")
st.write("Enter any URL and check Safe or Phishing")

url = st.text_input("Enter URL")

if st.button("submit"):
    if not url:
        st.warning("Please enter a URL")
    else:
        try:
            features = extract_features(url)
            prediction = model.predict([features])[0]

            
            

            if prediction == 0:
                st.error(" Phishing URL")
            else:
                st.success("Legitimate URL")

        except Exception as e:
            st.error(f"Error: {e}")
