import sys

file_path = "/Users/wilsonvan/Thỏ/QC12/mysecond.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# CSS lines: 1780 to 1869 (I'll need to check the exact end of CSS)
# Let's read first to just delete HTML and JS
# HTML: 3160 to 3209
# JS: 6602 to 6669

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the button texts
text = text.replace(
    'rBtn.innerHTML = `<span style="margin-right:8px;">🔮</span><span>View Summary</span>`;\n                    rBtn.onclick = () => showSummary();',
    'rBtn.innerHTML = `<span style="margin-right:8px;">🔮</span><span>Restart Ritual</span>`;\n                    rBtn.onclick = () => resetQuiz();'
)

text = text.replace(
    'cleanup3D();\n                                        showSummary();',
    'cleanup3D();\n                                        resetQuiz();'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

