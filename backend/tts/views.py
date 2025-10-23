from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from gtts import gTTS
import io
import json
import os

LOG_FILE = "logs.json"

def save_log(data):
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append(data)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

@api_view(['POST'])
def tts(request):
    data = request.data or {}
    save_log(data)
    text = data.get("text")
    lang = data.get("lang", "pl")
    slow = bool(data.get("slow", False))

    if not text:
        return Response({"error": "Brak pola 'text'"}, status=status.HTTP_400_BAD_REQUEST)

    tts_obj = gTTS(text=text, lang=lang, slow=slow)
    buf = io.BytesIO()
    tts_obj.write_to_fp(buf)
    buf.seek(0)
    response = FileResponse(buf, content_type="audio/mpeg")
    response['Content-Disposition'] = 'attachment; filename="tts.mp3"'
    return response
