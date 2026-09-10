import pickle


# Load the trained model
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)


# Example student
student = [[8.2, 88, 78, 3, 1]]

# Make prediction
prediction = model.predict(student)[0]

if prediction == 1:
    result = "PLACED"
else:
    result = "NOT PLACED"

print("Student Details:", student)
print("Predicted Placement:", result)