from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def eggs(request):
    return HttpResponse("<h1>Eggs</h1>")


def count(request):
    fulltext = request.GET["fulltext"]
    print("p1=", fulltext)
    a = fulltext.split(" ")
    wordcountdic = {}
    for word in a:
        if word in wordcountdic:
            wordcountdic[word] += 1
        else:
            wordcountdic[word] = 1
    sortedwords = sorted(wordcountdic.items(), key=operator.itemgetter(1), reverse=True)
    print("wordcountdic=", wordcountdic)
    print("wordcountdic=", wordcountdic.items())
    return render(request, 'count.html', {"fulltext": fulltext, "qtwords": len(a), "wordcountdic": sortedwords})


def about(request):
    return render(request, 'about.html')

