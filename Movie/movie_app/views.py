from django.shortcuts import render
from movie_app.MovieFilter import MovieFilter
from rest_framework import status

@api_view(["GET"])
def search_movie(request):
    try:
        title = request.GET.get("title")
        release_date = request.GET.get("release_date")
        overview = request.GET.get("overview")
        popularity = request.GET.get("popularity")
        vote_average = request.GET.get("vote_average")
        vote_count = request.GET.get("vote_count")

        serializer = SearchSerializer(data={
            'title': title,
            'release_date' : release_date,
            'overview' : overview,
            'popularity' : popularity,
            'vote_average' : vote_average,
            'vote_count' : vote_count,
        })

        filter = MovieFilter(path)
        rows = filter.search(title = title, release_date=release_date, overview=overview, popularity=popularity, vote_average=vote_average, vote_count=vote_count)
        filter.get_full_rows(rows)
        result = df.to_json(orient="index")
        return Response({"result":result},status=status.HTTP_200_OK)

    except:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)