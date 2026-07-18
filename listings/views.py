# views.py
from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

def dashboard(request):
    return render(request, 'dashboard.html')

def create_listing(request):
    flow = request.POST.get('flow') or request.GET.get('flow', 'offer')
    
    listings = None
    query = None
    form = None

    if flow == 'seek':
        listings = Listing.objects.all().order_by('-created_at')
        query = request.GET.get('dept_code')
        if query:
            listings = listings.filter(dept_code__icontains=query.strip())
            
    else:
        # OFFER FLOW: Handle processing the simple HTML form
        if request.method == 'POST':
            form = ListingForm(request.POST)
            if form.is_valid():
                # 1. Tell Django to look at the data but DON'T save to DB yet
                listing = form.save(commit=False)
                
                # 2. Explicitly inject the missing field value
                listing.listing_type = 'OFFER'
                
                # 3. Now safely commit it to the database
                listing.save()
                
                return redirect('dashboard')
        else:
            form = ListingForm()

    return render(request, 'create_form.html', {
        'flow': flow,
        'form': form,
        'listings': listings,
        'query': query
    })