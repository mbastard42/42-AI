import json

def main():

    with open("data.csv", "r") as f:
        next(f)
        lines = f.readlines()
    
    tmp_t0 = 0
    tmp_t1 = 0

    learningRate = 0.001

    for _ in range(1000):

        t0_sum = 0
        t1_sum = 0
        length = 0

        for line in lines:

            length += 1
            key, value = map(float, line.strip().split(","))
            print(tmp_t0 + (tmp_t1 * key), value)
            t0_sum += (tmp_t0 + (tmp_t1 * key) - value)
            t1_sum += (tmp_t0 + (tmp_t1 * key) - value) * key

        tmp_t0 -= learningRate / length
        tmp_t1 -= learningRate / length
        print(t0_sum, t1_sum, tmp_t0, tmp_t1)

    with open("theta.json", "w") as f:
        json.dump({"theta0": tmp_t0, "theta1": tmp_t1}, f)

if __name__ == "__main__":
    main()
