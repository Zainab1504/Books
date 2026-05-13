from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)
FLAG = "JIC{Zainab_collision_master}"

HTML = '''
<h1> books</h1>
<p>Upload two <strong>different</strong> files with the <strong>same MD5 hash</strong>.</p>
<form method="POST" enctype="multipart/form-data">
  <input type="file" name="file1" required><br><br>
  <input type="file" name="file2" required><br><br>
  <button type="submit">Check Books</button>
</form>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f1 = request.files.get("file1")
        f2 = request.files.get("file2")
        if not f1 or not f2:
            return "Upload both files."

        data1 = f1.read()
        data2 = f2.read()
        h1 = hashlib.md5(data1).hexdigest()
        h2 = hashlib.md5(data2).hexdigest()

        if data1 != data2 and h1 == h2:
            return f"🎉 Success! Flag: {FLAG}"
        else:
            return f"Hashes:<br>{h1}<br>{h2}<br>No flag. Files must be different but hash the same."

    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
