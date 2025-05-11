## Intro
A simple example of 2 typical approaches to scanning natural language to classify it.  In this example we want to classify whether a user entered sentence is sports-related.

To try the "Lexicon with a REGEX" approach, add terms in the "sports_dataset.txt", then run "use-regex.py".  It gives a simple "true/false" for whether a sentence is sports related, if any word in the sentence entered is matched to any word in "sports_dataset.txt"

To try the "Machine Learning Model" approach, add sentences in the "sports_dataset.csv", run "train-model.py" to train the model for any new sentences added, then run "use-model.py".  It gives a probability score between 0-1 for whether a sentence is sports related based on the sentences labelled as "1".

## To run
When cloned to your local, run this to setup the python env
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
All py files should now be runnable

## Next steps
Play around by adding new terms/sentences to make it better, so less false positives (when the program thinks it's sport but it's not) and less false negatives (when the program thinks it's not sport but it is) -> congratulations, youre now a data scientist :)

Play around with the code so it crawls BBC sport for sports sentences rather than hand crafted text -> congratulations, you're now an AI engineer :)

Play around with the code so it consumes large blocks of text on a UI and presents back where the alerted sections are -> congratulations you're now a programmer :)