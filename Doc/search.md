## 搜索模块

/search
- [按照关键字搜索](#search_get)

<a id="search_get"></a>

---

### 按照关键字搜索
>GET: /search

参数

参数|参数类型|数据类型|描述
-|-|-|-
token|header|**string** |用户token
page|query|**int** |默认为0(可选)
key|query|**string** |关键字(必选)

返回码

返回码|描述
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|参数错误
[401](index.md.html#401)|未登录

返回数据: [***Music类***](music.md.html#class_music)

<a id="class_music"></a>
