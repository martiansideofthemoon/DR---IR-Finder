from django.shortcuts import render
from drirfinder.models import Category
from drirfinder.forms import CategoryForm
def index(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return display(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'drirfinder/index.html', {'form': form})


def display(request):
	category_list = Category.objects.order_by('-cpi')[:5]
	context_dict = {'categories': category_list}
	return render(request, 'drirfinder/display.html', context_dict)