# 飞书消息归档 2026-05-13

以下为同一时间窗口内的飞书会话摘录，已按优先级分组。可直接粘贴到大模型，并要求提取待办、决策与风险点。

## 重点（我发送 / @我 / @所有人）

- **2026-05-13 10:32** · `oc_52fdd080b74628c0c13647af8dd315b7` · ou_b367b07f8b1f4ca91e4fbdabfe086ccd （@我）
  - 类型: text；message_id: `om_x100b6f0a65a0b4d0c31f220ec1fd002`
  <p>开门汽车评测数据已下发</p><p>3D_OD_V2.2_开门汽车评测_0513（1-5），5期，886帧</p><p>@杨思雅 ，cc@常夜 ，@易铃 </p><p>交付时间，今天(5.13)18:00</p><p>需要重点关注其中车门打开的目标必须标注正确</p>
  _(消息已编辑)_

- **2026-05-13 10:32** · `oc_a3da123bf52139099d2516ae1b7b189d` · ou_b367b07f8b1f4ca91e4fbdabfe086ccd （@我）
  - 类型: text；message_id: `om_x100b6f0a659e1494c4941a1868c2e94`
  <p>开门汽车评测数据已下发</p><p>3D_OD_V2.2_开门汽车评测_0513（6-10），5期，767帧</p><p>@尚程洋 ，cc@常夜 ，@易铃 </p><p>交付时间，今天（5.13）18:00</p><p>需要重点关注其中车门打开的目标必须标注正确</p>
  _(消息已编辑)_

- **2026-05-13 10:50** · `OCC数据交付沟通（内部）` · 宋泽旭 （@我）
  - 类型: post；message_id: `om_x100b6f0a2067c15cc3d53814a7d8c73`
  今日停车位站会总结
  1. 0512累计交付130W有效帧，下游需求120W帧，超额10W帧，相比原计划0522提前10天交付。
  2. 下一步计划0520达成200W帧目标，需要增量70W帧。目前待标注数据量足够，暂无风险。@易铃 
  3. OD FP过滤功能已上线，对比效果如下。
  [Image: img_v3_0211l_81775662-b260-4b9d-8242-dde958cb9deg]
  [Image: img_v3_0211l_e23b2959-208e-4c15-9634-2ad8d55a3aeg]
  4. 下游反馈标注问题与车位问题已答复。@宋泽旭 @易铃 
  cc @史天才 @常夜
  _(消息已编辑)_

- **2026-05-13 11:00** · `OD数据接收` · 杨学凯 （@我）
  - 类型: text；message_id: `om_x100b6f0ada3e08e8b227a0f90de6213`
  @常夜 @易铃 这个能热更新嘛，加个二级标签[捂脸]
  _(消息已编辑)_

- **2026-05-13 11:04** · `OD数据接收` · 易铃 （@我）
  - 类型: text；message_id: `om_x100b6f0aeb8978f0b326a6a412f854d`
  @常夜 辛苦看下
  _(消息已编辑)_

- **2026-05-13 11:23** · `OD数据接收` · 易铃 （@我）
  - 类型: text；message_id: `om_x100b6f0aa7b1e0b4b2f9ced19c0d39c`
  @常夜 可以了[感谢]
  _(消息已编辑)_

- **2026-05-13 13:30** · `oc_a3da123bf52139099d2516ae1b7b189d` · ou_b367b07f8b1f4ca91e4fbdabfe086ccd （@我）
  - 类型: text；message_id: `om_x100b6f748b3bcc90c45cc29a5c17522`
  <p>动物专项任务已下发</p><p>3d_od_v2.2_动物专项_0513（1~300），期数：300，任务量：19213</p><p>@尚程洋 @成铭 ，cc@常夜 ，cc@易铃 </p><p>交付时间：5.15周五15:00</p><p>任务优先级：开门车辆＞动物专项>异型</p><p>连同之前下发的动物一起5.15周五15:00交付</p>
  _(消息已编辑)_

- **2026-05-13 13:30** · `oc_52fdd080b74628c0c13647af8dd315b7` · ou_b367b07f8b1f4ca91e4fbdabfe086ccd （@我）
  - 类型: text；message_id: `om_x100b6f748685b0b4c21aa3eecf847a7`
  <p>动物专项任务已下发</p><p>3d_od_v2.2_动物专项_0513（1~300），期数：300，任务量：19188</p><p>@杨思雅  ，cc@常夜 ，cc@易铃 </p><p>交付时间：5.15周五15:00</p><p>任务优先级：开门车辆＞动物专项>异型</p>
  _(消息已编辑)_

- **2026-05-13 13:53** · `OD数据接收` · 杨学凯 （@我）
  - 类型: post；message_id: `om_x100b6f75501d8084b20ae97cfe68e1d`
  [Image: img_v3_0211l_23273da3-4600-4504-9c89-5f8c9e16ab6g]
  [Image: img_v3_0211l_3995ba3c-a122-4aa9-a0a3-ea82a66eeefg]
  目前看了一些疑似的车头车身分开标注的样例得出结论：
  1、标注存在truck_head + truck_body这样类别的标注；
  2、还存在truck_head + truck_head这种误标，但不影响车头车身合并；
  3、无overlap时，车头车尾相连且极近，这种方式不靠谱，看到的几乎都是两辆正常的小卡；
  目前交付的211w帧内，筛出的超大车分体标注确实特别少，所以目前就采用‘有overlap的大车框合并’这一策略了。@张达 。
  [Image: img_v3_0211l_81b54eec-a7a5-4f3f-bab9-4856e5a971cg]
  建议：大车转弯分体标注可采用有overlap的‘truck_head + truck_body’这种唯一方式标注@常夜 @易铃；
  cc@花云铭 @王见山 @李素雯 @李坤翔
  _(消息已编辑)_

- **2026-05-13 13:57** · `OD数据接收` · 杨学凯 （@我）
  - 类型: text；message_id: `om_x100b6f7565d0dc88b2ef95ff6ab1a8e`
  @常夜 这个很兼容当前的标注方式不怎么需要修改，唯二需要注意的就是“确认规则”+“有重叠”；
  _(消息已编辑)_

- **2026-05-13 15:30** · `oc_52fdd080b74628c0c13647af8dd315b7` · ou_b367b07f8b1f4ca91e4fbdabfe086ccd （@我）
  - 类型: text；message_id: `om_x100b6f76c64110b0c26a4eff72a054c`
  <p>开门货车评测数据已下发</p><p>3D_OD_V2.2_开门货车评测_0513（6-10），5期，656帧</p><p>@杨思雅 ，cc@常夜 ，@易铃 </p><p>交付时间，明天中午(5.14)12:00</p><p>任务优先级：开门车辆＞动物专项>异型</p>
  _(消息已编辑)_

- **2026-05-13 15:31** · `oc_a3da123bf52139099d2516ae1b7b189d` · ou_b367b07f8b1f4ca91e4fbdabfe086ccd （@我）
  - 类型: text；message_id: `om_x100b6f76c53d1cbcc3205302a72b6e2`
  <p>开门货车评测数据已下发</p><p>3D_OD_V2.2_开门货车评测_0513（1-5），5期，389帧</p><p>@尚程洋 @成铭  ，cc@常夜 ，@易铃 </p><p>交付时间，明天中午(5.14)12:00</p><p>任务优先级：开门车辆＞动物专项>异型</p>
  _(消息已编辑)_

- **2026-05-13 16:43** · `oc_a3da123bf52139099d2516ae1b7b189d` · 易铃 （@我）
  - 类型: text；message_id: `om_x100b6f77d556656cb3d3aa74dd0b93d`
  @尚程洋 cc@常夜
  _(消息已编辑)_

- **2026-05-13 18:02** · `oc_ddf03801cbbd86b51688149c081e6567` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f708d7870b8b3c67b4d788cca3`
  这会儿方便语音吗？不是急事，回头再说也行

- **2026-05-13 18:09** · `oc_ddf03801cbbd86b51688149c081e6567` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f7090a568a4c4d1a0b8720aa04`
  晚些时候吧

- **2026-05-13 18:29** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f7166958cb0c2ec19e6f4a5bff`
  哪怕它本质上是标注任务也不列吗

- **2026-05-13 18:55** · `oc_79e55b258e2849e239b0086629571122` · ou_bacb74d08c484f7efb1b7cb22517122c （@我）
  - 类型: text；message_id: `om_x100b6f71c4efa4b8b123b127449491a`
  2026.5.11
  出勤：28人培训9人
  真值作业：1677条   培训；168
  验收occ：279包
  共出勤：31.75人天（请假3人）新人培训9人@易铃 @常夜
  _(消息已编辑)_

- **2026-05-13 18:56** · `oc_79e55b258e2849e239b0086629571122` · ou_bacb74d08c484f7efb1b7cb22517122c （@我）
  - 类型: text；message_id: `om_x100b6f71c202acb0b2fc959db23e974`
  2026.5.11
  出勤：1人
  停车位障碍物
  验收:85包
  共出勤：1人天@易铃 @常夜
  _(消息已编辑)_

- **2026-05-13 18:56** · `oc_79e55b258e2849e239b0086629571122` · ou_bacb74d08c484f7efb1b7cb22517122c （@我）
  - 类型: text；message_id: `om_x100b6f71c043b440b39ee310e973913`
  2026.5.11
  出勤：7人
  停车位可视化
  作业:1728
  共出勤：7人天@常夜 @易铃
  _(消息已编辑)_

- **2026-05-13 19:44** · `标注运营` · 王见山 （@我）
  - 类型: text；message_id: `om_x100b6f720ca074a0c39e48ef9214c14`
  @常夜 @李鑫鑫 zhangda 提了大车的采集需求了吗
  _(消息已编辑)_

- **2026-05-13 20:12** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f72e2bcad3cb19bde0f73f9ac6`
  只是计提的话应该可以

