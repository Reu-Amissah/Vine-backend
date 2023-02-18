from django.http import JsonResponse

def api_contact (request, *args, **kwarg):
    return JsonResponse({"message" : "Hello there, this is your Django API Response!!"})