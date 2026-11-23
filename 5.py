#LG
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create and train model
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200))
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Display accuracy metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# User input prediction
print("\nEnter flower measurements:")
sl = float(input("Sepal Length: "))
sw = float(input("Sepal Width: "))
pl = float(input("Petal Length: "))
pw = float(input("Petal Width: "))

sample = np.array([[sl, sw, pl, pw]])
prediction = model.predict(sample)

print("Predicted Class:", iris.target_names[prediction[0]])
print("Probabilities:", model.predict_proba(sample))
