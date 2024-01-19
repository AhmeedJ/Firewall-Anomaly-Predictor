import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn import metrics
import itertools
import joblib

# Load data
train = pd.read_csv('/content/Train_data.csv')
test = pd.read_csv('/content/Test_data.csv')

# Data preprocessing
def preprocess_data(df):
    label_encoder = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = label_encoder.fit_transform(df[col])
    df.drop(['num_outbound_cmds'], axis=1, inplace=True)

preprocess_data(train)
preprocess_data(test)

# Feature selection using Recursive Feature Elimination (RFE)
X_train = train.drop(['class'], axis=1)
Y_train = train['class']

rfc = RandomForestClassifier(n_estimators=50)
rfe = RFE(rfc, n_features_to_select=10)
rfe = rfe.fit(X_train, Y_train)

feature_map = [(i, v) for i, v in itertools.zip_longest(rfe.get_support(), X_train.columns)]
selected_features = [v for i, v in feature_map if i == True]

X_train = X_train[selected_features]
test = test[selected_features]
print("selected_features:", selected_features)
# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
test = scaler.transform(test)

# Save the trained StandardScaler
scaler_filename = '/content/scaler_model1.sav'
joblib.dump(scaler, scaler_filename)  # Added to save the StandardScaler
print(f"Scaler saved as {scaler_filename}")

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X_train, Y_train, train_size=0.70, random_state=2)

# Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(x_train, y_train)

# Model evaluation
clf_y_pred = clf.predict(x_test)

accuracy = metrics.accuracy_score(y_test, clf_y_pred)
print("Accuracy:", accuracy)

# Use other metrics for evaluation
precision = metrics.precision_score(y_test, clf_y_pred, average='weighted')
recall = metrics.recall_score(y_test, clf_y_pred, average='weighted')
f1_score = metrics.f1_score(y_test, clf_y_pred, average='weighted')

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1_score)

# Specificity calculation function
def calculate_specificity(y_true, clf_y_pred, class_label):
    true_negative = np.sum((y_true != class_label) & (clf_y_pred != class_label))
    false_positive = np.sum((y_true != class_label) & (clf_y_pred == class_label))
    specificity = true_negative / (true_negative + false_positive)
    return specificity

class_label = 0
specificity = calculate_specificity(y_test, clf_y_pred, class_label)
print("Specificity:", specificity)

# Prediction on a new data point
input_data = np.array([1,5, 0, 0, 123, 0.05, 0.07, 26, 0, 0]).reshape(1, -1)
input_data = scaler.transform(input_data)
prediction = clf.predict(input_data)

if prediction[0] == 0:
    print('ANOMALY')
else:
    print('NORMAL')

import pickle
filename = 'INTRUSION_model1.sav'
pickle.dump(clf, open(filename, 'wb'))