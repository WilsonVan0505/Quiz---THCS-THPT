import sys

file_path = "/Users/wilsonvan/Thỏ/QC12/mysecond.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

out_lines = []
skip_html = False
skip_js = False
skip_css = False

for i, line in enumerate(lines):
    if 'id="summary-overlay"' in line:
        skip_html = True
    
    if skip_html and '<!-- Finished summary overlay' in line: # doesn't exist, wait
        pass
        
    if skip_html and '</div>' in line and lines[i-1].strip() == '</div>' and lines[i-2].strip() == '</button>': # heuristic to stop
        # wait it's better to just use known line numbers
        pass

# Since line numbers can shift after string replace, let's just do text block replace.
