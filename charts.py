import matplotlib.pyplot as plt
import os, uuid

def generate_chart_from_result(data, labels, title):
    os.makedirs("static/charts", exist_ok=True)
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join("static/charts", filename)

    plt.figure(figsize=(10, 5))
    plt.bar(labels, data, color="skyblue")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()

    return f"/static/charts/{filename}"
