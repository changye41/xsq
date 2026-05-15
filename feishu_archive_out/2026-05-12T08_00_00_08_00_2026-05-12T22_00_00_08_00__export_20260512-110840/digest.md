# 飞书消息归档 2026-05-12T08:00:00+08:00 — 2026-05-12T22:00:00+08:00

以下为同一时间窗口内的飞书会话摘录，已按优先级分组。可直接粘贴到大模型，并要求提取待办、决策与风险点。

## 重点（我发送 / @我 / @所有人）

- **2026-05-12 10:10** · `oc_ec1876c35e5187d9af9c532479316df0` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1c8de3d88cb4a12094d4b384a`
  @温俊薇 @董碧璇 hi，请教个问题
  现在解析od数据的时候，是一整个采集任务的数据只创建一个数据集吧，还是如果一个采集任务中的数据过多，会拆分为多个数据集？
  _(消息已编辑)_

- **2026-05-12 10:12** · `oc_ec1876c35e5187d9af9c532479316df0` · 董碧璇 （@我）
  - 类型: text；message_id: `om_x100b6f1c87dae1e4b3f87d0b35b22b1`
  @常夜 od数据是30个clip生产一个数据集，如果一个采集任务超过30clip就会拆分为多个数据集
  _(消息已编辑)_

- **2026-05-12 10:13** · `oc_ec1876c35e5187d9af9c532479316df0` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1c826810a4b2fab83bcf6c12d`
  @董碧璇 有办法改下参数，无论数据量多大，统一都放在同一个数据集中吗？有一类任务需要这样处理
  _(消息已编辑)_

- **2026-05-12 10:14** · `oc_ec1876c35e5187d9af9c532479316df0` · 董碧璇 （@我）
  - 类型: text；message_id: `om_x100b6f1c81fa517cb128a0d8efde48f`
  @常夜 按照采集任务来吗，一个采集任务生产一个数据集，这样是可以的
  _(消息已编辑)_

- **2026-05-12 10:15** · `oc_ec1876c35e5187d9af9c532479316df0` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1c9b53e8b0b32244269a2df58`
  @易铃 动物挖掘的数据重新提一下解析，按照一个采集任务生产一个数据集的规格来处理，后续凡是经过挖掘、需要刷无效包的任务，都按这个规格提，采集数据可以按默认格式
  _(消息已编辑)_

- **2026-05-12 10:16** · `易铃, 张俊芳, 常夜` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1c974968bcb28747c5c918ff3`
  昨天的问题定位到原因了，是解析规格的问题，相关数据要重新跑下解析再刷

- **2026-05-12 10:17** · `oc_ddf03801cbbd86b51688149c081e6567` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1c944bf8a4b32d0e8be83f905`
  动物这个任务着急吗？

- **2026-05-12 10:17** · `易铃, 张俊芳, 常夜` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1c9396f114b2b4139aa12a57c`
  是的

- **2026-05-12 10:18** · `易铃, 张俊芳, 常夜` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1cafcc18e4b3ff3209d2ba8bf`
  @张俊芳 还是只能前缀匹配，但预计不会有昨天这个问题了
  _(消息已编辑)_

- **2026-05-12 10:19** · `oc_ddf03801cbbd86b51688149c081e6567` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1cad7048f8b3f6cf15c21b8d6`
  那还是挺急的

- **2026-05-12 10:21** · `oc_ec1876c35e5187d9af9c532479316df0` · ou_a5b75f03cdacc4e5eb4e0939a7312864 （@我）
  - 类型: text；message_id: `om_x100b6f1ca47d4498c4a7245f15031f7`
  @常夜 好的
  _(消息已编辑)_

- **2026-05-12 10:21** · `oc_ec1876c35e5187d9af9c532479316df0` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1ca4dcf898b28fed62f5944d3`
  @温俊薇 需求比较紧急，辛苦给最高优先级
  _(消息已编辑)_

- **2026-05-12 10:23** · `oc_ddf03801cbbd86b51688149c081e6567` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1cbcbd6484b3b0bedc2622888`
  现在需要做评测任务的有三类：动物、开门、异形，每类都要三千有效帧
  开门、异形的数据应该都有，可以先评估下什么时间能交付
  动物可以等实际下发后再评估

- **2026-05-12 10:25** · `oc_ddf03801cbbd86b51688149c081e6567` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1cb4fff4b4b24ef7ac1524883`
  可以，各类场景分布尽量平均就行

- **2026-05-12 10:26** · `oc_ec1876c35e5187d9af9c532479316df0` · 易铃 （@我）
  - 类型: text；message_id: `om_x100b6f1cb2dd6cb8b29baa236ee908f`
  @常夜 只有挖掘要按这个规格提，采集还是和之前一样的处理方式嘛
  _(消息已编辑)_

- **2026-05-12 10:29** · `oc_ddf03801cbbd86b51688149c081e6567` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1d46f3e4b0b3416ec0083de35`
  解析格式那个问题对采集数据的影响就是任务大小
  当前默认的处理方式，解析出来的数据最大也就是在1800-2000帧左右，比如一个数据集原本是6000帧，解析后可能会拆分为三个数据集，也就是三期标注任务
  挖掘这边因为要通过数据集匹配recordID，所以必须保证数据集内容完整，但采集任务一般都是所有数据都做，所以没有这个强制要求，可以看你感觉是拆分还是不拆分更合适

