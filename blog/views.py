from django.shortcuts import render
from datetime import date
# Create your views here.
posts = [
   {
       "slug": "hike-in-the-mountains",
       "image": "mountains.jpg",
       "author": "Hemant",
       "date":  date(2022, 7, 21),
       "title": "Mountain Hiking",
       "excerpt" : """There's nothing like the views you get when hiking in the
            mountains! And I wasn't even prepared for what happened whilst I
            was enjoying the view!""",
        "content": """
             Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
        Dolorem odio ullam dolorum eveniet natus quis, 
        explicabo laborum saepe blanditiis exercitationem consequatur
         debitis reiciendis placeat quos incidunt amet, quod minima ipsum?
             """

   }
]
def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-details.html")
