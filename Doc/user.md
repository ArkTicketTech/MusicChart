## 用户模块

/users
- [注册](#users_signup_post)
- [登录](#users_signin_post)
- [修改密码](#users_resetpassword_post)

类:
- [***User类***](#class_user)

[返回索引页](index.md.html)

<a id="user_signup"></a>

---

### 注册
>POST: /users/signup

参数

参数|参数类型|数据类型|描述
-|-|-|-
username|json|**string** |用户名(必选)
password|json|**string** |密码(必选)

返回码

返回码|描述
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|缺少用户名密码
[409](index.md.html#409)|用户名存在

返回数据: [***User类***](#class_user)

[返回顶部](#)

<a id="user_signin"></a>

---

### 登录
>POST: /users/signin

参数

参数|参数类型|数据类型|描述
-|-|-|-
username|json|**string** |用户名(必选)
password|json|**string** |密码(必选)

返回码

返回码|描述
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|缺少用户名密码
[404](index.md.html#404)|用户名或密码错误

返回数据: [***User类***](#class_user)

[返回顶部](#)

<a id="users_resetpassword"></a>

---

## 修改密码
>POST: /users/reset_password

参数

参数|参数类型|数据类型|描述
-|-|-|-
token|header|**string** |用户的token  
oldPassword|json|**string** |旧密码
newPassword|json|**string** |新密码


返回码

返回码|描述返回数据: 无
-|
[200](index.md.html#200)|OK
[400](index.md.html#400)|缺少参数或参数错误
[401](index.md.html#401)|未登录
[404](index.md.html#404)|错误的旧密码

返回数据: [***User类***](#class_user)

[返回顶部](#)

<a id="class_user"></a>

---

## ***Account类***
字段|类型|描述
-|
username|**String** |用户名
token|**string** |验证用的token
expire|**long** |剩余多久过期

[返回顶部](#)
