import pandas as pd
import numpy as np
import re
import tldextract

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


# 1. LOAD DATA
df = pd.read_csv("Zieni_Dataset for phishing detection.csv")


# 2. FEATURES & LABEL
X = df.drop("phishing", axis=1)
y = df["phishing"]


# 3. TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 4. MODEL TRAINING
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)


# 5. EVALUATION
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# 6. FEATURE EXTRACTION (USER INPUT)

def extract_features_from_url(url):
    features = {}

    features['num_dots_url'] = url.count('.')
    features['num_hyph_url'] = url.count('-')
    features['num_underline_url'] = url.count('_')
    features['num_slash_url'] = url.count('/')
    features['num_questionmark_url'] = url.count('?')
    features['num_equal_url'] = url.count('=')
    features['at_sign_url'] = url.count('@')
    features['num_and_url'] = url.count('&')
    features['num_exclamation_url'] = url.count('!')
    features['num_space_url'] = url.count(' ')
    features['tilde_url'] = url.count('~')
    features['num_comma_url'] = url.count(',')
    features['num_plus_url'] = url.count('+')
    features['num_asterisk_url'] = url.count('*')
    features['hashtag_url'] = url.count('#')
    features['num_dollar_url'] = url.count('$')
    features['num_percent_url'] = url.count('%')
    features['length_url'] = len(url)

    
    ext = tldextract.extract(url)
    domain = ext.domain
    features['length_dom'] = len(domain)
    features['num_vowels_dom'] = sum(1 for c in domain if c in 'aeiou')

    
    for col in X.columns:
        if col not in features:
            features[col] = 0

    return pd.DataFrame([features])[X.columns]

# 7. USER INPUT LOOP
while True:
    user_url = input("\nEnter URL to check: ")

    input_features = extract_features_from_url(user_url)
    prediction = model.predict(input_features)[0]

    print("\nResult:")
    if prediction == 1:
        print("Malicious URL")
    else:
        print("Safe URL")

    
    choice = input("\nDo you want to check another URL? (yes/no): ").lower()

    if choice == "no":
        print("Exiting program...")
        break
