from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from symposium.models import Exhibition_Entry
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
# Retrieve all Exhibition_Entry objects
Exhibition_Entries = Exhibition_Entry.objects.all()


# Landing page
def index(request):
    return render(request, 'symposium/index.html')


# Model view
def model(request, pk):
    # Get a specific Exhibition_Entry object based on the provided slug
    Exhibit_Wall_Display = Exhibition_Entries.get(slug=pk)
    return render(request, 'symposium/model.html', {"Exhibition_Entry": Exhibit_Wall_Display})


# Exhibition booth
def exhibition(request):
    return render(request, 'symposium/exhibition_booth.html')

# Infodesk
def infodesk(request):
    return render(request, 'symposium/infodesk.html')


# Lobby
def lobby(request):
    return render(request, 'symposium/lobby.html', {"Exhibition_Entries": Exhibition_Entries})

def ok(request):
    return HttpResponse("ok working in symposium")

##################################### WE HAD CREATED THE EDIT PAGE AS THE EARLIER APPRAOCH INCLUDED A STUDENT BASED UPLOAD MODEL #####################################

# User upload space
# @login_required(login_url="/login")
# def upload_model(request):
#     if request.method == "POST":
#         # Attempt to sign user in
#         description = request.POST["description"]
#         title = request.POST["title"]
#         poster = request.FILES.get("poster")
#         model = request.FILES.get("model")
#         front_view = request.FILES.get("front_view")

#         # Create a new Exhibition_Entry object and set its attributes
#         exhibition_entry = Exhibition_Entry()
#         exhibition_entry.username = request.user.username
#         exhibition_entry.poster = poster
#         exhibition_entry.exhibition_wall = model

#         if front_view is not None:
#             exhibition_entry.exhibition_front_view = front_view
#         else:
#             exhibition_entry.exhibition_front_view = "profile_pic/no_pic.png"
#         if model is not None:
#             exhibition_entry.exhibition_wall = model
#         else:
#             exhibition_entry.exhibition_wall = "profile_pic/no_pic.png"
#         if poster is not None:
#             exhibition_entry.poster = poster
#         else:
#             exhibition_entry.poster = "profile_pic/no_pic.png"

#         exhibition_entry.description = description
#         exhibition_entry.title = title
#         exhibition_entry.save()
#         messages.success(request, 'Upload successful!')
#         return render(request, "symposium/upload.html")
#     else:
#         return render(request, "symposium/upload.html")


# @login_required(login_url="/login")
# def edit_model(request, entry_id):
#     if request.method == "POST":
#         # Get the Exhibition_Entry object with the provided entry_id
#         obj = Exhibition_Entry.objects.get(id=entry_id)
#         description = request.POST["description"]
#         title = request.POST["title"]
#         poster = request.FILES.get("poster")
#         model = request.FILES.get("model")
#         front_view = request.FILES.get("front_view")

#         if front_view is not None:
#             obj.exhibition_front_view = front_view
#         if model is not None:
#             obj.exhibition_wall = model
#         if poster is not None:
#             obj.poster = poster
#         if description is not None: 
#             obj.description = description
#         if title is not None:
#             obj.title = title    
#         obj.save()
#         messages.success(request, 'Upload successful!')
#         return render(request, "symposium/editModel.html")
#     else:
#         user_name = request.user.username
#         exhibition_model = Exhibition_Entry.objects.filter(id=entry_id)
#         if exhibition_model is None:
#             return render(request, "symposium/upload.html")
#         return render(request, 'symposium/editModel.html', {'exhibition_model': exhibition_model})



# @login_required(login_url="/login")
# def edit_page(request):
#     user_name = request.user.username
#     exhibition_entries = Exhibition_Entry.objects.filter(username=user_name)
#     return render(request, 'symposium/editPage.html', {'exhibition_entries': exhibition_entries})


@login_required(login_url="/login")
def model_page(request, pk):
    # Get a specific Exhibition_Entry object based on the provided slug
    Current_Exhibit = Exhibition_Entries.get(slug=pk)
    return render(request, 'symposium/modelPage.html', {'Exhibit': Current_Exhibit})