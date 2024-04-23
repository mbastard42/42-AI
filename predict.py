import json
import matplotlib.pyplot as plt

def predict(mileage):

    with open("theta.json", "r") as f:
        values = json.load(f)

    t0 = values["theta0"]
    t1 = values["theta1"]

    return t0 + (t1 *mileage)

def main():
    
    print(predict(float(input())))

if __name__ == "__main__":
    main()
