from django.shortcuts import render

# Create your views here.
finches = [
    {"species": "Galapagos Finch", "beak_length": 10.5, "beak_width": 3.2, "color": "brown"},
    {"species": "Darwin's Finch", "beak_length": 8.7, "beak_width": 2.5, "color": "yellow"},
    {"species": "Gouldian Finch", "beak_length": 12.0, "beak_width": 4.0, "color": "red"},
    {"species": "Zebra Finch", "beak_length": 9.2, "beak_width": 2.8, "color": "black"},
    {"species": "Society Finch", "beak_length": 11.1, "beak_width": 3.5, "color": "white"},
    # Add more finch dictionaries as needed
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })