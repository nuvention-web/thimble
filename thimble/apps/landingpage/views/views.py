from django.shortcuts import render
from django.core.context_processors import csrf
import os, chimpy
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):
    try:
        if request.user.buyer is not None:
            return HttpResponseRedirect(reverse('landingpage:dashboard', args=(request.user.username,)))
    except:
        return HttpResponseRedirect(reverse('Portfolios:render_portfolio', args=(request.user.username,)))

@login_required
def dashboard(request, username):
    if request.user.username== username:
        return render(request, "landingpage/dashboard.html")
    else:
        raise Http404

def landingpage(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        chimp = chimpy.Connection(os.environ['MAILCHIMP_API_KEY'])

        try:
            chimp.list_subscribe(os.environ['MAILCHIMP_LIST_ID'], email, {},
                                 double_optin=False, send_welcome=True)
        except:
            context['error'] = "We're sorry, it seems there was an error. This may be because you haves already signed up."
        else:
            context['success'] = "Thank you for your interest in Thimble!"

    return render(request, "landingpage/beta.html", context)

# about/
def oldlandingpage(request):
    context = {}
    return render(request, "landingpage/about.html", context)

