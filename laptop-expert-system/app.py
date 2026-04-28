from flask import Flask, render_template, request

app = Flask(__name__)

issue_rules = {
    "Battery Problem": {
        "symptoms": ["battery draining fast", "not charging", "laptop shuts down suddenly", "battery percentage fluctuates"],
        "required": 2,
        "advice": "Check charger, replace battery if needed, reduce background apps, and lower brightness."
    },
    "Overheating Issue": {
        "symptoms": ["laptop heating", "fan noise", "slow performance", "automatic shutdown"],
        "required": 2,
        "advice": "Clean cooling fan, use cooling pad, avoid heavy usage for long periods."
    },
    "Software Crash": {
        "symptoms": ["apps crashing", "system freezing", "blue screen", "slow startup"],
        "required": 2,
        "advice": "Update OS, reinstall software, scan for malware, increase RAM if needed."
    },
    "Internet Connectivity Issue": {
        "symptoms": ["wifi not connecting", "slow internet", "network disconnecting", "limited access"],
        "required": 2,
        "advice": "Restart router, update network drivers, check WiFi settings."
    },
    "Keyboard Problem": {
        "symptoms": ["keys not working", "wrong characters typing", "keyboard unresponsive"],
        "required": 2,
        "advice": "Clean keyboard, check drivers, or use external keyboard."
    },
    "Display Issue": {
        "symptoms": ["screen flickering", "black screen", "low brightness", "lines on screen"],
        "required": 2,
        "advice": "Update display drivers, check cable connection, or consult technician."
    }
}

all_symptoms = [
    "battery draining fast", "not charging", "laptop shuts down suddenly", "battery percentage fluctuates",
    "laptop heating", "fan noise", "slow performance", "automatic shutdown",
    "apps crashing", "system freezing", "blue screen", "slow startup",
    "wifi not connecting", "slow internet", "network disconnecting", "limited access",
    "keys not working", "wrong characters typing", "keyboard unresponsive",
    "screen flickering", "black screen", "low brightness", "lines on screen"
]

def diagnose(user_symptoms):
    results = []

    for issue, info in issue_rules.items():
        matched = [s for s in info["symptoms"] if s in user_symptoms]
        match_count = len(matched)

        if match_count >= info["required"]:
            confidence = (match_count / len(info["symptoms"])) * 100
            results.append({
                "issue": issue,
                "matched": matched,
                "confidence": round(confidence, 1),
                "solution": info["advice"]
            })

    return results


@app.route("/", methods=["GET", "POST"])
def home():
    results = None

    if request.method == "POST":
        user_symptoms = request.form.getlist("symptoms")
        results = diagnose(user_symptoms)

    return render_template("index.html", symptoms=all_symptoms, results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)