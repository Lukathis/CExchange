import sys

from django.shortcuts import render

def home(request):

    return render(request, 'home.html',{

    })

# define 500 error
def trigger_500(request):
    """Hot-wired method of triggering a server error to test reporting."""
    raise Exception("Congratulations, you've triggered an exception! Go tell all your friends what an exceptional "
                    "person you are.")

def handle_500(request):
    """Custom server error handler"""
    type_, error, traceback = sys.exc_info()
    return render(request, '500.html', {
        'exception': str(type_),
        'error': error,
    }, status=500)

