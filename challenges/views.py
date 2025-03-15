from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your tests here.
from django.template.loader import render_to_string
monthly_challenges = {
    "january": "No Meat for a month",
    "february": "Exercising 20 min a day !",
    "march": "Meditate for  15 mins !",
    "april": "Learn Django for a Day !",
    "may": "stay away from relapcing",
    "june": "learn coding pattern",
    "july": "learn DSA",
    "August": "learn to be quite inside",
    "september": "stop watching screens",
    "october": "start learning machine learning",
    "november": "learn about the world",
    "december": "keep health the no 1 priority"
}


def index(request):
    months = list(monthly_challenges.keys())
    # list_items = ''
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse(
    #         "month-challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalized_month} </a></l1>"
    # response_data = f"<ul> {list_items} </ul>"
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_num(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
        redirect_path = reverse(
            "month-challenge", args=[redirect_month])
    except:
        return HttpResponseNotFound("on redirect month does't exists")
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    challenge_text = ""
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f'<h1>{challenge_text} </h1>'\
        # response_data = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
            'text':  challenge_text,
            'month_name': month
        })
    except:
        return HttpResponseNotFound("<h2>This Month is not found !</h2>")
