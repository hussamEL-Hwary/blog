from rest_framework.views import APIView
from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework.response import Response

class PostView(APIView):
    def get(self, request):
        # get latest added posts
        latest_posts = Tutorial.objects.all().order_by('-created_at')[:10]
        data = TutorialSerializer(latest_posts, many=True).data
        return Response(data)
