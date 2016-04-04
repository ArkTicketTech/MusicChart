## 收藏模块

/collects/{musicId}
- [收藏/取消收藏音乐](#collects_{musicId}_put)

[返回索引页](index.md.html)

<a id="collects_{musicId}_put"></a>

---

### 收藏/取消收藏音乐
>PUT: /collects/{musicId}

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
[404](index.md.html#404)|未找到音乐

返回数据: 无
