import json

transcript_path = r"C:\Users\dell\.gemini\antigravity\brain\01f28193-a72d-4cd9-9a35-1aa6c949860c\.system_generated\logs\transcript_full.jsonl"
output_path = r"c:\Users\dell\Documentos\Workspace\Pagina Oficial Taboada\footer_untruncated.html"

last_user_input = None
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("type") == "USER_INPUT":
            last_user_input = data

if last_user_input:
    content = last_user_input["content"]
    # We want to extract the footer part.
    # It starts with "el footer porfavro" and ends with "</html>"
    prefix = "el footer porfavro"
    idx = content.find(prefix)
    if idx != -1:
        footer_html = content[idx + len(prefix):].strip()
        with open(output_path, "w", encoding="utf-8") as out:
            out.write(footer_html)
        print("Successfully extracted footer HTML to:", output_path)
    else:
        print("Could not find 'el footer porfavro' in the last user message.")
else:
    print("No user input found in transcript.")
