from rest_framework.views import APIView
from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework.response import Response
from rest_framework.views import status

class PostView(APIView):
    def get(self, request):
        # get latest added posts
        latest_posts = Tutorial.objects.all().order_by('-created_at')[:10]
        data = TutorialSerializer(latest_posts, many=True).data
        return Response(data)


class PostDetail(APIView):
    def get(self, request, slug):
        try:
            a_post = Tutorial.objects.get(slug=slug)
            return Response(TutorialSerializer(a_post).data)
        except Tutorial.DoesNotExist:
            return Response(
                data={"message": "post not found"},
                status=status.HTTP_404_NOT_FOUND
            )
