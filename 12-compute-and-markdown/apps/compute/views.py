# apps/compute/views.py
from django.shortcuts import render

# Summation View
def summation(request):
    # Default values for the form inputs
    input1 = ''  
    input2 = ''  
    input3 = ''  
    input4 = ''  
    input5 = ''  
    sum_values = None

    # Check if the form is submitted and handle the clear action
    if request.method == 'POST':
        action = request.POST.get('action')  # Get the action from the button
        
        # If the action is "clear", reset all fields to empty strings
        if action == 'clear':
            input1 = input2 = input3 = input4 = input5 = ''  # Reset values
            sum_values = None  # Reset the sum
        elif action == 'compute':
            # Get the form inputs
            input1 = request.POST.get('input1', '')
            input2 = request.POST.get('input2', '')
            input3 = request.POST.get('input3', '')
            input4 = request.POST.get('input4', '')
            input5 = request.POST.get('input5', '')

            # Convert empty fields to 0 and calculate the sum
            input1 = input1 if input1 else '0'
            input2 = input2 if input2 else '0'
            input3 = input3 if input3 else '0'
            input4 = input4 if input4 else '0'
            input5 = input5 if input5 else '0'

            try:
                # Convert inputs to float
                input1 = float(input1)
                input2 = float(input2)
                input3 = float(input3)
                input4 = float(input4)
                input5 = float(input5)

                # Calculate the sum
                sum_values = input1 + input2 + input3 + input4 + input5
            except ValueError:
                sum_values = 'Invalid input. Please enter numeric values.'  # Handle non-numeric inputs

    return render(request, 'compute/summation.html', {
        'title': 'Summation',
        'input1': input1,
        'input2': input2,
        'input3': input3,
        'input4': input4,
        'input5': input5,
        'sum_values': sum_values,
    })


# Summary View (Static page)
def summary(request):
    return render(request, 'compute/summary.html', {
        'title': 'Summary',
    })
