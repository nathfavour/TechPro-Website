from django.shortcuts import render, redirect
from django.http import JsonResponse
import subprocess
from .models import CustomUser
from rest_framework import viewsets
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


def index(request):
    return render(request, 'index.html')

def apply(request):
    return render(request, 'apply.html')

def kyc(request):
    return render(request, 'kyc.html')

def webhook(request):
    if request.method == 'POST':
        # Execute the Git pull shell script
        try:
            subprocess.check_output(['/home/Techprotutorials/Techprotutorials/git_pull.sh'], stderr=subprocess.STDOUT)
            message = 'Webhook received and Git pull completed successfully.'
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during the Git pull
            message = f'Git pull encountered an error: {e.output.decode()}'
    else:
        message = 'Webhook received, but not processed. Expected POST request.'

    return JsonResponse({'message': message})

def submit_kyc(request):
    if request.method == 'POST':
        # Get the form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        aim = request.POST.get('aim')

        # Create a new CustomUser object and save it to the database
        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
            aim=aim
        )
        user.save()

        # Save the data to the database
        # Your database logic here...

        # Redirect to the Paystack page with parameters for autofill
        paystack_url = f'https://paystack.com/pay/0k72rdmm14?first_name={first_name}&last_name={last_name}&email={email}'
        return redirect(paystack_url)
    else:
        # Handle GET request for the form display
        return render(request, 'kyc.html')
