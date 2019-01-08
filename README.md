小刺猬Scrapy最小单元
简单修改快速投产


三个模块
1
2
3 requetsModel
4


Demo说明：
1、单次下发任务:新浪搜狐新闻列表抓取。
2、循环抓取任务:百度热词抓取。
3、深度抓取任务:爱奇艺深度优先全站视频链接抓取。
4、REDIS队列抓取任务:企查查网页HTML抓取。

辅助服务：
1、队列下发辅助服务：使用【小刺猬】下发组件给REDIS队列抓取任务下发任务。
2、监控辅助服务：使用【小刺猬】监控服务动态，包括数据库、redis、进程存活与日志。
3、ITEM生成辅助工具：使用【小刺猬】ITEM辅助工具，自动从json生成ITEM对象。

教程：
1、代理middleware使用教程：重写中间件达到使用代理的目的。
2、去重middleware使用教程：使用redis达到分布式全局去重。
3、管道pipeline使用教程：使用mongo、kafka、本地文件和OSS持久化你的数据。

高级教程:
1、middleware升阶：如何让你的middleware中间件优雅的处理异常。
2、crawlSpider升阶：让你的scrapy全站抓取代码量不超过50行。
3、scrapy异步模型twisted：scrapy的多线程到底是怎么跑的。
4、scrapy+webdriver：利用单例和池思想优雅的管理开销极大的浏览器。

开发流程
1、克隆本github项目,创造一个Spider,这有几种办法可以推荐给你。
（1）从既有的spiders文件夹内复制一个最像的你业务场景的spiderDemo，把name和类名修改一下，并基于此修改。
（2）从百度搜索一个spider文件，并拷贝到spiders中。
最终，需要在spiders文件夹中创造一个独有类，并使里面的name字段唯一。

2、开发抓取流程
（1）在start_requests中，下发种子并且重定向callback至你的parse函数。
（2）在parse中完成简单解析,跑通代码,能够正常打印部分需要抓取的内容。
（3）撰写item，完成一个字段模型的构建。
（4）在parse中完成Item的实例化，赋值并yield。
（5）选择一个pipelines(一般pipelines都是可以复用的，无需重复映射去写)作为存储方式持久化。
（6）删除临时的打印、临时的代码。臆想几个可能问题并据此完善日志。
（7）上线，并启动【小刺猬监控辅助服务】在危险期内持续监控当前情况。

3、后续
（0）使用pip3 freeze > requirements.txt 指令生成requirements文件
（1）使用Docker封装服务，去环境。
（2）完善必要的文档，上传技术沉淀平台。
（3）向我分享最小单元改进建议。