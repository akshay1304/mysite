from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')


def count(request):
    data=request.GET['fulltextarea']
    print(data)
    word_list = data.split()
    list_length = len(word_list)
    word_dict={}
    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1

    sorted_dict = sorted(word_dict.items(), key = lambda word_dict:word_dict[1],reverse=True)
    # sorted_dict = sorted(word_dict.items(), key=operator.itemgetter[1], reverse=True)   This is also used to sort a dictionary


    return render(request,'count.html',{'fulltext':data ,'word':list_length, 'word_d':sorted_dict})

    sorted_dict = sorted(word_dict.items())


def contact(request):
    return HttpResponse("<h1>contact page</h1> <br> This is our contact page",)