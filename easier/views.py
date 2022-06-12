from django.shortcuts import render
from .models import TestMessage

def only_view(request):
    message = TestMessage.objects.first()
    return render(
            request, 
            "easier/test.html", 
            context={"one": message.test_message}
    )
