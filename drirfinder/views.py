from django.shortcuts import render
from drirfinder.models import Category
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = Category.objects.order_by('-cpi')[:5]
    context_dict = {'categories': category_list}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'drirfinder/index.html', context_dict)


def display(request):
	category_list = Category.objects.order_by('-cpi')[:5]
	context_dict = {'categories': category_list}
	return render(request, 'drirfinder/display.html', context_dict)