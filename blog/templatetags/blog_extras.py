from django import template
from django.contrib.auth import get_user_model
from blog.models import Post
user_model = get_user_model()
register = template.Library()


@register.filter(name="author_details")
def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""
    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"
    return name



@register.inclusion_tag("blog/post-list.html")
def recent_posts(*args):
    if args:
        posts = Post.objects.exclude(pk=args[0].pk)[:5]
        return {"posts": posts}
    else:
        posts = Post.objects.all()[:5]
        return {"posts": posts}


