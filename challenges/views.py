from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string


# variables
monthly_challenges = {
    "january": "learn python",
    "february": "learn basics web development",
    "march": "learn django",
    "april": "learn python",
    "may": "learn basics web development",
    "june": "learn django",
    "july": "learn python",
    "august": "learn basics web development",
    "september": "learn django",
    "october": "learn python",
    "november": "learn basics web development",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(
        request,
        "challenges/index.html",
        {
            "months": months,
        }
    )


def monthly_numb(request, numb):
    months = list(monthly_challenges.keys())
    if numb > len(months):
        # return HttpResponseNotFound("invalid month!")
        raise Http404()

    numb_month = months[numb-1]
    redirect_path = reverse("monthly-challenge", args=[numb_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # return HttpResponse(f"This is {month}")
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {
                "challenge": challenge_text,
                "month": month,
            },
        )
    except:
        # error_page = render_to_string("404.html")
        # return HttpResponseNotFound(error_page)
        raise Http404()
