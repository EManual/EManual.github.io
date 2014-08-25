目前有许多DBMS产品，如DB2、Oracle、Microsoft SQL Server、Sybase SQLServer、Informix、MySQL等，它们在数据库市场上各自占有一席之地。下面简要介绍几种常用的数据库管理系统。
（1）DB2
DB2第一种使用使用SQL的数据库产品。DB2 于1982 年首次发布，现在已经可以用在许多操作系统平台上，它除了可以运行在OS/390和VM 等大型机操作系统以及中等规模
的AS/400 系统之外，IBM还提供了跨平台（包括基于UNIX 的LINUX，HP-UX，Sun Solaris，
以及SCO UnixWare；还有用于个人电脑的Windows 2000系统）的DB2 产品。应用程序可以通过使用微软的ODBC接口、Java的JDBC接口或者CORBA接口代理来访问DB2数据库。
DB2 有不同的版本，比如DB2 Everyplace是为移动用户提供的一个内存占用小且性能出色的版本；DB2 for z/OS则是为主机系统提供的版本；Enterprise Server Edition(ESE)是一种适用于中型和大型企业的版本；Workgroup Server Edition(WSE)主要适用于小型和中型企业，它提供除大型机连接之外的所有ESE 特性；而DB2 Express则是为开发人员提供的可以免费使用的版本。
IBM 是最早进行关系数据库理论研究和产品开发的公司，在关系数据库理论方面一直走在业界的前列，所以DB2 的功能和性能都是非常优秀的，不过对开发人员的要求也比其他数据库系统更高，使用不当很容易造成宕机、死锁等问题；DB2 在SQL的扩展方面比较保守，很多其他数据库系统支持的SQL 扩展特性在DB2 上都无法使用；同时DB2 对数据的类型要求也非常严格，在数据类型不匹配的时候会报错而不是进行类型转换，而且如果发生精度溢出、数据超长等问题的时候也会直接报错，这虽然保证了数据的正确性，但是也使得基于DB2的开发更加麻烦。因此，很多开发人员称DB2 为“最难用的数据库系统”。
（2）Oracle
Oracle是和DB2 同时期发展起来的数据库产品，也是第二个采用SQL的数据库产品。Oracle从DB2等产品中吸取到了很多优点，同时又避免了IBM的官僚体制与过度学术化，大胆的引进了许多新的理论与特性，所以Oracle无论是功能、性能还是可用性都是非常好的。
（3）Microsoft SQL Server
Microsoft SQL Server 是微软推出的一款数据库产品。细心的读者也许已经发现我们前面提到了另外一个名字非常相似的Sybase SQLServer，这里的名字相似并不是一种巧合，这还要从Microsoft SQL Server 的发展史谈起。
微软当初要进军图形化操作系统，所以就开始和IBM“合作”开发OS/2，最终当然无疾而终，但是微软就很快的推出了自己的新一代视窗操作系统；而当微软发现数据库系统这块新的市场的时候，微软没有自己重头开发一个数据库系统，而是找到了Sybase来“合作”开发基于OS/2 的数据产品，当然微软达到目的以后就立即停止和Sybase的合作了，于1995
年推出了自己的Microsoft SQL Server6.0，经过几年的发展终于在1998年推出了轰动一时的Microsoft SQL Server7.0，也正是这一个版本使得微软在数据库产品领域有了一席之地。正因为这段“合作”历史，所以使得Microsoft SQL Server 和Sybase SQLServer 在很多地方非常类似，比如底层采用的TDS协议、支持的语法扩展、函数等等。
微软在2000年推出了Microsoft SQL Server 2000，这个版本继续稳固了Microsoft SQL Server的市场地位，由于Windows操作系统在个人计算机领域的普及，Microsoft SQL Server理所当然的成为了很多数据库开发人员的接触的第一个而且有可能也是唯一一个数据库产品，很多人甚至在“SQL Server”和“数据库”之间划上了等号，而且用“SQL”一次来专指Microsoft SQL Server，可见微软的市场普及做的还是非常好的。做足足够的市场以后，微软在2005年“审时度势”的推出了Microsoft SQL Server 2005，并将于2008年发布新一代的Microsoft SQL Server 2008。
Microsoft SQL Server 的可用性做的非常好，提供了很多了外围工具来帮助用户对数据库进行管理，用户甚至无需直接执行任何SQL 语句就可以完成数据库的创建、数据表的创建、数据的备份/恢复等工作；Microsoft SQL Server 的开发者社区也是非常庞大的，因此有众多可以参考的学习资料，学习成本非常低，这是其他数据库产品做不具有的优势；同时从Microsoft SQL Server 2005开始开发人员可以使用任何支持.Net的语言来编写存储过程，这进一步降低了Microsoft SQL Server 的使用门槛。
不过正如微软产品的一贯风格，Microsoft SQL Server 的劣势也是非常明显的：只能运行于Windows 操作系统，因此我们无法在Linux、Unix 上运行它；不管微软给出什么样的测试数据，在实际使用中Microsoft SQL Server 在大数据量和大交易量的环境中的表现都是不尽人意的，当企业的业务量到达一个水平后就要考虑升级到Oracle或者DB2了。
（4）MySQL
MySQL是一个小型关系型数据库管理系统，开发者为瑞典MySQL AB 公司。目前MySQL被广泛地应用在中小型系统中，特别是在网络应用中用户群更多。MySQL 没有提供一些中小型系统中很少使用的功能，所以MySQL的资源占用非常小，更加易于安装、使用和管理。
由于MySQL是开源的，所以在PHP和Java 开发人员心中更是首选的数据库开发搭档，目前Internet上流行的网站构架方式是LAMP（Linux+Apache+MySQL+PHP），即使用Linux作为操作系统，Apache 作为Web 服务器，MySQL 作为数据库，PHP 作为服务器端脚本解释器。
MySQL目前还很难用于支撑大业务量的系统，所以目前MySQL大部分还是用来运行非核心业务；同时由于MySQL在国内没有足够的技术支持力量，所以对MySQL的技术支持工作是由ISV或者系统集成商来承担，这也导致部分客户对MySQL比较抵制，他们更倾向于使用有更强技术支持力量的数据库产品。