- **2026-05-12 10:57** · `oc_ddf03801cbbd86b51688149c081e6567` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f1d2114c450b3cac0750d84d28`
  对

## 其他消息

- **2026-05-12 08:30** · `oc_40c66712add143c86fd6fc292be79bfc` · 易铃 
  - 类型: text；message_id: `om_x100b6f129d36d8a4c27cd841d28747b`
  5.12可视化质检批次：8e1d98d4-24cb-42e7-bb57-7f5aaf9e6222
  图片数：17288
  辛苦安排人员作业@HS王宇

- **2026-05-12 08:35** · `oc_a3da123bf52139099d2516ae1b7b189d` · 庞佳润 
  - 类型: post；message_id: `om_x100b6f1310ac74a0c3b7ace3df4d8f7`
  [Image: img_v3_0211k_8d967677-e9cb-4d95-8a9f-7b95b8ed1f8g]
  @陈光萍 老师这种的分开标还是标一起？
  _(消息已编辑)_

- **2026-05-12 08:41** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: post；message_id: `om_x100b6f133c854488b1368ae3bc928f2`
  [Image: img_v3_0211k_71d8a690-4279-44b3-b6a0-341d2768bb0g]
  5月11日标注交付不存在缺口
  项目名称：3D_OD_V2.2极近物流车
  - 人力缺口：0
  - 交付缺口：0
  - 累计交付缺口:0
  - [https://s5f8x04da1.feishu.cn/wiki/OMASwn2X7i2lLyks5XacxRyDnZe?from=from_copylink&sheet=RGDmd6](https://s5f8x04da1.feishu.cn/wiki/OMASwn2X7i2lLyks5XacxRyDnZe?from=from_copylink&sheet=RGDmd6)

- **2026-05-12 08:41** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: post；message_id: `om_x100b6f133c8aa8b0b3c62d99eed34ce`
  [Image: img_v3_0211k_a1369fab-afd4-4396-a946-eb470ecb93cg]
  5月11日标注交付不存在缺口
  项目名称：3D_OD_V2.2极近物流车
  - 人力缺口：0
  - 交付缺口：0
  - 累计交付缺口:0
  - [https://s5f8x04da1.feishu.cn/wiki/OMASwn2X7i2lLyks5XacxRyDnZe?from=from_copylink&sheet=RGDmd6](https://s5f8x04da1.feishu.cn/wiki/OMASwn2X7i2lLyks5XacxRyDnZe?from=from_copylink&sheet=RGDmd6)

- **2026-05-12 08:47** · `【AI】AI 工具讨论&客服组` · 驭川 
  - 类型: text；message_id: `om_x100b6f13c560d4a8b349d8e6ca66f8e`
  是传说中那种删数据库的bug 吗[石化]

- **2026-05-12 08:56** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f13e3748ca8c43a14a6040a665`
  @庞佳润 一起给异形
  _(消息已编辑)_

- **2026-05-12 09:00** · `oc_c93fa1ba6427659dbfbc22ab9433be3b` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f2d86de90a4c439fc7f84b4ffe`
  异型＞历史数据（补标，2.0路口10%，极近数据10%，倒地专项10%，极近物流车10%）

- **2026-05-12 09:00** · `oc_2fc508994bc3c995810297c8577da2b0` · ou_81286f02539b56ccce6940172440bb8b 
  - 类型: text；message_id: `om_x100b6f13c19ce8a8c49b725a71e6000`
  今日任务量需通过190个工单@方心成 ，cc@易铃

- **2026-05-12 09:02** · `oc_40c66712add143c86fd6fc292be79bfc` · ou_61026839c0ebe2273356788d3d38cac6 
  - 类型: post；message_id: `om_x100b6f138c11e8acc32757432fa6335`
  [Image: img_v3_0211k_e0e565d7-50ba-4c4d-9653-6014254efd1g]
  @易铃 老师，我今天也遇到了这种没有图的情况，也是等后续通知了在处理吗？
  _(消息已编辑)_

- **2026-05-12 09:03** · `oc_26f131b833bb664ce27a5238de726ed3` · 飞书用户0792VI 
  - 类型: text；message_id: `om_x100b6f13889cbca8b2eb15baee50ef2`
  @李金秀 老师，能下发点occ的数据吗
  _(消息已编辑)_

- **2026-05-12 09:04** · `oc_52fdd080b74628c0c13647af8dd315b7` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1385e92874c3ca3f04835136c`
  @张建 打开车门异型
  _(消息已编辑)_

- **2026-05-12 09:04** · `oc_52fdd080b74628c0c13647af8dd315b7` · 张建 
  - 类型: post；message_id: `om_x100b6f138658f4b0c2ca7c71ec12a12`
  [Image: img_v3_0211k_1b82d08c-9aa7-47c3-b96c-ac0dcf315afg]
  3D_OD_V2.1_异型车_0412_1_250-03
  @陈光萍 老师，这个车给异型吗
  _(消息已编辑)_

- **2026-05-12 09:06** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f139dc024a8c2a7ef73ccb09a6`
  平台数据不够了，待提交数据记得及时提交@尚程洋
  _(消息已编辑)_

- **2026-05-12 09:06** · `oc_52fdd080b74628c0c13647af8dd315b7` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f139f5070a0c4e53c49b7fbebb`
  <p>平台数据不够了，待提交数据记得及时提交@杨思雅</p>
  _(消息已编辑)_

- **2026-05-12 09:08** · `oc_40c66712add143c86fd6fc292be79bfc` · ou_1b76328bd412ee5d48e3435eafb8e24e 
  - 类型: text；message_id: `om_x100b6f13968d493cc2d070352899717`
  @易铃 老师  今日数据都没有图片
  _(消息已编辑)_

- **2026-05-12 09:10** · `oc_40c66712add143c86fd6fc292be79bfc` · 易铃 
  - 类型: text；message_id: `om_x100b6f13913cf888b190bcefa43f220`
  @宋泽旭 辛苦看下吧，确实都没有图片诶
  _(消息已编辑)_

- **2026-05-12 09:13** · `oc_40c66712add143c86fd6fc292be79bfc` · 宋泽旭 
  - 类型: text；message_id: `om_x100b6f13a41ea0acc34f3dc7b18ddca`
  @易铃 ok 我看下
  _(消息已编辑)_

