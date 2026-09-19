import numpy as np

def phm_score(rul_pred, rul_true):
    d = np.array(rul_pred) - np.array(rul_true)
    return float(np.sum(np.where(d < 0, np.exp(-d / 13) - 1, np.exp(d / 10) - 1)))

if __name__ == "__main__":
    print(phm_score([50, 60], [55, 55]))
