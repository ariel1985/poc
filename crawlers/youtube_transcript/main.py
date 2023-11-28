from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube

def download_transcript(video_id, filename):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_generated_transcript(["iw"]).fetch()

        with open(filename, 'w') as file:
            for line in transcript:
                file.write(line['text'] + '\n')

        print(f"Transcript saved to {filename}")
    except Exception as e:
        print(f"Error occurred: {e}")

youtubeID = 'eDVTxkF-tHY'
url2scoop = 'https://www.youtube.com/watch?v=' + youtubeID
output_folder = youtubeID + '.txt'

download_transcript( youtubeID,output_folder)
