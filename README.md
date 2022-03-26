# 自动填写晨午晚检及疫情通程序模板

fork自 https://github.com/SamZhou-2019/autoXidianDaily_Demo

感谢大佬学长


## 使用方法：

- 下载仓库中的run.yml（在子文件夹里）和六个后缀名为py的源代码。

- 注册一个Github账号（步骤可百度）已注册请跳过

- 新建仓库上传配置好的py代码，在repository页面上点击Action，选择`set up a workflow yourself` 自定义任务

- 将run.yml的代码复制到文本框中，提交即可

## 更新内容（2022.3.26）

- 可以供多人使用：

    - 允许选择一名管理员，脚本日志将通过邮箱发送给管理员。

    - 管理员在Setting.py的Admin中指定

- 新增 email_confirm.json 和 identity_confirm.json 独立保存**email配置项**和**身份配置项**

    - email_confirm 配置发送信息的**邮箱地址**和**授权码**（不是密码）

    - identity_confirm 配置一站式身份验证信息


- 新增地址库：

    - 每次填报的地址将从地址库中随机选择一条，避免每次填入相同地址

    - 地址库保存在geo_pool.json中。如果在脚本定时填写前已手动填写晨午晚检，手动填写的定位地址将添加至地址库中

    - 该地址库最好**不要**手动修改