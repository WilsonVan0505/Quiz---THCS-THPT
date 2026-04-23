import sys
import re

file_path = "/Users/wilsonvan/Thỏ/QC12/mysecond.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# remove HTML overlay
html_start_marker = "<!-- Final Ritual Summary Overlay -->"
if html_start_marker in text:
    start_idx = text.find(html_start_marker)
    # find the next line with <script> to know where to stop loosely?
    # actually div id="summary-overlay" has matching pairs.
    end_idx = text.find("<!-- Mystery Card Template -->", start_idx) 
    # Let me check if there's a good end marker.
    # Actually, I'll just use regex for the whole block.
    # It starts with <!-- Final Ritual Summary Overlay --> and ends before <!-- AUDIO --> or something.
    pass

# Remove JS function
js_pattern = re.compile(r'        function showSummary\(\) \{.*?(?=\n        function playAlertSound\(\) \{)', re.DOTALL)
text = js_pattern.sub('', text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

