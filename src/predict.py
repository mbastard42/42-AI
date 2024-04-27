import json

def main():
    
    with open("src/theta.json", "r") as f:
        values = json.load(f)

    x = float(input())
    theta0 = values["theta0"]
    theta1 = values["theta1"]

    print(theta0 + (theta1 * x))

if __name__ == "__main__":
    main()
