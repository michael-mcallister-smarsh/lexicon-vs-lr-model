import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset from a CSV file
data_path = 'sport_dataset.csv'
df = pd.read_csv(data_path)
df.columns = ["sentence", "label"]

# Display dataset info
print(f"Loaded {len(df)} records from {data_path}")
print(df.head())

# vectorize the text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["sentence"])
Y = df["label"]
print("X shape:", X.shape)
print("y shape:", Y.shape)

# Train a simple model
model = LogisticRegression()
model.fit(X, Y)

# Save the model using pickle
with open('sport-classifier-model.pkl', 'wb') as f:
        pickle.dump(model, f)

# Save the vectorizer too since you'll need it for preprocessing new data
with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

print("Model and vectorizer saved successfully.")
