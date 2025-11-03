from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer

@api_view(['GET'])
def index(request):
    qs = Listing.objects.all()
    serializer = ListingSerializer(qs, many=True)
    return Response(serializer.data)
