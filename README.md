# gitpath

A few functions to make working with python
inside git repos easier.

## path handling

`gitpath.root()` returns the absolute path of the repository root
directory

`gitpath.abspath(_rel_path_)` returns an absolute path for a path given relative to the
root directory,
so assuming, this repo resites in `/home/maxnoe/python-gitpath`:

```{python}
import gitpath

print(gitpath.abspath('setup.py'))
```

Will give you:
`/home/maxnoe/python-gitpath/setup.py`

---

Installation 

```bash
pip install git+https://github.com/ruxi/python-gitpath.git
```
