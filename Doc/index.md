<a id="home"></a>
## MusicChart REST API

目录:
0. [user模块](user.md.html)
0. [music模块](music.md.html)
0. [setlist模块](setlist.md.html)

---

### 通用结构
发送HTTP header

域|值
-|
Authorization|token {token}

返回HTTP header

域|值
-|
Content-Type|application/json

---

### 返回码

返回码|简称|说明
-|
<a id="200"></a>0|OK|成功
||
<a id="400"></a>400|BAD_REQUEST|参数错误
<a id="401"></a>401|UNAUTHORIZED|未登录
<a id="403"></a>403|FORBIDDEN|用户权限不足
<a id="404"></a>404|NOT_FOUND|查找失败
<a id="409"></a>409|CONFLICT|出现重复/冲突
||
<a id="500"></a>500|INTERNAL_SERVER_ERROR|服务端内部错误


[返回顶部](#)
