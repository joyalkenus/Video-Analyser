import json
from youtube_transcript_api import YouTubeTranscriptApi

def save_transcript_as_json_paragraph(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split('v=')[-1]
    
    # Fetch the transcript for the video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Concatenate all text segments into a paragraph
    transcript_paragraph = ' '.join(segment['text'] for segment in transcript)

    return transcript_paragraph
    



# Example usage


