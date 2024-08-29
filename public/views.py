from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from config.config import Config, HttpResponseCodes

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
    
    else:
        return JsonResponse({ "Message": "Method not allowed" }, status=403) #todo: check for correct 

 
@csrf_exempt
def get_all_notes(request):
    if request.method == 'GET':
        notes = Note.objects.all()

        # Create a list of dictionaries for each note
        notes_list = [
            {
                "note-id"       : note.id,
                "note-title"    : note.title,
                "note-content"  : note.content,
                "created-at"    : note.created_at.strftime("%d / %b / %Y %I:%M %p")  
            }
            for note in notes
        ]

        # Return the JSON response
        return JsonResponse(notes_list, safe=False)
    
    return JsonResponse({ "message" : "method not allow" }, status=HttpResponseCodes.response_codes['method-not-allowed'])
    


@csrf_exempt
def delete_by_id(request, id):
    if request.method == 'DELETE':
        try:
            note = Note.objects.get(id=id)
            note.delete()
            return JsonResponse({'result': 'Note deleted successfully'})
        except Note.DoesNotExist:
            return JsonResponse({'result': 'Note not found'}, status=404)

    return JsonResponse({ "message" : "method not allow" }, status=HttpResponseCodes.response_codes['method-not-allowed'])


@csrf_exempt
def update_by_id(request, id):
    pass