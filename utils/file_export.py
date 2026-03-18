from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from docx import Document

def save_as_txt(text, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return filename

def save_as_pdf(text, filename="output.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    lines = text.split('\n')
    y = height - 40
    for line in lines:
        if y < 40:
            c.showPage()
            y = height - 40
        c.drawString(40, y, line)
        y -= 15
    c.save()
    return filename

def save_as_docx(text, filename="output.docx"):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
    return filename

def save_tasks_csv(tasks, filename="tasks.csv"):
    import csv
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Task", "Status"])
        for task in tasks.split('\n'):
            if task.strip():
                writer.writerow([task.strip(), "Pending"])
    return filename
