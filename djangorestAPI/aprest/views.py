from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Aprest
from .permissions import IsOwnerOrReadOnly
from .serializers import AprestSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, format=None):  # build API root endpoint
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'aprests': reverse('aprest-list', request=request, format=format)
    })

# Create a read-only endpoint that lists all available Aprest instances
class AprestList(generics.ListCreateAPIView):
    queryset = Aprest.objects.all()
    serializer_class = AprestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """This is to associate aprests with users, when creating aprests."""
        serializer.save(owner=self.request.user)


# Create a detail view of individual Aprests which supports create/read/update/delete-like functionality
class AprestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aprest.objects.all()
    serializer_class = AprestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # added custom permission class IsOwnerOrReadOnly from permisions.py


# The same for Users
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AprestHighlight(generics.GenericAPIView):
    queryset = Aprest.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)
    serializer_class = AprestSerializer

    def get(self,request,*args,**kwargs):
        aprest = self.get_object()
        return Response(aprest.highlighted)

