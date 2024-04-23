import json

def main():
    
    with open("src/theta.json", "r") as f:
        values = json.load(f)

    return values["theta0"] + (values["theta1"] * mileage)

if __name__ == "__main__":
    main()
