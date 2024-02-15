from django.shortcuts import render
from django.http import HttpResponse
import openai , os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
openai.api_key = api_key

def Home(request):
    user_input = request.POST.get('user_input', None)  # แก้ชื่อของฟิลด์ให้ถูกต้อง
    print(user_input)  # แก้ชื่อตัวแปรให้ถูกต้อง
    if api_key is not None and request.method == 'POST' and user_input:  # ตรวจสอบว่ามีข้อมูลที่ผู้ใช้ป้อนหรือไม่
        try:
            response = openai.Image.create(
                prompt = user_input,
                size = '256x256'
            )
            print(response)
        except Exception as e:
            print(e)
    return render(request,"myapp/main.html", {})