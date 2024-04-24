import json

def main():
    
    with open("src/theta.json", "r") as f:
        values = json.load(f)

    print values["theta0"] + (values["theta1"] * float(input()))

if __name__ == "__main__":
    main()
