from flask import Flask, render_template, redirect, url_for
from reservations import check_free_slots
from notifications import send_email_notification

app = Flask(__name__)

script_running = False

@app.route("/")
def home():
    global script_running

    if script_running:
        slots = check_free_slots() 
        send_email_notification(slots)  
    else:
        slots = {}  # Jos skripti ei ole päällä, käytetään tyhjää sanakirjaa

    return render_template("index.html", slots=slots, script_running=script_running)

@app.route("/toggle_script", methods=["POST"])
def toggle_script():
    global script_running
    script_running = not script_running
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
