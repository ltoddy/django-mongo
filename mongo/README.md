# mongo web 可视化

## 日期: 2018-11-15

## 设计:

通过环境变量获得mongodb的uri(`mongodb://user:password@host:port/db`), 默认为: `mongodb://localhost:27017/`

### 第一步要做的事情

`endpoints` 设计:

- /mongo/ 首页,提供db的选择(左侧side-bar).
- /mongo/db/collection collection的展示页面(考虑到数据量的问题, 使用分页.)
- /mongo/db/collection/page 分页, 或者 /mongo/db/collection?page=/
- /mongo/login 考虑到可能你设置了mongo的密码,如果认证失败redirect到这里,输入账户密码后存到session中.
- /mongo/logout 退出,删除session中存的帐号密码

### 未来要做的事情

- 在web页面编辑数据.
- 基于web页面的mongo shell

**目前先考虑这些**

----------------------------------------------------------