- **2026-05-12 09:14** · `oc_26f131b833bb664ce27a5238de726ed3` · 李金秀 
  - 类型: text；message_id: `om_x100b6f13a302fcbcb10889418258309`
  @飞书用户0792VI  3D_OCC_V1.4 occ减速带专项正式任务已下发：
  3d_OCC_V1.4_减速带_0512_1_（1-200）
  _(消息已编辑)_

- **2026-05-12 09:15** · `oc_2fc508994bc3c995810297c8577da2b0` · ou_81286f02539b56ccce6940172440bb8b 
  - 类型: text；message_id: `om_x100b6f13bf7504bcb32a25d58da6bc9`
  3d_parking_v1.0_0512_hh（1~42）已下发@方心成
  _(消息已编辑)_

- **2026-05-12 09:15** · `易铃, 张俊芳, 常夜` · 易铃 
  - 类型: text；message_id: `om_x100b6f13bf93507cb2e15da4b1fde71`
  @张俊芳 100期任务已经重新下发了，现在可以正常刷数据了嘛
  _(消息已编辑)_

- **2026-05-12 09:15** · `oc_72811ede6885e73bafaf59833751bb54` · cli_a0c2cea3eef8100d 
  - 类型: interactive；message_id: `om_x100b6f13ba574ca8c269cb738d11f62`
  <card title="权限变更（外部）">
  外部用户 @7633640505781111994 给外部用户 @7638573812929318081 开通了文档 [OCC真值质检规则文档 V1.0](https://r3c0qt6yjw.feishu.cn/wiki/TBM3wBM2YiXB2rkml52czRCQnZg?from=auth_notice) 的阅读权限。
  📝 授权对象为外部用户，可分享此文档的用户均可添加外部协作者和查看协作者列表，请注意信息安全。
  </card>

- **2026-05-12 09:21** · `oc_72811ede6885e73bafaf59833751bb54` · cli_a0c2cea3eef8100d 
  - 类型: interactive；message_id: `om_x100b6f1c448854b4c2a7c3e93468821`
  <card title="权限变更（外部）">
  外部用户 @7617650816794495953 给外部群“停车位”的成员开通了文档 [停车位标注质检规则文档](https://r3c0qt6yjw.feishu.cn/docx/KlKddaxn0oaUE0xi4Yhc6UK5ntf?from=auth_notice) 的阅读权限。
  📝 授权对象为外部群，可分享此文档的用户均可添加外部协作者和查看协作者列表，请注意信息安全。
  </card>

- **2026-05-12 09:28** · `oc_2fc508994bc3c995810297c8577da2b0` · ou_81286f02539b56ccce6940172440bb8b 
  - 类型: text；message_id: `om_x100b6f1c6c70c16cb119f9f991c86a5`
  3d_parking_v1.0_0512-1_hh（1~40）已下发@方心成
  _(消息已编辑)_

- **2026-05-12 09:29** · `oc_ec1876c35e5187d9af9c532479316df0` · 易铃 
  - 类型: text；message_id: `om_x100b6f1c6799dca8b29e9a3cf069664`
  @温俊薇 https://r3c0qt6yjw.feishu.cn/wiki/K3pOw9ZxJiPRTekgDWicrmIXnlc?from=from_copylink辛苦处理od解析任务，送解析时间已更新
  _(消息已编辑)_

- **2026-05-12 09:30** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · ou_1f0dcb6a2638c26abb205f2a6fa49db0 
  - 类型: text；message_id: `om_x100b6f1c65712090c35f2fbd386aff7`
  https://r3c0qt6yjw.feishu.cn/wiki/QimXw2k2OiZqlXk7qJPc9tacnCe?sheet=u4wB5S@梁世铭 新的IUSSE专修任务已添加，请在青岛合区西-iusse专修+末端-0511、青岛合区东-iusse专修+末端-0511作业
  _(消息已编辑)_

- **2026-05-12 09:34** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1c77cd98acc2b67726d89b72b`
  <p>没有待审核数据了，麻烦及时提交@尚程洋</p>
  _(消息已编辑)_

- **2026-05-12 09:34** · `oc_52fdd080b74628c0c13647af8dd315b7` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1c74ee5080c2a52b4b1f7ccc6`
  没有待审核数据了，麻烦及时提交@杨思雅
  _(消息已编辑)_

- **2026-05-12 09:39** · `TLD&ROD数据交付` · 马晓宇 
  - 类型: text；message_id: `om_x100b6f1c031700e4c4c0e6bca5fdd7a`
  @李鑫鑫 你们建好图层我往里导吧，名字你们自己取了
  _(消息已编辑)_

- **2026-05-12 09:39** · `oc_ec1876c35e5187d9af9c532479316df0` · 温俊薇 
  - 类型: text；message_id: `om_x100b6f1c026fb094c2af6a5af90d30c`
  @易铃 开门车辆已提
  https://nds.data.neolix.cn/#/resource/data-workflow/batch-task/detail/34306
  _(消息已编辑)_

- **2026-05-12 09:44** · `自助生产数据` · 董碧璇 
  - 类型: text；message_id: `om_x100b6f1c107570a4b2874c8507b7cab`
  @赵广 哥，昨天提交的occ解析任务全部失败了，辛苦看看是什么原因呢https://nds.data.neolix.cn/#/resource/data-workflow/batch-task/detail/33905
  _(消息已编辑)_

- **2026-05-12 09:46** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1c2b6e9914b11441930147c91`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6988436794
  [extricate_pnc_ratio_X6S6115_2026-05-12 09:09:13](https://project.feishu.cn/ubh28t/issue/detail/6988436794) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6988436794)
  </card>

- **2026-05-12 09:47** · `oc_c93fa1ba6427659dbfbc22ab9433be3b` · ou_ce9be48f872188a6d065d787c6f60186 
  - 类型: text；message_id: `om_x100b6f1c22ceacb8c2a5117ec6ddf52`
  @陈光萍 今日出勤，正式验收15人
  _(消息已编辑)_

- **2026-05-12 09:52** · `建图风险解决` · 苏子豪 
  - 类型: text；message_id: `om_x100b6f1c336ac51cb4acc7c7010a125`
  @李明 明哥，这个为啥要降啊，这降的也太多了
  _(消息已编辑)_

- **2026-05-12 09:53** · `建图风险解决` · 李明 
  - 类型: text；message_id: `om_x100b6f1cce0ef4bcb12dc0fcb56185c`
  @苏子豪 DCL数据回流要抽帧才能录制长片段
  _(消息已编辑)_

- **2026-05-12 09:54** · `建图风险解决` · 苏子豪 
  - 类型: text；message_id: `om_x100b6f1cc87eeca8b2f15454544fa7a`
  这个感觉风险蛮大的，10m/s这两帧之间就10m出去了

- **2026-05-12 09:57** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1cc1a058a8c274cc4017a3a24`
  @尚程洋 平台没待审核数据了，待提交瀚晖2有七十七页，瀚晖有七页，麻烦尽快提交
  _(消息已编辑)_

- **2026-05-12 09:58** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1cdddf0094b253d70af463cd0`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6988662249
  [cloudapp_event__X6S6188_2026-05-12 09:17:48](https://project.feishu.cn/ubh28t/issue/detail/6988662249) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6988662249)
  </card>

- **2026-05-12 10:03** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1ce8200490b2eee4f077e6727`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6987479016
  [（自动）自车行驶，闯红灯，接管](https://project.feishu.cn/ubh28t/issue/detail/6987479016) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6987479016)
  </card>

- **2026-05-12 10:04** · `oc_37ec9e7d49f0435b4335b0ef92bce67b` · ou_81286f02539b56ccce6940172440bb8b 
  - 类型: text；message_id: `om_x100b6f1ce4c828b4b1142e2610dab3b`
  2026.5.11
  验收人数：11/人，【应出勤11人，实出勤11人】7人od验收，4人停车位质检加班0.5h
  验收产出：
  极近专项：10825/帧，倒地专项：36/帧，异型专项：75/帧，总计：10935/帧
  通过验收：
  极近专项：9512/帧，倒地专项：36/帧，异型专项：51/帧，总计：9599/帧
  折合账号数：7/人天

- **2026-05-12 10:05** · `oc_40c66712add143c86fd6fc292be79bfc` · HS王宇 
  - 类型: text；message_id: `om_x100b6f1ce3671088c33fae9b0c8542d`
  @宋泽旭 老师   这个预计的什么时候可以有图片
  _(消息已编辑)_

- **2026-05-12 10:07** · `oc_40c66712add143c86fd6fc292be79bfc` · 宋泽旭 
  - 类型: text；message_id: `om_x100b6f1cfb20dce0c3c0434b2b86ec5`
  @HS王宇 要重新刷写一下，大概12点左右。
  _(消息已编辑)_

- **2026-05-12 10:10** · `自助生产数据` · 赵广 
  - 类型: post；message_id: `om_x100b6f1c8c408098c26c116c9e236d0`
  @董碧璇 应该还是高频信号问题，我看今天高频信号才刷好，要不重试下？
  [Image: img_v3_0211k_6fb7b0ce-be06-4dd2-91c6-9e5595cdc1ag]
  _(消息已编辑)_

- **2026-05-12 10:13** · `建图风险解决` · 苏子豪 
  - 类型: text；message_id: `om_x100b6f1c80cca0a0c337c72d472d43f`
  @王琢琰 琢哥，现在线上运行的是多少hz的数据，我看给到我们这解析的结果都是10hz的lidar
  _(消息已编辑)_

- **2026-05-12 10:15** · `oc_2f32aa954945ae95cdbf43cf36942033` · ou_90cfae844f63d63d8b6023cd01bdf19d 
  - 类型: post；message_id: `om_x100b6f1c9c017888b36c8ef6967377d`
  [Image: img_v3_0211k_cb1364e8-1388-4c0a-84cb-5a696e80e4cg]
  [Image: img_v3_0211k_e766956a-ef07-4bc7-99d2-2c0cca37097g]
  @李杰 老师 麻烦确认下图二的任务用例对应图一那个单价版本号吧
  _(消息已编辑)_

- **2026-05-12 10:15** · `易铃, 张俊芳, 常夜` · 张俊芳 
  - 类型: text；message_id: `om_x100b6f1c9dcfd0b0c2679dcc96a59d1`
  新任务的列表发我

- **2026-05-12 10:15** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1c9c98f0b8b2f5148cabfa606`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6987723947
  [（自动）异常刹停 接管，感知模型右转未识别到](https://project.feishu.cn/ubh28t/issue/detail/6987723947) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6987723947)
  </card>

- **2026-05-12 10:16** · `oc_ec1876c35e5187d9af9c532479316df0` · 崔佳峰 
  - 类型: text；message_id: `om_x100b6f1c967d60b0c32476635fd71b9`
  @温俊薇 hi，这个数据集怎么没有看到
  _(消息已编辑)_

- **2026-05-12 10:17** · `易铃, 张俊芳, 常夜` · 张俊芳 
  - 类型: text；message_id: `om_x100b6f1c921fd488c2c836a441f2256`
  得再重新创建项目再刷是吧。等你们给我列表

- **2026-05-12 10:17** · `oc_ec1876c35e5187d9af9c532479316df0` · 温俊薇 
  - 类型: post；message_id: `om_x100b6f1c93ccf484c2b84536fa93402`
  @崔佳峰 
  [Image: img_v3_0211k_f611ac07-23f4-4098-922d-00eb4e13c67g]
  昨天的任务成功率为0，早上反馈后定位为高频信号问题，我再重新提一下
  _(消息已编辑)_

- **2026-05-12 10:17** · `oc_ec1876c35e5187d9af9c532479316df0` · 董碧璇 
  - 类型: text；message_id: `om_x100b6f1c94b81968b392c6e217296a8`
  @温俊薇 解析的时候group size=0
  _(消息已编辑)_

- **2026-05-12 10:17** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1c946e1cecc38903738a68cf1`
  <p>一条待审数据都没有了，麻烦提交@尚程洋</p>
  _(消息已编辑)_

- **2026-05-12 10:17** · `oc_52fdd080b74628c0c13647af8dd315b7` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1c92852cb4c438c37f134440c`
  @杨思雅 及时提交待提交数据
  _(消息已编辑)_

- **2026-05-12 10:18** · `易铃, 张俊芳, 常夜` · 张俊芳 
  - 类型: text；message_id: `om_x100b6f1c91c32cbcc2735462ce0ae75`
  新的recordId是精确匹配还是前缀匹配

- **2026-05-12 10:18** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: text；message_id: `om_x100b6f1c90c21094b39d37e49cbe132`
  @陈光萍 老师 我们昨天已经提交了将近两万数据，今天都还在标检中，标检完成还要再过一遍二审环节才能体验
  _(消息已编辑)_

- **2026-05-12 10:18** · `oc_26f131b833bb664ce27a5238de726ed3` · ou_3b92bf225082b23c75274a356f7dcf6e 
  - 类型: post；message_id: `om_x100b6f1c9322a0b0b3b4386358ac3af`
  3d_OCC_V1.4_减速带_0512_1_52
  [Image: img_v3_0211k_84c1971a-fe25-4c19-b7ae-7206aeabbbeg]
  @李金秀 老师这种减速带需要标注吗
  _(消息已编辑)_

- **2026-05-12 10:18** · `建图风险解决` · 王琢琰 
  - 类型: text；message_id: `om_x100b6f1c904d2c90b483c343f6e591f`
  @苏子豪 嗯，帧对齐应该是按10hz来的 cc@张安竹 对吧，竹哥
  _(消息已编辑)_

- **2026-05-12 10:19** · `oc_ddf03801cbbd86b51688149c081e6567` · 易铃 
  - 类型: text；message_id: `om_x100b6f1cac6d08a8b487adb74104dd8`
  昨天定的5.14周四交，但没说是全量交还是交一部分

- **2026-05-12 10:20** · `oc_ec1876c35e5187d9af9c532479316df0` · 易铃 
  - 类型: file；message_id: `om_x100b6f1ca86bf480c42c7db86ebfc65`
  <file key="file_v3_0011k_7b79e5d5-399f-4fb5-a622-965be9245e6g" name="animal_20260424.csv"/>

- **2026-05-12 10:20** · `建图风险解决` · 张安竹 
  - 类型: text；message_id: `om_x100b6f1ca9fc34b4b3774a252b1567c`
  @王琢琰 post od里面的帧对齐么，要@花云铭 确认下
  _(消息已编辑)_

- **2026-05-12 10:20** · `oc_ec1876c35e5187d9af9c532479316df0` · 易铃 
  - 类型: text；message_id: `om_x100b6f1ca949cca8b3233e9b31883b6`
  @温俊薇 辛苦处理od-动物采集数据
  _(消息已编辑)_

- **2026-05-12 10:21** · `建图风险解决` · 苏子豪 
  - 类型: text；message_id: `om_x100b6f1ca592d8b4c387f7f54886a6e`
  @张安竹 不是，现在采集的lidar帧的频率
  _(消息已编辑)_

- **2026-05-12 10:22** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1ca15f8c84c4901f89dbc904a`
  @尚程洋 但平台确实没有数据了，而且昨天该交付的极近物流车，也没交完
  _(消息已编辑)_

- **2026-05-12 10:23** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: text；message_id: `om_x100b6f1cbd7bc4e4b3b5bd323739645`
  @陈光萍 老师 我这边随机搜了下还是有待验收数据
  _(消息已编辑)_

- **2026-05-12 10:24** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 王健博 
  - 类型: text；message_id: `om_x100b6f1cb8eb1174c454cec95e4d6b9`
  <p>后续咱们地图对小路的lane的绘制，需要跟4Dlane保持一致哈</p>

- **2026-05-12 10:24** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 王健博 
  - 类型: merge_forward；message_id: `om_x100b6f1cb8d1bcacc3c99e5eec154a1`
  <forwarded_messages>
  [2026-05-12T01:40:02+08:00] 李明:
      <forwarded_messages>
      [2026-05-12T01:26:06+08:00] 李明:
          [Image: img_v3_0211k_0e80d19c-7909-42d0-8005-7825720190cg]
          [https://project.feishu.cn/ubh28t/issue/detail/6985225214?parentUrl=%2Fubh28t%2FissueView%2FKdTPWMAvg%3FquickFilterId%3Dz7G1wRH4-wGnV-KGYn-ax8z-mzdpaVDt4AuS&openScene=4](https://project.feishu.cn/ubh28t/issue/detail/6985225214?parentUrl=%2Fubh28t%2FissueView%2FKdTPWMAvg%3FquickFilterId%3Dz7G1wRH4-wGnV-KGYn-ax8z-mzdpaVDt4AuS&openScene=4) 
          hi 这种小路，我要怎么给你标图？车道中心线都往中间画吗？可能会造成正反车道中心线距离过近
      [2026-05-12T01:38:36+08:00] 郭林桥:
          我觉得就画中间吧，这种没必要区分双向车道了。
      [2026-05-12T01:39:07+08:00] 李明:
          会有和对向来车碰撞的风险不？
      </forwarded_messages>
  [2026-05-12T01:45:45+08:00] 郭林桥:
      @李辰 看看这个。我倾向直接标中间，这种小路我感觉靠一边意义也不大。
  [2026-05-12T01:45:59+08:00] 王见山:
      考虑下路宽，给几个标准？
  [2026-05-12T09:59:29+08:00] 黄培煜:
      我也倾向于标中间，除非宽度超过七米
  [2026-05-12T10:01:04+08:00] 史天才:
      4dlane的话是标中间，标双向车道属性
  [2026-05-12T10:05:10+08:00] 李明:
      @王健博 图南标注也注意一下这个小路，和4DLANE的对齐
  </forwarded_messages>

- **2026-05-12 10:24** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1cbb9358bcc2a339aacff7965`
  <p>@尚程洋 只有你刚刚交上来的路口</p>
  _(消息已编辑)_

- **2026-05-12 10:25** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 王健博 
  - 类型: text；message_id: `om_x100b6f1cb5c2f8bcc39379fb8a561d5`
  <p>那种宽度不超过七米的小路，统一都是只标中间一条，给双向属性就可以了，不用画两条；</p><p>这个注意一下@梁世铭 @李晓通 @张祥伟 @张妍</p>
  _(消息已编辑)_

- **2026-05-12 10:25** · `建图风险解决` · 张安竹 
  - 类型: text；message_id: `om_x100b6f1cb44058bcb15e2eed985c83c`
  @苏子豪 那是10hz的。
  _(消息已编辑)_

- **2026-05-12 10:25** · `oc_ddf03801cbbd86b51688149c081e6567` · 易铃 
  - 类型: text；message_id: `om_x100b6f1cb603c0acb2ff8d71049d786`
  开门数据在解析了，异型数据就选整期未交付的数据来做评测可以不

- **2026-05-12 10:28** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: post；message_id: `om_x100b6f1d4b51a49cb3b8f1b257b3c84`
  @陈光萍 老师  类似之前参与的大车数据
  
  [Image: img_v3_0211k_ae321d01-805b-4fb3-a4c3-037838f5c87g]
  _(消息已编辑)_

- **2026-05-12 10:29** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: post；message_id: `om_x100b6f1d4979fcdcb292312a2d6d1bc`
  老师  麻烦看下这个给什么类别吧@陈光萍 
  [Image: img_v3_0211k_f740aa50-be58-49f4-8b74-6587d8211d8g]
  _(消息已编辑)_

- **2026-05-12 10:30** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1d44132888c342ff96c81557a`
  @尚程洋 优先给三轮
  _(消息已编辑)_

- **2026-05-12 10:31** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 张祥伟 
  - 类型: post；message_id: `om_x100b6f1d41dfd0a4b2f62d0c2054ba5`
  @王健博 
  [Image: img_v3_0211k_d9b4fcba-31b1-47fd-ac3c-24cff97899dg]
  老师，超过7m的应该是分开画吧，小于7m的在中间画双向
  _(消息已编辑)_

- **2026-05-12 10:31** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1d41472c98c269d34b62a5840`
  @尚程洋平台没有这两条数据
  _(消息已编辑)_

- **2026-05-12 10:32** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 王健博 
  - 类型: text；message_id: `om_x100b6f1d5bf4dca0c3808d206c2cfee`
  少打了一个字，不好意思，已经改了，不超过7m

- **2026-05-12 10:32** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 王健博 
  - 类型: sticker；message_id: `om_x100b6f1d5b64ac8cc31f61e5bb18689`
  [Sticker]

- **2026-05-12 10:32** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: text；message_id: `om_x100b6f1d5d77e4a0b2926ace7b386a3`
  @陈光萍 3D_OD_V2.1_大车cutin_0410_2_8-054
  3D_OD_V2.1_大车cutin_0410_2_8-062 
  老师 就是以上两条数据，我这边在平台看是待验收状态
  _(消息已编辑)_

- **2026-05-12 10:33** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: post；message_id: `om_x100b6f1d59951ca4b284c4552aaff39`
  老师  这个看起来不像是常规的卡车，麻烦看下给什么类别吧@陈光萍 
  [Image: img_v3_0211k_a7ea6b1c-1908-4d7c-b27a-decb761c9d6g]
  _(消息已编辑)_

- **2026-05-12 10:34** · `数采软件专项沟通群` · 文一 
  - 类型: text；message_id: `om_x100b6f1d55097424c31c133f9d303d3`
  <p>@_all 后续数采软件的会议follow素雯数据域的会议体系规划做一下调整，原来的软件daily会议讨论议题调整到这个会上，对数采软件有需求的大家可以反馈我，我会视需求按需拉大家入会，相关背景可以了解昨天数据域会议体系文档，当前软件各环节在跟进的内容大家也可提前多维表格了解，后续daily跟踪各部分进展、计划、风险行动项等。</p><p>https://r3c0qt6yjw.feishu.cn/docx/RG0HdYncroKgKVx4WfrczQRRn1d</p><p>https://r3c0qt6yjw.feishu.cn/base/VcU0bLpKNaMrnksSjoccYJ57nJu?table=tblpfJqX5y9OzrUl&view=vewMd6ZDgI</p>
  _(消息已编辑)_

- **2026-05-12 10:35** · `数采软件专项沟通群` · 文一 
  - 类型: share_calendar_event；message_id: `om_x100b6f1d53f3fca8c260cb8abe45453`
  <calendar_share open_calendar_id="feishu.cn_qxdhNjmW4E556BeFEi487f@group.calendar.feishu.cn" open_event_id="22c42648-95ea-4345-bf48-7e50a62fdc81_0">
  [能力] 数采软件 squad 站会
  2026-05-12 11:00:00 ~ 2026-05-12 11:15:00
  </calendar_share>

- **2026-05-12 10:35** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1d518d6ca4b328ced3e56256a`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6987668407
  [（自动）长黄灯不走（接管）](https://project.feishu.cn/ubh28t/issue/detail/6987668407) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6987668407)
  </card>

- **2026-05-12 10:36** · `4D lane人工标注对齐` · 李素雯 
  - 类型: share_calendar_event；message_id: `om_x100b6f1d6dab64a8c4297ece27c5a46`
  <calendar_share open_calendar_id="feishu.cn_Bm5V5WpW5fnt6wfmbZ36qh@group.calendar.feishu.cn" open_event_id="f0f2ef75-3c51-42bb-aa4d-92704f0ed485_0">
  [交付] lane squad 站会
  2026-05-12 11:30:00 ~ 2026-05-12 11:45:00
  </calendar_share>

- **2026-05-12 10:37** · `4D lane人工标注对齐` · 李素雯 
  - 类型: text；message_id: `om_x100b6f1d66eaf0a8c3933b3d12a231a`
  @_all 4d lane的会议合并到lane squad站会统一管理，这个会议从今天起取消，相关同事请参加上面的会议

- **2026-05-12 10:38** · `oc_ddf03801cbbd86b51688149c081e6567` · 易铃 
  - 类型: text；message_id: `om_x100b6f1d672c8ca0b198ec6e45cb6bf`
  好的👌

- **2026-05-12 10:38** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1d65b580b4c227f05c4610876`
  @尚程洋 数据名称发下
  _(消息已编辑)_

- **2026-05-12 10:39** · `oc_72811ede6885e73bafaf59833751bb54` · cli_a0c2cea3eef8100d 
  - 类型: interactive；message_id: `om_x100b6f1d634ccd44c2d7ea82ce46684`
  <card title="权限申请（外部）">
  外部用户 @7561253355551932419 向你申请文档 [3d_抬杆_v1.0 标注规则文档](https://r3c0qt6yjw.feishu.cn/wiki/IcljwYD6SivdXEkbd1QcqPu9nSd?from=botpush) 的阅读权限。
  📝 该用户为外部用户，请注意信息安全。
  [同意] [拒绝]
  </card>

- **2026-05-12 10:39** · `oc_ec1876c35e5187d9af9c532479316df0` · 温俊薇 
  - 类型: text；message_id: `om_x100b6f1d63fe396cc228e1d2de5d29a`
  <p>@易铃 动物挖掘已按groupsize=0重提</p><p>https://nds.data.neolix.cn/#/resource/data-workflow/batch-task/detail/34344</p>
  _(消息已编辑)_

- **2026-05-12 10:40** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1d7cd332d0b3cc8bff90126bb`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6988463404
  [extricate_pnc_ratio_X6S6570_1778550587558](https://project.feishu.cn/ubh28t/issue/detail/6988463404) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6988463404)
  </card>

- **2026-05-12 10:42** · `OCC数据交付沟通（内部）` · 易铃 
  - 类型: post；message_id: `om_x100b6f1d765e2c50b32379e86fa1e1b`
  [Image: img_v3_0211k_354aaf3b-0704-4c69-864a-a129b47abfeg]
  无障碍车位需不需要标呀@宋泽旭
  _(消息已编辑)_

- **2026-05-12 10:43** · `oc_a3da123bf52139099d2516ae1b7b189d` · 尚程洋 
  - 类型: text；message_id: `om_x100b6f1d72fcdca0b48405f2ac19538`
  @陈光萍 3D_OD_V2.2_异型车_0509_2_30-10
  _(消息已编辑)_

- **2026-05-12 10:44** · `TLD&ROD数据交付` · 车启谣 
  - 类型: text；message_id: `om_x100b6f1d0fe68c88b4c6cd4cc24dd85`
  https://r3c0qt6yjw.feishu.cn/wiki/GBmnwJmspi663GkF1Omchlacnee@李奥 @李鑫鑫 需要采集+挖掘掉头灯数据，期望能够在周五先标注1w的数据回来 cc@李素雯
  _(消息已编辑)_

- **2026-05-12 10:46** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1d09e1a488c44fdaa8373c6d6`
  @尚程洋 保持当前属性
  _(消息已编辑)_

- **2026-05-12 10:46** · `OCC数据交付沟通（内部）` · 宋泽旭 
  - 类型: text；message_id: `om_x100b6f1d09dbd098c10fd1827d85655`
  @易铃 按正常车位标吧，现在也区分不了无障碍车位。
  _(消息已编辑)_

- **2026-05-12 10:46** · `TLD&ROD数据交付` · 车启谣 
  - 类型: text；message_id: `om_x100b6f1d04de0940b30c9d934a01a90`
  同级别吧，这个只要求返回1w，剩下的后面再补

- **2026-05-12 10:46** · `TLD&ROD数据交付` · 李素雯 
  - 类型: text；message_id: `om_x100b6f1d08296cacc3bd315ee7f62c2`
  @车启谣 跟右转灯比，哪个更高优？
  _(消息已编辑)_

- **2026-05-12 10:47** · `mil benchmark数据集` · 韩少华 
  - 类型: text；message_id: `om_x100b6f1d0544b8acc3c3a3c566a09fc`
  @凌逸峰 yifeng,想问下两次交付是同一批数据吗
  https://r3c0qt6yjw.feishu.cn/wiki/Ewk8wpp7riLASGk9cRaciDaDnZWhttps://r3c0qt6yjw.feishu.cn/wiki/F8XMw5rlJiVNIkkozvmcP4v9nRf
  _(消息已编辑)_

- **2026-05-12 10:48** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: post；message_id: `om_x100b6f1d018104bcc32cfcecc4cb174`
  [Image: img_v3_0211k_3e1e26ed-4e39-4620-98e9-6ee90aa7857g]
  确实没有待审核数据了，麻烦待提交数据及时提交@尚程洋
  _(消息已编辑)_

- **2026-05-12 10:54** · `oc_ec1876c35e5187d9af9c532479316df0` · 温俊薇 
  - 类型: text；message_id: `om_x100b6f1d296aad68c2121a1e4b5d320`
  @崔佳峰  0511-occ任务已重提，batchid如下
  三角架：occsjj_0512_rawdata_output
  _(消息已编辑)_

- **2026-05-12 10:56** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1d20d4c0b8b16c35d786beb57`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6930237611
  [左转失败，接管](https://project.feishu.cn/ubh28t/issue/detail/6930237611) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6930237611)
  </card>

- **2026-05-12 10:56** · `oc_ddf03801cbbd86b51688149c081e6567` · 易铃 
  - 类型: text；message_id: `om_x100b6f1d203bdc94b3953ac98b3ee5c`
  停车位的采集数据是需要按4dlane的方式来解析哈

- **2026-05-12 10:56** · `mil benchmark数据集` · 凌逸峰 
  - 类型: text；message_id: `om_x100b6f1d21a1b0b0c2c40c8c2506aee`
  @韩少华 等会我确认下
  _(消息已编辑)_

- **2026-05-12 10:57** · `oc_ec1876c35e5187d9af9c532479316df0` · 易铃 
  - 类型: text；message_id: `om_x100b6f1d3f9c10acb2eb55b19e88720`
  https://r3c0qt6yjw.feishu.cn/wiki/UpLswH0x0i5HFOkkYmUcgYElnie?from=from_copylink@温俊薇 辛苦解析停车场采集数据，按4dlane的方式解析，送解析时间已更新
  _(消息已编辑)_

- **2026-05-12 10:58** · `oc_72811ede6885e73bafaf59833751bb54` · cli_a0c2cea3eef8100d 
  - 类型: interactive；message_id: `om_x100b6f1d38be208cc4a45ecdf400ab6`
  <card title="权限申请（外部）">
  外部用户 @7561253355551932419 向你申请文档 [3d_抬杆_v1.0 标注规则文档](https://r3c0qt6yjw.feishu.cn/wiki/IcljwYD6SivdXEkbd1QcqPu9nSd?from=botpush) 的阅读权限。
  📝 该用户为外部用户，请注意信息安全。
  [同意] [拒绝]
  </card>

- **2026-05-12 11:00** · `oc_0c8ac7bcf8356d609d43292bca9de9e4` · cli_a0d9fec6ffb8d00e 
  - 类型: calendar；message_id: `om_x100b6f1d326a38b0b4ca30baa12f268`
  <calendar_invite>
  [交付] od/rod squad 站会
  2026-05-12 10:30:00 ~ 2026-05-12 10:45:00
  </calendar_invite>

- **2026-05-12 11:00** · `oc_a3da123bf52139099d2516ae1b7b189d` · 晋苏航 
  - 类型: post；message_id: `om_x100b6f1d327bd91cc2b19cc641e1f35`
  @陈光萍 @易铃 老师，这边在抽查数据的时候，发现部分数据存在待提交，但是交不上去，也无法驳回，麻烦看下吧
  [Media: file_v3_0011k_08218d82-7296-497a-bd90-fd674823cfcg]
  _(消息已编辑)_

- **2026-05-12 11:01** · `oc_a3da123bf52139099d2516ae1b7b189d` · 陈光萍 
  - 类型: text；message_id: `om_x100b6f1d3190c96cc34f387a05e5dee`
  @晋苏航 统计一下数据包，我这边处理
  _(消息已编辑)_

- **2026-05-12 11:02** · `oc_ec1876c35e5187d9af9c532479316df0` · 崔佳峰 
  - 类型: text；message_id: `om_x100b6f1dcb075488c3c9fda0fb8c968`
  @温俊薇 @董碧璇 后面occ的生产模板需要更新一下，已经生产的就维持现状
  版本41 
  模板ID 16
  _(消息已编辑)_

- **2026-05-12 11:03** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1dc8ad5cacb15de626446b474`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6987495971
  [（自动）闯红灯，p停安全接管，没有停止点](https://project.feishu.cn/ubh28t/issue/detail/6987495971) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6987495971)
  </card>

- **2026-05-12 11:04** · `parking标注` · 蔡孟玥 
  - 类型: post；message_id: `om_x100b6f1dc2e14480c394c4a27fc3711`
  @宋泽旭 泊车位可视化看起来还有个别标注问题，我用的是之前17万val,是都质检过了的嘛
  [Image: img_v3_0211j_176ec5c9-d9d2-4f32-a8ea-4ea02d06712g]
  这个右边车位heading不对
  [Image: img_v3_0211j_3523c617-861b-4eb0-8558-fca9d53840dg]
  右前方投影和实际车位线对不上
  _(消息已编辑)_

- **2026-05-12 11:04** · `oc_ec1876c35e5187d9af9c532479316df0` · 崔佳峰 
  - 类型: text；message_id: `om_x100b6f1dc5877ca0c310d57923a26e7`
  主要改动就是最后保存到pfs上的文件夹内容做了一些精简

- **2026-05-12 11:06** · `parking标注` · 蔡孟玥 
  - 类型: text；message_id: `om_x100b6f1dda808824c45a158e374a60a`
  目前泊车单任务和混合训练有评测和可视化结果，桥总看看效果够用嘛@郭林桥 cc@黄培煜 https://r3c0qt6yjw.feishu.cn/wiki/DFPfwzeA1i7FiokLjC9cqPAUnKc?from=from_copylink
  _(消息已编辑)_

- **2026-05-12 11:07** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f1ddb8998a0b4a16c1510681af`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6930237612
  [闪黄灯不走，接管](https://project.feishu.cn/ubh28t/issue/detail/6930237612) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6930237612)
  </card>

---

_生成说明：`priority=high` 当消息为我方发送、包含对我的 @，或包含 @所有人。可按需调整分类规则。_


---

_已启用「不统计群聊」过滤：**substring** 匹配；模式：AD标注平台正式环境备份清理通知群。拉取 **664** 条，排除 **535** 条，保留 **129** 条。_
