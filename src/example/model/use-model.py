import pickle

with open('sport-classifier-model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

while True:
    sentence = input("Enter a sentence: ")
    # Preprocess the input sentence
    sentence_as_a_vector = vectorizer.transform([sentence])
    # Predict the probability of label 1 (sport)
    prediction = model.predict_proba(sentence_as_a_vector)[0][1]
    # Print the prediction
    print(f"Probability this sentence is about sports: {prediction:.2f}")
