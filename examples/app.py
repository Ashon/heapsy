from flask import Flask
from heapsy import HeapDendrogram

app = Flask(__name__)


class LeakObj(object):
    data = 1


leakable = []


@app.route('/leakable')
def leak():
    global leakable
    leakable.append(LeakObj())

    return f'hi {len(leakable)}'


@app.route('/metrics')
def heap_usage():
    hd = HeapDendrogram()
    hd.generate()

    return hd.as_prometheus_metric()


if __name__ == '__main__':
    app.run()
