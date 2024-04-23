import json
import pandas

def main():
    
    dataFrame = pandas.read_csv("src/data.csv")

    length = dataFrame.shape[0]
    mileage = dataFrame[dataFrame.columns[0]].values
    price = dataFrame[dataFrame.columns[1]].values

    mean = mileage.mean()
    norm_mileage = mileage / mean

    t0 = 0
    t1 = 0
    
    learning_rate = 0.1

    for _ in range(1000):

        prediction = t0 + (t1 * norm_mileage)
        t0 -= learning_rate / length * sum(prediction - price)
        t1 -= learning_rate / length * sum((prediction - price) * norm_mileage)

    t1 = t1 / mean

    with open("src/theta.json", "w") as f:
        json.dump({"theta0": t0, "theta1": t1}, f)

if __name__ == "__main__":
    main()
