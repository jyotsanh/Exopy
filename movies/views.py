#   Movies   URL

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def movies(request):
    if request.method == 'POST':
        None
    else:
        if request.user.username is not None:

            # return render(request,"movies.html")
            
            return render(request,"movies.html")
        else:
            print("User not authenticated. Redirecting User to login page")
            return redirect('accounts:dash')