from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from config.config import Config

from .models import Note

def index(request):
    context = { 
        "app_name" : Config.__APP_NAME__,
        "app_version" : Config.__APP_VER__,
    }
    return render(request, 'index.html', context=context)

@csrf_exempt
def save_text(request):
    if request.method == 'POST':
        # Get the content from the textarea named 'content'
        # content = request.POST.get('content', '')
        data = json.loads(request.body)

        new_note = Note(
            title=data['title'],
            content=data['content']
        )

        try: 
            new_note.save()

        except Exception as e:
            return JsonResponse({ "message" : f"error: {e}" }, status=400)

        # Process the content as needed (save to database, manipulate, etc.)
        # For now, we'll just return it as a response
        return JsonResponse({ "message" : "Note Saved" }, status=200)
    

def get_all_notes(request):
    # Query all notes from the database
    notes = Note.objects.all()

    # Create a list of dictionaries for each note
    notes_list = [
        {
            "note-id": note.id,
            "note-title": note.title,
            "note-content": note.content,
            "created-at": note.created_at.strftime("%d / %b / %Y %I:%M %p")  # Custom format
        }
        for note in notes
    ]

    # Return the JSON response
    return JsonResponse(notes_list, safe=False)