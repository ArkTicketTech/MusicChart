## 歌单模块

/setlists
- [获取歌单列表](#setlists_get)

/setlists/{setlistId}
- [获取某个歌单](#setlists_get_{setlistId})

类:
- [***Setlist类***](#class_setlist)


<a id="setlists_get"></a>

---

### 获取歌单列表
>GET: /setlists

参数

参数|参数类型|数据类型|描述
-|-|-|-
token|header|**string** |用户token
page|query|**int** |默认为0(可选)

返回码

返回码|描述
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|参数错误
[401](index.md.html#401)|未登录

返回数据: array([***Setlist类***](#class_setlist))


<a id="setlists_get_{setlistId}"></a>

---

### 获取某个歌单
>GET: /setlists/{setlistId}

参数

参数|参数类型|数据类型|描述
-|-|-|-
token|header|**string** |用户token

返回码

返回码|描述
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|参数错误
[401](index.md.html#401)|未登录
[404](index.md.html#404)|未找到

返回数据: [***Setlist类***](#class_setlist)

<a id="class_setlist"></a>

---

## ***Setlist类***
字段|类型|描述
-|
id|**int** |歌单id
description|**string** |歌单简介
photoUrl|**string** |音乐图片地址
musics|**string** |音乐列表
<!-- collects|**int** |收藏数 -->
<!-- comments|**int** |评论数 -->
time|**string** |创建时间
listType|**int** |0表示普通歌单，1表示专辑
singer|**string** |歌手,list_type=1时有值


[返回顶部](#)
