import argparse

from sanic import Sanic
from sanic.response import json

app = Sanic('simple-app')


@app.route('/')
async def index(_request):
    return json({'hello': 'world'})


@app.route('/health')
async def health(_request):
    return json({'status': 'OK'})


def parse_arguments():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-p', '--port', type=int, help='port number', default=80)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    port = args.port
    app.run(host='0.0.0.0', port=port)
