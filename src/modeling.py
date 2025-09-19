# src/modeling.py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def run_linear_regression(df, features=["Political_Stability"], target="FDI", test_size=0.2, random_state=42):
    """
    Train a linear regression model and return results.
    """
    X = df[features].dropna()
    y = df.loc[X.index, target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return {
        "model": model,
        "r2": r2_score(y_test, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
        "coef": model.coef_,
        "intercept": model.intercept_
    }
