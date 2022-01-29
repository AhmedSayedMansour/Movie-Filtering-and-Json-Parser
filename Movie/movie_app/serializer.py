from rest_framework import serializers 

class SearchSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, allow_null=True)
    release_date = serializers.DateField(allow_null=True)
    overview = serializers.CharField(max_length=255, allow_null=True)
    popularity = serializers.IntegerField(allow_null=True)
    vote_average = serializers.FloatField(allow_null=True)
    vote_count = serializers.IntegerField(allow_null=True)