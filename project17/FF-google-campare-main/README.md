# FF-google-campare

#实验名称

FF-google-compare

#实验简介

比较Firefox和谷歌的记住密码插件的实现区别

#姓名

王晖

202100141110

githubID：jokerduck

#差异对比

存储位置：

Firefox: 在 Firefox 中，密码是使用“Login Manager”存储的。这些密码被保存在一个名为“logins.json”的文件中。

谷歌浏览器: 谷歌浏览器使用“密码管理器”来存储密码。这些密码保存在浏览器的设置中，通过“chrome://settings/passwords”访问。

加密和安全性：

Firefox: Firefox 使用主密码（Master Password）来加密保存在“logins.json”文件中的密码。用户可以设置主密码，这样在打开浏览器时需要输入主密码才能访问保存的密码。

谷歌浏览器: 谷歌浏览器将密码保存在操作系统的加密存储中（如Keychain（macOS）或Credential Manager（Windows））。这样，用户登录操作系统时，可以自动解锁密码，无需额外的密码输入。

跨设备同步：

Firefox: Firefox Sync 功能允许用户将保存的密码和其他浏览器数据同步到不同的设备，前提是用户拥有 Firefox 账号。

谷歌浏览器: 谷歌账号允许用户将保存的密码和其他浏览器数据自动同步到其他设备。

自动填充：

Firefox: Firefox 提供自动填充功能，但在某些情况下可能不如谷歌浏览器的自动填充功能智能。

谷歌浏览器: 谷歌浏览器具有智能自动填充功能，可以根据用户的历史输入和账户信息智能填充表单。

第三方插件支持：

Firefox: Firefox 允许第三方开发者开发插件来增强密码管理功能，用户可以选择安装适合自己需求的插件。

谷歌浏览器: 谷歌浏览器也支持第三方插件，但是由于安全考虑，Google Chrome 插件需要通过 Chrome Web Store 进行审核和发布。
