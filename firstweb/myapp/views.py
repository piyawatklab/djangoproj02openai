from django.shortcuts import render
from django.http import HttpResponse
import openai , os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
openai.api_key = api_key

def Home(request):
    if api_key is not None and request.method == 'POST':
        user_imput = request.POST.get('user_imput')
        response = openai.images.generate(
            prompt = user_imput,
            size = '256x256'
        )
        print(response)
    return render(request,"myapp/main.html", {})
