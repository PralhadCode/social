from django.views.decorators.csrf import csrf_exempt
from .models import Visitor
from django.http import HttpResponse
from .models import Visitor  # Assuming your model is named 'Visitor'
from django.shortcuts import render
from .models import QRCode


def home_view(request):
    name = "Welcome To"

    obj = QRCode.objects.latest('id')
    print(obj.qr_code.url)

    context = {
        'name': name,
        'obj': obj,
    }
    return render(request, 'qrcode.html', context)


# views.py

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email', '')
        # Update the name to 'selected_office'
        # purpose = request.POST.get('selected_office', '')
        # print(purpose)
        selected_office = request.POST.get('selected_office', '')
        selected_restrorant = request.POST.get('selected_restrorant', '')
        print(selected_restrorant)
        # Choose the correct value based on the selection
        purpose = selected_office if selected_office else selected_restrorant

        purpose_desc = request.POST.get('purpose_desc', '')
        number_of_people = request.POST.get('number_of_people')

        visitor = Visitor.objects.create(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            email=email,
            purpose=purpose,
            purpose_desc=purpose_desc,
            number_of_people=number_of_people
        )

        # You can add more logic here if needed

        return HttpResponse("Form submitted successfully!")

    return render(request, 'contact.html')
