from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')

def rst(request):
    return render(request,'rst.html')
def news_input_page(request):
    # if request.method== 'POST':
    #     news_url.get()

    #     return redirect('results/')
    
    
    return render(request,'news-input-page.html')
