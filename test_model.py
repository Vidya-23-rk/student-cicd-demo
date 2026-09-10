import os
import pickle


def load_model():
    with open("placement_model.pkl", "rb") as file:
        return pickle.load(file)


def test_model_file_exists():
    assert os.path.exists("placement_model.pkl")


def test_model_can_predict():
    model = load_model()

    student = [[8.5, 92, 85, 3, 1]]

    prediction = model.predict(student)

    assert prediction[0] in [0, 1]


def test_model_prediction_shape():
    model = load_model()

    student = [[7.0, 75, 65, 2, 1]]

    prediction = model.predict(student)

    assert len(prediction) == 1