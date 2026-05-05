from data import split_data
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
import joblib

def train_model():
    X_train, X_test, y_train, y_test = split_data()

    # Handle imbalance
    smote = SMOTE()
    X_train, y_train = smote.fit_resample(X_train, y_train)

    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    joblib.dump(model, "fraud_model.pkl")
    print("✅ Fraud model trained and saved!")

if __name__ == "__main__":
    train_model()