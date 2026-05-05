import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def generate_data(n=5000):
    np.random.seed(42)

    data = pd.DataFrame({
        "amount": np.random.uniform(10, 10000, n),
        "device_risk": np.random.randint(1, 100, n),
        "ip_risk": np.random.randint(1, 100, n),
        "is_international": np.random.choice([0, 1], n),
    })

    # Fraud logic (rare cases)
    data["fraud"] = (
        (data["amount"] > 8000) &
        (data["device_risk"] > 70) &
        (data["ip_risk"] > 70)
    ).astype(int)

    return data

def split_data():
    df = generate_data()

    X = df.drop("fraud", axis=1)
    y = df["fraud"]

    return train_test_split(X, y, test_size=0.2, random_state=42)