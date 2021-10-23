# absolute-import-py3
## Overview
- Examples of inner module import (e.g. to import m1 which import m2 by writing import m2 in the top line of m1) by creating [__init__.py](module/__init__.py).
- **Without** relative path and any modification to submodules (in this example, [child](module/child) is not edited)
- Only for Python3

## Structure
```
main.py
module
├── __init__.py
├── m1.py # `import m2` is written
├── m2.py
└── child
    ├── m3.py
    └── m4.py `import m3` is written

```

## Run
```shell script
python main.py
```

## Comment
本サンプルの`child/`に相当する部分に，`git submodule add`で取り込んだパッケージを入れられるはず

## References
- https://qiita.com/ysk24ok/items/2711295d83218c699276
- https://chaika.hatenablog.com/entry/2018/08/24/090000
