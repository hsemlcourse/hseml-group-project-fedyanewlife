import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def evaluate(name, model, X, y_true):
    """Считает RMSE, MAE, R² и выводит результат."""
    y_pred = model.predict(X)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"{name}: RMSE={rmse:.4f}, MAE={mae:.4f}, R²={r2:.4f}")
    return {'Модель': name, 'RMSE': rmse, 'MAE': mae, 'R²': r2}
