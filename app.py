# Python Script (app.py)
result = 2 + 2

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Python HTML</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            padding: 50px;
        }}
        .result {{
            color: #333;
            font-size: 2em;
        }}
    </style>
</head>
<body>
    <h1>Calculation Result</h1>
    <div class="result">{result}</div>
</body>
</html>
"""

# Salvando o conteúdo HTML em um arquivo
with open("result.html", "w") as file:
    file.write(html_content)

# Abrindo o arquivo HTML no navegador
import webbrowser
webbrowser.open("result.html")
