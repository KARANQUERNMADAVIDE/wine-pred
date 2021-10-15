import pandas as pd
import numpy as np
import pickle as pkl
import joblib
import json

# Features:-
# fixed acidity	
# volatile acidity	
# citric acid	
# residual sugar	
# chlorides	
# free sulfur dioxide	
# total sulfur dioxide	
# density	
# pH	
# sulphates	
# alcohol	

# Save calculated weights as json and scalar multiplication
# row x weights

# Save scaler object and transform row

# Save model-
# SVC(kernel='linear',C=100,decision_function_shape='ovo',gamma=0.01)


class Processing():
	def preprocess(dic):
		x = {}
		# fixed acidity
		x['fixed acidity'] = np.float(dic['fixed acidity'])
		# volatile acidity
		x['volatile acidity'] = np.float(dic['volatile acidity'])
		# citric acid
		x['citric acid'] = np.float(dic['citric acid'])
		# residual sugar
		x['residual sugar'] = np.float(dic['residual sugar'])
		# chlorides
		x['chlorides'] = np.float(dic['chlorides'])
		# free sulfur dioxide
		x['free sulfur dioxide'] = np.float(dic['free sulfur dioxide'])
		# total sulfur dioxide
		x['total sulfur dioxide'] = np.float(dic['total sulfur dioxide'])
		# density
		x['density'] = np.float(dic['density'])
		# pH
		x['pH'] = np.float(dic['pH'])
		# sulphates
		x['sulphates'] = np.float(dic['sulphates'])
		# pH
		x['alcohol'] = np.float(dic['alcohol'])
		
		X=pd.DataFrame({'x':x}).transpose()
		return X

	def predict_quality(X):
		# Modify values with weight multiplication
		weightfile = open('wine_app/ml_models/weights.json',)
		weights = json.load(weightfile)
		weightfile.close()

		# Standard Approach:-
		# Standard Scaling
		scaler = joblib.load('wine_app/ml_models/scaler.mod')
		X_scaled=scaler.transform(X)

		# Model predict
		model = pkl.load(open('wine_app/ml_models/winemodel.pkl', 'rb'))
		pred = model.predict(X_scaled)[0]
		print("Prediction Standard :- ",pred)

		preds = []
		for w in weights:
			# Weight Multiplication
			X_weighted=X*weights[w]
			# Standard Scaling
			scaler = joblib.load('wine_app/ml_models/scaler.mod')
			X_scaled=scaler.transform(X_weighted)
			# Model predict
			model = pkl.load(open('wine_app/ml_models/winemodel.pkl', 'rb'))
			pred = model.predict(X_scaled)[0]
			preds.append(pred)
		print(preds)
		print()
		prediction=int(sum(preds)/len(preds))
		print("Prediction New :-",prediction)
		return prediction
		

