from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
import numpy as np
from keras.models import load_model
import tensorflow as tf
import sklearn 
from sklearn.preprocessing import Normalizer, StandardScaler
from django.decorators import de

# Create your views here.
def homepage(request):
    if request.method == "POST":
        scaler=StandardScaler()
        date=request.POST['date']
        average_cost=request.POST['average_cost']
        population=request.POST['population']
        household_size=request.POST['household_size']
        water_cost=request.POST['water_cost']
        x_predict=[average_cost,population,household_size,water_cost]
        x_predict=np.asarray(x_predict)
        x_predict=np.reshape(x_predict,(-1,1))
        x_predict=scaler.fit_transform(x_predict)
        x_predict=np.reshape(x_predict,(1,x_predict.shape[0]))
        x_predict=tf.convert_to_tensor(x_predict)
        model = load_model('model/IS_Project_2.h5')
        prediction=model.predict(x_predict)
        prediction=scaler.inverse_transform(prediction)
        #print(prediction)
        return render(request,'system/index.html',context={'value':int(prediction)})

    return render(request,'system/index.html')

