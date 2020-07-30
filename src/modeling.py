#Write a function to train a lightGBM model using a dictionary of parameters, and another function to output predictions of that function. Store the lightGBM modeling object in a global variable called MODELING_DICT for use in the second function.    
#TODO start functions with verbs

MODELING_DICT = {}



def train_lgbm(param,X_train,Y_train):
    #TODO don't pass data as a global; take in two dataframes as arguments that you'll need to convert to LGBM objects
    #TODO modeling dict should be a dictionary; what if you want to run multiple models?
    import lightgbm as lgb
    model = lgb.LGBMRegressor(**param)
    model.fit(X_train, Y_train)
    MODELING_DICT["LGBM"] = model
    
    
def lgbm_predict(features):
    #TODO modeling dict should be a dictionary; what if you want to run multiple models?
    return MODELING_DICT["LGBM"].predict(features)



#Create in-sample residual plots for either LightGBM or XGBoost (y-axis: actual value; x-axis: (predicted - actual))
#TODO this won't run, right? what's the issue here?
def lgbm_plot(actual, predict):
    import matplotlib.pyplot as plt
    plt.scatter(predict - actual, actual)


    
#Write a function to train an XGBoost model using a dictionary of parameterse, and another function to output predictions of that function. Store the XGBoost modeling object in a global variable called MODELING_DICT for use in second function
#TODO use lower_case_naming (see PEP8 for more details)
#TODO store your state in a dictionary, not as another global
#TODO pass data as an argument, then convert to XGB objects
def Train_XGBoost_Model(dictionary_of_parameters):
    global XGBOOST_MODELING_DICT
    XGBOOST_MODELING_DICT = XGBClassifier(**dictionary_of_parameters) #unpacking the variable length of the dictionary of parameters
    XGBOOST_MODELING_DICT.fit(X_train, y_train)
    
#TODO see above
def Make_Predictions_With_XGBoost_Model(X_test):
    Y_Predictions =  XGBOOST_MODELING_DICT.predict(X_test)
    return Y_Predictions

#I read some articles, and they evaluated the predictions right after, so I added it in case?
#TODO not a bad idea, but you need to be sure you've untransformed your actuals first
def evaluate_predictions(Y_test, Y_Predictions):
    accuracy = accuracy_score(Y_test, Y_Predictions)
    return("Accuracy: %.3f%%%" % (accuracy * 100.0)) #displaying accuracy to 3 decimals in percent format
    