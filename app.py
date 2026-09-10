def predict_result(marks):
    if marks >= 90:
        return "PASS"
    else:
        return "FAIL"


if __name__ == "__main__":
    marks = int(input("Enter student marks: "))

    result = predict_result(marks)

    print("Student Marks:", marks)
    print("Predicted Result:", result)
    
    