# Malicious-URL-Detection-using-Machine-Learning
A machine learning project for detecting phishing websites using labeled datasets, data preprocessing, and classification models.

# Phishing URL Detection using Machine Learning

## Overview

This project implements a **phishing website detection system** using machine learning. It uses a labeled dataset of URLs and extracts structural features from URLs to classify them as **malicious (phishing)** or **legitimate (safe)**.

The system includes:
* Data loading and preprocessing
* Model training using Random Forest
* Evaluation metrics
* Real-time URL prediction via user input

---

## Dataset

The project uses the dataset:
* `Zieni_Dataset for phishing detection.csv`

### Features:
The dataset contains various URL-based features such as:
* Number of dots, hyphens, special characters
* URL length
* Domain-based features (length, vowels, etc.)

### Label:
* `phishing`
  * `1` → Malicious
  * `0` → Legitimate

---

## Model Details

* Algorithm: **Random Forest Classifier**
* Number of trees: `200`
* Train/Test Split: `80% / 20%`
* Random State: `42`

---

## Evaluation

The model outputs:
* Accuracy Score
* Classification Report (Precision, Recall, F1-score)

### Results:

| Metric | Class 0 (Safe) | Class 1 (Malicious) | Macro Avg |
|---|---|---|---|
| Precision | 0.89 | 0.90 | 0.90 |
| Recall | 0.90 | 0.89 | 0.90 |
| F1-Score | 0.90 | 0.90 | 0.90 |
| Support | 996 | 1004 | 2000 |

**Overall Accuracy: `0.897`**

---

## Feature Extraction

The system extracts the following features directly from user-provided URLs:

| Feature | Description |
|---|---|
| `num_dots_url` | Count of `.` |
| `num_hyph_url` | Count of `-` |
| `num_underline_url` | Count of `_` |
| `num_slash_url` | Count of `/` |
| `num_questionmark_url` | Count of `?` |
| `num_equal_url` | Count of `=` |
| `at_sign_url` | Count of `@` |
| `num_and_url` | Count of `&` |
| `length_url` | Total URL length |
| `length_dom` | Domain name length |
| `num_vowels_dom` | Vowel count in domain |

These features are aligned with the training dataset columns before prediction.

---

## User Interaction

After training, the program allows real-time predictions:
```
Enter URL to check: https://github.com/
```

Output:
```
✅ Safe URL
```

or
```
⚠️ Malicious URL
```

The program loops until the user chooses to exit:
```
Do you want to check another URL? (yes/no): no
Exiting program...
```

---

## How to Run

### 1. Install Dependencies
```bash
pip install pandas numpy scikit-learn tldextract
```

### 2. Run the Script
```bash
python code_new.py
```

---

## Project Structure
```
phishing-detection/
│
├── Zieni_Dataset for phishing detection.csv
├── code_new.py
├── README.md
└── requirements.txt
```

---

## Requirements
```
pandas
numpy
scikit-learn
tldextract
```

---

## Future Improvements

* Add more advanced feature engineering
* Use deep learning models
* Build a web interface (Flask / Streamlit)
* Save and reuse trained model using `joblib`
* Improve accuracy with larger datasets

---

## License

This project is for educational purposes.
