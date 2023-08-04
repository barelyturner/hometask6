car1 = {"Toyota", "Sedan", 2.0, "Automatic", "White"}
car2 = {"Honda", "SUV", 2.0, "Manual", "White"}
car3 = {"Volvo", "Sedan", 2.0, "Manual", "White"}
car4 = {"Honda", "Bus", 4.0, "Manual", "Purple"}
car5 = {"Audi", "Coupe", 2.5, "Automatic", "Black"}
car6 = {"Mitsubishi", "SUV", 2.0, "Manual", "Purple"}
car7 = {"Toyota", "Coupe", 2.2, "Automatic", "White"}
car8 = {"Mercedes", "Truck", 4.0, "Manual", "Yellow"}

def common_features(a, b):
    similarity = a.intersection(b)
    if similarity == set():
        print("No matches found")
    else:
        print(f'Actual matches: {similarity}')

common_features(car5, car1)
