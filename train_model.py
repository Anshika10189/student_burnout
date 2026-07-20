import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
#load dataset
data=pd.read_csv("burnout.csv")

#input features
X=data[["study_hours","sleep_hours","stress_level","attendence","assignments"]]

#output lebal
y=data["burnout"]
#convert label(low,medium,high) to numbers
encoder=LabelEncoder()
y_encoded=encoder.fit_transform(y)

#train model
model=DecisionTreeClassifier(random_state=42)
model.fit(X,y_encoded)

#savethe model and encoder
joblib.dump(model,"model,pkl")
joblib.dump(encoder,"encoder.pkl")
print("model trained successfully!")
