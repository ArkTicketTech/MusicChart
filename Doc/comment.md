## 评论模块

/comments/{musicId}
- [获取音乐评论](#comments_{musicId}_get)
- [发表评论](#comments_{musicId}_post)

类:
- [***Comment类***](#class_comment)

[返回索引页](index.md.html)

<a id="comments_{musicId}_get"></a>

---

### 获取音乐评论
>GET: /collects/{musicId}

参数

参数|参数类型|数据类型|描述
-|-|-|-
token|header|**string** |用户token
page|query|**int** |页数(可选，默认为0)

返回码

返回码|描述
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|参数错误
[401](index.md.html#401)|未登录
[404](index.md.html#404)|未找到音乐

返回数据: array([***Comment类***](#class_comment))

<a id="comments_{musicId}_post"></a>

---

### 发表评论
>POST: /collects/{musicId}

参数

参数|参数类型|数据类型|描述
-|-|-|-
token|header|**string** |用户token
comment|json|**string** |评论

返回码

返回码|描述
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|参数错误
[401](index.md.html#401)|未登录
[404](index.md.html#404)|未找到音乐

返回数据: array([***Comment类***](#class_comment))

<a id="class_comment"></a>

---

## ***Comment类***
字段|类型|描述
-|
id|**int** |评论id
userId|**int** |评论者id
musicId|**int** |音乐id
comment|**string** |评论内容
time|**long** |发表评论的时间戳

[返回顶部](#)
