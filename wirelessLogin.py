#coding:utf-8
"""
程序需要给予预设的用户名和密码，
然后自动完成登录所需数据的获取，
并在修改一次密码后（与原密码相同）登录。
每一个模块单独编写。
"""

url = "http://rbsi.yxzl.top:5001/"
你的用户名 = "xiongtianhu"
你的密码 = "qwer-1234"
DICT_ALL = [
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'wangdeyao', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '5b5c3694-3b2d-4702-8db2-e97677a4e2cb', 'QZDB_JIAOSHIGUANLI_STATE7': 'c2c602e1-c962-488e-ada8-f01d55c83772'},
    {'CLOUD_NAME': 'JTJ', 'QZDB_JIAOSHIGUANLI_STATE2': 'yunwei2', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验初中',
     'ID': '3d0fabc7-54ed-4cb1-805f-9b1a093648b1', 'QZDB_JIAOSHIGUANLI_STATE7': '991543a0-385a-4df7-b50d-b6aa0a8c7846'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'xukai', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': 'a1655671-f7d4-4e54-bb76-ab897d1fefeb', 'QZDB_JIAOSHIGUANLI_STATE7': '86e82417-ebd7-41b6-8ea9-d754a75225f8'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'wangtianyu', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '53021cc2-f851-4eaf-9ebb-0dc42039535b', 'QZDB_JIAOSHIGUANLI_STATE7': '43c9d289-bcda-4457-9f97-ded9fdc47fee'},
    {'CLOUD_NAME': 'LSSYCZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'sycz029', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验初中',
     'ID': '63319541-b46e-42f9-89f1-d6b06a53921e', 'QZDB_JIAOSHIGUANLI_STATE7': 'd659af35-7e4c-48ad-a164-45a0abf27162'},
    {'CLOUD_NAME': 'MDXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'duweidong', 'QZDB_JIAOSHIGUANLI_STATE4': '大麦岛小学',
     'ID': '648e1801-d5f2-48c6-bf6b-c37cf8eacebf', 'QZDB_JIAOSHIGUANLI_STATE7': 'afd28b8a-ad39-4ecf-8e30-fd09333025ea'},
    {'CLOUD_NAME': 'YCXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'ycxx106', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区育才小学',
     'ID': 'a6796839-12a2-499a-b2c2-2962b3505965', 'QZDB_JIAOSHIGUANLI_STATE7': 'a95bbecb-44ec-4399-adf2-3fe30dfb5ce7'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'wangdeyao', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': 'c8b48333-5312-43a3-97db-b9a0a8212095', 'QZDB_JIAOSHIGUANLI_STATE7': 'c2c602e1-c962-488e-ada8-f01d55c83772'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'cuizhian', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '34431515-01b7-4aaf-a064-97dc6af870a9', 'QZDB_JIAOSHIGUANLI_STATE7': 'aca7b92b-b1e0-40f1-940d-96cae48573f4'},
    {'CLOUD_NAME': 'LSSIZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'lsszmutt', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山四中',
     'ID': '354b7aba-556a-48cf-a836-443687ca061e', 'QZDB_JIAOSHIGUANLI_STATE7': '9d2715ea-98f7-421f-8ea5-aa99a4d0c57c'},
    {'CLOUD_NAME': 'SYEX', 'QZDB_JIAOSHIGUANLI_STATE2': 'syex034', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验二小',
     'ID': 'f02de305-1578-4c00-910a-319ff6a921bf', 'QZDB_JIAOSHIGUANLI_STATE7': 'd499612d-521c-489e-8547-9aa31f342072'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'xukai', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': 'f5e9710f-0a81-4e98-b9bb-415923c52ce5', 'QZDB_JIAOSHIGUANLI_STATE7': '86e82417-ebd7-41b6-8ea9-d754a75225f8'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'shanzhengqing', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '2206295e-810e-4e4e-9482-208e0f093d3a', 'QZDB_JIAOSHIGUANLI_STATE7': '4e369232-a2dd-432f-8fc3-43a97535f9ab'},
    {'CLOUD_NAME': 'MDXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'lina', 'QZDB_JIAOSHIGUANLI_STATE4': '大麦岛小学',
     'ID': 'a3490a08-18e7-4abd-8e9c-4f2364db47d3', 'QZDB_JIAOSHIGUANLI_STATE7': 'ed7e89e8-cddc-4ead-bc47-95095c7c3697'},
    {'CLOUD_NAME': 'LSSYZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'tuzhongqing', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山十一中',
     'ID': 'accad82e-8e26-414f-814d-378a044d3ca8', 'QZDB_JIAOSHIGUANLI_STATE7': '2cfe5213-ce90-41ec-ac04-6debb4c3b9d3'},
    {'CLOUD_NAME': 'MDXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'mdxx012', 'QZDB_JIAOSHIGUANLI_STATE4': '大麦岛小学',
     'ID': '96b743a2-2101-4a02-85a2-5e4c83299c78', 'QZDB_JIAOSHIGUANLI_STATE7': '597f5896-7f06-491a-8105-0389d4ee44c9'},
    {'CLOUD_NAME': 'MDXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'mdxx045', 'QZDB_JIAOSHIGUANLI_STATE4': '大麦岛小学',
     'ID': 'bd5c7e0c-ff36-4a9a-bbaa-5fc2074397a5', 'QZDB_JIAOSHIGUANLI_STATE7': '8f909487-63ce-4ddf-9f18-a5f0bc4b4753'},
    {'CLOUD_NAME': 'SYEX', 'QZDB_JIAOSHIGUANLI_STATE2': 'syex168', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验二小',
     'ID': 'bd680450-5ef7-450e-9933-795b7520a14a', 'QZDB_JIAOSHIGUANLI_STATE7': '72592cc0-57ef-4d93-8377-2c720d6dcca7'},
    {'CLOUD_NAME': 'JJLXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'xiuchang', 'QZDB_JIAOSHIGUANLI_STATE4': '金家岭中学',
     'ID': '426d37b8-983a-40b1-a164-1129a576a71f', 'QZDB_JIAOSHIGUANLI_STATE7': '09c2347d-02a8-4d9f-8a67-c6294204dd53'},
    {'CLOUD_NAME': 'JJLXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'wuxueyan', 'QZDB_JIAOSHIGUANLI_STATE4': '金家岭中学',
     'ID': '4260f20a-4e0f-4aef-8800-cea40ca546b0', 'QZDB_JIAOSHIGUANLI_STATE7': '18f0a52a-366f-4b88-8259-d2ef4585cfc8'},
    {'CLOUD_NAME': 'HHXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'hhxx018', 'QZDB_JIAOSHIGUANLI_STATE4': '汉河小学',
     'ID': 'bd72ffec-af8a-4471-8ef4-30f13892b233', 'QZDB_JIAOSHIGUANLI_STATE7': '679adc2f-3a87-4fe6-892b-e71e47aba8bd'},
    {'CLOUD_NAME': 'FSXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'liangtiantian', 'QZDB_JIAOSHIGUANLI_STATE4': '浮山小学',
     'ID': 'd560ab11-d16a-499b-82eb-bcbad901eb43', 'QZDB_JIAOSHIGUANLI_STATE7': '68992a29-c6e5-45d7-805a-901833b48d98'},
    {'CLOUD_NAME': 'JJLXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'wuxueyan', 'QZDB_JIAOSHIGUANLI_STATE4': '金家岭中学',
     'ID': 'a5508ef8-c462-4166-9432-ec7318a0800a', 'QZDB_JIAOSHIGUANLI_STATE7': '18f0a52a-366f-4b88-8259-d2ef4585cfc8'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'daimeng', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': 'c7f1fb0a-a0c6-48c0-8a11-eea2856a51eb', 'QZDB_JIAOSHIGUANLI_STATE7': '3e01b871-c6eb-48a1-b157-f57b93cf3d26'},
    {'CLOUD_NAME': 'DSSY', 'QZDB_JIAOSHIGUANLI_STATE2': '370212198910042522', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验三小',
     'ID': '50cc0608-ebc1-4ba3-bd53-499a3cc6d1da', 'QZDB_JIAOSHIGUANLI_STATE7': 'f934a552-dd47-49ba-b229-48d0284c9d8f'},
    {'CLOUD_NAME': 'MDXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'mdxx071', 'QZDB_JIAOSHIGUANLI_STATE4': '大麦岛小学',
     'ID': '887e7f5c-5321-4e9a-971d-69901bef4721', 'QZDB_JIAOSHIGUANLI_STATE7': 'ad7cc83c-1e83-4db5-9c08-9875c44c23e2'},
    {'CLOUD_NAME': 'YCZX', 'QZDB_JIAOSHIGUANLI_STATE2': 'yczx074', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区育才中学',
     'ID': '3502476e-8539-4073-8fab-a697e8ab2538', 'QZDB_JIAOSHIGUANLI_STATE7': '9ae23e31-ff5f-4a99-a7d9-eaf0f7457758'},
    {'CLOUD_NAME': 'JGZXX', 'QZDB_JIAOSHIGUANLI_STATE2': '20180146', 'QZDB_JIAOSHIGUANLI_STATE4': '姜哥庄小学',
     'ID': '42deee83-5816-42bc-a7df-34c0fa2b5e70', 'QZDB_JIAOSHIGUANLI_STATE7': '65574da6-2e89-4629-9696-d46c7e2c5cea'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'zhangyujiao', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '0a935f97-2a0f-4eff-9afa-9a0157f8883b', 'QZDB_JIAOSHIGUANLI_STATE7': '9d44b1b6-a478-4e75-ba78-54e5be79def1'},
    {'CLOUD_NAME': 'ZHXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'liuweihai', 'QZDB_JIAOSHIGUANLI_STATE4': '中韩小学',
     'ID': 'e9274e7f-4264-4d5d-9dda-08b7f5bb5512', 'QZDB_JIAOSHIGUANLI_STATE7': '777ce1dd-920e-4cff-af24-73fc888f0224'},
    {'CLOUD_NAME': 'JJLXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'wuxueyan', 'QZDB_JIAOSHIGUANLI_STATE4': '金家岭中学',
     'ID': '870f6483-cfc7-41a6-b315-bfab52146b73', 'QZDB_JIAOSHIGUANLI_STATE7': '18f0a52a-366f-4b88-8259-d2ef4585cfc8'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'jiangyu', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '6d61ac5d-0b2d-40a8-81b6-869a924ccb46', 'QZDB_JIAOSHIGUANLI_STATE7': 'e6dfde55-eefa-4dae-8a77-6ded0611d82e'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'wangruilin', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '5b121b0d-1fd2-4e0b-bfd0-f802758905d5', 'QZDB_JIAOSHIGUANLI_STATE7': '783b418f-246c-4dd2-96e3-d84e437f0832'},
    {'CLOUD_NAME': 'SYEX', 'QZDB_JIAOSHIGUANLI_STATE2': 'syex041', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验二小',
     'ID': 'aa13213d-1b7f-49af-9741-a9fc3b3c049e', 'QZDB_JIAOSHIGUANLI_STATE7': '16fd5817-741a-4024-a1f7-c885acc67964'},
    {'CLOUD_NAME': 'ZHXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'wanglinjing', 'QZDB_JIAOSHIGUANLI_STATE4': '中韩小学',
     'ID': '562541a3-636c-420f-8b59-09ed7cc05738', 'QZDB_JIAOSHIGUANLI_STATE7': '45c00da2-8ae2-49b8-852d-17c891f89d92'},
    {'CLOUD_NAME': 'SYEX', 'QZDB_JIAOSHIGUANLI_STATE2': 'syex411', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验二小',
     'ID': '86d85956-ff8c-4e0c-9cdc-b22c4f78e9c0', 'QZDB_JIAOSHIGUANLI_STATE7': 'b2e749cd-f2e5-468b-abab-0bed847bf13d'},
    {'CLOUD_NAME': 'LSSANZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'lssanz059', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山三中',
     'ID': '9192ccce-4818-4717-a69e-54cca13b0a28', 'QZDB_JIAOSHIGUANLI_STATE7': '8026c935-2daa-4efb-a1ca-f29668d026f3'},
    {'CLOUD_NAME': 'SYYEY', 'QZDB_JIAOSHIGUANLI_STATE2': '370212199503191568', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园',
     'ID': 'def0f9e8-ed90-4a90-8410-8a412abddbf3', 'QZDB_JIAOSHIGUANLI_STATE7': '70280b84-50ba-40aa-bd2d-24a1fcdae2da'},
    {'CLOUD_NAME': 'SYYEY', 'QZDB_JIAOSHIGUANLI_STATE2': '37020519921107602X', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园',
     'ID': 'f4fb5429-d107-4c4a-8b70-80daee2c5133', 'QZDB_JIAOSHIGUANLI_STATE7': 'c171e6aa-97e8-4fe7-9308-54538c4bcfbc'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'tianjie', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '17557a77-ce23-4d38-962b-46f765ba8e69', 'QZDB_JIAOSHIGUANLI_STATE7': '843ccb0d-bfba-497f-9f8c-c3c96def5639'},
    {'CLOUD_NAME': 'LSSANZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'lssanz190', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山三中',
     'ID': '53a9fb3b-c0a8-41a4-a4c9-aad4db253938', 'QZDB_JIAOSHIGUANLI_STATE7': '4a37eba1-9579-4f93-b3df-cbc5434b7a99'},
    {'CLOUD_NAME': 'SZKXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'szkxxwk', 'QZDB_JIAOSHIGUANLI_STATE4': '沙子口小学',
     'ID': 'fb12e0cb-7483-4516-887f-3e1bdbb64ec5', 'QZDB_JIAOSHIGUANLI_STATE7': '9485333c-2cd4-4a64-b6f9-caf1002b1d16'},
    {'CLOUD_NAME': 'LSBZ', 'QZDB_JIAOSHIGUANLI_STATE2': '370284198703150442', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山八中',
     'ID': 'e7186b53-f157-450f-8014-85f34e53ffb0', 'QZDB_JIAOSHIGUANLI_STATE7': 'd0f9591d-48cd-4a38-9bd6-47fc1b16e0ce'},
    {'CLOUD_NAME': 'LSWZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'huweixuan', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山五中',
     'ID': '52b7295e-d89b-4cb9-a962-083026b9c1bc', 'QZDB_JIAOSHIGUANLI_STATE7': 'cb6dd062-4318-4cb9-962c-1c2e822b9f19'},
    {'CLOUD_NAME': 'JJLXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'lizheng', 'QZDB_JIAOSHIGUANLI_STATE4': '金家岭中学',
     'ID': 'ad7b5e25-6402-4ab5-9813-8855e674bbcc', 'QZDB_JIAOSHIGUANLI_STATE7': 'f4672930-4f30-407e-92ca-92f2010a70d9'},
    {'CLOUD_NAME': 'LSTJ', 'QZDB_JIAOSHIGUANLI_STATE2': 'chenyulian', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山特殊教育学校',
     'ID': '241d59d0-5753-4ce8-a91f-1b33b0d1ab33', 'QZDB_JIAOSHIGUANLI_STATE7': '927047af-676b-4783-9af3-45bf0c382b1a'},
    {'CLOUD_NAME': 'LSBZ', 'QZDB_JIAOSHIGUANLI_STATE2': '370212198210012525', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山八中',
     'ID': '663f12e2-ad4d-4639-935e-53a663d213d2', 'QZDB_JIAOSHIGUANLI_STATE7': 'fa2afd43-5d4b-43ef-96b2-bab10543f009'},
    {'CLOUD_NAME': 'SYXXZHXQ', 'QZDB_JIAOSHIGUANLI_STATE2': 'sxzh066', 'QZDB_JIAOSHIGUANLI_STATE4': '实验小学中韩校区',
     'ID': 'faf5e108-3852-47b1-bdb8-081d80217c3e', 'QZDB_JIAOSHIGUANLI_STATE7': '44482180-1db8-4788-a444-8142abbe7873'},
    {'CLOUD_NAME': 'FSXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'zhaotongchao', 'QZDB_JIAOSHIGUANLI_STATE4': '浮山小学',
     'ID': '23b817c1-1c2e-43cd-bd4c-04b4b4db8e11', 'QZDB_JIAOSHIGUANLI_STATE7': '68ff2647-c1b6-4384-a522-ec04f344cfc5'},
    {'CLOUD_NAME': 'LSSANZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'lssanz029', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山三中',
     'ID': '9e83d4ea-f130-4d5f-b95d-c5f01f4d7906', 'QZDB_JIAOSHIGUANLI_STATE7': '5adbd32f-c6f0-406d-b81b-1be0f52ea2d3'},
    {'CLOUD_NAME': 'YCXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'ycxx099', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区育才小学',
     'ID': '4789d9c2-04e2-480c-891e-7e4e59174b29', 'QZDB_JIAOSHIGUANLI_STATE7': '4b9c4d74-c457-4b4c-849e-db1d7a9f5d58'},
    {'CLOUD_NAME': 'ZCHXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'gaolaisong', 'QZDB_JIAOSHIGUANLI_STATE4': '张村河小学',
     'ID': 'fc0ee043-7769-41a8-beee-b1e36d52eda5', 'QZDB_JIAOSHIGUANLI_STATE7': 'dc6bcb00-3827-4528-8d7a-d4b77f151e43'},
    {'CLOUD_NAME': 'DYXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'shitang', 'QZDB_JIAOSHIGUANLI_STATE4': '登赢小学',
     'ID': 'c00fc4c7-354c-41fa-a58c-0826520ca0be', 'QZDB_JIAOSHIGUANLI_STATE7': 'a332e796-660a-41a2-8268-49250bbc03f2'},
    {'CLOUD_NAME': 'ZCHXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'sunjianling', 'QZDB_JIAOSHIGUANLI_STATE4': '张村河小学',
     'ID': 'af35a162-2823-4ed3-82a4-8434fbbebf4b', 'QZDB_JIAOSHIGUANLI_STATE7': '0fde6cdc-afd0-4d12-a1de-25ff3b4bf329'},
    {'CLOUD_NAME': 'ZCHXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'sunjianling', 'QZDB_JIAOSHIGUANLI_STATE4': '张村河小学',
     'ID': '62d41bc6-c6df-4bd3-92db-efdfc1d5dd5c', 'QZDB_JIAOSHIGUANLI_STATE7': '0fde6cdc-afd0-4d12-a1de-25ff3b4bf329'},
    {'CLOUD_NAME': 'SDTXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'sdt073', 'QZDB_JIAOSHIGUANLI_STATE4': '山东头小学',
     'ID': '9d0fc7d2-0e58-43b0-83ee-b0a81cb18904', 'QZDB_JIAOSHIGUANLI_STATE7': '51811e8e-62c3-4e96-92dd-5cf1020b8151'},
    {'CLOUD_NAME': 'SYXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'syxx005', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验小学',
     'ID': '58947bf7-ac8d-4d3e-8f44-5a5141d55165', 'QZDB_JIAOSHIGUANLI_STATE7': 'd0b119b4-1d5b-47da-8f0a-f56b2ab10905'},
    {'CLOUD_NAME': 'LFXX', 'QZDB_JIAOSHIGUANLI_STATE2': '152', 'QZDB_JIAOSHIGUANLI_STATE4': '崂发小学',
     'ID': '6426bf09-65e3-4df7-9cf2-54bffbc646f5', 'QZDB_JIAOSHIGUANLI_STATE7': '5c8a25d5-af77-4d4a-9929-21f0e8893fd5'},
    {'CLOUD_NAME': 'LYDLXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'lydl006', 'QZDB_JIAOSHIGUANLI_STATE4': '辽阳东路小学',
     'ID': '306e74a3-ac12-4c82-ba50-a615254e7a73', 'QZDB_JIAOSHIGUANLI_STATE7': '57ab8ea2-6141-46a6-9f20-3b0add5be776'},
    {'CLOUD_NAME': 'SZKXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'szkxxlcx', 'QZDB_JIAOSHIGUANLI_STATE4': '沙子口小学',
     'ID': '04efca9b-a7f1-433a-b5f8-39489c695710', 'QZDB_JIAOSHIGUANLI_STATE7': '098d0dc8-d162-4d3c-ba2d-2f6a17d6fd17'},
    {'CLOUD_NAME': 'SYXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'syxx161', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验小学',
     'ID': 'cdc7b32c-0d7a-402c-a8e9-73716c6a43d4', 'QZDB_JIAOSHIGUANLI_STATE7': '67d092b6-805d-4fc9-8e58-20866335ec28'},
    {'CLOUD_NAME': 'SYXXZHXQ', 'QZDB_JIAOSHIGUANLI_STATE2': 'sxzh083', 'QZDB_JIAOSHIGUANLI_STATE4': '实验小学中韩校区',
     'ID': '2f230417-a78d-46b0-b7b1-6cc420a6e14e', 'QZDB_JIAOSHIGUANLI_STATE7': 'c50a46e6-6347-4fc0-8b77-df13a1e93978'},
    {'CLOUD_NAME': 'NANZXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'nzxx057', 'QZDB_JIAOSHIGUANLI_STATE4': '南宅小学',
     'ID': '5c94fc00-4ce6-41ca-b79f-59fb5b7b44d4', 'QZDB_JIAOSHIGUANLI_STATE7': '3bc4975b-9869-41fc-8578-eb7ec4581d3d'},
    {'CLOUD_NAME': 'LSSZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'ls10003', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山十中',
     'ID': '74ed816d-a574-4177-8219-e77a0f77fc2b', 'QZDB_JIAOSHIGUANLI_STATE7': '88e02833-0874-4660-a2c8-b3770eb5f6d4'},
    {'CLOUD_NAME': 'LWXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'zhangyanyan', 'QZDB_JIAOSHIGUANLI_STATE4': '林蔚小学',
     'ID': 'af87cd42-c6b9-411b-8818-dc9b1e6865fe', 'QZDB_JIAOSHIGUANLI_STATE7': 'fe113cf5-0288-4038-baa6-f9abf5264016'},
    {'CLOUD_NAME': 'HTXX', 'QZDB_JIAOSHIGUANLI_STATE2': '20180020', 'QZDB_JIAOSHIGUANLI_STATE4': '惠特小学',
     'ID': '24c79df5-c6e6-41db-86a9-30cfcfb6b0d8', 'QZDB_JIAOSHIGUANLI_STATE7': 'bb4b5cdc-8500-43aa-9176-9af23c5fd279'},
    {'CLOUD_NAME': 'JGZXX', 'QZDB_JIAOSHIGUANLI_STATE2': '20180138', 'QZDB_JIAOSHIGUANLI_STATE4': '姜哥庄小学',
     'ID': '72530fe9-1b7e-4601-b4df-3f1d0beb8004', 'QZDB_JIAOSHIGUANLI_STATE7': '46c3651a-ab1e-418a-8821-63047e6c61b7'},
    {'CLOUD_NAME': 'DYXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'chenyameng', 'QZDB_JIAOSHIGUANLI_STATE4': '登赢小学',
     'ID': '8890f2af-ba1e-4ecf-96a6-ac09f9a34d1e', 'QZDB_JIAOSHIGUANLI_STATE7': '4f1acb93-4124-42a8-afeb-6aaeaa59c7c8'},
    {'CLOUD_NAME': 'MDXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'mdxx053', 'QZDB_JIAOSHIGUANLI_STATE4': '大麦岛小学',
     'ID': '381ce30c-cd41-45d7-bd8a-9debf40e3efc', 'QZDB_JIAOSHIGUANLI_STATE7': '1f8efce4-9bf2-47bd-9714-ddb823103808'},
    {'CLOUD_NAME': 'JGZXX', 'QZDB_JIAOSHIGUANLI_STATE2': '20180138', 'QZDB_JIAOSHIGUANLI_STATE4': '姜哥庄小学',
     'ID': 'dfee013e-3ee5-4581-885f-706fcf50e8c5', 'QZDB_JIAOSHIGUANLI_STATE7': '46c3651a-ab1e-418a-8821-63047e6c61b7'},
    {'CLOUD_NAME': 'LSWZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'xingyan', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山五中',
     'ID': 'd1685bae-ddc7-4d08-9b88-3dfb238c5537', 'QZDB_JIAOSHIGUANLI_STATE7': '34701879-2070-424c-a7fd-3e61533ac1da'},
    {'CLOUD_NAME': 'SYYEYLAY', 'QZDB_JIAOSHIGUANLI_STATE2': 'wangxf', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山实验幼儿园蓝岸园',
     'ID': '2bb4d20c-6c9d-4634-8b96-0d21a389d5e1', 'QZDB_JIAOSHIGUANLI_STATE7': '1bed1fd8-999a-4f6e-a3dc-662f4008362e'},
    {'CLOUD_NAME': 'LFXX', 'QZDB_JIAOSHIGUANLI_STATE2': '031', 'QZDB_JIAOSHIGUANLI_STATE4': '崂发小学',
     'ID': 'ec45ae6f-9919-4c89-9ebe-711656cea2ad', 'QZDB_JIAOSHIGUANLI_STATE7': 'cb4233b7-bc0e-4542-bb0a-81e9eef033a2'},
    {'CLOUD_NAME': 'SYXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'syxx112', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验小学',
     'ID': '3c860dc0-d7a3-48d7-b6ed-3e590a61247d', 'QZDB_JIAOSHIGUANLI_STATE7': 'af1a2a61-6061-4b62-a57c-9901c2ca52b7'},
    {'CLOUD_NAME': 'LSSYCZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'sycz016', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验初中',
     'ID': '28da3e11-f6da-437c-83b7-e5891f4e93dc', 'QZDB_JIAOSHIGUANLI_STATE7': 'af17bcbf-1aa9-4818-8d86-46522811525d'},
    {'CLOUD_NAME': 'SYXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'syxx206', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验小学',
     'ID': '4f78946c-b563-4cea-87de-f8e23a56595f', 'QZDB_JIAOSHIGUANLI_STATE7': '1c2c74c2-09c2-4d17-8b66-675d59badc14'},
    {'CLOUD_NAME': 'LSLZ', 'QZDB_JIAOSHIGUANLI_STATE2': 'lslz2018043', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山六中',
     'ID': '5cef2857-14c7-47ce-bf55-850b74f8d865', 'QZDB_JIAOSHIGUANLI_STATE7': '6ca2bca1-ee08-4c50-a087-845a55ff7919'},
    {'CLOUD_NAME': 'DSSY', 'QZDB_JIAOSHIGUANLI_STATE2': '370212198910042522', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验三小',
     'ID': 'f33ea2f5-041b-42a7-9be8-de9fd6716cec', 'QZDB_JIAOSHIGUANLI_STATE7': 'f934a552-dd47-49ba-b229-48d0284c9d8f'},
    {'CLOUD_NAME': 'DSSY', 'QZDB_JIAOSHIGUANLI_STATE2': '370726197412112429', 'QZDB_JIAOSHIGUANLI_STATE4': '崂山区实验三小',
     'ID': 'adbc180f-3953-49e1-b422-34989fef2f7d', 'QZDB_JIAOSHIGUANLI_STATE7': '59a365c4-b372-48d6-a383-563d56d94d3f'},
    {'CLOUD_NAME': 'JGZXX', 'QZDB_JIAOSHIGUANLI_STATE2': '20180106', 'QZDB_JIAOSHIGUANLI_STATE4': '姜哥庄小学',
     'ID': 'fefd71bb-defc-4003-bd53-a0f5787a8006', 'QZDB_JIAOSHIGUANLI_STATE7': '2ebfb546-c735-4e6c-9ff7-2022aa5e36d4'},
    {'CLOUD_NAME': 'MDXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'mdxx081', 'QZDB_JIAOSHIGUANLI_STATE4': '大麦岛小学',
     'ID': '09e1f4d9-fd10-45d4-a9b6-77147cffea6d', 'QZDB_JIAOSHIGUANLI_STATE7': '12648fa4-bebd-4d35-a87b-4c2a4c37fa08'},
    {'CLOUD_NAME': 'SDTXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'sdt086', 'QZDB_JIAOSHIGUANLI_STATE4': '山东头小学',
     'ID': 'e6ed32ce-ba1d-4e8f-833a-5eae85adf9a5', 'QZDB_JIAOSHIGUANLI_STATE7': '856be386-3e24-405d-a6c6-fd729e4846fa'},
    {'CLOUD_NAME': 'XHXX', 'QZDB_JIAOSHIGUANLI_STATE2': 's002', 'QZDB_JIAOSHIGUANLI_STATE4': '西韩小学',
     'ID': 'ece513b9-3927-4588-9d6c-7abb4408452d', 'QZDB_JIAOSHIGUANLI_STATE7': 'b69c483c-0877-449b-878d-bd9a7da5ed22'},
    {'CLOUD_NAME': 'MDXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'mdxx060', 'QZDB_JIAOSHIGUANLI_STATE4': '大麦岛小学',
     'ID': '0de396a6-5e8b-47cc-a260-798fc64a6468', 'QZDB_JIAOSHIGUANLI_STATE7': 'eba72606-cf1d-40f7-808c-094d0adac017'},
    {'CLOUD_NAME': 'SYXXZHXQ', 'QZDB_JIAOSHIGUANLI_STATE2': 'sxzh083', 'QZDB_JIAOSHIGUANLI_STATE4': '实验小学中韩校区',
     'ID': '5d33fe13-0424-43c9-bc17-a609671ea866', 'QZDB_JIAOSHIGUANLI_STATE7': 'c50a46e6-6347-4fc0-8b77-df13a1e93978'},
    {'CLOUD_NAME': 'LWXX', 'QZDB_JIAOSHIGUANLI_STATE2': 'yinianji2', 'QZDB_JIAOSHIGUANLI_STATE4': '林蔚小学',
     'ID': '10e10747-68de-4405-9c93-6709407da8bd', 'QZDB_JIAOSHIGUANLI_STATE7': 'a855c42e-a0ae-46e5-aa43-0e7f494d35df'}]

import hashlib
import requests


def check():
    try:
        r = requests.get("https://www.baidu.com/")
        if r.status_code == 200 and len(r.text) > 500:
            return True
        else:
            return False
    except:
        return False


def check_network():
    try:
        if requests.post(url + "check-network").text == "Success":
            return True
        else:
            return False
    except:
        return False


def get_md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest()


class MyError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class wirelessLogin:
    username = ""
    password = ""
    pass_md5 = ""
    COOKIE = {}
    ip = ""
    id = ""

    def __init__(self, username=你的用户名, password=你的密码, JSESSION=None):
        self.username = username
        self.password = password
        self.pass_md5 = get_md5(self.password)
        if JSESSION:
            self.COOKIE["JSESSION"] = JSESSION

    def get_cookie(self):
        r = requests.post(
            "http://s.laoshanedu.com/s/wirelessLogin/login.action",
            data={
                "action": "11",
                "USERS1": self.username,
                "USERS2": self.pass_md5
            })
        if r.json()["loginmsg"] != "2":
            raise MyError("你可能输入了错误的密码（%s），导致服务器没有正确返回数据！" % self.password)
        self.ip = r.json()["localIP"]
        self.COOKIE = requests.utils.dict_from_cookiejar(r.cookies)
        print("成功获取Cookie（JSESSIONID）的值：%s" % requests.utils.dict_from_cookiejar(r.cookies)["JSESSIONID"])

    def get_id(self):
        r = requests.post(
            "http://s.laoshanedu.com/s/wirelessLogin/usersession.action",
            data={"action": "11"},
            cookies=self.COOKIE)
        if r.status_code != 200:
            raise MyError("获取userID时返回了状态码：%s" % r.status_code)
        self.id = r.json()["usersession"]["ID"]
        print("成功获取ID：%s" % self.id)

    def login(self, ip=None, check_function=check):
        r = requests.post(
            "http://s.laoshanedu.com/s/wirelessLogin/sendUDP.action",
            data={
                "opr": "LOGON",
                "username": self.username,
                "ip": ip or self.ip,  # self.ip
                "groups": "%E9%87%91%E5%AE%B6%E5%B2%AD%E4%B8%AD%E5%AD%A6",  # 金家岭中学
                "usrID": self.id,
                "cloudName": "JJLXX",
                "mac": "",
                "authway": ""
            })
        if check_function():
            print("登录成功！")
            return True
        else:
            raise MyError("登录出现异常！")

    def logout(self):
        r = requests.post(
            "http://s.laoshanedu.com/s/wirelessLogin/sendUDP.action",
            data={
                "opr": "LOGOUT",
                "username": self.username,
                "ip": self.ip,
                "groups": "%E9%87%91%E5%AE%B6%E5%B2%AD%E4%B8%AD%E5%AD%A6",  # 金家岭中学
                "cloudName": "JJLXX",
                "mac": "",
                "authway": ""
            })
        if r.status_code != 200 or r.json()["list"][1]["QZDB_JIAOSHIGUANLI_STATE5"] != "LOGON":
            raise MyError("登出出现异常！")
        print("登出成功！")

    def change_password(self, new_password=None):
        new_password = new_password or self.password
        r = requests.post(
            "http://s.laoshanedu.com/s/wirelessLogin/edit_QZDB_JIAOSHIGUANLI_2.action",
            data={
                "ID": self.id,
                "QZDB_JIAOSHIGUANLI3": new_password,
                "QZDB_JIAOSHIGUANLI13": get_md5(new_password)
            },
            cookies=self.COOKIE)
        self.password = new_password
        self.pass_md5 = get_md5(new_password)
        print("修改密码成功！（新密码为%s）" % new_password)
        # print("重新初始化成功！")


def login_others(check_function=check_network, DICT=DICT_ALL):
    r = requests.post(
        "http://s.laoshanedu.com/s/wirelessLogin/login.action",
        data={
            "action": "11",
            "USERS1": "USER1",
            "USERS2": "USER2"
        })
    ip = r.json()["localIP"]

    for i in DICT:
        requests.post(
            "http://s.laoshanedu.com/s/wirelessLogin/sendUDP.action",
            data={
                "opr": "LOGON",
                "username": i['QZDB_JIAOSHIGUANLI_STATE2'],
                "ip": ip,  # self.ip
                "groups": i['QZDB_JIAOSHIGUANLI_STATE4'],  # 金家岭中学
                "usrID": i['ID'],
                "cloudName": i['CLOUD_NAME'],
                "mac": "",
                "authway": ""
            })
        if check_function():
            print("登录成功！")
            return True
    return False


if __name__ == "__main__":
    print("初始化成功！")
    # t = wirelessLogin(你的用户名, 你的密码)
    # t.get_cookie()
    # t.get_id()
    # t.change_password()
    # t.login()
    # t.logout()
    login_others()
