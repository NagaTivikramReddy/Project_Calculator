from django.shortcuts import render


def index(request):
    '''
    This function returns the name to 'home.html file' 
    Added by vikarm
    '''
    return render(request, 'home.html', {'name': 'Vikram'})


def add(request):
    '''
    This function performs the addition of 2 given numbers and returns result to 'result.html file' 
    Added by vikarm

    '''

    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1 + num2

    return render(request, 'result.html', {'result': result})


def sub(request):
    '''
    This function performs the subtraction of 2 given numbers and returns result to 'result.html file' 
    Added by vikarm
    '''

    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1 - num2

    return render(request, 'result.html', {'result': result})


def mul(request):
    '''
    This function performs the multiplication of 2 given numbers and returns result to 'result.html file' 
    Added by vikarm
    '''

    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1 * num2

    return render(request, 'result.html', {'result': result})


def div(request):
    '''
    This function performs the division of 2 given numbers and returns result to 'result.html file' 
    This fuction also handles ZeroDivisionError
    Added by vikarm
    '''

    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])

    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        result = e

    # if num2 != 0:
    #     result = num1 / num2
    # else:
    #     result = "Cannot divide by zero"

    return render(request, 'result.html', {'result': result})
