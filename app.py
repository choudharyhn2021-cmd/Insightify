from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from services.youtube_service import get_transcript
from services.groq_service import generate_study_material

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize-notes", methods=["POST"])
def summarize_notes():

    data = request.json

    notes = data["notes"]

    result = generate_study_material(notes)

    return jsonify(
        {
            "result": result
        }
    )


@app.route("/summarize-youtube", methods=["POST"])
def summarize_youtube():

    data = request.json

    url = data["url"]

    transcript = get_transcript(url)

    result = generate_study_material(
        transcript
    )

    return jsonify(
        {
            "result": result
        }
    )


if __name__ == "__main__":
    app.run(debug=True)