from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import User, Pet
from .serializers import PetSerializer, UserSerializer


@api_view(['GET'])
def get_pets(request):
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_pets_by_name(request):
    pet_name = request.GET.get('pet_name', None)
    if pet_name is not None:
        pets = Pet.objects.filter(pet_name__icontains=pet_name)
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)
    else:
        return Response({"error': 'Не вказано ім'я"}, status=400)


@api_view(['POST'])
def add_pet(request):
    serializer = PetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({'error': 'Some parameters are required'}, status=400)
    return Response(serializer.data)


@api_view(['GET'])
def search_user_by_id(request):
    user_id = request.GET.get('id', None)
    print(user_id)
    if user_id is not None:
        user = User.objects.filter(id__icontains=user_id)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    else:
        return Response({"error': 'Неправильне ID"}, status=400)