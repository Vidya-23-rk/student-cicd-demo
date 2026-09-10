import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. Load dataset
data = pd.read_csv("data/student_placement.csv")

# 2. Separate input features and target
X = data.drop("Placement", axis=1)
y = data["Placement"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 4. Create ML model
model = LogisticRegression(max_iter=1000)

# 5. Train model
model.fit(X_train, y_train)

# 6. Test model
predictions = model.predict(X_test)

# 7. Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Training Completed")
print("Test Accuracy:", accuracy)

# 8. Save trained model
with open("placement_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as placement_model.pkl")