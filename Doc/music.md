## 音乐模块

/musics
- [获取音乐列表](#musics_get)

[返回索引页](index.md.html)

<a id="musics_get"></a>

---

### 获取音乐列表
>GET: /musics

参数

参数|参数类型|数据类型|描述
-|-|-|-
token|header|**string** |用户token
page|query|**int** |默认为0(可选)
language|json|**string** |语种(可选)
style|json|**string** |风格(可选)
theme|json|**string** |主题(可选)
order|json|**int** |推荐为1 最新为0 默认为0(可选)

返回码

返回码|描述
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|参数错误
[401](index.md.html#401)|未登录

返回数据: [***Music类***](#class_music)

<a id="class_music"></a>

---

## ***Music类***
字段|类型|描述
-|
id|**int** |音乐id
name|**string** |音乐名字
language|**string** |语种
style|**string** |风格
theme|**string** |主题
collects|**int** |收藏数
comments|**int** |评论数

[返回顶部](#)
