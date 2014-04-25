EManual
---

EManual makes you learn programming language more  easier.Currently, it focuse on **Java and Android**


run
---
```shell

    python EManual/java/make.py
```

File Structure
---
```file

    ./
     ----[program lang]/
       ---kind1/
          --topic1/
             -[num]-[title].md
             -[num]-[title].md
             -[num]-[title].md
          --topic2/
             -[num]-[title].md
             -[num]-[title].md
             -[num]-[title].md
       ---kind1/
          --topic1/
             -[num]-[title].md
             -[num]-[title].md
             -[num]-[title].md
          --topic2/
             -[num]-[title].md
             -[num]-[title].md
             -[num]-[title].md

```


* **[program lang],kind1 , topic1 All are `Directory`**
  typically, it should include `info.json` in current directory with follow format:
  ```json


     {
        "result":[list of file in this directory],
        "last_motify":timestamp
     }

  ```

* **[num]-[title].md** is the content file
  typically, it should include `info.json` and `[num of page].json` below current directory with follow format：
  info.json
  ```json


     {
       "last_motify": timestamp,
       "pages": total of page
     }

  ```

  [num of page].json
  ```json


     {
       "result":[list of content file(mostly is .md) below current directory]
     }

  ```




License
---
MIT

