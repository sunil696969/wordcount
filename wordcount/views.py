from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    Data = request.GET['textarea']
    Word_list = Data.split()
    list_length = len(Word_list)

    word_dictionary = {}
    for word in Word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'count.html', {'textarea': Data, 'words': list_length,'word_dictionary': word_dictionary})

def about(request):
    return render(request, 'about.html')







