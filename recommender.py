from googleapiclient.discovery import build

API_KEY = "AIzaSyB5egRjMsSd-Rcm0AyUtf5bsQHqoUtko8M"

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_songs(mood, language):
    query = f"{language} {mood} songs playlist"

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=50,
        videoCategoryId="10"
    )

    response = request.execute()

    songs = []

    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        thumbnail = item['snippet']['thumbnails']['high']['url']

        songs.append({
            "title": title,
            "link": f"https://www.youtube.com/watch?v={video_id}",
            "thumbnail": thumbnail
        })

    return songs