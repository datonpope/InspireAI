from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")
openai.api_key = api_key


def query_gpt3(prompt):
    new_prompt = f"Using the following keywords or themes: '{prompt}', create a unique and engaging story prompt for writers.\n\nStory Prompt:"

    response = openai.Completion.create(
        engine="davinci",
        prompt=new_prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    response_text = query_gpt3(prompt)
    return jsonify({"response": response_text})


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    response_text = query_gpt3(prompt)
    return jsonify({"response": response_text})
