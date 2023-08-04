
def common_features():
    car1 = {"Toyota", "Sedan", 2.0, "Automatic", "White"}
    car2 = {"Honda", "SUV", 2.0, "Manual", "White"}
    similarity = car1.intersection(car2)
    print(similarity)

common_features()