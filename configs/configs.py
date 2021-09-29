import os

# ********************************************************************************************************************************
# To be updated by user accordingly if to run this script using saved csv files
# Replace 'example_xxx.csv' with user's file name
xFeature_filename = 'example_xFeatures.csv'
yTrue_filename = 'example_yTrue.csv'
yPred_filename = ['example_yPred_model_xx.csv', 'example_yPred_model_yy.csv']  # can be single file or max 2 files, wrap in a list

# model name must be listed according to the same sequence of the yPred_filename list above in order to 
# indicate the prediction outputs are generated by the mentioned model
MODEL_NAME_LIST = ['example_model_xx', 'example_model_yy']  # can be single model or max bi-modal, wrap in a list
ANALYSIS_TYPE = 'Regression'  # Supported analysis types : 'Regression', 'Binary Classification', 'Multiclass Classification'
ANALYSIS_TITLE = 'example_Customer Churn Prediction'
PORT = 8000  # Defaults to 8000, user can re-define to a new port number of choice
# *******************************************************************************************************************************

# No modification from user is needed from this line onwards
DATA_DIR = 'csv_data'
XFEATURE_FILEPATH = os.path.join(DATA_DIR, xFeature_filename)
YTRUE_FILEPATH = os.path.join(DATA_DIR, yTrue_filename)
YPRED_FILEPATH = [os.path.join(DATA_DIR, file) for file in yPred_filename]
