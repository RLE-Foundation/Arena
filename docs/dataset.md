---
hide:
#   - toc
  - navigation
---
# **Dataset**

## **Dataset List**
All the datasets are saved using the `JSON` format.

|Benchmark|Top 100|Full Version|Benchmark|Top 100|Full Version|
|:-:|:-:|:-:|:-:|:-:|:-:|
|Arcade Learning Benchmark| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|Procgen| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|
|DeepMind Control Suite| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|MineDojo| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|
|MiniGrid| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|Craftax| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|
|Meta-World| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|ViZDoom| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|
|SuperMarioBros| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|D4RL| <a href="" download>Download Link</a>|<a href="" download>Download Link</a>|



## **Data Structure**
The data structure is as follows:
``` sh
.
└── Dataset/
    ├── Version1/
    │   ├── Environment1/
    │   │   ├── Data Point1/
    │   │   │   ├── Team
    │   │   │   ├── Name
    │   │   │   ├── Training Stes
    │   │   │   ├── Params
    │   │   │   ├── Score: [..., ..., ...]
    │   │   │   ├── Code
    │   │   │   └── Date
    │   │   ├── Data Point2
    │   │   └── ...
    │   ├── Environment2
    │   └── ...
    ├── Version2/
    │   ├── Environment1
    │   ├── Environment2
    │   └── ...
    └── ...
```