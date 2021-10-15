from django.shortcuts import render
from .preprocessing.wine_preprocess import Processing

# Create your views here.
def winequality(request):
	if request.method == 'POST':
		dic = request.POST
		print(dic)
		# Preprocess POST request
		X = Processing.preprocess(dic)
		# Quality Predictor
		pred = Processing.predict_quality(X)
		context = {'pred':pred}
		print("Prediction : ",pred)
		return render(request,'wine_app/result.html',context)

	context = {}
	return render(request,'wine_app/wine.html',context)


def result(request):
	context = {}
	return render(request,'wine_app/result.html',context)