#Write a function to train a lightGBM model using a dictionary of parameters, and another function to output predictions of that function. Store the lightGBM modeling object in a global variable called MODELING_DICT for use in the second function.    
def lgbm_train(param):
    global MODELING_DICT
    MODELING_DICT = LGBMClassifier(**param)
    MODELING_DICT.fit(X_train, y_train)
    
    
def lgbm_predict(features):
    return MODELING_DICT.predict(features)



#Create in-sample residual plots for either LightGBM or XGBoost (y-axis: actual value; x-axis: (predicted - actual))
def lgbm_plot(actual, predict):
    plt.scatter(predicted - actual, actual)