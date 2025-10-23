from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import os

DB_FILE = "quiz_results.json"

def load_results():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    return []

def save_results(results):
    with open(DB_FILE, "w") as file:
        json.dump(results, file, indent=4)

@api_view(['GET'])
def get_top_players(request):
    results = load_results()
    top_players = sorted(results, key=lambda x: x.get("score", 0), reverse=True)[:5]
    return Response(top_players)

@api_view(['POST'])
def save_result(request):
    new_result = request.data
    results = load_results()
    results.append(new_result)
    save_results(results)
    return Response({"message": "Wynik zapisany pomyślnie!"}, status=status.HTTP_200_OK)
