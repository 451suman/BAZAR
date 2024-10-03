from bazar_app.models import Category, Product, Tag

def navigationFunc(request):
    categories = Category.objects.all().order_by("-created_at")[:5]  # Fetch all categories for navgations
    tags = Tag.objects.all().order_by("-created_at")[:7]  # Fetch the first 10 tags for navgations
    deals = Product.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-published_at")
    
    return {
        "categories": categories,
        "tags": tags,
        "deals": deals,
    }
