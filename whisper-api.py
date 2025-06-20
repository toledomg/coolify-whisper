from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("base")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file"}), 400
    audio = request.files["file"]
    path = "/tmp/audio.wav"
    audio.save(path)
    result = model.transcribe(path, language="pt")
    os.remove(path)
    return jsonify({"text": result["text"]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
