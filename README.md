# Heapsy

python heap tracer

## Install

``` sh
pip install heapsy
```

## Usage

``` python
from heapsy import HeapDendrogram

dendrogram = HeapDendrogram(
    # referrer depth (default 5)
    max_depth=5,

    # trace 10000 objects (default 10000)
    max_items=10000,

    # ignore types (default [])
    ignore_types=['list', 'of', 'types'],

    # ignore module list (default ['builtins'])
    ignore_modules=['ignore', 'my', 'module']
)

# generate heap dendrogram
dendrogram.generate()

# print prometheus exporter format
print(dendrogram.as_prometheus_metric())
```

## Examples

See [./examples](./examples)

## License

MIT
