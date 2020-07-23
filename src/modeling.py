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
    


    
#Write a function to train an XGBoost model using a dictionary of parameterse, and another function to output predictions of that function. Store the XGBoost modeling object in a global variable called MODELING_DICT for use in second function
def Train_XGBoost_Model(dictionary_of_parameters):
    global XGBOOST_MODELING_DICT
    XGBOOST_MODELING_DICT = XGBClassifier(**dictionary_of_parameters) #unpacking the variable length of the dictionary of parameters
    XGBOOST_MODELING_DICT.fit(X_train, y_train)
    
def Make_Predictions_With_XGBoost_Model(X_test):
    Y_Predictions =  XGBOOST_MODELING_DICT.predict(X_test)
    return Y_Predictions

#I read some articles, and they evaluated the predictions right after, so I added it in case?
def evaluate_predictions(Y_test, Y_Predictions):
    accuracy = accuracy_score(Y_test, Y_Predictions)
    return("Accuracy: %.3f%%%" % (accuracy * 100.0)) #displaying accuracy to 3 decimals in percent format
    