
import os
import joblib
from django.shortcuts import render, redirect

# Create your views here.
def Home(request):
    return render(request,'index.html')

def rst(request):
    news_accuracy='Fake'
    news_title='The Moon Landing Was a Hoax'
    news_source='CNN'
    cornfidence='75%'
    biased_laguage='84%'
    source_credibilty='50%'
    fact_agreement='65%'
    related_news=['Moon Landing Conspiracy Theories','The truth behind the moon land']
    fact_resources=['Snopes','FactCheck.org','PolitiFact']

    return render(request,'rst.html',
                  {
        'news_accuracy': news_accuracy,
        'news_source': news_source,
        'cornfidence': cornfidence,
        'biased_laguage':biased_laguage,
         'news_title': news_title,
         'source_credibilty':source_credibilty,
         'fact_agreement':fact_agreement,
         'related_news':related_news,
         'fact_resources':fact_resources
       

                                      }
                                      )

def news_input_page(request):
    if request.method == 'POST':
        news_text = request.POST['news_text']
        
        # Correctly load the models
        vectorizer_path = os.path.join(os.path.dirname(__file__), 'models', 'vectorizer.pkl')
        classifier_path = os.path.join(os.path.dirname(__file__), 'models', 'news_classifier_model.pkl')
        vectorizer = joblib.load(vectorizer_path)
        classifier = joblib.load(classifier_path)

        # Process the input data
        vectorized_data = vectorizer.transform([news_text])
        prediction = classifier.predict(vectorized_data)

        # Format the prediction result
        result = 'Genuine' if prediction[0] == 1 else 'Fake'
        return render(request, 'news-input-page.html', {'news_text': news_text, 'result': result})
    
    return render(request, 'news-input-page.html')

