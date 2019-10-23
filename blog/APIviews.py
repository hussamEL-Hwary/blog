from rest_framework.views import APIView
from .models import Tutorial, Category
from .serializers import TutorialSerializer, CategorySerializer
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


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data)


# get all posts in specific category
class CategoryPostsView(APIView):
    def get(self, request, slug):
        try:
            category = Category.objects.get(category_slug=slug)
        except Category.DoesNotExist:
            return Response(
                data={"message": "category does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        # related posts

        posts = Tutorial.objects.filter(category=category).all()
        
        data = TutorialSerializer(posts, many=True).data
        return Response(data)
