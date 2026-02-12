MSE = sklearn.metrics.mean_squared_error(y_test, y_pred)

print(f"RMSE = {math.sqrt(MSE):.2f}")
print(f"Average house price = {y_test.mean():.2f}")
print(f"R_square = {model.score(x_test,y_test):.2f}")