- **2026-05-13 20:12** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f72e7a56888b19b10cbfabc945`
  不是今天必须做完吧？有啥时间上的要求吗

- **2026-05-13 20:21** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f728235209cc2d5138bbe0299b`
  行是行，但5月审批是暂时不看还是以后也不看了？

- **2026-05-13 20:22** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f729e2198bcc31307dd062ddc1`
  我咋不记得有这事，但这样倒是省事了

- **2026-05-13 20:41** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 常夜 （我发送）
  - 类型: text；message_id: `om_x100b6f7359d2c4a4c3485bf02d5d868`
  是跑了

- **2026-05-13 23:39** · `【高优】高架转禁行区` · 李明 （@我）
  - 类型: post；message_id: `om_x100b6f7dfda0a4a0b302201ed95a90d`
  [https://project.feishu.cn/ubh28t/issueView/KdTPWMAvg?quickFilterId=3K5Qxemq-KiB4-CYQF-LX1W-tQfCLYCOvuSE](https://project.feishu.cn/ubh28t/issueView/KdTPWMAvg?quickFilterId=3K5Qxemq-KiB4-CYQF-LX1W-tQfCLYCOvuSE)
  @王宏伟 hi 宏伟，后续有这类issue流转到你这的话，一般是高架桥下，导航导到高架桥上导致的错误，按以下处理：
  1. 找@常夜 加上高架禁行区（需要@江南 生效到百度平台）；
  2. 加完后找@常夜 用仿真算路测试是否符合预期（是否正确避让高架下的路，是否误避开高架下的路） cc @王见山 
  [Image: img_v3_0211l_c17dd700-d1ad-43b5-80a7-077791b68f7g]
  _(消息已编辑)_

- **2026-05-13 23:40** · `标注运营` · 王见山 （@我）
  - 类型: text；message_id: `om_x100b6f7df64928a4c2a0309389c7a44`
  @常夜 @李鑫鑫 啊对，明天11点，我们对对大车的事
  _(消息已编辑)_

- **2026-05-13 23:48** · `【高优】高架转禁行区` · 李明 （@我）
  - 类型: text；message_id: `om_x100b6f7d98e9b4a4b32c81b1b71ae83`
  @王宏伟 更正了一下，1也找@常夜
  _(消息已编辑)_

## 其他消息

- **2026-05-13 11:01** · `AD二部` · 江岳 
  - 类型: text；message_id: `om_x100b6f0ad9e9048cb280b0ddd0d6902`
  @陈陌 @_all
  _(消息已编辑)_

- **2026-05-13 16:03** · `OCC批量交付通知群` · cli_a3cf26612bf8d00c 
  - 类型: interactive；message_id: `om_x100b6f7748235d00c36e6fc2507e249`
  <card title="项目批量交付通知">
  **交付批次编号：** **20260513155843**
  **交付版本：** **v1.4**
  **交付描述：** **occmil地锁专项交付实例框**
  **交付类型：** **训练**
  **交付项目总量：** 1
  **原始数据集成功：** 1
  **原始数据集失败：** 0
  **子项目成功：** 1
  **子项目失败：** 0
  [交付详情下载](https://annoapi.data.neolix.cn/deliveryNoAuth/detailDownload?recordId=2054471383953584128) [统计详情下载](https://annoapi.data.neolix.cn/deliveryNoAuth/statDownload?recordId=2054471383953584128&statId=2054472707222941696)
  📢 标注平台通知 @everyone
  </card>

- **2026-05-13 16:17** · `高架禁行区导入测试` · 王宏伟 
  - 类型: post；message_id: `om_x100b6f7776d9bcbcc2a0cde553b810f`
  [Image: img_v3_0211l_ad41a8c8-b080-47fa-ac15-f26fea7d2a3g]
  [Image: img_v3_0211l_20d9bcc8-361b-4d8f-be12-a3da0ec86aag]
  @all 请教一下，为什么有的还没有导入的禁行区会显示在仿真页面上呀

- **2026-05-13 17:58** · `TLD&ROD数据交付` · 董碧璇 
  - 类型: post；message_id: `om_x100b6f70f8faa078b3232863f4c2873`
  @车启谣 
  今天交付
  1.回灌数据，有效帧数3.5w，951个clip。每期任务对应的回灌id更新在表中
  [Image: img_v3_0211l_6a88a434-0085-4dd5-93c8-022679c33e1g]
  2.不同方向灯在同一灯框，交付挖掘数据5k帧
  [Image: img_v3_0211l_8172096d-639f-422a-bf53-e705de009a9g]
  @李杰 @李奥 @李素雯 cc
  _(消息已编辑)_

- **2026-05-13 17:59** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f70f6d218b0c456e225ac4356d`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990605013
  [takeover_event__X6S0847_2026-05-13 13:50:08](https://project.feishu.cn/ubh28t/issue/detail/6990605013) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990605013)
  </card>

- **2026-05-13 18:03** · `oc_ddf03801cbbd86b51688149c081e6567` · 易铃 
  - 类型: text；message_id: `om_x100b6f708bb7bc88b280958ee672188`
  马上，最后一个停车位交了就行

- **2026-05-13 18:04** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f708786bca4c34f2fe4e6bdae6`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990396641
  [takeover_event__X6S5107_2026-05-13 16:11:55](https://project.feishu.cn/ubh28t/issue/detail/6990396641) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990396641)
  </card>

- **2026-05-13 18:05** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f70832d20a8c36cf5703bb5c3d`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990460071
  [takeover_event__X6S5811_1778656995895](https://project.feishu.cn/ubh28t/issue/detail/6990460071) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990460071)
  </card>

- **2026-05-13 18:06** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f709d5700bcc3333927c477f47`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990660510
  [extricate_pnc_ratio_X610036_1778661987820](https://project.feishu.cn/ubh28t/issue/detail/6990660510) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990660510)
  </card>

- **2026-05-13 18:08** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7094e90494c4244f65eb97ee5`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990457039
  [extricate_pnc_ratio_X6S5142_2026-05-13 17:06:29](https://project.feishu.cn/ubh28t/issue/detail/6990457039) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990457039)
  </card>

- **2026-05-13 18:08** · `OCC数据交付沟通（内部）` · 易铃 
  - 类型: text；message_id: `om_x100b6f7094c6c8a0b2f88eadba9588d`
  https://r3c0qt6yjw.feishu.cn/wiki/G7CBwlQmXijNCKkJMi8cpE4tnOh?from=from_copylinkhttps://r3c0qt6yjw.feishu.cn/wiki/GY0UwMye6iYtdKkzCk6cJuBXnRf?from=from_copylink今日停车位交付了@宋泽旭
  _(消息已编辑)_

- **2026-05-13 18:08** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7097828084c2cd6d111e26e00`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990649497
  [extricate_pnc_ratio_X6S5107_2026-05-13 16:11:50](https://project.feishu.cn/ubh28t/issue/detail/6990649497) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990649497)
  </card>

- **2026-05-13 18:09** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7091fe1cb8c4cfe54a89a5e5c`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990412471
  [extricate_pnc_ratio_X6S5816_1778659046232](https://project.feishu.cn/ubh28t/issue/detail/6990412471) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990412471)
  </card>

- **2026-05-13 18:09** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7093ec3cb0c225e52033e3c32`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990496674
  [extricate_pnc_ratio_X6S6115_2026-05-13 16:29:06](https://project.feishu.cn/ubh28t/issue/detail/6990496674) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990496674)
  </card>

- **2026-05-13 18:09** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7090de9cb4c22217227e9f3b3`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989938701
  [extricate_pnc_ratio_X6S6141_2026-05-13 13:34:46](https://project.feishu.cn/ubh28t/issue/detail/6989938701) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989938701)
  </card>

- **2026-05-13 18:09** · `oc_ddf03801cbbd86b51688149c081e6567` · 易铃 
  - 类型: text；message_id: `om_x100b6f7091ced484b3cd1351040fe41`
  好滴

- **2026-05-13 18:10** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 张祥伟 
  - 类型: post；message_id: `om_x100b6f70916e38b8b39a794823d626f`
  [Image: img_v3_0211l_7c90f4bd-ad3c-48fe-96ff-ea1a3bce859g]
  @王健博 老师，表格新增的看了一遍。截图这个和20是一个位置。24和25检查了中心线是联通的，红绿灯关联是对的
  _(消息已编辑)_

- **2026-05-13 18:10** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f70ac502458c36a6a56b5762bb`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990504994
  [extricate_pnc_ratio_X6S7873_1778660352803](https://project.feishu.cn/ubh28t/issue/detail/6990504994) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990504994)
  </card>

- **2026-05-13 18:11** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 王健博 
  - 类型: text；message_id: `om_x100b6f70aae34c88c4da8be9cd83dbc`
  @张祥伟 
  好的，修改那一列同步说明好就行
  _(消息已编辑)_

- **2026-05-13 18:11** · `oc_293709c98fa3c8f96f55c2b4fcb89a0d` · 张祥伟 
  - 类型: text；message_id: `om_x100b6f70a898a8a8b2ea543ee497457`
  @王健博 我没有修改权限
  _(消息已编辑)_

- **2026-05-13 18:12** · `oc_a3da123bf52139099d2516ae1b7b189d` · ou_7e6b306e1c0900135d2babcf03d49a9f 
  - 类型: post；message_id: `om_x100b6f70a4e050b4b4a2749f618719c`
  老师 厂房里的物体标注吗@陈光萍 
  [Image: img_v3_0211l_c6334a2b-1475-4132-9b03-91a69c0257cg]
  _(消息已编辑)_

- **2026-05-13 18:13** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f70a3e0e4a0c3a12b7afc40237`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990702002
  [extricate_pnc_ratio_X6S6060_2026-05-13 14:19:52](https://project.feishu.cn/ubh28t/issue/detail/6990702002) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990702002)
  </card>

- **2026-05-13 18:13** · `oc_26f131b833bb664ce27a5238de726ed3` · ou_3b92bf225082b23c75274a356f7dcf6e 
  - 类型: text；message_id: `om_x100b6f70a581ec94b34c6b366f2bc8c`
  @王健博 可以作业了吧老师
  _(消息已编辑)_

- **2026-05-13 18:15** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f70bd0390b8c266740d7d942f5`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990552028
  [takeover_event__X6S0525_1778658473434](https://project.feishu.cn/ubh28t/issue/detail/6990552028) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990552028)
  </card>

- **2026-05-13 18:20** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f714866a4a4c4944f8874cbe1c`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990025626
  [takeover_event__X6S5817_1778655250796](https://project.feishu.cn/ubh28t/issue/detail/6990025626) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990025626)
  </card>

- **2026-05-13 18:20** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f714b7e90b0c3d8e467c9cd4e3`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990051830
  [takeover_event__X6S5817_1778656544649](https://project.feishu.cn/ubh28t/issue/detail/6990051830) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990051830)
  </card>

- **2026-05-13 18:24** · `oc_ec1876c35e5187d9af9c532479316df0` · 郑思琪 
  - 类型: file；message_id: `om_x100b6f715ba00cbcb253bcac254c623`
  <file key="file_v3_0011l_45a7a068-d8b1-4586-8303-92699939f07g" name="issue2.xlsx"/>
  _(消息已编辑)_

- **2026-05-13 18:24** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7158f678a0c44c1a16d4d83eb`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990037077
  [extricate_pnc_ratio_X6S0778_2026-05-13 14:00:53](https://project.feishu.cn/ubh28t/issue/detail/6990037077) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990037077)
  </card>

- **2026-05-13 18:25** · `oc_ec1876c35e5187d9af9c532479316df0` · 郑思琪 
  - 类型: text；message_id: `om_x100b6f7159099918b398fc83a95c5b0`
  <p>@董碧璇 麻烦提一下解析41</p>
  _(消息已编辑)_

- **2026-05-13 18:26** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f71536ff4a4c42ada7e2a08197`
  不然就结重了

- **2026-05-13 18:26** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: post；message_id: `om_x100b6f71539e8088c395871715c4d14`
  y哥，后面中研按照人天结算的不用在标注账单里列出来哈，这部分费用会出现在验收表单里
  [Image: img_v3_0211l_8bf21797-c8ab-4509-8407-6e3f1688fe5g]

- **2026-05-13 18:28** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f716b40a4a0c4a18ab3d1a9c36`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990019795
  [extricate_pnc_ratio_X6S6172_2026-05-13 15:13:12](https://project.feishu.cn/ubh28t/issue/detail/6990019795) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990019795)
  </card>

- **2026-05-13 18:31** · `oc_ec1876c35e5187d9af9c532479316df0` · 董碧璇 
  - 类型: text；message_id: `om_x100b6f7161e1c0a0b29db84ba72000b`
  @郑思琪 https://nds.data.neolix.cn/#/resource/data-workflow/batch-task/detail/35031
  _(消息已编辑)_

- **2026-05-13 18:31** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7161d384a8c22867dfd868348`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989546424
  [localfail_event_X6S8234_1778596260084](https://project.feishu.cn/ubh28t/issue/detail/6989546424) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989546424)
  </card>

- **2026-05-13 18:35** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f71718428b8c2a9f9607c9857d`
  只要给中研按照人力来结算的，就不出现在标注账单里

- **2026-05-13 18:36** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f710fef5480c44f41bbf85e141`
  给其他供应商按人力来结算的可以出现在标注账单

- **2026-05-13 18:37** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71094e7ca4c332225fb982121`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990404563
  [takeover_event__X6S5101_2026-05-13 15:50:30](https://project.feishu.cn/ubh28t/issue/detail/6990404563) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990404563)
  </card>

- **2026-05-13 18:38** · `oc_029d77c6f6164f7af06a0795e8afb8d5` · 冯义洋 
  - 类型: text；message_id: `om_x100b6f7104f524b4c3bda21ebb6c192`
  @崔佳峰 采集地锁lock_rawdata_0512_pfs已回收
  _(消息已编辑)_

- **2026-05-13 18:39** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71015d70a8c439ba635dadee3`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990485609
  [extricate_pnc_ratio_X6S5107_2026-05-13 15:25:35](https://project.feishu.cn/ubh28t/issue/detail/6990485609) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990485609)
  </card>

- **2026-05-13 18:39** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f710170e0a0c21c6090e6085e8`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990560521
  [vehicle_control_error_max_X6S5142_2026-05-13 15:28:34](https://project.feishu.cn/ubh28t/issue/detail/6990560521) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990560521)
  </card>

- **2026-05-13 18:41** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f711a2d9104c3c819a3bafa484`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990493578
  [extricate_pnc_ratio_X6S5817_1778650843114](https://project.feishu.cn/ubh28t/issue/detail/6990493578) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990493578)
  </card>

- **2026-05-13 18:42** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7116dd4ca4c2c6bb873b3bffe`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990644522
  [extricate_pnc_ratio_X6S5107_2026-05-13 15:38:47](https://project.feishu.cn/ubh28t/issue/detail/6990644522) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990644522)
  </card>

- **2026-05-13 18:43** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7110f9aca4c3a8a90ccfae9a2`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990550519
  [extricate_pnc_ratio_X6S6060_2026-05-13 13:49:07](https://project.feishu.cn/ubh28t/issue/detail/6990550519) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990550519)
  </card>

- **2026-05-13 18:48** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f713fccecbcc38f76bc236dfbb`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6988746925
  [cloudapp_event_X6S0730_2026-05-12 10:28:38](https://project.feishu.cn/ubh28t/issue/detail/6988746925) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6988746925)
  </card>

- **2026-05-13 18:51** · `高架禁行区导入测试` · 李明 
  - 类型: text；message_id: `om_x100b6f713429cca4b25329a90846dbf`
  @王宏伟 这个页面上的就是从百度的里面拿的，在这里看得到的说明就是生效了的。至于为什么会上传生效，需要找@江南 确认
  _(消息已编辑)_

- **2026-05-13 18:51** · `高架禁行区导入测试` · 李明 
  - 类型: text；message_id: `om_x100b6f7132260cacb30c8ab2d3e548c`
  @王宏伟 这个是你加的吗
  _(消息已编辑)_

- **2026-05-13 18:53** · `高架禁行区导入测试` · 李明 
  - 类型: text；message_id: `om_x100b6f71cafffcb8b115f1ddfedb90c`
  https://nem.neolix.net/#/login 你注册一个准时达正式版，从这里可以看到的网联画的是啥
  _(消息已编辑)_

- **2026-05-13 18:53** · `高架禁行区导入测试` · 王宏伟 
  - 类型: text；message_id: `om_x100b6f71ce320484c3d47e8f048dabf`
  @李明 我没加啊，自己就有的
  _(消息已编辑)_

- **2026-05-13 18:54** · `高架禁行区导入测试` · 李明 
  - 类型: text；message_id: `om_x100b6f71ca6774a4b3e5a4d7dfc1147`
  @王宏伟 那可能是网联加的
  _(消息已编辑)_

- **2026-05-13 18:54** · `高架禁行区导入测试` · 李明 
  - 类型: text；message_id: `om_x100b6f71cb5ee8bcb3701eccabfc15d`
  @王宏伟 没同步给百度是啥意思
  _(消息已编辑)_

- **2026-05-13 18:55** · `高架禁行区导入测试` · 李明 
  - 类型: text；message_id: `om_x100b6f71c51c6108b30eb1d7d46ca33`
  @王宏伟 你在仿真页面上能看到的 都是同步到百度那了的
  _(消息已编辑)_

- **2026-05-13 18:55** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71c6f0ecb4c36350a43d1c600`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989946140
  [takeover_event__X6S6007_2026-05-13 11:04:10](https://project.feishu.cn/ubh28t/issue/detail/6989946140) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989946140)
  </card>

- **2026-05-13 18:55** · `高架禁行区导入测试` · 王宏伟 
  - 类型: text；message_id: `om_x100b6f71c77a68a0c105141371abc57`
  @李明 就是这些禁行区要先给到百度那边生效才会参与算路
  _(消息已编辑)_

- **2026-05-13 18:56** · `高架禁行区导入测试` · 王宏伟 
  - 类型: post；message_id: `om_x100b6f71c3da5cbcc2c52d93688070a`
  [Image: img_v3_0211l_71adf85a-5155-4dd7-8624-04ae38edc02g]
  @江南 南哥说有这个才是生效的
  _(消息已编辑)_

- **2026-05-13 18:56** · `高架禁行区导入测试` · 江南 
  - 类型: post；message_id: `om_x100b6f71c1aa5d68b3280832d0bfaba`
  [Image: img_v3_0211l_d90614be-0149-48dd-a987-8031b8adf48g]
  这个页面里的数据是从 NDS 上同步过来的，还是从 百度绘图同步过来的？
  _(消息已编辑)_

- **2026-05-13 18:57** · `高架禁行区导入测试` · 李明 
  - 类型: text；message_id: `om_x100b6f71c11b9480b2f9ce1aed845fa`
  @王宏伟 那你和他对齐一下看看，仿真页面上的是从百度数据库里面拉取的
  _(消息已编辑)_

- **2026-05-13 18:57** · `高架禁行区导入测试` · 王宏伟 
  - 类型: text；message_id: `om_x100b6f71ddd500a8c2eae855155020d`
  那意思是不走这个平台也能把禁行区添加到百度数据库里吗

- **2026-05-13 18:57** · `高架禁行区导入测试` · 李明 
  - 类型: text；message_id: `om_x100b6f71def37c8cb24a7c55903b3b9`
  @江南 百度
  _(消息已编辑)_

- **2026-05-13 19:00** · `静态数据交付沟通（内部）` · 郑思琪 
  - 类型: text；message_id: `om_x100b6f71d5389d00b2469fb7080e03a`
  @史天才 https://r3c0qt6yjw.feishu.cn/wiki/IZCpwf2wWiut1pkG2whcaHaynjd?from=from_copylink
  _(消息已编辑)_

- **2026-05-13 19:00** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71d21754b8c260932da5f7a73`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989919067
  [takeover_event__X6S6007_2026-05-13 09:44:46](https://project.feishu.cn/ubh28t/issue/detail/6989919067) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989919067)
  </card>

- **2026-05-13 19:05** · `高架禁行区导入测试` · 王宏伟 
  - 类型: text；message_id: `om_x100b6f71e08ddca0c35a72fb5244709`
  @李明
  _(消息已编辑)_

- **2026-05-13 19:05** · `高架禁行区导入测试` · 王宏伟 
  - 类型: text；message_id: `om_x100b6f71e3206080c24607f916785b3`
  http://180.76.118.182:8060/limitation_live.html

- **2026-05-13 19:06** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71fadfdca8c39e10dd65f9d2f`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990503052
  [extricate_pnc_ratio_X6S5101_2026-05-13 15:45:04](https://project.feishu.cn/ubh28t/issue/detail/6990503052) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990503052)
  </card>

- **2026-05-13 19:06** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71fd60acb0c2d84c2c93ed59c`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989981530
  [extricate_pnc_ratio_X6S6007_2026-05-13 11:03:52](https://project.feishu.cn/ubh28t/issue/detail/6989981530) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989981530)
  </card>

- **2026-05-13 19:13** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71809decacc22bf973eac8363`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990404580
  [extricate_pnc_ratio_X6S5107_2026-05-13 15:14:09](https://project.feishu.cn/ubh28t/issue/detail/6990404580) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990404580)
  </card>

- **2026-05-13 19:14** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f719cf078bcc3668f01600cbb0`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990066211
  [extricate_pnc_ratio_X610034_1778660832561](https://project.feishu.cn/ubh28t/issue/detail/6990066211) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990066211)
  </card>

- **2026-05-13 19:15** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f719879f080c332a228d901188`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989899732
  [p_stop_X6S6007_2026-05-13 13:03:16](https://project.feishu.cn/ubh28t/issue/detail/6989899732) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989899732)
  </card>

- **2026-05-13 19:17** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71953cc0acc39f91198ae8fbf`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990258093
  [extricate_pnc_ratio_X6S5107_2026-05-13 15:28:18](https://project.feishu.cn/ubh28t/issue/detail/6990258093) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990258093)
  </card>

- **2026-05-13 19:17** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71936ec8b0c3222b0d8f90d3c`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990353165
  [extricate_pnc_ratio_X6S0860_2026-05-13 18:18:57](https://project.feishu.cn/ubh28t/issue/detail/6990353165) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990353165)
  </card>

- **2026-05-13 19:18** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71ae3604a4c2d59ed7ccf0f14`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990437566
  [p_stop_X6S6060_2026-05-13 13:25:33](https://project.feishu.cn/ubh28t/issue/detail/6990437566) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990437566)
  </card>

- **2026-05-13 19:22** · `图南标注沟通-内部` · 李明 
  - 类型: text；message_id: `om_x100b6f71a362e4b0b294568df5da24c`
  @王健博 今天新标了多少issue路线？
  _(消息已编辑)_

- **2026-05-13 19:24** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f71b8e37500c3cdecd72135141`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990614003
  [takeover_event__X6S6060_2026-05-13 13:21:50](https://project.feishu.cn/ubh28t/issue/detail/6990614003) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990614003)
  </card>

- **2026-05-13 19:27** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f724dacbf90c31bb2a07994bf6`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989520453
  [localfail_event_X6S8240_1778608655615](https://project.feishu.cn/ubh28t/issue/detail/6989520453) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989520453)
  </card>

- **2026-05-13 19:30** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7245602490c446cd6a400606a`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990568023
  [extricate_pnc_ratio_X6S0847_2026-05-13 13:49:27](https://project.feishu.cn/ubh28t/issue/detail/6990568023) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990568023)
  </card>

- **2026-05-13 19:30** · `图南标注沟通-内部` · 王健博 
  - 类型: text；message_id: `om_x100b6f7243d8d0f8c4a80a6b54d5285`
  @李明 56条明哥
  _(消息已编辑)_

- **2026-05-13 19:32** · `oc_029d77c6f6164f7af06a0795e8afb8d5` · 崔佳峰 
  - 类型: text；message_id: `om_x100b6f7258679ca8c2e49d123d8c3f4`
  @冯义洋 @王健博 这个已经送人标了哈
  _(消息已编辑)_

- **2026-05-13 19:36** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f726b4294acc10073acef7d041`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990464630
  [vehicle_control_error_max_X6S6022_2026-05-13 16:11:02](https://project.feishu.cn/ubh28t/issue/detail/6990464630) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990464630)
  </card>

- **2026-05-13 19:40** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f727c8f1cb4c4c7b62a897e920`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990394570
  [takeover_event__X6S6141_2026-05-13 13:56:06](https://project.feishu.cn/ubh28t/issue/detail/6990394570) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990394570)
  </card>

- **2026-05-13 19:42** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f727462f8bcc4a0b59ac6e5798`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990624606
  [routertrigger_event_X6S5814_1778663894639](https://project.feishu.cn/ubh28t/issue/detail/6990624606) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990624606)
  </card>

- **2026-05-13 19:44** · `标注运营` · 王见山 
  - 类型: image；message_id: `om_x100b6f720c04acb8b486aa9f1827bac`
  [Image: img_v3_0211l_6a03fd05-e1b4-47f7-8242-c7d5a2a84acg]

- **2026-05-13 19:45** · `标注运营` · 李鑫鑫 
  - 类型: text；message_id: `om_x100b6f720a14c0a0b39c5a77aa06a0c`
  @王见山 提了
  _(消息已编辑)_

- **2026-05-13 19:45** · `标注运营` · 王见山 
  - 类型: text；message_id: `om_x100b6f720bb028bcc3d17f403a8c5e5`
  啥时候提的啊

- **2026-05-13 19:46** · `标注运营` · 李鑫鑫 
  - 类型: text；message_id: `om_x100b6f7204480ca0b4cb2445b2d39d5`
  <p>@王见山 </p><p>昨天提的，期望28号拿到标注数据</p>
  _(消息已编辑)_

- **2026-05-13 19:47** · `标注运营` · 王见山 
  - 类型: text；message_id: `om_x100b6f7205a6fcb0c362c1697e5257a`
  @李鑫鑫 需求文档有吗
  _(消息已编辑)_

- **2026-05-13 19:49** · `标注运营` · 李鑫鑫 
  - 类型: text；message_id: `om_x100b6f721d5a88b0b254a9a2e610b40`
  @王见山  28号拿到标注数据  山哥
  https://r3c0qt6yjw.feishu.cn/wiki/Wgr1whmkbiV9Eok1W8hc9ql3nGe
  https://r3c0qt6yjw.feishu.cn/wiki/PpMpwWHhli0JNokL61qc9U5enRb
  https://r3c0qt6yjw.feishu.cn/wiki/WFtwwVfpoifF5lkC2fxci1mrn7b
  _(消息已编辑)_

- **2026-05-13 19:53** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f722ce030b0c31e042a9c31a3e`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990394733
  [hard_brake__X6S5816_1778668172213](https://project.feishu.cn/ubh28t/issue/detail/6990394733) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990394733)
  </card>

- **2026-05-13 19:56** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f723e6ff4b8c4c8b4416c90a33`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990587508
  [vehicle_control_error_max_X6S6022_2026-05-13 14:15:01](https://project.feishu.cn/ubh28t/issue/detail/6990587508) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990587508)
  </card>

- **2026-05-13 19:56** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f723eb298b0c108cb1db07834d`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990464764
  [takeover_event__X6S4764_1778658409210](https://project.feishu.cn/ubh28t/issue/detail/6990464764) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990464764)
  </card>

- **2026-05-13 19:56** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f72210eeca4c447e28ef5342bd`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990493661
  [extricate_pnc_ratio_X6S5816_1778667414677](https://project.feishu.cn/ubh28t/issue/detail/6990493661) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990493661)
  </card>

- **2026-05-13 19:57** · `数采软件专项沟通群` · 王泽旭 
  - 类型: text；message_id: `om_x100b6f723c07f8a4b3d788d07af2900`
  https://git.neodrive.neolix.net/longshan/model/interface/model_infer/-/commit/14b326919c26ff95bd56e28e448eef7334bcdad2
  @李逸辰 chen 哥用这个 model infer 的commit 试下吧
  _(消息已编辑)_

- **2026-05-13 20:05** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f72dfd888a0c3169a48dc79c9a`
  https://r3c0qt6yjw.feishu.cn/wiki/GymJwKIWqi0jCDkd2Fuc90wPntf

- **2026-05-13 20:05** · `oc_72811ede6885e73bafaf59833751bb54` · cli_a0c2cea3eef8100d 
  - 类型: interactive；message_id: `om_x100b6f72ded91ca8b30ed9a3d8ccb33`
  <card title="图表授权提醒">
  @7561364314662502402 已为文档 [ 数据运营汇报-2605 ](https://r3c0qt6yjw.feishu.cn/docx/RI16dBPigocDxbxx5WrcWzXqnNl?from=botpush) 的协作者开通了表格 [ 各月运营情况图表 ](https://r3c0qt6yjw.feishu.cn/sheets/OPl1sRqfGhiH2ItsgdTc8enanef) 里的图表 [ 3月标注业务花费占比情况 ](https://r3c0qt6yjw.feishu.cn/sheets/OPl1sRqfGhiH2ItsgdTc8enanef?floatBlock=chtcn2ztvDR11mCavzLwlkN0Sbf) 的阅读权限。
  </card>

- **2026-05-13 20:05** · `oc_72811ede6885e73bafaf59833751bb54` · cli_a0c2cea3eef8100d 
  - 类型: interactive；message_id: `om_x100b6f72ded5c0a8c278a22b1fec9b4`
  <card title="图表授权提醒">
  @7561364314662502402 已为文档 [ 数据运营汇报-2605 ](https://r3c0qt6yjw.feishu.cn/docx/RI16dBPigocDxbxx5WrcWzXqnNl?from=botpush) 的协作者开通了表格 [ 2026数据标注生产需求统计 ](https://r3c0qt6yjw.feishu.cn/sheets/CnlbsdaprhVkIctmigqcCBqAnbe) 里的图表 [ 四月单项需求预计花费 ](https://r3c0qt6yjw.feishu.cn/sheets/CnlbsdaprhVkIctmigqcCBqAnbe?floatBlock=chtcnLccyHDmpoW32JGDR29xinb) 的阅读权限。
  </card>

- **2026-05-13 20:05** · `oc_72811ede6885e73bafaf59833751bb54` · cli_a0c2cea3eef8100d 
  - 类型: interactive；message_id: `om_x100b6f72ded91110b2f43158692d27e`
  <card title="图表授权提醒">
  @7561364314662502402 已为文档 [ 数据运营汇报-2605 ](https://r3c0qt6yjw.feishu.cn/docx/RI16dBPigocDxbxx5WrcWzXqnNl?from=botpush) 的协作者开通了表格 [ 各月运营情况图表 ](https://r3c0qt6yjw.feishu.cn/sheets/OPl1sRqfGhiH2ItsgdTc8enanef) 里的图表 [ 业务大类花费占比情况 ](https://r3c0qt6yjw.feishu.cn/sheets/OPl1sRqfGhiH2ItsgdTc8enanef?floatBlock=chtcnLebBOZDZoVPC9gGLkY9c0d) 的阅读权限。
  </card>

- **2026-05-13 20:05** · `oc_72811ede6885e73bafaf59833751bb54` · cli_a0c2cea3eef8100d 
  - 类型: interactive；message_id: `om_x100b6f72dedb84a4b4cab0daddb3dfc`
  <card title="图表授权提醒">
  @7561364314662502402 已为文档 [ 数据运营汇报-2605 ](https://r3c0qt6yjw.feishu.cn/docx/RI16dBPigocDxbxx5WrcWzXqnNl?from=botpush) 的协作者开通了表格 [ 各月运营情况图表 ](https://r3c0qt6yjw.feishu.cn/sheets/OPl1sRqfGhiH2ItsgdTc8enanef) 里的图表 [ 26Q1标注预算 ](https://r3c0qt6yjw.feishu.cn/sheets/OPl1sRqfGhiH2ItsgdTc8enanef?floatBlock=chtcnXDWoLOYAZMg0W9ks3FhIQh) 的阅读权限。
  </card>

- **2026-05-13 20:06** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f72dd64e0a0c3b348e3334a92d`
  咱俩先把计提费用做起来吧

- **2026-05-13 20:06** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f72dc2a58b0c424f818de0b3ca`
  我打算把能填的都先填了，目前账单还短4dlane的没出金额

- **2026-05-13 20:12** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f72e5a3c93cc49e3e3cac0c55e`
  你估么明天上午能做出来不
  _(消息已编辑)_

- **2026-05-13 20:13** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f72fecf3480c3d5f38f049b02b`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990561668
  [extricate_pnc_ratio_X6S7871_1778671445724](https://project.feishu.cn/ubh28t/issue/detail/6990561668) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990561668)
  </card>

- **2026-05-13 20:13** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f72e0440cb8c218e61d085ad12`
  其他的只更新一下图表的底表文字应该也还ok吧

- **2026-05-13 20:13** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f72e182bcb8c435f7569d35273`
  5月审批先不看，只看4月账单相关的

- **2026-05-13 20:21** · `oc_2793e8b0517616a39634d0cfb843eca4` · 齐登科 
  - 类型: image；message_id: `om_x100b6f7282802118b3779d045608ee7`
  [Image: img_v3_0211l_daa4801d-13be-4f29-b4bf-d5990d8eb7dg]
  _(消息已编辑)_

- **2026-05-13 20:21** · `oc_2793e8b0517616a39634d0cfb843eca4` · 齐登科 
  - 类型: text；message_id: `om_x100b6f7280df6484b3748f8be422f77`
  @李金秀 老师保存需要很长时间，然后还不显示保存成功[捂脸]
  _(消息已编辑)_

- **2026-05-13 20:22** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f728037fca0c24ae3c2fc33efd`
  不知道，上次4月审批把5月的一块批了，我估计是不咋看了吧

- **2026-05-13 20:24** · `oc_2793e8b0517616a39634d0cfb843eca4` · 李金秀 
  - 类型: text；message_id: `om_x100b6f7298e0d0a4b322210afe68b55`
  @齐登科 等我一下哈
  _(消息已编辑)_

- **2026-05-13 20:25** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f729431bcb0c3585b370f463e9`
  rod归类到OD里面？

- **2026-05-13 20:25** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: image；message_id: `om_x100b6f729497f0a4c4299b31f94d8cc`
  [Image: img_v3_0211l_a2e544a7-7126-4010-8423-94b21de91fdg]

- **2026-05-13 20:26** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f7290657cbcc338172a4897b0c`
  你还在电脑前不，几个归类我还是拉上你一块说吧

- **2026-05-13 20:26** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f72936ff4a4c392b7597d3cc0f`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990551237
  [takeover_event__X6S0829_2026-05-13 19:09:02](https://project.feishu.cn/ubh28t/issue/detail/6990551237) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990551237)
  </card>

- **2026-05-13 20:30** · `oc_2793e8b0517616a39634d0cfb843eca4` · 李金秀 
  - 类型: text；message_id: `om_x100b6f72a199b880b3c8dc50b9e9871`
  @齐登科 刷新一下页面再试试呢，我这边试了一下刷新后更改的东西都还在
  _(消息已编辑)_

- **2026-05-13 20:31** · `oc_2793e8b0517616a39634d0cfb843eca4` · 齐登科 
  - 类型: text；message_id: `om_x100b6f72bcc3e8a8b3b7852a36f8403`
  @李金秀 好的老师，麻烦您啦
  _(消息已编辑)_

- **2026-05-13 20:36** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f734af0f86cc316bd66d3b189b`
  看来Y跑了

- **2026-05-13 20:40** · `可视化质检平台测试` · 袁甫 
  - 类型: text；message_id: `om_x100b6f735bb854a8c33869e9b0f6ffa`
  @_all 质检平台后端服务将于今晚 22:00 更新

- **2026-05-13 20:41** · `oc_9cb8bfdb77d674b1ae72fc3b63dde152` · 李杰 
  - 类型: text；message_id: `om_x100b6f7356981cb8c298b33bf47b2c7`
  跑吧

- **2026-05-13 20:48** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f737e0fa4b4c4353c32f34de77`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989766325
  [p_stop_X6S6141_2026-05-13 09:27:41](https://project.feishu.cn/ubh28t/issue/detail/6989766325) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989766325)
  </card>

- **2026-05-13 20:49** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7378d894a4c34d6d87c117b8b`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990258915
  [extricate_pnc_ratio_X6S0769_2026-05-13 19:57:24](https://project.feishu.cn/ubh28t/issue/detail/6990258915) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990258915)
  </card>

- **2026-05-13 20:49** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f737a8768b0c44b341b56048b7`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990563655
  [extricate_pnc_ratio_X6S6190_2026-05-13 19:58:01](https://project.feishu.cn/ubh28t/issue/detail/6990563655) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990563655)
  </card>

- **2026-05-13 21:00** · `oc_5cd81f2bd38922fb2ac22b16676af3a0` · cli_9ea79da68f35d102 
  - 类型: interactive；message_id: `om_x100b6f7313be24a4c4aa6902e2b18bb`
  <card title="温馨提示">
  为进一步强化办公区域安全管理，提升全员节约意识，营造安全、整洁、节能的办公环境，请各办公室同事严格落实以下事项：
  1. 下班后请及时关闭办公电脑、显示器及各类测试设备电源；确因工作需要长期开机测试的，须履行登记手续并安排专人加强巡查。
  2. 会议室使用完毕后，务必随手关闭电视、空调等电器，严格执行人走电断要求；因会议室通风效果不佳，严禁在会议室内用餐，请自觉保持会议室环境卫生整洁。
  3. 每日最后离开办公室的同事，须认真履行检查职责，确...
  🖼️ Image
  [查看详情](https://applink.feishu.cn/client/web_app/open?appId=cli_9ea79da68f35d102&mode=window&path=%2fannouncement%2fdetail%2f7638618040536763616)
  </card>

- **2026-05-13 21:02** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f732b6f60a0c318875a9d47dd9`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990438321
  [extricate_pnc_ratio_X6S0783_2026-05-13 20:14:36](https://project.feishu.cn/ubh28t/issue/detail/6990438321) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990438321)
  </card>

- **2026-05-13 21:03** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7324a9a0acc433d4243265945`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990069051
  [takeover_event__X6S0525_1778655067082](https://project.feishu.cn/ubh28t/issue/detail/6990069051) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990069051)
  </card>

- **2026-05-13 21:07** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7336b9c0b4c3551040b53f3c7`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990650716
  [extricate_pnc_ratio_X6S5056_2026-05-13 16:46:45](https://project.feishu.cn/ubh28t/issue/detail/6990650716) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990650716)
  </card>

- **2026-05-13 21:18** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f73ef4caca8c2e1aadc18ed420`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990439815
  [extricate_pnc_ratio_X6S5220_2026-05-13 20:22:39](https://project.feishu.cn/ubh28t/issue/detail/6990439815) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990439815)
  </card>

- **2026-05-13 21:18** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f73ee0618acc2a79b68aa0da95`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990258935
  [takeover_event__X6S6029_2026-05-13 19:36:18](https://project.feishu.cn/ubh28t/issue/detail/6990258935) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990258935)
  </card>

- **2026-05-13 21:20** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f73e5632ca4c42c0bb12f6fe0e`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990494791
  [extricate_pnc_ratio_X6S5056_2026-05-13 19:33:03](https://project.feishu.cn/ubh28t/issue/detail/6990494791) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990494791)
  </card>

- **2026-05-13 21:24** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f73f97170b8c32ba9ca6a21207`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990370236
  [extricate_pnc_ratio_X6S6170_2026-05-13 20:29:48](https://project.feishu.cn/ubh28t/issue/detail/6990370236) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990370236)
  </card>

- **2026-05-13 21:30** · `oc_f3c9056e9af49d2aa00fb6b8de03ee76` · 刘轩 
  - 类型: text；message_id: `om_x100b6f7381bfc8b4b13452e93d4bf98`
  @郑思琪 现在可以上线吗。这个修复了
  _(消息已编辑)_

- **2026-05-13 21:33** · `oc_f3c9056e9af49d2aa00fb6b8de03ee76` · 郑思琪 
  - 类型: text；message_id: `om_x100b6f739615d8a4b3d007ab7a70d82`
  @刘轩 辛苦辛苦[送你小红花]
  _(消息已编辑)_

- **2026-05-13 21:34** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7391dc40a0c39b249c3134609`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989966393
  [（自动）变道不打灯 R3](https://project.feishu.cn/ubh28t/issue/detail/6989966393) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989966393)
  </card>

- **2026-05-13 21:34** · `oc_f3c9056e9af49d2aa00fb6b8de03ee76` · 史天才 
  - 类型: sticker；message_id: `om_x100b6f7393d4e4acc3cff21f70026de`
  [Sticker]

- **2026-05-13 21:37** · `oc_f3c9056e9af49d2aa00fb6b8de03ee76` · 刘轩 
  - 类型: text；message_id: `om_x100b6f73a5f9c4a8b3b38e3e9a9e0b8`
  @郑思琪 done
  _(消息已编辑)_

- **2026-05-13 21:38** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f73a221e8a8c339a714d834a08`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990611221
  [extricate_pnc_ratio_X6S5056_2026-05-13 19:35:38](https://project.feishu.cn/ubh28t/issue/detail/6990611221) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990611221)
  </card>

- **2026-05-13 21:38** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f73a20740a0c37d2ba621b5cd3`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990429840
  [takeover_event__X6S6022_2026-05-13 20:17:07](https://project.feishu.cn/ubh28t/issue/detail/6990429840) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990429840)
  </card>

- **2026-05-13 21:42** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f73b36708b0c31eaf99beadd39`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990600239
  [extricate_pnc_ratio_X6S6170_2026-05-13 19:49:37](https://project.feishu.cn/ubh28t/issue/detail/6990600239) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990600239)
  </card>

- **2026-05-13 21:42** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f73b45f2ca0c2eddcd69538751`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990430512
  [extricate_pnc_ratio_X6S6029_2026-05-13 20:40:22](https://project.feishu.cn/ubh28t/issue/detail/6990430512) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990430512)
  </card>

- **2026-05-13 21:51** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c5360a0a4c2c030bb412a174`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990091537
  [extricate_pnc_ratio_X6S5056_2026-05-13 15:34:46](https://project.feishu.cn/ubh28t/issue/detail/6990091537) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990091537)
  </card>

- **2026-05-13 21:53** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c68aed934c2d220c43b7a97c`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989908452
  [routertrigger_event_X6S6172_2026-05-13 11:38:49](https://project.feishu.cn/ubh28t/issue/detail/6989908452) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989908452)
  </card>

- **2026-05-13 21:53** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c6ba9d0a8c49b8c1ae2d694c`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989859700
  [routertrigger_event_X6S6172_2026-05-13 12:47:51](https://project.feishu.cn/ubh28t/issue/detail/6989859700) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989859700)
  </card>

- **2026-05-13 21:54** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c6956a8a4c2dab49de8ef747`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990552374
  [extricate_pnc_ratio_X6S5056_2026-05-13 14:00:44](https://project.feishu.cn/ubh28t/issue/detail/6990552374) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990552374)
  </card>

- **2026-05-13 22:02** · `批量交付通知群` · cli_a3cf26612bf8d00c 
  - 类型: interactive；message_id: `om_x100b6f7c096f5ca0c29bc551a43790d`
  <card title="项目批量交付通知">
  **交付批次编号：** **20260513215308**
  **交付版本：** **v1.4**
  **交付描述：** **掉头**
  **交付类型：** **训练**
  **交付项目总量：** 282
  **原始数据集成功：** 282
  **原始数据集失败：** 0
  **子项目成功：** 282
  **子项目失败：** 0
  [交付详情下载](https://annoapi.data.neolix.cn/deliveryNoAuth/detailDownload?recordId=2054560580282552320) [统计详情下载](https://annoapi.data.neolix.cn/deliveryNoAuth/statDownload?recordId=2054560580282552320&statId=2054562950336942080)
  📢 标注平台通知 @everyone
  </card>

- **2026-05-13 22:05** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c1ae2c4a4c2a7b81a99bcb40`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990479816
  [extricate_pnc_ratio_X6S6038_2026-05-13 19:58:59](https://project.feishu.cn/ubh28t/issue/detail/6990479816) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990479816)
  </card>

- **2026-05-13 22:05** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c1c391ca0c44d33024374e86`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990661348
  [takeover_event__X6S8218_1778677239794](https://project.feishu.cn/ubh28t/issue/detail/6990661348) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990661348)
  </card>

- **2026-05-13 22:05** · `可视化质检平台测试` · 袁甫 
  - 类型: text；message_id: `om_x100b6f7c1a86c8a0c4a69d0d78e4f8e`
  已完成质检平台后端服务更新

- **2026-05-13 22:18** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7cca9374a4c246bd4722c3afe`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990661360
  [takeover_event__X6S0847_2026-05-13 21:12:04](https://project.feishu.cn/ubh28t/issue/detail/6990661360) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990661360)
  </card>

- **2026-05-13 22:18** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7cca03a0a8c4a3c878bff10fe`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990415337
  [extricate_pnc_ratio_X6S5220_2026-05-13 21:35:00](https://project.feishu.cn/ubh28t/issue/detail/6990415337) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990415337)
  </card>

- **2026-05-13 22:18** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7ccccff8acc38822c33e54341`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990369348
  [takeover_event__X6S0879_1778671613314](https://project.feishu.cn/ubh28t/issue/detail/6990369348) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990369348)
  </card>

- **2026-05-13 22:22** · `批量交付通知群` · cli_a3cf26612bf8d00c 
  - 类型: interactive；message_id: `om_x100b6f7cdff160a8c45ebae2077bc97`
  <card title="项目批量交付通知">
  **交付批次编号：** **20260513221413**
  **交付版本：** **v1.4**
  **交付描述：** **直行**
  **交付类型：** **训练**
  **交付项目总量：** 172
  **原始数据集成功：** 172
  **原始数据集失败：** 0
  **子项目成功：** 172
  **子项目失败：** 0
  [交付详情下载](https://annoapi.data.neolix.cn/deliveryNoAuth/detailDownload?recordId=2054565884856578048) [统计详情下载](https://annoapi.data.neolix.cn/deliveryNoAuth/statDownload?recordId=2054565884856578048&statId=2054567889838739456)
  📢 标注平台通知 @everyone
  </card>

- **2026-05-13 22:23** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7cd98c28b0c4c3920af4b4ac6`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990067306
  [vehicle_control_error_max_X6S6172_2026-05-13 16:19:23](https://project.feishu.cn/ubh28t/issue/detail/6990067306) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990067306)
  </card>

- **2026-05-13 22:25** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7cd0c098a4c38c61f3dbdc94a`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990606310
  [takeover_event__X6S6561_1778672737277](https://project.feishu.cn/ubh28t/issue/detail/6990606310) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990606310)
  </card>

- **2026-05-13 22:35** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c8dfbe0a8c38fb9253a138c2`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990371339
  [hard_brake__X6S5056_2026-05-13 13:57:46](https://project.feishu.cn/ubh28t/issue/detail/6990371339) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990371339)
  </card>

- **2026-05-13 22:37** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c874c2ca0c2acbdccfdee5ce`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990700252
  [hard_brake__X6S6008_2026-05-13 21:40:57](https://project.feishu.cn/ubh28t/issue/detail/6990700252) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990700252)
  </card>

- **2026-05-13 22:39** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c9f12bcacc355ca4502c61d2`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990671878
  [takeover_event__X6S6038_2026-05-13 19:36:29](https://project.feishu.cn/ubh28t/issue/detail/6990671878) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990671878)
  </card>

- **2026-05-13 22:39** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c9f73d8a0c45cc257b16f3d0`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989947025
  [takeover_event__X6S6038_2026-05-13 12:00:14](https://project.feishu.cn/ubh28t/issue/detail/6989947025) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989947025)
  </card>

- **2026-05-13 22:40** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c980c2934c4d18e6fc20a64a`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990406290
  [routertrigger_event_X6S0829_2026-05-13 19:04:04](https://project.feishu.cn/ubh28t/issue/detail/6990406290) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990406290)
  </card>

- **2026-05-13 22:41** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c9751ecb0c2ef927433934d5`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990618803
  [routertrigger_event_X6S0793_2026-05-13 21:37:05](https://project.feishu.cn/ubh28t/issue/detail/6990618803) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990618803)
  </card>

- **2026-05-13 22:42** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7c9312a4b0c2cbabf09f09a25`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990492639
  [p_stop_X6S6141_2026-05-13 15:29:39](https://project.feishu.cn/ubh28t/issue/detail/6990492639) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990492639)
  </card>

- **2026-05-13 22:53** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d468204b0c24c6daca05dcbb`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990594281
  [routertrigger_event_X6S0790_2026-05-13 21:54:45](https://project.feishu.cn/ubh28t/issue/detail/6990594281) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990594281)
  </card>

- **2026-05-13 22:55** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d42199ca0c2d114ea95678a2`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990570303
  [extricate_pnc_ratio_X6S0860_2026-05-13 22:08:46](https://project.feishu.cn/ubh28t/issue/detail/6990570303) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990570303)
  </card>

- **2026-05-13 22:57** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d5bb1e8a4c26fa11cf78b4ee`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990652438
  [takeover_event__X6S5142_2026-05-13 21:31:43](https://project.feishu.cn/ubh28t/issue/detail/6990652438) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990652438)
  </card>

- **2026-05-13 22:58** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d54b1f8a0c22025e57ee1c32`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990565264
  [extricate_pnc_ratio_X6S0861_2026-05-13 22:16:19](https://project.feishu.cn/ubh28t/issue/detail/6990565264) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990565264)
  </card>

- **2026-05-13 22:59** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d500294a0c21509dbda65494`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990354607
  [takeover_event__X6S6141_2026-05-13 16:04:23](https://project.feishu.cn/ubh28t/issue/detail/6990354607) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990354607)
  </card>

- **2026-05-13 22:59** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d53c0f4a4c367d51acec83dc`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990648856
  [extricate_pnc_ratio_X6S0790_2026-05-13 22:02:09](https://project.feishu.cn/ubh28t/issue/detail/6990648856) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990648856)
  </card>

- **2026-05-13 23:00** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d6c9458a4c2e0d642ce2d4c4`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990394383
  [extricate_pnc_ratio_X6S0778_2026-05-13 21:45:04](https://project.feishu.cn/ubh28t/issue/detail/6990394383) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990394383)
  </card>

- **2026-05-13 23:02** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d673194a0c22ec06d8dfbe3e`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990464246
  [routertrigger_event_X6S0829_2026-05-13 17:56:04](https://project.feishu.cn/ubh28t/issue/detail/6990464246) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990464246)
  </card>

- **2026-05-13 23:02** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d66eeecacc3533c42dcb1f4b`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990691295
  [routertrigger_event_X6S6073_2026-05-13 21:38:15](https://project.feishu.cn/ubh28t/issue/detail/6990691295) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990691295)
  </card>

- **2026-05-13 23:13** · `MIL 客服群` · cli_a93bbcabb939dcb3 
  - 类型: text；message_id: `om_x100b6f7d1c46a4a4c224650fd9f6506`
  ▶️ 开始 #85223058: @halo 用 vesper/bev-v2.10.3 提交所有任务，halo用master 最新的tag版本

- **2026-05-13 23:13** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d1c9ac0a4c2a8adcf7acf2a2`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990554514
  [p_stop_X6S5080_2026-05-13 16:44:48](https://project.feishu.cn/ubh28t/issue/detail/6990554514) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990554514)
  </card>

- **2026-05-13 23:13** · `MIL 客服群` · 顾梦洲 
  - 类型: text；message_id: `om_x100b6f7d1f0c08b0c2cd51bc9995e83`
  @halo 用 vesper/bev-v2.10.3 提交所有任务，halo用master 最新的tag版本
  _(消息已编辑)_

- **2026-05-13 23:13** · `MIL 客服群` · cli_a93bbcabb939dcb3 
  - 类型: text；message_id: `om_x100b6f7d1cb090acc26dd0322d9ee1d`
  ✅ 排队 (#85223058)

- **2026-05-13 23:17** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d2f8cd8a4c45cc14bae9a9e1`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990653013
  [takeover_event__X6S5080_2026-05-13 16:20:35](https://project.feishu.cn/ubh28t/issue/detail/6990653013) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990653013)
  </card>

- **2026-05-13 23:18** · `MIL 客服群` · cli_a93bbcabb939dcb3 
  - 类型: text；message_id: `om_x100b6f7d2bb290a0c360f0608a96538`
  ✅ #85223058 完成 (302s, opus):
  全部 9 个 MIL 任务已成功提交 ✅
  
  ## 提交参数
  
  | 参数 | 值 |
  |------|------|
  | **Infer (TEP)** | `vesper/bev-v2.10.3` |
  | **Eval (Halo)** | `v2.2.31` (master 最新 tag) |
  | **Name prefix** | `bev-v2.10.3_20260513` |
  
  ## 任务汇总
  
  | 业务 | task_id | MIL 链接 |
  |------|---------|---------|
  | **od** | 9578495967 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495967?name=bev-v2.10.3_20260513_od_20260513231824) |
  | **lane** | 9578495968 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495968?name=bev-v2.10.3_20260513_lane_20260513231824) |
  | **tld** | 9578495969 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495969?name=bev-v2.10.3_20260513_tld_20260513231824) |
  | **occ** | 9578495970 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495970?name=bev-v2.10.3_20260513_occ_20260513231824) |
  | **barrier** | 9578495971 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495971?name=bev-v2.10.3_20260513_barrier_20260513231824) |
  | **lane_issue** | 9578495972 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495972?name=bev-v2.10.3_20260513_lane_issue_20260513231824) |
  | **tld_issue** | 9578495973 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495973?name=bev-v2.10.3_20260513_tld_issue_20260513231824) |
  | **occ_issue** | 9578495974 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495974?name=bev-v2.10.3_20260513_occ_issue_20260513231824) |
  | **barrier_issue** | 9578495975 | [查看报告](https://nds.data.neolix.cn/#/test/mil/task/report-table/9578495975?name=bev-v2.10.3_20260513_barrier_issue_20260513231824) |
  
  所有 5 个基准业务 (od/lane/tld/occ/barrier) 和 4 个 issue 业务 (lane_issue/tld_issue/occ_issue/barrier_issue) 共 9 个任务均已提交，等待 MIL 平台执行。

- **2026-05-13 23:20** · `MIL 客服群` · 顾梦洲 
  - 类型: post；message_id: `om_x100b6f7d255170a4c337687cd9b3faa`
  如上，v2.10.3的任务就提交好了。后面稳定了会陆续转换成面向研发自助、以及潜入飞书流程自动触发。 cc @孟斐 
  [Image: img_v3_0211l_1520e182-0358-4a3c-817c-78b004d6c4bg]
  _(消息已编辑)_

- **2026-05-13 23:20** · `MIL 客服群` · cli_a93bbcabb939dcb3 
  - 类型: text；message_id: `om_x100b6f7d2298f8acc37ac87bd929eac`
  ✅ 排队 (#85636571)

- **2026-05-13 23:20** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d256f84a0c3cc86e1e00da41`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6989884094
  [p_stop_X6S6038_2026-05-13 12:00:14](https://project.feishu.cn/ubh28t/issue/detail/6989884094) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6989884094)
  </card>

- **2026-05-13 23:20** · `MIL 客服群` · cli_a93bbcabb939dcb3 
  - 类型: text；message_id: `om_x100b6f7d23bc74acc37d0bcc6f67ba4`
  ✅ #85636571 完成 (14s, opus):
  收到，了解了 👍
  
  v2.10.3 的训练任务已经提交完成。后续的两个方向也很清晰：
  
  1. **研发自助化** — 让开发者自己能触发/管理训练任务，降低人工介入
  2. **飞书流程自动触发** — 把提交动作嵌入飞书审批/消息流，实现事件驱动的自动化提交
  
  目前这边没有需要我执行的具体任务。如果后续需要我帮忙做技术方案设计（比如飞书 webhook → 训练平台 API 的自动提交流程），或者在 agent-crew / torchengine 里做相关的代码改动，随时说一声。
  _(消息已编辑)_

- **2026-05-13 23:20** · `MIL 客服群` · cli_a93bbcabb939dcb3 
  - 类型: text；message_id: `om_x100b6f7d22b51ca8c2753f918eb4b21`
  ▶️ 开始 #85636571: 如上，v2.10.3的任务就提交好了。后面稳定了会陆续转换成面向研发自助、以及潜入飞书流程自动触发。 cc @孟斐 
  [
  _(消息已编辑)_

- **2026-05-13 23:22** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d3d9f64a0c24ca6b056f8ab7`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990633308
  [takeover_event__X6S6553_1778657848391](https://project.feishu.cn/ubh28t/issue/detail/6990633308) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990633308)
  </card>

- **2026-05-13 23:23** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d38fda53cc22203dc5043758`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990124600
  [routertrigger_event_X6S6073_2026-05-13 15:44:36](https://project.feishu.cn/ubh28t/issue/detail/6990124600) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990124600)
  </card>

- **2026-05-13 23:31** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7ddbed0534c2219ef9614a722`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990498973
  [takeover_event__X6S5056_2026-05-13 15:49:53](https://project.feishu.cn/ubh28t/issue/detail/6990498973) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990498973)
  </card>

- **2026-05-13 23:37** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7de2cec4a4c368ef12c1b6907`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990613372
  [extricate_pnc_ratio_X6S6190_2026-05-13 22:51:09](https://project.feishu.cn/ubh28t/issue/detail/6990613372) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990613372)
  </card>

- **2026-05-13 23:47** · `图南标注沟通-内部` · 李明 
  - 类型: post；message_id: `om_x100b6f7d9c5e94a0b20acc47f4186d5`
  [Image: img_v3_0211l_4712d119-ea29-4a1b-b1ce-3017813307dg]
  [https://project.feishu.cn/ubh28t/issueView/KdTPWMAvg?quickFilterId=Q2KQrpt8-YcVH-hQmv-WMWS-2H1cLtpZmMcU](https://project.feishu.cn/ubh28t/issueView/KdTPWMAvg?quickFilterId=Q2KQrpt8-YcVH-hQmv-WMWS-2H1cLtpZmMcU)
  @王健博 hi 后续你在这个页面里面，筛选这个标签的issue，看到以后：检查issue对应的路口TLD标注是否正确，包括有无、绑定关系，在issue里面评论，如果有问题需要修复，修复完也要评论
  _(消息已编辑)_

- **2026-05-13 23:48** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d9d3378a8c37534a40ad8a1d`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990633893
  [takeover_event__X6S0746_2026-05-13 22:52:04](https://project.feishu.cn/ubh28t/issue/detail/6990633893) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990633893)
  </card>

- **2026-05-13 23:49** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d96ad6ca4c2ca39321282651`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990652450
  [takeover_event__X610036_1778673181508](https://project.feishu.cn/ubh28t/issue/detail/6990652450) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990652450)
  </card>

- **2026-05-13 23:49** · `【高优】高架转禁行区` · 李明 
  - 类型: text；message_id: `om_x100b6f7d9652b8a8b3d74c52e3f2c98`
  @柏光耀 需要你培训一下常夜如何基于issue判断要在哪个地方画高架禁行区，以及画的高架禁行区如何在@江南 里面生效
  _(消息已编辑)_

- **2026-05-13 23:51** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7d916630a0c2c34b01e8724fa`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990456443
  [vehicle_control_error_max_X6S5107_2026-05-13 22:56:39](https://project.feishu.cn/ubh28t/issue/detail/6990456443) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990456443)
  </card>

- **2026-05-13 23:53** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7da941e4a0c31449af9b79e70`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990644617
  [takeover_event__X6S5080_2026-05-13 14:02:35](https://project.feishu.cn/ubh28t/issue/detail/6990644617) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990644617)
  </card>

- **2026-05-13 23:55** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7da1ed64a4c2946f4fa4dd497`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990485924
  [takeover_event__X6S6038_2026-05-13 16:38:09](https://project.feishu.cn/ubh28t/issue/detail/6990485924) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990485924)
  </card>

- **2026-05-13 23:55** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7da14030a4c294235667429cb`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990699659
  [extricate_pnc_ratio_X6S4398_1778672750099](https://project.feishu.cn/ubh28t/issue/detail/6990699659) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990699659)
  </card>

- **2026-05-13 23:57** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7dba00b0a0c3131055efb94c8`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990433843
  [takeover_event__X6S6562_1778672647288](https://project.feishu.cn/ubh28t/issue/detail/6990433843) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990433843)
  </card>

- **2026-05-13 23:57** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7db98dbca0c39f42404bf57fa`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990389368
  [takeover_event__X6S6562_1778681691399](https://project.feishu.cn/ubh28t/issue/detail/6990389368) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990389368)
  </card>

- **2026-05-13 23:58** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7db4b178a0c22677ec38ed5be`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990655421
  [takeover_event__X6S8217_1778682257468](https://project.feishu.cn/ubh28t/issue/detail/6990655421) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990655421)
  </card>

- **2026-05-13 23:58** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7db51140a4c244787be56672b`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990460419
  [extricate_pnc_ratio_X6S5107_2026-05-13 23:01:20](https://project.feishu.cn/ubh28t/issue/detail/6990460419) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990460419)
  </card>

- **2026-05-13 23:58** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7db2c344a4c2e3c74b90059dd`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990682242
  [extricate_pnc_ratio_X6S6060_2026-05-13 22:57:35](https://project.feishu.cn/ubh28t/issue/detail/6990682242) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990682242)
  </card>

- **2026-05-13 23:59** · `【高优】高架转禁行区` · 李明 
  - 类型: text；message_id: `om_x100b6f7db15650b0b32a76fb756c2ef`
  @柏光耀 高架禁行区，因为理论上只会躲避桥上，不会影响桥下的路，所以没必要贴着link边界画太小，免得框不住百度的LINK
  _(消息已编辑)_

- **2026-05-13 23:59** · `数据闭环新增通知` · cli_a118f15c3b78900d 
  - 类型: interactive；message_id: `om_x100b6f7db20c1ca8c3887829bf153ce`
  <card title="issue进入数据闭环通知">
  AD研发管理 · 路测批量回流case · #6990705319
  [takeover_event__X6S8217_1778684085919](https://project.feishu.cn/ubh28t/issue/detail/6990705319) 信息变更
  **操作人**: @自动化规则
  **数据闭环: **未设置    👉    数据闭环相关
  
  [查看详情](https://project.feishu.cn/ubh28t/issue/detail/6990705319)
  </card>

---

_生成说明：`priority=high` 当消息为我方发送、包含对我的 @，或包含 @所有人。可按需调整分类规则。_


---

_已启用「不统计群聊」过滤：**substring** 匹配；模式：AD标注平台正式环境备份清理通知群。拉取 **816** 条，排除 **594** 条，保留 **222** 条。_
