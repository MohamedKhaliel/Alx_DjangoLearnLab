from django.shortcuts import render

#["viewsets", "viewsets.ModelViewSet", "Comment.objects.all()", "Post.objects.all()"]
# Create your views here.

#["Post.objects.filter(author__in=following_users).order_by"
# "following.all()"
# "permissions.IsAuthenticated"]
#["generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)", "Notification.objects.create"]