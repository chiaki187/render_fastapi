from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Worldoooooo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return {"result" : omikuji_list[random.randrange(10)]}




##########第９回目課題

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Hi!</h1>
            <h1>Render is very difficult for me!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


#9-2
@app.post("/subject")
async def give_subject(subject):
    return {"response": f"サーバです。 {subject}の試験お疲れ様。結果は100点満点だよ！"}  # f文字列というPythonの機能を使っている


