# lengthattack

#实验名称

SM3—rho-attack

#实验简介

implement the Rho method of reduced SM3

#姓名

王晖

202100141110

githubID：jokerduck

#实验思路

长度扩展攻击的思路如下：

1.计算出消息r1的SM3值h1

2.计算r1||padding||r2的SM3值h2

3.以h1作为IV，计算r2的SM3值h3

4.判断h2和h3是否相等

![image](https://github.com/jokerduck/lengthattack/assets/130890730/3d006dc0-d944-4931-85dc-ec3380338c7e)
