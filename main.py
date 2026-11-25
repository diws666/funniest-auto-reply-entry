import os

LINE = "I am out of office today. My human finally approved my day off, so I am using it to do absolutely nothing, efficiently."  # verified: 119 chars, 119 bytes

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(f"wrote {len(LINE.encode('utf-8'))} bytes to {os.path.join(output_dir, 'entry.txt')}")
