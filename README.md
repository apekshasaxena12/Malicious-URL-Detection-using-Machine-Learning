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

## How to Run

Run the main script:

```bash
python code_new.py
```

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

Example:

```
Accuracy: 0.95
```

---

## Feature Extraction

The system extracts features directly from user-provided URLs, including:

* Special character counts (`.`, `-`, `_`, `/`, `?`, etc.)
* URL length
* Domain length
* Number of vowels in domain

These features are aligned with the training dataset before prediction.

---

## User Interaction

After training, the program allows real-time predictions:

```
Enter URL to check: https://example.com
```

Output:

```
Safe URL
```

or

```
Malicious URL
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

## Future Improvements

* Add more advanced feature engineering
* Use deep learning models
* Build a web interface (Flask / Streamlit)
* Save and reuse trained model
* Improve accuracy with larger datasets

---

## License

This project is for educational purposes.

---

