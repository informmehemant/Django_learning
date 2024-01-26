from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# def january(req):
#     return HttpResponse("Eat no meat for entire meat!")

# def february(req):
#     return HttpResponse("Walk for at least 20 minutes every day!")


# def march(req):
#     return HttpResponse("learn Django for at least 20 minutes every day!")

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for atlest 20 minutes every day!!",
    "march":"Learn Django for atlest 20 minutes every day!!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for atlest 20 minutes every day!!",
    "june":"Learn Django for atlest 20 minutes every day!!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for atlest 20 minutes every day!!",
    "september":"Learn Django for atlest 20 minutes every day!!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for atlest 20 minutes every day!!",
    "december":"Learn Django for atlest 20 minutes every day!!"
}

def index(request):
    list_months = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_months += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_months}</ul>"  
    return HttpResponse(response_data)
    
def monthly_challenge_by_number(request, month):
    # returns dict for monthly_challenges.keys() => converting to list
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound(f"{month} month is not found in this url")
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january will get constructed
    
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h2>This month is not supported!</h2>")    
    return HttpResponse(response_data)




