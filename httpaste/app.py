from flask import Flask, render_template, request
from pynput.keyboard import Controller, Key
from argparse import ArgumentParser

app = Flask(__name__)
kb = Controller()


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        for char in request.form["code"]:
            if char == "\t":
                kb.tap(Key.tab)
            elif char == "\n" or char=="\r\n":
                kb.tap(Key.enter)
            else:
                kb.tap(char)
    return render_template("home.html")


def main():
    parser = ArgumentParser()
    parser.add_argument("-p", "--port", default=8080,
                        type=int, help="Quickpaste listen port")
    parser.add_argument("-i", "--iface", default="0.0.0.0",
                        help="Quickpaste Network Interface")
    args = parser.parse_args()
    IFACE = args.iface
    PORT_NO = args.port
    app.run(host=IFACE, port=PORT_NO)


if __name__ == "__main__":
    main()
