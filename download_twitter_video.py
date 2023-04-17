import os
import yt_dlp

def download_video(tweet_url, output_folder="output"):
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(uploader_id)s_%(upload_date)s-%(id)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
        'restrictfilenames': True,
        'noplaylist': True
    }
    try:
        os.makedirs(output_folder, exist_ok=True)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([tweet_url])
        print(f"Video downloaded to {output_folder}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    urls = input("Enter the Twitter video URLs separated by commas: ")
    tweet_urls = urls.strip().split(',')

    for tweet_url in tweet_urls:
        tweet_url = tweet_url.strip()
        download_video(tweet_url)

if __name__ == "__main__":
    main()
