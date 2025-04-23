# 🥩 git roast

> Roast your code. Roast your coworkers. Roast **yourself.**  
> Because `git blame` was too polite.

fun for the whole family :D

```
$ git roast README.md

meepstertron committed this disaster on 2025-04-23.
Message: "added readme"
This file has been touched 1 time. Almost a virgin.
Last edit was at 2PM — clearly a decision only made by a mentally sane user.
```



## 🔥 What is this?

`git roast` is a spicy CLI tool that digs through your git history and serves up **roasts** based on:

- 🕒 commit time ("3AM code goblin detected")
- 🧠 message vibes ("final fix fr" = lies)
- 📈 line change chaos
- 😬 who wrote it

Basically, it’s `git blame` with *personality issues*.



## 🚀 Install

### With Python
```bash
pip install git-roast
```

Or clone and run:
```bash
git clone https://github.com/meepstertron/git-roast
cd git-roast
```
run it directly:
```bash
python roast.py path/to/file.js
```
or install it
```bash
python install.py
```


🧪 Usage

```bash
git roast path/to/file.js
```

Or roast an entire repo:

```
git roast .
```

Options coming soon:

 -[] `--savage` (maximum roast)

 -[] `--nice` (if your self-esteem is low)

 -[] `--roast-me` (targets only your commits)

