import json

def main():
    
    theta0 = 0
    theta1 = 0

    try:
        with open("src/theta.json", "r") as f:
            values = json.load(f)
        theta0 = values["theta0"]
        theta1 = values["theta1"]
    except:
        theta0 = theta1

    x = float(input())

    print(theta0 + (theta1 * x))

if __name__ == "__main__":
    main()
