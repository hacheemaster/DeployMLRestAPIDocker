# Train and save a model

from sklearn.externals import joblib
from sklearn import datasets
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# Load the Iris dataset
iris = datasets.load_iris()

# Set up a pipeline
pipeline = Pipeline([
    ('feature_selection', SelectKBest(chi2, k=2)),
    ('classification', RandomForestClassifier(n_estimators=100))
])

pipeline.fit(iris.data, iris.target)

# Export the classifier to a file
joblib.dump(pipeline, 'model.joblib')