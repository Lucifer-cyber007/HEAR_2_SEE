for f in *.mp3; do ffmpeg -i "$f" -ar 16000 -ac 1 "${f%.mp3}.wav"; done
