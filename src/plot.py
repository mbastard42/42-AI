import json
import pandas
import matplotlib.pyplot as plt

def main():

    dataFrame = pandas.read_csv("src/data.csv")

    mileages = dataFrame[dataFrame.columns[0]].values
    prices = dataFrame[dataFrame.columns[1]].values

    plt.scatter(mileages, prices)
    
    with open("src/theta.json", "r") as f:
        values = json.load(f)

    plt.plot(mileages, [values["theta1"] * x + values["theta0"] for x in mileages])
    
    plt.savefig('tmp/plot.png')

if __name__ == "__main__":
    main()
