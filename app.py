from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_readiness(data):
    """
    Calculate internship readiness based on student inputs.
    """

    score = 0
    strengths = []
    weaknesses = []
    recommendations = []

    # -------------------------
    # Programming
    # -------------------------
    programming = int(data.get("programming", 0))

    if programming >= 8:
        score += 20
        strengths.append("Strong programming fundamentals")
    elif programming >= 5:
        score += 14
        strengths.append("Good programming foundation")
        weaknesses.append("Programming needs more practice")
        recommendations.append(
            "Practice Java/Python coding problems regularly."
        )
    else:
        score += 8
        weaknesses.append("Programming fundamentals need improvement")
        recommendations.append(
            "Start with programming basics, loops, functions, arrays and strings."
        )

    # -------------------------
    # DSA
    # -------------------------
    dsa = int(data.get("dsa", 0))

    if dsa >= 8:
        score += 20
        strengths.append("Good Data Structures and Algorithms knowledge")
    elif dsa >= 5:
        score += 13
        weaknesses.append("DSA needs more practice")
        recommendations.append(
            "Practice arrays, strings, linked lists, stacks, queues and sorting."
        )
    else:
        score += 7
        weaknesses.append("DSA is a major improvement area")
        recommendations.append(
            "Start DSA from arrays and strings and gradually move to trees and graphs."
        )

    # -------------------------
    # Core CS
    # -------------------------
    core = int(data.get("core", 0))

    if core >= 8:
        score += 15
        strengths.append("Strong computer science fundamentals")
    elif core >= 5:
        score += 10
        weaknesses.append("Core CS subjects need revision")
        recommendations.append(
            "Revise DBMS, OS, Computer Networks and OOP concepts."
        )
    else:
        score += 5
        weaknesses.append("Core CS fundamentals need improvement")
        recommendations.append(
            "Build fundamentals in DBMS, OS, CN and OOP."
        )

    # -------------------------
    # Projects
    # -------------------------
    projects = int(data.get("projects", 0))

    if projects >= 3:
        score += 15
        strengths.append("Good project portfolio")
    elif projects >= 1:
        score += 10
        weaknesses.append("Project portfolio can be improved")
        recommendations.append(
            "Build 2–3 strong projects and upload them to GitHub."
        )
    else:
        score += 3
        weaknesses.append("No significant projects")
        recommendations.append(
            "Build at least two practical projects related to your target role."
        )

    # -------------------------
    # Aptitude
    # -------------------------
    aptitude = int(data.get("aptitude", 0))

    if aptitude >= 8:
        score += 10
        strengths.append("Strong aptitude preparation")
    elif aptitude >= 5:
        score += 7
        weaknesses.append("Aptitude needs more practice")
        recommendations.append(
            "Practice quantitative aptitude, logical reasoning and verbal ability."
        )
    else:
        score += 3
        weaknesses.append("Aptitude preparation is weak")
        recommendations.append(
            "Practice aptitude questions for at least 20–30 minutes daily."
        )

    # -------------------------
    # Communication
    # -------------------------
    communication = int(data.get("communication", 0))

    if communication >= 8:
        score += 10
        strengths.append("Good communication skills")
    elif communication >= 5:
        score += 7
        weaknesses.append("Communication can be improved")
        recommendations.append(
            "Practice explaining your projects and answering interview questions."
        )
    else:
        score += 3
        weaknesses.append("Communication skills need improvement")
        recommendations.append(
            "Practice speaking about yourself, your projects and technical concepts."
        )

    # -------------------------
    # Resume
    # -------------------------
    resume = int(data.get("resume", 0))

    if resume >= 8:
        score += 10
        strengths.append("Good resume preparation")
    elif resume >= 5:
        score += 7
        weaknesses.append("Resume needs improvement")
        recommendations.append(
            "Create a concise, ATS-friendly one-page resume."
        )
    else:
        score += 3
        weaknesses.append("Resume needs significant improvement")
        recommendations.append(
            "Create an ATS-friendly resume highlighting skills, projects and achievements."
        )

    # -------------------------
    # Readiness level
    # -------------------------

    if score >= 85:
        level = "Excellent"
        message = (
            "You are highly prepared for internship opportunities. "
            "Focus mainly on interview practice and advanced problem solving."
        )

    elif score >= 70:
        level = "Good"
        message = (
            "You have a good internship foundation. "
            "Strengthen your weak areas and start applying actively."
        )

    elif score >= 50:
        level = "Moderate"
        message = (
            "You have started building the required skills, "
            "but several areas need improvement before you are fully internship-ready."
        )

    else:
        level = "Needs Improvement"
        message = (
            "You need to strengthen your fundamentals before focusing heavily "
            "on internship applications."
        )

    return {
        "score": score,
        "level": level,
        "message": message,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.form

    result = calculate_readiness(data)

    return render_template(
        "index.html",
        result=result,
        submitted=True
    )


if __name__ == "__main__":
    app.run(debug=True)