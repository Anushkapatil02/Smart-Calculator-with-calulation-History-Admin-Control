from django.shortcuts import render
from .models import CalculationHistory
from django.utils import timezone
from datetime import timedelta

# Set admin password here (or use environment variable in production)
ADMIN_PASSWORD = 'admin123'  # Change this to your secure password

def index(request):
    result = ''
    history = CalculationHistory.objects.all().order_by('-created_at')
    confirm_clear = False
    ask_password = False
    popup_message = ''

    if request.method == 'POST':
        if 'calculate' in request.POST:
            num1 = request.POST.get('num1')
            num2 = request.POST.get('num2')
            operator = request.POST.get('operator')

            try:
                n1 = float(num1)
                n2 = float(num2)
                if operator == '+':
                    result = n1 + n2
                elif operator == '-':
                    result = n1 - n2
                elif operator == '*':
                    result = n1 * n2
                elif operator == '/':
                    result = n1 / n2
                else:
                    result = 'Invalid Operator'

                CalculationHistory.objects.create(
                    num1=n1,
                    num2=n2,
                    operator=operator,
                    result=str(result)
                )
            except:
                result = 'Invalid Input'

        elif 'filter' in request.POST:
            filter_option = request.POST.get('filter_option')
            now = timezone.now()

            if filter_option == 'today':
                history = CalculationHistory.objects.filter(created_at__date=now.date())
            elif filter_option == 'last_10_days':
                history = CalculationHistory.objects.filter(created_at__gte=now - timedelta(days=10))
            elif filter_option == 'weekly':
                history = CalculationHistory.objects.filter(created_at__gte=now - timedelta(days=7))
            elif filter_option == 'monthly':
                history = CalculationHistory.objects.filter(created_at__month=now.month)

        elif 'clear_request' in request.POST:
            confirm_clear = True  # Step 1: Show Yes/No popup

        elif 'clear_yes' in request.POST:
            confirm_clear = True
            ask_password = True  # Step 2: Show password input

        elif 'clear_confirm' in request.POST:
            entered_password = request.POST.get('admin_password')
            if entered_password == ADMIN_PASSWORD:
                CalculationHistory.objects.all().delete()
                popup_message = '✅ Calculation history cleared successfully!'
                history = CalculationHistory.objects.all()
                confirm_clear = False
                ask_password = False
            else:
                popup_message = '❌ Incorrect password. Unauthorized action.'
                confirm_clear = False
                ask_password = False

        elif 'clear_no' in request.POST:
            confirm_clear = False
            ask_password = False

    return render(request, 'calculator/index.html', {
        'result': result,
        'history': history,
        'confirm_clear': confirm_clear,
        'ask_password': ask_password,
        'popup_message': popup_message
    })
