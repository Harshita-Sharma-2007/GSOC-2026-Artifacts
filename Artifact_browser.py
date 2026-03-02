import os
import json
import re
import tkinter as tk
from tkinter import filedialog
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ================= BASIC FUNCTIONS =================

def list_artifacts():
    return [
        f for f in os.listdir(BASE_DIR)
        if os.path.isdir(os.path.join(BASE_DIR, f))
        and not f.startswith(".")
    ]

def show_artifact_info(folder_name):
    info_path = os.path.join(BASE_DIR, folder_name, "info.txt")
    if os.path.exists(info_path):
        with open(info_path, "r", encoding="utf-8") as f:
            print(f"\n=== {folder_name} Information ===\n")
            content = f.read()
            print(content)
            return content
    else:
        print("\ninfo.txt not found.")
        return ""

# ================= SEARCH ENGINE =================

def search_artifacts(query, mode="AND", use_regex=False):
    keywords = query.lower().split()
    results = []

    for folder in list_artifacts():
        folder_text = folder.lower()
        info_text = ""
        info_file = os.path.join(BASE_DIR, folder, "info.txt")

        if os.path.exists(info_file):
            with open(info_file, "r", encoding="utf-8") as f:
                info_text = f.read().lower()

        combined_text = folder_text + " " + info_text
        score = 0

        if use_regex:
            try:
                pattern = re.compile(query, re.IGNORECASE)
                matches = pattern.findall(combined_text)
                score = len(matches)
                if score > 0:
                    results.append({"artifact": folder, "score": score})
            except re.error:
                print("Invalid regex pattern.")
                return []

        elif mode == "AND":
            match = True
            for kw in keywords:
                if kw in combined_text:
                    score += 1
                else:
                    match = False
                    break
            if match:
                results.append({"artifact": folder, "score": score})

        elif mode == "OR":
            for kw in keywords:
                if kw in combined_text:
                    score += 1
            if score > 0:
                results.append({"artifact": folder, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    return results

# ================= EXPORT FUNCTIONS =================

def export_json_with_dialog(data):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")],
        title="Save JSON As"
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"JSON saved at: {file_path}")
    else:
        print("JSON save cancelled")

def export_pdf_with_dialog(title, lines):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save PDF As"
    )
    if file_path:
        doc = SimpleDocTemplate(file_path)
        styles = getSampleStyleSheet()
        story = [Paragraph(f"<b>{title}</b>", styles["Title"])]
        story.append(Paragraph("<br/>", styles["Normal"]))

        for line in lines:
            story.append(Paragraph(line, styles["Normal"]))

        doc.build(story)
        print(f"PDF saved at: {file_path}")
    else:
        print("PDF save cancelled")

# ================= MAIN MENU =================

print("\n=== ASL MRI Artifact Browser ===")
print("1. Browse Artifacts")
print("2. Search (AND logic)")
print("3. Search (OR logic)")
print("4. Regex Search")

choice = input("\nEnter choice (1-4): ")

# ================= OPTION 1: BROWSE =================

if choice == "1":
    artifacts = list_artifacts()

    if not artifacts:
        print("No artifacts found.")
    else:
        print("\nAvailable Artifacts:\n")
        for i, art in enumerate(artifacts, start=1):
            print(f"{i}. {art}")

        try:
            selected = int(input("\nSelect artifact number: "))
            if 1 <= selected <= len(artifacts):
                artifact_name = artifacts[selected - 1]
                content = show_artifact_info(artifact_name)

                if content:
                    save_json = input("\nDo you want to save JSON? (y/n): ").lower()
                    if save_json == "y":
                        export_json_with_dialog({
                            "mode": "browse",
                            "artifact": artifact_name,
                            "content": content
                        })

                    save_pdf = input("\nDo you want to save PDF? (y/n): ").lower()
                    if save_pdf == "y":
                        lines = content.split("\n")
                        export_pdf_with_dialog(f"Artifact: {artifact_name}", lines)

            else:
                print("Invalid selection")

        except ValueError:
            print("Please enter a valid number.")

# ================= SEARCH OPTIONS =================

elif choice in ["2", "3", "4"]:
    query = input("\nEnter search query: ")

    if choice == "2":
        results = search_artifacts(query, mode="AND")
    elif choice == "3":
        results = search_artifacts(query, mode="OR")
    else:
        results = search_artifacts(query, use_regex=True)

    if not results:
        print("\nNo matching artifacts found.")
    else:
        print("\nSearch Results (Ranked):\n")
        for i, res in enumerate(results, start=1):
            print(f"{i}. {res['artifact']} (Score: {res['score']})")

        try:
            selected = int(input("\nSelect artifact number to view: "))
            if 1 <= selected <= len(results):
                artifact_name = results[selected - 1]["artifact"]
                content = show_artifact_info(artifact_name)

                if content:
                    save_json = input("\nDo you want to save JSON? (y/n): ").lower()
                    if save_json == "y":
                        export_json_with_dialog({
                            "mode": "search",
                            "query": query,
                            "artifact": artifact_name,
                            "content": content
                        })

                    save_pdf = input("\nDo you want to save PDF? (y/n): ").lower()
                    if save_pdf == "y":
                        lines = content.split("\n")
                        export_pdf_with_dialog(f"Artifact: {artifact_name}", lines)

            else:
                print("Invalid selection")

        except ValueError:
            print("Please enter a valid number.")

else:
    print("Invalid choice.")