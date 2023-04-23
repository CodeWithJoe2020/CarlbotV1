from googleapiclient.discovery import build

# Set up the API client
api_key = ""
youtube = build("youtube", "v3", developerKey=api_key)

# Get the channel ID
channel_name = "MMCryptoTube"
channel_response = youtube.search().list(
    q=channel_name,
    type="channel",
    part="id"
).execute()
channel_id = channel_response["items"][0]["id"]["channelId"]

# Set the maximum number of results per request and the total number of results to get
max_results = 600
total_results = 1000

# Get the videos from the channel
video_titles = []
next_page_token = None
while len(video_titles) < total_results:
    videos_response = youtube.search().list(
        channelId=channel_id,
        type="video",
        part="id,snippet",
        maxResults=max_results,
        pageToken=next_page_token
    ).execute()

    # Extract the video titles
    for item in videos_response["items"]:
        title = item["snippet"]["title"]
        video_titles.append(title)

    # Check if there are more pages to get
    if "nextPageToken" in videos_response:
        next_page_token = videos_response["nextPageToken"]
    else:
        break

# Print the video titles
print(video_titles)
# Save the video titles to a file
with open("video_titles_raw.txt", "w") as f:
    for title in video_titles:
        f.write(title + "\n")



