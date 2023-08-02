# SM2-PGP

#实验名称

SM2-PGP

#实验简介

Implement a PGP scheme with SM2

#姓名

王晖

202100141110

githubID：jokerduck

#实验截图

PGP(Pretty Good Privacy)，是一个基于RSA公钥和对称加密相结合的邮件加密软件。该系统能为电子邮件和文件存储应用过程提供认证业务和保密业务。PGP是个混合加密算法，它由一个对称加密算法、一个非对称加密算法、与单向散列算法以及一个随机数产生器（从用户击键频率产生伪随机数序列的种子）组成。

本次实验旨在实现一个简易PGP，调用GMSSL库中封装好的SM2/SM4加解密函数。加密时使用对称加密算法SM4加密消息，非对称加密算法SM2加密会话密钥；解密时先使用SM2解密求得会话密钥，再通过SM4和会话密钥求解原消息。


![image](https://github.com/jokerduck/SM2-PGP/assets/130890730/a71843ef-b3db-490c-aeb1-fc741c866800)
