# Text classification and analysis of restaurant reviews using NLP techniques
## Description
- Classifying restaurant reviews as positive or negative, using ***spaCy*** & ***sklearn***, as well as
analysing the dataset by determining important words & phrases and extracting emotional affect using ***text2emotion***. 
- A **web demo** is included to showcase the information.
## Setup
- For starting up the web demo use `docker-compose up` & **access demo on port 8000**
- For starting up the presentation **Review Classification.ipynb** use:
1. `pip install -r jupyter/requirements.txt` or
`conda install --file jupyter/requirements.txt`
2. `python -m spacy download en_core_web_lg`
3. run `jupyter notebook`

***Both setups use spaCy's large english vocabulary (~800MB), therefore first initialization might take some time***

## Contents

### Main presentation
The jupyter presentation **Review Classification** contains the models trained for classifying the reviews,
as well as the main examples of most commonly used nouns & extraction of emotions from the reviews.
#### The trained models are:
     - Support Vector Classifier
     - Logistic Regression
     - Artificial Neural Network
### Vectorizing the dataset
The jupyter notebook **Vectorizing reviews.ipynb** showcases the vectorizing of the reviews
 using spaCy's large english vocabulary which turns the reviews into 300 dimensional vector
that are used for training the models.
