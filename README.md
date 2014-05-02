EManual
---

EManual makes you learn programming language more  easier.Currently, it focuse on **Java and Android**


build the lastest book sites
---
```shell

    python EManual/java/make2.py
```

File Structure
---
```xml

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

  **info.json**
  ```json


     {
        "result":[list of file in this directory],
        "last_motify":timestamp
     }

  ```

* **[num]-[title].md** is the content file
  typically, it should include `info.json` and `[num of page].json` below current directory with follow format：

  **info.json**
  ```json


     {
       "last_motify": timestamp,
       "pages": total of page
     }

  ```

  **[num of page].json**
  ```json


     {
       "result":[list of content file(mostly is .md) below current directory]
     }

  ```




License
=======

```
Copyright 2014 Jayin Ton

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

```

