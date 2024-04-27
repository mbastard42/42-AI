import json
import math
import pandas
import matplotlib.pyplot as plt

def standardize(length, mileage, price):

    mean_mileage = sum(mileage) / length
    mean_price = sum(price) / length

    std_dev_mileage = math.sqrt((sum((mileage - mean_mileage) ** 2) / length))
    std_dev_price = math.sqrt((sum((price - mean_price) ** 2) / length))

    std_mileage = (mileage - mean_mileage) / std_dev_mileage
    std_price = (price - mean_price) / std_dev_price

    return std_mileage, std_price

def destandardize(std_theta0, std_theta1, mileage, price, length):

    mean_mileage = sum(mileage) / length
    mean_price = sum(price) / length

    std_dev_mileage = math.sqrt((sum((mileage - mean_mileage) ** 2) / length))
    std_dev_price = math.sqrt((sum((price - mean_price) ** 2) / length))
    
    theta0 = mean_price - (mean_mileage * std_theta1 * std_dev_price) / std_dev_mileage + std_theta0 * std_dev_price
    theta1 = std_theta1 * std_dev_price / std_dev_mileage

    return theta0, theta1

def data_scaling(length, mileage, price):

    plt.scatter(mileage, price)
    plt.savefig('tmp/1.1.data_values.png')
    plt.figure()

    std_mileage, std_price = standardize(length, mileage, price)

    plt.scatter(std_mileage, std_price)
    plt.savefig('tmp/1.2.std_values.png')
    plt.figure()

    return std_mileage, std_price

def train(learning_rate, length, mileage, price, rounds):

    theta0, theta1 = 0, 0
    tmp_t0, tmp_t1 = [], []
    
    for _ in range(rounds):
        
        prediction = theta0 + (theta1 * mileage)
        theta0 -= learning_rate / length * sum(prediction - price)
        theta1 -= learning_rate / length * sum((prediction - price) * mileage)
        tmp_t0.append(theta0)
        tmp_t1.append(theta1)

    return theta0, theta1, tmp_t0, tmp_t1

def main():
    
    dataFrame = pandas.read_csv("src/data.csv")

    length = dataFrame.shape[0]
    mileage = dataFrame[dataFrame.columns[0]].values
    price = dataFrame[dataFrame.columns[1]].values
    
    std_mileage, std_price = data_scaling(length, mileage, price)

    std_lr = 0.1
    std_round = 1000
    std_t0, std_t1, std_t0_step, std_t1_step = train(std_lr, length, std_mileage, std_price, std_round)
    std_t0, std_t1 = destandardize(std_t0, std_t1, mileage, price, length)

    std_rmse = []
    for r in range(std_round):
        std_t0_step[r], std_t1_step[r] = destandardize(std_t0_step[r], std_t1_step[r], mileage, price, length)
        std_rmse.append(math.sqrt(sum([(y - (std_t0_step[r] + (x * std_t1_step[r]))) ** 2 for x, y in zip(std_mileage, std_price)]) / (r + 1)))

    plt.plot([r for r in range(std_round)], std_rmse)
    plt.savefig('tmp/2.1.rmse.png')
    plt.figure()

    plt.scatter(mileage, price)
    plt.plot(mileage, [std_t0 + (x * std_t1) for x in mileage])
    plt.savefig('tmp/3.result.png')
    plt.figure()

    with open("src/theta.json", "w") as f:
        json.dump({"theta0": std_t0, "theta1": std_t1}, f)

if __name__ == "__main__":
    main()
