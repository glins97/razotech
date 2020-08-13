from .models import IOTDevice, Lamp, Request, Person, Access
from django.http import JsonResponse

def get_lamps_endpoint(request, mac):
    person = Person.objects.filter(user=request.user).first()
    if not person:
        return JsonResponse({})

    device = Lamp.objects.filter(mac=mac).first()
    if not device:
        return JsonResponse({})
    
    access = Access.objects.filter(person=person, building=device.space.building)
    if not access:
        return JsonResponse({})

    devices = [ {
            attr: getattr(device, attr) for attr in ['mac', 'circuit', 'status'] 
        } for device in Lamp.objects.filter(mac=mac)
    ]
    return JsonResponse(devices, safe=False)

def update_lamps_endpoint(request, mac, circuit, status):
    person = Person.objects.filter(user=request.user).first()
    if not person:
        return JsonResponse({})

    device = Lamp.objects.filter(mac=mac, circuit=circuit).first()
    if not device:
        return JsonResponse({})
    
    access = Access.objects.filter(person=person, building=device.space.building)
    if not access:
        return JsonResponse({})
    
    if device:
        Request(person=person, device=device, status=status).save()
        device.status = status
        device.save()
    return JsonResponse({
        attr: getattr(device, attr) for attr in ['mac', 'circuit', 'status'] 
    }, safe=False)