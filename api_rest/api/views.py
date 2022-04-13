from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

import json

from .models import NationalTeam


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the World Champions page")


class TeamsView(View):

    # Para eliminar el error CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            # Sabemos que retornaría uno solo pero por las dudas colocamos como si retornara más de un team
            teams = list(NationalTeam.objects.filter(id=id).values())
            if len(teams) > 0:
                team = teams[0]
                datos = { 'message': 'Success' , 'teams': team}
            else:
                datos = { 'message': 'Team not found'}
            return JsonResponse(datos)
        else:
            teams = list(NationalTeam.objects.values())
            if len(teams) > 0:
                datos = { 'message': 'Success' , 'teams': teams}
            else:
                datos = { 'message': 'No teams are available'}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        NationalTeam.objects.create(name=json_data['name'], 
                                    continent=json_data['continent'],
                                    world_champion=json_data['world_champion'])

        datos = { 'message': 'Success'}
        return JsonResponse(datos)


    def put(self, request, id):
        json_data = json.loads(request.body)
        teams = list(NationalTeam.objects.filter(id=id).values())
        if len(teams) > 0:
            team = NationalTeam.objects.get(id=id)
            team.name = json_data['name']
            team.continent = json_data['continent']
            team.world_champion = json_data['world_champion']
            team.save()
            datos = { 'message': 'Success'}
        else:
            datos = { 'message': 'Team not found'}
        return JsonResponse(datos)

    def delete(self, request, id):
        teams = list(NationalTeam.objects.filter(id=id).values())
        if len(teams) > 0:
            team = NationalTeam.objects.get(id=id)
            team.delete()
            datos = { 'message': 'Success'}
        else:
            datos = { 'message': 'Team not found'}
        return JsonResponse(datos)