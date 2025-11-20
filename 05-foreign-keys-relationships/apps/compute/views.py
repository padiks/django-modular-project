# apps/compute/views.py
'''
from django.shortcuts import render

def index(request):
    # Example values to compute
    input1 = 10  # Example input 1
    input2 = 15  # Example input 2
    sum_result = input1 + input2  # Perform the sum operation

    return render(request, 'compute/index.html', {
        'title': 'Compute Values',
        'input1': input1,
        'input2': input2,
        'sum_result': sum_result,
    })
'''
from django.shortcuts import render

def index(request):
    input1 = ''  # Default to an empty string
    input2 = ''  # Default to an empty string
    sum_values = None

    if request.method == 'POST':
        input1 = request.POST.get('input1', '')  # Get the value of input1 from the form, default to empty string
        input2 = request.POST.get('input2', '')  # Get the value of input2 from the form, default to empty string

        try:
            input1 = float(input1)  # Try converting input1 to float
            input2 = float(input2)  # Try converting input2 to float
            sum_values = input1 + input2  # Sum the two values
        except ValueError:
            sum_values = 'Invalid input. Please enter numeric values.'  # Handle non-numeric inputs

    return render(request, 'compute/index.html', {
        'title': 'Compute Values',
        'input1': input1,
        'input2': input2,
        'sum_values': sum_values,
    })
