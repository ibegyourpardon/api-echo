<!--
 * @Date: 2022-02-04 22:04:29
 * @LastEditors: ibegyourpardon
 * @LastEditTime: 2022-02-04 23:31:58
 * @FilePath: /api-echo/README.md
-->


```POST``` any ```JSON``` request to ```'/'```, just like:

```
{
    "a": 2
}
```
 I will hold it for 2 hours and give you a response like:

```
{
    "code": 1,
    "created_at": 1643987892,
    "data": {
        "a": 2
    },
    "hash": "Jl3aVwA0",
    "msg": "success"
}
```

send a ```GET``` request to ```'/<hash>'```, I will give you the data you just posted:

```
http://xxx.com/Jl3aVwA0
```

```
{
    "a": 2
}
```

All data are stored in memory.

Just for you to create your mock data.

easy to use with Docker.
