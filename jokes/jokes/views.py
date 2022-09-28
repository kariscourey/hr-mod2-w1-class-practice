from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Joke
import json
from common.json import ModelEncoder


class JokePunchOnlyEncoder(ModelEncoder):
    model=Joke
    properties=[
        "punchline",
    ]


class JokeEncoder(ModelEncoder):
    model=Joke
    properties=[
        "setup",
        "punchline",
        "laugh_count"
    ]

@require_http_methods(["GET", "POST"])
def jokes(request):
    if (request.method == "GET"):
        jokes = Joke.objects.all()
        return JsonResponse(
            jokes,
            encoder=JokeEncoder,
            # encoder=JokePunchOnlyEncoder,
            safe=False,
        )

        # response = []
        # for joke in jokes:
        #     response.append({
        #         "setup": joke.setup,
        #         "punchline": joke.punchline,
        #         "laugh_count": joke.laugh_count,
        #     })

        # return JsonResponse({
        #     "jokes": response,
        # })

    else:
        joke_data = json.loads(request.body)
        Joke.objects.create(setup=joke_data["setup"], punchline=joke_data["punchline"])

        return JsonResponse(
            joke,
            encoder=JokeEncoder,
            safe=False,
        )

        # return JsonResponse({
        #     "setup": joke.setup,
        #     "punchline": joke.punchline,
        #     "laugh_count": joke.laugh_count,
        # })

    # if (request.method == "POST"):
    #     return JsonResponse({
    #         "status": "succesful create",
    #     })


@require_http_methods(["GET", "PUT", "DELETE"])
def joke(request, id):

    try:
        joke = Joke.objects.get(id=id)
    except Joke.DoesNotExist:
        return JsonResponse({
            "message": "Joke Not Found",
            "status":404,
        })

    # jokes = Joke.objects.filter(id=id)

    # if len(jokes) == 0:
    #     return JsonResponse({
    #         "message": "Joke Not Found",
    #         "status":404,
    #     })

    # joke = Joke.objects.filter(id=id)[0]


    if (request.method == "GET"):
        return JsonResponse(
            joke,
            encoder=JokeEncoder,
            safe=False,
        )

        # return JsonResponse({
        #     "status": f"successful read: {id}"
        # })

    elif (request.method == "PUT"):
        joke_data = json.loads(request.body)

        for key in joke_data:
            setattr(joke, key, joke_data[key])
        joke.save()

        return JsonResponse(
            joke,
            encoder=JokeEncoder,
            safe=False,
        )

        # return JsonResponse({
        #     "status": f"successful update: {id}"
        # })

    elif (request.method == "DELETE"):
        joke.delete()

        return JsonResponse({
            "status": f"deteled successfully",
        }
        )

        # return JsonResponse({
        #     "status": f"successful update: {id}"
        # })

@require_http_methods(["PUT"])
def add_laugh(request, id):
    try:
        joke = Joke.objects.get(id=id)
    except Joke.DoesNotExist:
        return JsonResponse({
            "message": "Joke Not Found",
            "status":404,
        })

    joke.laugh_count += 1
    joke.save()

    return JsonResponse(
        joke,
        encoder=JokeEncoder,
        safe=False,
    )
