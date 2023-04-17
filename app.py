import os
import youtube_dl
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('video_url')

        # Extract video URL and metadata using youtube-dl
        ydl_opts = {'quiet': True}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video = info_dict['entries'][0] if 'entries' in info_dict else info_dict
            extracted_video_url = video['url']
            extracted_user_id = video['uploader_id']
            extracted_date = f"{video['upload_date'][:4]}-{video['upload_date'][4:6]}-{video['upload_date'][6:]}"

        return jsonify({
            "video_url": extracted_video_url,
            "user_id": extracted_user_id,
            "date": extracted_date
        })

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


