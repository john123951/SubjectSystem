data = [{
	"subject_title": "为保护本地主机，对Applet安全限制中正确的是（　　）。",
	"subject_choice_A": "Applet可加载本地库或方法",
	"subject_choice_B": "Applet可读、写本地计算机的文件系统",
	"subject_choice_C": "Applet可向Applet之外的任何主机建立网络连接",
	"subject_choice_D": "Applet不能运行任何本地可执行程序",
	"subject_answer": "D",
	"analysis": "Java平台为了防范恶意程序的攻击，保护本地主机，对Applet作了如下安全限制：①Applet不能运行任何本地可执行程序。②禁止加载本地库或方法。③禁止读、写本地计算机的文件系统。④禁止向提供Applet之外的任何主机建立网络连接。⑤不能读取某些系统信息。⑥由一个Applet弹出的窗口外观上与一个Application弹出的窗口不同，Applet弹出的窗口中会有警告提示信息，帮助用户区分Applet窗口与可信的Application窗口。"
}, {
	"subject_title": "下面的（　　）关键字通常用来对对象加锁，从而使得对对象的访问是排他的。",
	"subject_choice_A": "serialize",
	"subject_choice_B": "transient",
	"subject_choice_C": "synchronized",
	"subject_choice_D": "static",
	"subject_answer": "C",
	"analysis": "本题考查Java中对象加锁的概念。Java是多线程的语言，多个线程可以”同时”访问同一数据区，而在处理某些数据时不希望其他的线程修改那些数据的值或者某些操作是不可打断的，要做到这个，可以使用synchronized关键字声明这一点。"
}, {
	"subject_title": "下列叙述中，错误的是（　　）。",
	"subject_choice_A": "JavaApplication与Applet所用编译命令相同",
	"subject_choice_B": "通常情况下JavaApplication只能有一个main()方法",
	"subject_choice_C": "JavaApplet必须有HTML文件才能运行",
	"subject_choice_D": "JavaApplet程序的．class文件可用Java命令运行",
	"subject_answer": "D",
	"analysis": "本题考查的是Java中的Applet以及Applet与Application的区别。Applet是能够嵌入HTML语言中，并能够在浏览器中运行的类。Applet的运行环境是Web浏览器，所以必须建立HTML文件，告诉浏览器如何加载与运行Applet。因为Applet是不能直接通过Java命令行启动运行的。所以选项D的说法错误。"
}, {
	"subject_title": "以下程序计算1+1／3+1／5+…+1／(2N+1)，直至1／(2N+1)小于0．00001，横线处应补充的程序是（　　）。\npublic class Sun{\npublic static void main(String args[]){\nint n=1：\ndouble term，sum=1．0：\ndo{\nn= __ ；\nterm=1．0／n；\nsum=sum+term；\n}\nwhile(term>=0．00001)；\nSystem．out．println(n)；\nSystem．out．println(sum)；\n}\n}",
	"subject_choice_A": "2n",
	"subject_choice_B": "2n+1",
	"subject_choice_C": "2*n",
	"subject_choice_D": "2*n+1",
	"subject_answer": "D",
	"analysis": "本题考查do-while循环的用法。题目中没有给出累加次数，故不能使用for循环，在do循环中，由累加项term的值作为退出循环的条件。根据题目要求，应该填写2*n+1。本题的关键是while(term&gt;=0．00001)语句，题目要求计算直至1／(2N+1)小于0．00001，所以term l／(2N+1)，因此n=2*n+1。"
}, {
	"subject_title": "阅读下列代码片段\nclass InterestTest——ActionListener{\npublic\"void actionPerformed(ActionEvent event){\ndouble interest=balance*rate／1 00 ；\nbalance+=interest；\nNumberFormat format=NumberFormat．getCur-\nrencyInstance()；\nSystem．OUt．print]b(\"balance=\"+formatter．\nformat(balance))；\n}\nPrivate double rate；\n}\n在下画线处，应填的正确选项是（　　）。",
	"subject_choice_A": "Implementation",
	"subject_choice_B": "Inheritance",
	"subject_choice_C": "implements",
	"subject_choice_D": "extends",
	"subject_answer": "D",
	"analysis": "继承父类应使用的关键词为extends。"
}, {
	"subject_title": "对于循环队列，下列叙述中正确的是（　　）。",
	"subject_choice_A": "队头指针是固定不变的",
	"subject_choice_B": "队头指针一定大于队尾指针",
	"subject_choice_C": "队头指针一定小于队尾指针",
	"subject_choice_D": "队头指针可以大于队尾指针，也可以小于队尾指针",
	"subject_answer": "D",
	"analysis": "循环队列是把队列的头和尾在逻辑上连接起来，构成一个环。循环队列中首尾相连，分不清头和尾，此时需要两个指示器分别指向头部和尾部。插入就在尾部指示器的指示位置处插入，删除就在头部指示器的指示位置删除。"
}, {
	"subject_title": "Java为移动设备提供的平台是（　　）。",
	"subject_choice_A": "J2ME",
	"subject_choice_B": "J2SE",
	"subject_choice_C": "J2EE",
	"subject_choice_D": "JDK 5．0",
	"subject_answer": "A",
	"analysis": "Java2平台包括：J2ME平台、J2SE平台和J2EE平台。其中：J2ME是为嵌入式和移动设备提供的Java平台；J2SE是面向企业级应用与服务的综合性标准开发平台；J2EE是面向大型企业级用容器管理专用构件的应用平台。而JDK 5．0是一个Java开发软件包。"
}, {
	"subject_title": "使下列程序正常运行并且输出“Hello!”，横线处应填写的内容是（　　）。\nclass Test\n{\npublic static void main(string[]args){\nTest t=new Test()；\nstart()；\n}\nPublic void run(){\nSystem．out．println(\"Hello!¨)；\n)",
	"subject_choice_A": "extends Thread",
	"subject_choice_B": "extends Float",
	"subject_choice_C": "extends Iostream",
	"subject_choice_D": "extends Stdio",
	"subject_answer": "A",
	"analysis": "从后面重写了run()方法来看，这是通过继承Thread类，并重写run()方法定义线程体，然后创建该子类的对象的方式来创建线程。"
}, {
	"subject_title": "一个Java Application运行后，在系统中是作为一 个（　　）。",
	"subject_choice_A": "线程",
	"subject_choice_B": "进程",
	"subject_choice_C": "进程或线程",
	"subject_choice_D": "不确定",
	"subject_answer": "B",
	"analysis": "线程为一个程序中的单个执行流；进程是程序的一次动态执行过程，它对应了从代码加载、执行到执行完毕的一个完整过程，这个过程也是进程本身从产生、发展到消亡的过程。一个JavaApplication运行后，在系统中应该就是一个进程了(动态)。"
}, {
	"subject_title": "一间宿舍可住多个学生，则实体宿舍和学生之间的联系是（　　）。",
	"subject_choice_A": "一对一",
	"subject_choice_B": "一对多",
	"subject_choice_C": "多对一",
	"subject_choice_D": "多对多",
	"subject_answer": "B",
	"analysis": "两个实体集间的联系可以有一对一的联系、一对多或多对一联系、多对多联系。由于一个宿舍可以住多个学生，所以它们的联系是一对多联系。"
}, {
	"subject_title": "当Applet需要更新显示内容时，应该调用的方法是（　　）。",
	"subject_choice_A": "paint",
	"subject_choice_B": "update()",
	"subject_choice_C": "start()",
	"subject_choice_D": "repaint()",
	"subject_answer": "B",
	"analysis": "Applet与显示相关的有三个方法，①paint()方法，具体执行Applet的绘制；②update()方法，用于更新Applet的显示；③repaint()方法，主要用于Applet的重新显示；Applet程序可以在需要显示更新时调用该方法，通知系统刷新显示。"
}, {
	"subject_title": "下列Java语句从指定网址读取html文件，在下画线处应填上的选项是（　　）。\nReader in=new (new    URL(urlString)．\nopenStream())；",
	"subject_choice_A": "Reader",
	"subject_choice_B": "DataOutputStream",
	"subject_choice_C": "ByteArray InputStream",
	"subject_choice_D": "InputStreamReader",
	"subject_answer": "A",
	"analysis": "创建一个Reader流的对象in。"
}, {
	"subject_title": "阅读下列代码\npublic class Test2005{\npublic static void main(String args[]){\nString s=\"Test\"；\nswitch(s){\ncase\"Java\"：System．out．print(\"Java\")；\nbreak；\ncase\"Language\"：System．out．print(\"Lan-\nguage\")；\nbreak；\ncase\"Test\"：System．out．print(\"Test\")；\nbreak；\n}\n}\n}\n其运行结果是（　　）。",
	"subject_choice_A": "Java",
	"subject_choice_B": "Language",
	"subject_choice_C": "Test",
	"subject_choice_D": "编译时出错",
	"subject_answer": "D",
	"analysis": "本题考查switch语句的用法。switch语句是多分支语句，即根据表达式的值来执行多个操作中的一个。在switch语句中，”表达式”的返回值类型必须是这几种类型之一：int、byte、char、short。本题中，switch的表达式s是一个字符串Strin9类型的值，它不是int、byte、char、short中的任意一个。因此表达式s的类型不对，编译时出错。"
}, {
	"subject_title": "一棵二叉树有10个度为1的结点，7个度为2的结点，则该二叉树共有结点个数为（　　）。",
	"subject_choice_A": "8",
	"subject_choice_B": "25",
	"subject_choice_C": "17",
	"subject_choice_D": "7",
	"subject_answer": "B",
	"analysis": "在任意一棵二叉树中，度数为0的结点(即叶子结点)总比度为2的结点多一个，因此该二叉树中叶子结点为7+1=8，8+17=25。"
}, {
	"subject_title": "在数据管理技术发展的三个阶段中，数据共享最好，的是（　　）。",
	"subject_choice_A": "人工管理阶段",
	"subject_choice_B": "文件系统阶段",
	"subject_choice_C": "数据库系统阶段",
	"subject_choice_D": "3个阶段相同",
	"subject_answer": "C",
	"analysis": "数据管理技术的发展经历了3个阶段：人工管理阶段、文件系统阶段和数据库系统阶段。人工管理阶段无共享，冗余度大；文件管理阶段共享性差，冗余度大；数据库系统管理阶段共享性大，冗余度小。"
}, {
	"subject_title": "鼠标在窗口中移动时，产生的事件是（　　）。",
	"subject_choice_A": "ActionEvent",
	"subject_choice_B": "PrintEvent",
	"subject_choice_C": "KeyEvent",
	"subject_choice_D": "MouseEvent",
	"subject_answer": "D",
	"analysis": "鼠标在窗口中移动产生的事件是MouseEvent事件，ActionEvent是动作事件处理，PrintEvent是打印事件，KeyEvent是键盘事件。"
}, {
	"subject_title": "下列关于完全二叉树的叙述中，错误的是（　　）。",
	"subject_choice_A": "除了最后一层外，每一层上的结点数均达到最大值",
	"subject_choice_B": "可能缺少若干个左右叶子结点",
	"subject_choice_C": "完全二叉树一般不是满二叉树",
	"subject_choice_D": "具有结点的完全二叉树的深度为[log2n]+1",
	"subject_answer": "B",
	"analysis": "满二叉树指除最后一层外，每一层上所有结点都有两个子结点的二叉树。完全二叉树指除最后一层外，每一层上的结点数均达到最大值，在最后一层上只缺少右边的若干叶子结点的二叉树。由定义可知，满二叉树肯定是完全二叉树，而完全二叉树一般不是满二叉树。"
}, {
	"subject_title": "下列关于Applet的叙述中，正确的是（　　）。",
	"subject_choice_A": "Applet不仅可以嵌入到浏览器中运行，还可以独立运行",
	"subject_choice_B": "Applet的主类要定义为Applet类或JApplet类的子类",
	"subject_choice_C": "同一个页面中的Applet之间不能通信",
	"subject_choice_D": "Applet不支持多线程",
	"subject_answer": "B",
	"analysis": "Applet不可以单独运行，Applet支持多线程。"
}, {
	"subject_title": "为使下列代码正常运行，应该在下画线处填入的选项是（　　）。\nint[]numbers=new int[n]；\nfor(int i=0；i<NUMBERS．\n；i++)\nnumbers[i]=i+1：",
	"subject_choice_A": "size",
	"subject_choice_B": "length",
	"subject_choice_C": "dimension",
	"subject_choice_D": "measurement",
	"subject_answer": "B",
	"analysis": "length表示数组的长度。"
}, {
	"subject_title": "相对于数据库系统，文件系统的主要缺陷有数据依赖、数据不一致性和（　　）。",
	"subject_choice_A": "可重用性差",
	"subject_choice_B": "安全性差",
	"subject_choice_C": "非持久性",
	"subject_choice_D": "冗余性",
	"subject_answer": "D",
	"analysis": "文件系统所管理的数据文件基本上是分散、相互独立的。因此相对于数据库系统，以此为基础的数据处理存在3个缺点：数据冗余大、数据的不一致性、程序与数据的相互依赖(简称为数据依赖)。"
}, {
	"subject_title": "当一个Applet被加载，后续对Applet生命周期方法的调用中，可能存在的次序是（　　）。",
	"subject_choice_A": "start()，stop()，destroy()",
	"subject_choice_B": "init()，start()，stop()，start()，stop()，destroy()",
	"subject_choice_C": "start()，init()，stop()，destroy()",
	"subject_choice_D": "ink()，start()，destroy()",
	"subject_answer": "B",
	"analysis": "init()一般用来完成所有必需的初始化操作，start()是在初始化之后Applet被加载时调用，stop()在Applet停止执行时调用，destory()是Applet从系统中撤出时调用。"
}, {
	"subject_title": "设a=8，则表达式a>>>1的值是（　　）。",
	"subject_choice_A": "1",
	"subject_choice_B": "2",
	"subject_choice_C": "3",
	"subject_choice_D": "4",
	"subject_answer": "D",
	"analysis": "本题考查考生对位运算符中无符号右移运算符的掌握。无符号右移运算符&gt;&gt;&gt;，也叫逻辑右移，用于将一个数的各二进制位全部无符号右移若干位，与运算符&gt;&gt;不同的是左补0，而&gt;&gt;则是最高位移入原来高位的值。在本题中，8的二进制表示是1000，右移一位后变成了0100，对应的十进制数是4。可见，正确答案为选项D。"
}, {
	"subject_title": "下列方法中，不属于Throwable类的方法是（　　）。",
	"subject_choice_A": "printMessage",
	"subject_choice_B": "getMessage",
	"subject_choice_C": "toString",
	"subject_choice_D": "fillStackTrace",
	"subject_answer": "C",
	"analysis": "toString是Object类的方法，所有类都从Object类继承。"
}, {
	"subject_title": "Java对I／O访问所提供的同步处理机制是（　　）。",
	"subject_choice_A": "字节流",
	"subject_choice_B": "过滤流",
	"subject_choice_C": "字符流",
	"subject_choice_D": "压缩文件流",
	"subject_answer": "B",
	"analysis": "本题考查JavaI／O流中的过滤流。过滤流是Java对I／O访问提供的同步处理机制，保证某时刻只有一个线程访问一个I／O流。过滤流是FilterInputStream和FiherOutputStream。因此，本题的正确答案是选项B。"
}, {
	"subject_title": "为了支持压栈线程与弹栈线程之间的交互与同步，应在下画线处填入的选项是（　　）。\npublic class StackTest{\nprivate int idx=0；\nprivate int[]data=new int[8]\npublic void push(int i){\nsynchronized(this){\n；\ndata(idx)=i：\nidx++：\n}\n}\n}……",
	"subject_choice_A": "this．notify()",
	"subject_choice_B": "interrupt()",
	"subject_choice_C": "this．wait()",
	"subject_choice_D": "sleep()",
	"subject_answer": "A",
	"analysis": "当一个线程使用的同步方法中用到某个变量，而且需要其他线程修改此变量后才能复合本线程的需要，那么可以使用wait()方法。wait()方法的作用是使本线程等待，并允许其他线程使用此同步方法。当其他线程使用完后应使用notify()或者notifyAll()方法允许其他线程使用此同步方法。Interrupt()方法的作用是在run方法执行完之前就消灭此线程，而sleep()方法的作用是延迟一段时间后执行。因为本题是为了支持压栈线程与弹栈线程之间的交互与同步，所以选A。"
}, {
	"subject_title": "下面for循环语句的执行结果是（　　）。\nfor(int j=10；j>3；j--)\nif(j％3 1=O)\nj--；\n--j；\n--j；\nSystem．OUt．println(j)；\n}",
	"subject_choice_A": "63",
	"subject_choice_B": "74",
	"subject_choice_C": "62",
	"subject_choice_D": "73",
	"subject_answer": "B",
	"analysis": "该题考查对for循环的理解。①当j=10时，满足条件j&gt;3，由于for循环中j--执行了1次，j的值为9，执行if语句，j％3=0不满足条件，继续向下执行2次 - -j，j的值为7：②当j=7时，满足条件j&gt;3，由于for循环中J一 一执行了1次，j的值为6，执行if语句，i％3=0不满足条件，继续向下执行2次- -j，j的值为4。"
}, {
	"subject_title": "需求分析阶段的任务是（　　）。",
	"subject_choice_A": "软件开发方法",
	"subject_choice_B": "软件开发工具",
	"subject_choice_C": "软件开发费用",
	"subject_choice_D": "软件系统功能",
	"subject_answer": "D",
	"analysis": "需求分析是软件定义时期的最后一个阶段，它的基本任务就是详细调查现实世界要处理的对象，充分了解原系统的工作概况，明确用户的各种需求，然后在这些基础上确定新系统的功能。"
}, {
	"subject_title": "在E-R图中，表示实体联系的框是（　　）。",
	"subject_choice_A": "矩形",
	"subject_choice_B": "椭圆形",
	"subject_choice_C": "菱形",
	"subject_choice_D": "正方形",
	"subject_answer": "C",
	"analysis": "本题考察E-R的关系，在E-R图中，用菱形来表示实体之间的联系。矩形表示实体集，椭圆形表示属性。"
}, {
	"subject_title": "下列叙述中，错误的是（　　）。",
	"subject_choice_A": "Java中，方法的重载是指多个方法可以共享同一个名字",
	"subject_choice_B": "Java中，用abstract装饰的类称为抽象类，它不能实例化",
	"subject_choice_C": "Java中，接口是不包含成员变量和方法实现的抽象类",
	"subject_choice_D": "Java中，构造方法可以有返回值",
	"subject_answer": "D",
	"analysis": "构造方法是一种特殊的方法，是为对象初始化操作编写的方法，用它来定义对象的初始状态。Java中的每个类都有构造方法，它也是由方法名、参数和方法体组成的。构造方法的名字必须与类名相同，并且构造方法不返回任何数据。"
}, {
	"subject_title": "下列描述中，错误的是（　　）。",
	"subject_choice_A": "Java要求编程者管理内存",
	"subject_choice_B": "Java的安全性体现在多个层次上",
	"subject_choice_C": "Applet要求在支持Java的浏览器上运行",
	"subject_choice_D": "Java有多线程机制",
	"subject_answer": "A",
	"analysis": "为了充分利用资源，Java有一个系统级的线程，用来对内存的使用进行跟踪，它可以在系统空闲时对不用的内存空间进行回收，从而使程序员从繁忙的内存管理中解放出来。"
}, {
	"subject_title": "下面程序段的输出结果是（　　）。\npublic class Test{\npublic static void main(String args[]){\nint X，y；\nx=(int)Math．sqrt(5)／2+(int)Math．random()*5／2；\ny=(int)Math．sqrt(3)／2+(int)Math．random()*3／2；\nif(x>v)\nSystem．OUt．println(\"x>y\")；\nelseif(x= =y)\nSystem．out．println(\"x=Y\")；\nelse\nSystem．out．println(\"x\n}\n}",
	"subject_choice_A": "x>y",
	"subject_choice_B": "x=Y",
	"subject_choice_C": "x<Y",
	"subject_choice_D": "编译错误",
	"subject_answer": "A",
	"analysis": "本题考查Java语言中if-else分支结构和几个标准函数语句的用法。本题中赋值号右边的两个表达式分别求两个标准函数的值，再进行整除，判断出x与y的大小。Math．sqrt计算一个数的平方根，Math．random()输出[0，1)之间的随机数，本题中经过两条赋值语句后，x=1，y=0。进入分支结构后，满足if条件执行相应System．out．println(&quot;x&gt;y&quot;)；操作。"
}, {
	"subject_title": "下列标识符(名字)命名原则中，正确的是（　　）。",
	"subject_choice_A": "类名的首字母小写",
	"subject_choice_B": "变量和方法名的首字母大写",
	"subject_choice_C": "接口名的首字母小写",
	"subject_choice_D": "常量完全大写",
	"subject_answer": "D",
	"analysis": "Java命名的基本原则包括如下几条：_、$不作为变量名、方法名的开头；变量名、方法名首单词小写，其余单词只有首字母大写；接口名、类名首单词第一个字母大写；常量完全大写。根据上述命名规则，选项D的说法是正确的。"
}, {
	"subject_title": "在Java中，若要使用一个包中的类时，首先要求对该包进行导入，其关键字是（　　）。",
	"subject_choice_A": "import",
	"subject_choice_B": "package",
	"subject_choice_C": "include",
	"subject_choice_D": "packet",
	"subject_answer": "A",
	"analysis": "定义一个包要用package关键字，使用一个包中的类时，首先要使用import导入这些类所在的包。include为C语言的包含头文件的关键字，不是Java的。"
}, {
	"subject_title": "下列关于Java语言特点的叙述中，错误的是（　　）。",
	"subject_choice_A": "Java是面向过程的编程语言",
	"subject_choice_B": "Java支持分布式计算",
	"subject_choice_C": "Java是跨平台的编程语言",
	"subject_choice_D": "Java支持多线程",
	"subject_answer": "A",
	"analysis": "Java是新一代编程语言，具有很多特点：简单易学；利用面向对象技术；分布式计算；健壮性(鲁棒性)；安全性；跨平台(即体系结构中立)；可移植性；解释执行；高性能；多线程；动态性。因此，本题的正确答案是A。"
}, {
	"subject_title": "一个栈的初始状态为空，首先将元素5，4，3，2，1依次入栈，然后退栈一次，再将元素A，B，C。D依次入栈，之后将所有元素全部退栈，则所有元素退栈(包括中间退栈的元素)的顺序为（　　）。",
	"subject_choice_A": "54321ABCD",
	"subject_choice_B": "5ABCD4321",
	"subject_choice_C": "DCBAl2345",
	"subject_choice_D": "1DCBA2345",
	"subject_answer": "D",
	"analysis": "栈是限制仅在表的一端进行插入和删除的运算的线性表，通常称插入、删除的这一端为栈顶，另一端称为栈底。"
}, {
	"subject_title": "下列关于Java对import语句规定自叙述中，错误的是（　　）。",
	"subject_choice_A": "在Java程序中import语句可以有多个",
	"subject_choice_B": "在Java程序中import语句可以没有",
	"subject_choice_C": "在Java程序中import语句必须有一个",
	"subject_choice_D": "在Java程序中import语句必须引入在所有类定义之前",
	"subject_answer": "C",
	"analysis": "Java程序中使用import关键字导入一个包中的类。在一个Java源程序中，可以有0个或多个import语句，但是必须在所有类定义之前引入标准类。因此，本题中选项C的说法是错误的。"
}, {
	"subject_title": "Java语言中如果要使用某个包中的类时，需要使用 （　　）导人。",
	"subject_choice_A": "inport",
	"subject_choice_B": "outport",
	"subject_choice_C": "import",
	"subject_choice_D": "input",
	"subject_answer": "C",
	"analysis": "本题考查包的导入和使用。首先用package语句说明一个包，该包的层次结构必须与文件目录的层次相同，否则，在编译时可能出现找不到包的问题。Java语言中java．lang包是编译器自动导入，其他包中的类必须用import导入。"
}, {
	"subject_title": "下列选项成员变量声明正确的是（　　）。",
	"subject_choice_A": "public protected final int i；",
	"subject_choice_B": "abstract class Fl{…}",
	"subject_choice_C": "private double height；",
	"subject_choice_D": "double weight()",
	"subject_answer": "C",
	"analysis": "本题考查对成员变量的声明。成员变量的声明格式为：修饰符type变量名；其中type可以是java语言中的任意数据类型，而修饰符可以是public、protected，private，static，final，transient，volatile等。选项A错误，成员变量不能同时声明成public和protected。选项B是类的声明格式，并不是成员变量的声明。成员变量声明应以&quot;；&quot;结尾，选项D错误。选项C声明了一个私有的double型成员变量，为正确答案。"
}, {
	"subject_title": "Java中的字符变量在内存中占位(bit)为（　　）。",
	"subject_choice_A": "4",
	"subject_choice_B": "8",
	"subject_choice_C": "16",
	"subject_choice_D": "24",
	"subject_answer": "C",
	"analysis": "字符变量在内存中占16位二进制数位，int变量在内存中占32位二进制数位。"
}, {
	"subject_title": "下列数据结构中，属于非线性结构的是（　　）。",
	"subject_choice_A": "循环队列",
	"subject_choice_B": "带链队列",
	"subject_choice_C": "二叉树",
	"subject_choice_D": "带链栈",
	"subject_answer": "C",
	"analysis": "线性结构是指数据元素只有一个直接前驱和直接后继，线性表是线性结构，循环队列、带链队列和栈是指对插入和删除有特殊要求的线性表，是线性结构。而二叉树是非线性结构。"
}, {
	"subject_title": "设有一个已按各元素的值排好序的顺序表(长度大于2)，现分别用顺序查找法和二分查找法查找与给定值k相等的元素，比较的次数分别是s和b，在查找不成功情况下s和b的关系是( )。",
	"subject_choice_A": "s=b",
	"subject_choice_B": "s>b",
	"subject_choice_C": "s<B",
	"subject_choice_D": "s>=b",
	"subject_answer": "B",
	"analysis": "顺序查找的基本思想是：从表的一端开始，顺序扫描线性表，依次将扫描到结点的关键字和给定值k进行比较，若当前扫描到结点的关键字与k相等，则查找成功；若扫描结束后，仍未找到关键字等于k的结点，则查找失败。二分查找法是一种效率较高的查找方法，要求线性表是有序表。基本思想是：首先将待查的k值和有序表R[0]～R[n-1]的中间位置mid上的结点的关键字进行比较，若相等，则查找完成；否则，若R[mid]．key&gt;k，则说明待查找的结点只可能在左子表R[0]～R[mid-1]中，我们只需在左子表中继续进行折半查找，若R[mid]．key&lt;k，则说明待查找的结点只可能在右子表R[mid+1]～R[n-1]中，我们只需在右子表中继续进行折半查找。这样，经过一次关键字比较就缩小一半的查找范围。对顺序查找而言，如果查找失败，比较次数为n次；对二分查找而言，如果查找失败，比较次数为log2(n+1)次。"
}, {
	"subject_title": "在Java语言中，封闭是借助于（　　）实现的。",
	"subject_choice_A": "对象",
	"subject_choice_B": "类",
	"subject_choice_C": "数组",
	"subject_choice_D": "成员",
	"subject_answer": "B",
	"analysis": "Java是一个完全面向对象的语言，利用类把对象的属性和方法封装在一起，只对外界提供有限的接口。"
}, {
	"subject_title": "代码System．out．println(066)的输出结果是（　　）。",
	"subject_choice_A": "12",
	"subject_choice_B": "36",
	"subject_choice_C": "54",
	"subject_choice_D": "66",
	"subject_answer": "C",
	"analysis": "066代表8进制数据的66等于十进制的54。"
}, {
	"subject_title": "对于给出的一组权w={10，12，16，21，30}，通过霍夫曼算法求出的扩充二叉树的带权外部路径长度为（　　）。",
	"subject_choice_A": "89",
	"subject_choice_B": "189",
	"subject_choice_C": "200",
	"subject_choice_D": "300",
	"subject_answer": "C",
	"analysis": "其带权外部路径长度为：2×16+2×21+2×30+3×10+3×12=200。"
}, {
	"subject_title": "栈中允许进行插入和删除的一端称为（　　）。",
	"subject_choice_A": "栈顶",
	"subject_choice_B": "栈底",
	"subject_choice_C": "栈端",
	"subject_choice_D": "栈尾",
	"subject_answer": "A",
	"analysis": "栈是限定在表的一端进行插入和删除操作的线性表。在表中，允许插入和删除的一端叫做“栈顶”，不允许插入和删除的一端叫做“栈底”。"
}, {
	"subject_title": "当启动Applet程序时，首先调用的方法是（　　）。",
	"subject_choice_A": "stop()",
	"subject_choice_B": "init()",
	"subject_choice_C": "start()",
	"subject_choice_D": "destroy()",
	"subject_answer": "B",
	"analysis": "本题考查Applet程序的运行方式。在Applet运行时，首先由浏览器调用init()方法，所以选项B正确。初始化完成后，将调用start()方法使Applet成为激活状态。当Applet被覆盖时．可用stop()方法停止线程。关闭浏览器时调用destroy()，彻底终止Applet，从内存中卸载并释放该Applet的所有资源。Applet的生命周期及其运行方式是考试重点，应该牢记。"
}, {
	"subject_title": "下面代码段的输出是（　　）。\nif(5 8L7)0&8L5｜2)system．out．println(\"true\")；",
	"subject_choice_A": "编译出错",
	"subject_choice_B": "5752",
	"subject_choice_C": "true",
	"subject_choice_D": "无任何输出",
	"subject_answer": "A",
	"analysis": "本题考查对位运算符和逻辑运算符的理解。位运算符”&amp;”和”|¨用于按位将两个数进行与和或的操作，两个操作数可以是整型、字节型、长整型和短整型，但不能是浮点型数据。逻辑运算符&amp;&amp;只能对两个布尔型的数据进行运算，返回的结果也是布尔型的。"
}, {
	"subject_title": "在软件开发中，需求分析阶段可以使用的工具是（　　）。",
	"subject_choice_A": "N-S图",
	"subject_choice_B": "DFD图",
	"subject_choice_C": "PAD图",
	"subject_choice_D": "程序流程图",
	"subject_answer": "B",
	"analysis": "在软件开发中，需求分析阶段常使用的工具有数据流图(DFD)、数据字典(DD)、判断树和判断表。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "顺序存储结构的存储一定是连续的，链式存储结构的存储空间不一定是连续的",
	"subject_choice_B": "顺序存储结构只针对线性结构，链式存储结构只针对非线性结构",
	"subject_choice_C": "顺序存储结构能存储有序表，链式存储结构不能存储有序表",
	"subject_choice_D": "链式存储结构比顺序存储结构节省存储空间",
	"subject_answer": "A",
	"analysis": "顺序存储方式主要用于线性数据结构，它把逻辑上相邻的数据元素存储在物理上相邻的存储单元里，结点之间的关系由存储单元的邻接关系来体现。链式存储结构的存储空间不一定是连续的。"
}, {
	"subject_title": "下列方法被调用后，一定使调用线程改变当前状态的是（　　）。",
	"subject_choice_A": "notify()",
	"subject_choice_B": "yield()",
	"subject_choice_C": "sleep()",
	"subject_choice_D": "isAlive()",
	"subject_answer": "C",
	"analysis": "线程调用sleep函数后，使当前线程进入停滞状态。yield函数可使线程进入可执行状态，排程器从可执行状态的线程中重新排程，调用了yield函数的线程有可能被马上执行，也有可能不会马上执行。notify函数从线程等待池中移走任意一个线程，并把它放到锁标志等待池中，其状态仍旧是等待。所以只有sleep一定会改变线程状态。"
}, {
	"subject_title": "下列表达式中正确的是（　　）。",
	"subject_choice_A": "5++",
	"subject_choice_B": "(a+b)++",
	"subject_choice_C": "++(a+b)",
	"subject_choice_D": "++x",
	"subject_answer": "D",
	"analysis": "本题考查Java中的运算符。“++”和“--”都是一元算术运算符，主要用于自加和自减，在Java中不允许对表达式进行这样的运算，选项B和选项C都是错误的，更不允许对数字进行这样的运算，选项A也错误，只有选项D正确。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "在模块化程序设计中，一个模块应该尽量多的包括与其他模块联系的信息",
	"subject_choice_B": "在自顶向下、逐步细化的设计过程中，首先应设计解决问题的第一个细节",
	"subject_choice_C": "在模块化程序设计中，一个模块内部的控制结构也要符合结构化原则",
	"subject_choice_D": "在程序设计过程中，不能同时采用结构化程序设计方法与模块化程序设计方法",
	"subject_answer": "C",
	"analysis": "在模块化程序设计中，模块之间的联系可以通过程序的控制结构来实现，在自顶向下、逐步细化的设计过程中，首先要考虑全局目标，而不是细节。在程序设计中模块化和结构化可以同时使用，一个模块的内部结构也要符合结构化设计原则。"
}, {
	"subject_title": "下列代码中，将引起一个编译错误的行是（　　）。\n1)public class Test{\n2)int m，n；\n3)public Test(){}\n4)public Test(int a){m=a；)\n5)public static void main(String args[]){\n6)Test tl，t2；\n7)int j，k；\n8)j=0；k=0；\n9)tl=new Test()；\n10)t2=new Test(j，k)；\n11)}\n12)}",
	"subject_choice_A": "第3行",
	"subject_choice_B": "第5行",
	"subject_choice_C": "第6行",
	"subject_choice_D": "第l0行",
	"subject_answer": "D",
	"analysis": "本题考查考生对Java中构造方法的理解及应用。构造方法名必须与类名相同，没有返回值，用户不能直接调用，只能通过new自动调用。题目标两个构造方法Test()和Test(inta)，按照参数决定调用哪个方法。tl=newTest()语句调用Test()方法，而t2=newTest(j，k)将会找不到相应的构造方法，程序编译出错在第10行，所以选项D正确。"
}, {
	"subject_title": "下列说法中，（　　）是正确的。",
	"subject_choice_A": "子类拥有的成员数目大于等于父类拥有的成员数目",
	"subject_choice_B": "父类代表的对象范围比子类广",
	"subject_choice_C": "子类要调用父类的方法，必须使用super关键字",
	"subject_choice_D": "一个Java类可以有多个父类",
	"subject_answer": "B",
	"analysis": "本题考查对子类与父类关系的理解。对一个类的继承也就是构建了一个子类，子类继承了父类的方法和状态，同时还可以向新类中增添新的方法和状态。重点掌握两点：子类方法的访问权限比父类访问权限高，因此父类不能替代子类，但子类能够代替父类，子类方法不能产生比父类更多的异常。子类拥有的成员数目小于等于父类拥有的成员数目，选项A说法错误；父类代表的对象范围比子类广，选项B说法正确；子类要调用父类的方法，可以使用super关键字，也可以将父类的方法进行重写，选项C说法错误。在Java中一个类只能有一个父类，选项D说法错误。"
}, {
	"subject_title": "下面语句会产生编译错误的是（　　）。",
	"subject_choice_A": "float F=1024．OF；",
	"subject_choice_B": "double D=1024．0；",
	"subject_choice_C": "byte B=1024；",
	"subject_choice_D": "char C=1024；",
	"subject_answer": "C",
	"analysis": "本题考查考生对Java中数据类型的理解。为了防止计算机高低位字节存储顺序不同，通常byte类型用来表示数据避免出错，因为它只有8bit，范围是：-l28～+127。float类型数的表示范围是：-3．40282347E38～3．40282347E38：double类型数的表示范围是：-1．79769313486231570E308～ 1．79769313486231570E308；char类型在内存中占16bit，表示范围是O～65 535。"
}, {
	"subject_title": "下列代码将对象写入的设备是（　　）。\nByteArrayOutputStream bout=new ByteArrayOut-\nputStream()；\nObjectOutputStream out=new ObjectOutputStream\n(bout)；\nout．writeObject(this)；\nout．close()；",
	"subject_choice_A": "内存",
	"subject_choice_B": "硬盘",
	"subject_choice_C": "屏幕",
	"subject_choice_D": "网络",
	"subject_answer": "A",
	"analysis": "()bject()utputStream类的构造方法是ObjectOutputStream(0utputStreamout)。Java中的二进制流全都写入到内存中。"
}, {
	"subject_title": "下列组件不能添加进Frame主窗口的是（　　）。",
	"subject_choice_A": "Panel",
	"subject_choice_B": "CheckBox",
	"subject_choice_C": "Dialog",
	"subject_choice_D": "Choice",
	"subject_answer": "C",
	"analysis": "本题考查对Java组件容器中添加容器的基本知识。选项A错误，Panel组件是容器，可以添加到Frame窗口；选项B错误，CheekBox组件是复选框组件，可以添加到Frame窗口；选项C正确，Dialog继承自Windows类，Windows类型(或子类)的对象不能包含在其他容器中；选项D错误，Choice组件是选择框组件，可以添加到Frame窗口。"
}, {
	"subject_title": "Thread类中能运行线程的方法是（　　）。",
	"subject_choice_A": "resume()",
	"subject_choice_B": "start()",
	"subject_choice_C": "run()",
	"subject_choice_D": "init()",
	"subject_answer": "C",
	"analysis": "resume()是Thread类提供的用于线程控制的方法；start()是Thread类中的方法，新建的线程不会自动运行，必须调用线程的start()方法才能运行该线程；run()是Thread类中的方法，在该方法中定义了线程的具体行为，线程开始执行时，就是从它的run()方法开始执行的，就像Java应用程序从main()开始、Applet从ink()开始一样；init()不是Thread类中的方法。"
}, {
	"subject_title": "下列有关操作系统的叙述中，不正确的是（　　）。",
	"subject_choice_A": "操作系统管理计算机系统中的各种资源",
	"subject_choice_B": "操作系统为用户提供良好的界面",
	"subject_choice_C": "操作系统与用户程序必须交替运行",
	"subject_choice_D": "操作系统位于各种软件的最底层",
	"subject_answer": "C",
	"analysis": "操作系统是计算机系统中的一个系统软件，它能有效地组织和管理计算机系统中的各种资源，并且为用户提供良好的界面。没有任何软件支持的计算机称为裸机，而实际呈现在用户面前的计算机系统是经过若干层软件改造的计算机，而操作系统位于各种软件的最底层。"
}, {
	"subject_title": "下列关于栈叙述正确的是（　　）。",
	"subject_choice_A": "栈顶元素能最先被删除",
	"subject_choice_B": "栈顶元素最后才能被删除",
	"subject_choice_C": "栈底元素永远不能被删除",
	"subject_choice_D": "以上三种说法都不对",
	"subject_answer": "A",
	"analysis": "栈是限定在一端进行插入、删除的先入后出的线性表数据结构，栈顶元素最后被插入到栈中，但是最先被删除；而栈底元素最先被插入，最后被删除。"
}, {
	"subject_title": "在Java中能实现多重继承效果的方式是（　　）。",
	"subject_choice_A": "内部类",
	"subject_choice_B": "适配器",
	"subject_choice_C": "接口",
	"subject_choice_D": "同步",
	"subject_answer": "C",
	"analysis": "本题考查Java中多重继承的概念。首先要区分选项中各个概念。内部类是在一个类中的内部嵌套定义的类，主要用来生成事件适配器。适配器(Adapter)定义一个包装类，包装有不兼容接口的对象。这个包装类指的就是适配器，它包装的对象就是适配者(Adaptee)，适配器提供客户类需要的接口。接口是一种只含有抽象方法或常量的一种特殊的抽象类，因为接口不包括任何实现，所以与存储空间没有任何关系，将多个接口合并，即多重继承就可以很容易实现，选项C正确。同步主要用在多线程程序设计中。"
}, {
	"subject_title": "结构化程序设计的3种基本结构是（　　）。",
	"subject_choice_A": "过程、子程序和分程序",
	"subject_choice_B": "顺序、选择和重复",
	"subject_choice_C": "递归、堆栈和队列",
	"subject_choice_D": "调用、返回和转移",
	"subject_answer": "B",
	"analysis": "程序的三种基本控制结构包括：顺序、选择和重复(循环)，这三种结构就足以表达出各种其他形式的结构。"
}, {
	"subject_title": "一棵二叉树的中序遍历结果为DBEAFC，前序遍历结果为ABDECF，则后序历结果为（　　）。",
	"subject_choice_A": "ACFBED",
	"subject_choice_B": "DFBECA",
	"subject_choice_C": "ABCDEF",
	"subject_choice_D": "DEBFCA",
	"subject_answer": "D",
	"analysis": "这类题型一般通过前序遍历的结果来找根结点，用中序遍历的结构找分支结点，通过画出该二叉树可得到结果。"
}, {
	"subject_title": "AWT中用来表示颜色的类是（　　）。",
	"subject_choice_A": "Font",
	"subject_choice_B": "Color",
	"subject_choice_C": "Panel",
	"subject_choice_D": "Dialog",
	"subject_answer": "B",
	"analysis": "AWT中Font是表示字体的类，Color是表示颜色的类，Panel是表示面板的类，Dialog是表示对话框的类。"
}, {
	"subject_title": "下列运算符中，优先级最高的是（　　）。",
	"subject_choice_A": "+=",
	"subject_choice_B": "= =",
	"subject_choice_C": "&&",
	"subject_choice_D": "+ +",
	"subject_answer": "D",
	"analysis": "算术运算符的优先级中，++和--级别最高。"
}, {
	"subject_title": "在Java中，与数据库连接的技术是（　　）。",
	"subject_choice_A": "开放数据库连接",
	"subject_choice_B": "Java数据库连接",
	"subject_choice_C": "数据库厂家驱动程序",
	"subject_choice_D": "数据库厂家的连接协议",
	"subject_answer": "B",
	"analysis": "开放数据库连接(ODBC，OpenDatebase Connectivity)，它是用C语言定义的。由于J2EE要求与Java绑定，因此规定使用Java数据库连接(JDBC，Java DataBase Connectivity)，作为Java与数据库连接的技术。"
}, {
	"subject_title": "char类型被封装在（　　）中。",
	"subject_choice_A": "java．lang．Integer",
	"subject_choice_B": "java．lang．Char",
	"subject_choice_C": "java．lang．Boolean",
	"subject_choice_D": "java．lang．Character",
	"subject_answer": "D",
	"analysis": "Java语言中，char类型被封装在java．lang．Character中。"
}, {
	"subject_title": "在软件开发中，需求分析阶段产生的主要文档是（　　）。",
	"subject_choice_A": "软件集成测试计划",
	"subject_choice_B": "软件详细设计说明书",
	"subject_choice_C": "用户手册",
	"subject_choice_D": "软件需求规格说明书",
	"subject_answer": "D",
	"analysis": "需求分析阶段只能产生需求分析规格说明数，A测试说明书是软件测试阶段生成的，B软件详细设计说明书是设计阶段生成的，C用户手册是软件发布时随软件一同交付给用户的。"
}, {
	"subject_title": "可以使当前同级线程重新获得运行机会的方法是（　　）。",
	"subject_choice_A": "Sleep()",
	"subject_choice_B": "join()",
	"subject_choice_C": "yield()",
	"subject_choice_D": "interrupt()",
	"subject_answer": "C",
	"analysis": "本题考查线程的基本控制。Thread类提供的基本线程控制方法包括：sleep()——使比其低的优先级线程运行，可以让一个线程暂停运行一段固定的时间；yield()——使具有与当前线程相同优先级的线程有运行的机会；join()——使当前线‘程暂停执行，等待调用该方法的线程结束后，再恢复执行；interrupt()——中断线程的阻塞状态，并且线程接收到InterruptException异常。根据上述介绍可知，只有yield()方法可以使当前同级线程重新获得运行机会。因此，本题的正确答案是C。"
}, {
	"subject_title": "已知一个有序线性表为(13，18，24，35，47，50，62，83，90。115，134)，当用二分法查找值为90的元素时，查找成功的比较次数为（　　）。",
	"subject_choice_A": "1",
	"subject_choice_B": "2",
	"subject_choice_C": "3",
	"subject_choice_D": "9",
	"subject_answer": "B",
	"analysis": "根据二分法查找需要两次：首先将90与表中间的元素50进行比较，由于90大于50。所以在线性表的后半部分查找；第二次比较的元素是后半部分的中间元素，即90，这时两者相等，即查找成功。"
}, {
	"subject_title": "下列关于boolean类型的叙述中，正确的是（　　）。",
	"subject_choice_A": "可以将boolean类型的数值转换为int类型的数值",
	"subject_choice_B": "可以将boolean类型的数值转换为字符串",
	"subject_choice_C": "可以将boolean类型的数值转换为char类型的数值",
	"subject_choice_D": "不能将boolean类型的数值转换为其他基本数据类型",
	"subject_answer": "D",
	"analysis": "由于基本数据类型中boolean类型不是数字型，所以基本数据类型的转换是除了boolean类型以外的其他7种类型之间的转换。"
}, {
	"subject_title": "下面属于面向对象语言的是（　　）。",
	"subject_choice_A": "Java语言",
	"subject_choice_B": "机器语言",
	"subject_choice_C": "C语言",
	"subject_choice_D": "汇编语言",
	"subject_answer": "A",
	"analysis": "本题考查Java语言的特点。Java语言是面向对象的，将客观世界看成由各种对象组成的；机器语言是计算机实际处理时使用的语言，把客观世界都看成由0和1组成；过去的高级语言大多数是面向过程的，比如C语言等，它们是通过数据结构与算法来描述客观世界；汇编语言属于低级语言。考生应注意区分各种语言的区别。本题正确答案为选项A。"
}, {
	"subject_title": "结构化程序设计的核心和基础是( )。",
	"subject_choice_A": "结构化分析方法",
	"subject_choice_B": "结构化设计方法",
	"subject_choice_C": "结构化设计理论",
	"subject_choice_D": "结构化编程方法",
	"subject_answer": "C",
	"analysis": "结构化程序设计的核心和基础是结构化设计理论，其中包括：结构化分析方法、结构化设计方法和结构化编程方法。"
}, {
	"subject_title": "t为int类型，进入下面的循环之前，t的值为0。则下列说法中正确的是（　　）。 while(t=1){…}",
	"subject_choice_A": "循环控制表达式的值为0",
	"subject_choice_B": "循环控制表达式的值为1",
	"subject_choice_C": "循环控制表达式不合法",
	"subject_choice_D": "以上说法都不对",
	"subject_answer": "B",
	"analysis": "本题考查对while循环及逻辑表达式的理解。循环控制表达式为赋值表达white式t=1，永远为l(为真)。"
}, {
	"subject_title": "数据流图用于抽象描述一个软件的逻辑模型，数据流图由一些特定的图符构成。下列图符名标识的图符不属于数据流图合法图符的是（　　）。",
	"subject_choice_A": "控制流",
	"subject_choice_B": "加工",
	"subject_choice_C": "数据存储",
	"subject_choice_D": "源和终",
	"subject_answer": "A",
	"analysis": "数据流图简称DFD，它以图形的方式描绘数据在系统中流动和处理的过程，由于它只反映系统必须完成的逻辑功能，所以它是一种功能模型。数据流图有4种基本图形符号：箭头表示数据流；椭圆表示加工；双杠表示存储文件(数据源)；方框表示数据的源点或终点。"
}, {
	"subject_title": "当使用SomeThread t=new SomeThread()创建一个线程时，下列叙述中正确的是（　　）。",
	"subject_choice_A": "SomeThread类是包含run()方法的任意Java类",
	"subject_choice_B": "SomeThread类一定要实现Runnable接口",
	"subject_choice_C": "SomeThread类是Thread类的子类",
	"subject_choice_D": "SomeThread类是Thread类的子类并且要实现Run-",
	"subject_answer": "C",
	"analysis": "由SomeThreadt=new SomeThread()可知此题是通过继承Thread类来创建线程的。"
}, {
	"subject_title": "下列程序的输出结果是（　　）。\nclass Test{\npublic static void main(String args[]){\nint n=7：\nn<<=3；\nn=n&n+1｜n+2^n+3；\nn>>=2：\nSystem．out．println(n)；\n}\n)",
	"subject_choice_A": "0",
	"subject_choice_B": "-l",
	"subject_choice_C": "14",
	"subject_choice_D": "64",
	"subject_answer": "C",
	"analysis": "本题考查Java中的运算符。首先要清楚程序里面涉及的运算符的含义。&quot;&lt;&lt;&quot;是按位左移运算符，”&amp;”是按位与运算符，&quot;|&quot;是按位或运算符，&quot;^&quot;是按位异或运算符。题目中整型变量n=7相当于二进制中的111，n&lt;&lt;=3语句执行后，n值为lll000。相当于十进制的56，而语句n=n&amp;n+1｜n+2^n+3执行后，n值为57，n&gt;&gt;=2语句执行恬，n的值为14，所以选项C正确。"
}, {
	"subject_title": "下列程序的输出结果是（　　）。\npublic class ArrayTest\n{\npublic static void main(String args[])\n{\nint[]intArray=new int[3]\nfor(int i=0；i<3；i++)\n{\nintArray[i]=i+2：\nsystem．out．println(\"lntArray[\"+i+\"]¨=\nintArray[i])；\n}\nSystem．out．println(\"----------\")；\nint arrlen=4：\nIntArray=new int[arrLen]；\nFor(int j=intArray．length；j>=0；j--)\n{\nintArray[j]=j*3；\nsystem．out．println(\"hello\"+intArray[j])；\n}\n}\n}",
	"subject_choice_A": "编译未通过",
	"subject_choice_B": "编译通过，但运行错误",
	"subject_choice_C": "可以运行，但有错误",
	"subject_choice_D": "以上都不对",
	"subject_answer": "B",
	"analysis": "这是一道考查数组引用的题，目的是考查如何在程序中引用初始化后的数组。引用的方式为arrayName[index]，其中index为数组的下标，可以为整数、变量和表达式，范围从0开始，一直到数组的长度减l。在Java语言中，是要对数组下标进行检查的。因此，当程序运行到数组的长度值时，就发生了越界现象。"
}, {
	"subject_title": "int型public成员变量MAX_LENGTH，该值保持为常数100，则定义这个变量的语句是（　　）。",
	"subject_choice_A": "public int MAX LENGTH=100",
	"subject_choice_B": "final int MAX—LENGTH=100",
	"subject_choice_C": "public const int MAX_LENGTH=100",
	"subject_choice_D": "public final int MAX_LENGTH=100",
	"subject_answer": "D",
	"analysis": "本题考查Java中变量的声明。选项A虽然按照题目要求定义了一个变量，但没有满足保持为常数的要求，该变量可以被改变；选项B没有满足题目要求的public成员变量；选项C与C语言混淆，const是C语言用来定义常值变量的关键字；Java中定义常值变量使用的是final属性，说明该值赋值以后永不改变，所以选项D为正确答案。"
}, {
	"subject_title": "Java中所有类的父类是（　　）。",
	"subject_choice_A": "Father",
	"subject_choice_B": "Dang",
	"subject_choice_C": "ExceptionTM",
	"subject_choice_D": "Object",
	"subject_answer": "D",
	"analysis": "Object是所有类的根。"
}, {
	"subject_title": "软件设计中划分模块的一个准则是（　　）。",
	"subject_choice_A": "低内聚低耦合",
	"subject_choice_B": "高内聚低耦合",
	"subject_choice_C": "低内聚高耦合",
	"subject_choice_D": "高内聚高耦合",
	"subject_answer": "B",
	"analysis": "耦合性和内聚性是模块独立性的两个定性标准，是互相关联的。在软件设计中，各模块间的内聚性越强，则耦合性越弱。一般优秀的软件设计，应尽量做到高内聚、低耦合，这有利于提高模块的独立性。"
}, {
	"subject_title": "下列代码的执行结果是（　　）。\nint length=\"Hell0\"．length()；\nSystem．OUt．println(length)；",
	"subject_choice_A": "5",
	"subject_choice_B": "2",
	"subject_choice_C": "10",
	"subject_choice_D": "6",
	"subject_answer": "A",
	"analysis": "字符串&quot;Hello&quot;的长度是5，java在计算字符串长度时只计算实际字符串长度。"
}, {
	"subject_title": "下列运算符中，优先级最高的是（　　）。",
	"subject_choice_A": "++",
	"subject_choice_B": "十",
	"subject_choice_C": "*",
	"subject_choice_D": ">",
	"subject_answer": "A",
	"analysis": "在这些运算符中++运算符优先级最高。"
}, {
	"subject_title": "下列数中为八进制的是（　　）。",
	"subject_choice_A": "27",
	"subject_choice_B": "0x25",
	"subject_choice_C": "026",
	"subject_choice_D": "028",
	"subject_answer": "C",
	"analysis": "采用0，1，2，3，4，5，6，7八个数码，逢八进位，并且开头一定要以数字0开头的为八进制。"
}, {
	"subject_title": "Java API ee支持线程的类或接口是（　　）。\nⅠ．java．lang．Thread\nⅡ．java．lang．Runnable\nⅢ．java．lang．ThreadGroup\nIV．java．io．Serializable",
	"subject_choice_A": "I，Ⅱ",
	"subject_choice_B": "I，Ⅱ，Ⅲ",
	"subject_choice_C": "I，Ⅱ，IV",
	"subject_choice_D": "I，Ⅱ，Ⅲ，Ⅳ",
	"subject_answer": "A",
	"analysis": "java．lang．Thread类和java．lang．Runnable是创建线程的两个方法，分别是实现Thread类和继承Runnable接口，而ThreadGroup类是管理一组线程的类。而Serializable是序列化，将一个对象的状态保存起来，在适当的时候再获得，它不支持线程。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "线性表的链式存储结构与顺序存储结构所需要的存储空间是相同的",
	"subject_choice_B": "线性表的链式存储结构所需要的存储空间一般要多于顺序存储结构",
	"subject_choice_C": "线性表的链式存储结构所需要的存储空间一般要少于顺序存储结构",
	"subject_choice_D": "上述三种说法都不对",
	"subject_answer": "B",
	"analysis": "与顺序存储结构相比，线性表的链式存储结构需要更多的空间存储指针域，因此，线性表的链式存储结构所需要的存储空间一般要多于顺序存储结构。"
}, {
	"subject_title": "阅读下列代码：\npublic class Person{\nstatic int arr[]=new int[10]；\npublic static void main(String args){\nSystem．out．println{arr[9])；\n}\n}\n该代码的运行结果是（　　）。",
	"subject_choice_A": "编译时将产生错误",
	"subject_choice_B": "编译时正确，运行时将产生错误",
	"subject_choice_C": "输出零",
	"subject_choice_D": "输出空",
	"subject_answer": "C",
	"analysis": "arr[]为整型数组，分配地址后默认值为0，所以创建数组时也是对每个数组元素赋初值0。"
}, {
	"subject_title": "下列组件不能添加进Frame主窗口的是（　　）。",
	"subject_choice_A": "Panel",
	"subject_choice_B": "CheckBox",
	"subject_choice_C": "Dialog",
	"subject_choice_D": "Choice",
	"subject_answer": "C",
	"analysis": "本题考查Java组件中容器的基本知识。选项A错误，Panel组件是容器，可以添加到Frame窗口；选项B错误，CheekBox组件是复选框组件，可以添加到Frame窗口；选项C正确，Dialog继承自Window，Windows类型(或子类)的对象不能包含在其他容器中；选项D错误，Choice组件是选择框组件，可以添加到Frame窗口。"
}, {
	"subject_title": "下列描述中，正确的是（　　）。",
	"subject_choice_A": "在Serializable接口中定义了抽象方法",
	"subject_choice_B": "在Serializable接口中定义了常量",
	"subject_choice_C": "在Serializable接口中没有定义抽象方法，也没有定义常量",
	"subject_choice_D": "在Serializable接口中定义了成员方法",
	"subject_answer": "C",
	"analysis": "在java．i0包中，接口Serializable是实现对象串行化的工具。实际上，Serializable接口是一个空接口，它里面既没有定义抽象方法，也没有定义常量。Serializable接口的目的只是简单地标识一个类的对象是可以被串行化的。"
}, {
	"subject_title": "下列Java组件中，不属于容器的是（　　）。",
	"subject_choice_A": "Panel",
	"subject_choice_B": "Window",
	"subject_choice_C": "Frame",
	"subject_choice_D": "Label",
	"subject_answer": "D",
	"analysis": "本题考查Java组件中容器的基本知识。选项A错误，Panel类派生自容器类Container，属于容器的一种；选项B错误，Window类也派生自容器类Container，也属于容器的一种；选项C错误，Frame类派生自Window类，也是一种容器；选项D正确，Lable组件是标签组件，不属于容器。"
}, {
	"subject_title": "for(int x=0，y=0；!x＆&y<=5；y++)语句执行循环的次数是（　　）。",
	"subject_choice_A": "0",
	"subject_choice_B": "5",
	"subject_choice_C": "6",
	"subject_choice_D": "无穷",
	"subject_answer": "C",
	"analysis": "此题是典型的考题。题中X=0，则!x永远为真，对于条件表达式!x&amp;&amp;y&lt;=5只考虑y&lt;=5，由于每次循环Y都增加1，而且y从0开始到5。所以可知总共循环了6次。"
}, {
	"subject_title": "对下列程序的叙述中，正确的是（　　）。\n1：public class X extends Thread implements Runnable{\n2：public void run(){\n3：system．out．println(\"this is run()\")；\n4：}\n5：oublic static void main(String args[]){\n6：Thread t=new Thread(new X())：\n7：t．start()；\n8：}\n9：}",
	"subject_choice_A": "第l行会产生编译错误",
	"subject_choice_B": "第6行会产生编译错程",
	"subject_choice_C": "第6行会产生运行错误",
	"subject_choice_D": "程序正常运行",
	"subject_answer": "D",
	"analysis": "程序正常运行打印thisis run()。用Thread类的构造方法Thread(Runnable target)创建线程对象时，构造方法中的参数必须是一个具体的对象，该对象称作线程的目标对象，创建的目标对象的类必须实现Runnable接口。"
}, {
	"subject_title": "将一个容器panel1放到容器framel中的方法是（　　）。",
	"subject_choice_A": "framel．insert(panel1)",
	"subject_choice_B": "framel．add(panel1)",
	"subject_choice_C": "framel．addJPanel(panel1)",
	"subject_choice_D": "framel．insertJPanel(panel1)",
	"subject_answer": "B",
	"analysis": "本题考查容器的嵌套。将一个容器Panel1放到容器framel中的方法和在容器上添加部件是一样的，使用add()方法即可。"
}, {
	"subject_title": "若类声明加上（　　）修饰符，则表示该类不能有子类。",
	"subject_choice_A": "close",
	"subject_choice_B": "final",
	"subject_choice_C": "down",
	"subject_choice_D": "end",
	"subject_answer": "B",
	"analysis": "如果一个类被final修饰符修饰说明这个类不可能有子类，被定义为final的类通常是一些有固定作用，用来完成某种标准功能的类。"
}, {
	"subject_title": "数据的存储结构是指（　　）。",
	"subject_choice_A": "存储在外存中的数据",
	"subject_choice_B": "数据所占的存储空间量",
	"subject_choice_C": "数据在计算机中的顺序存储方式",
	"subject_choice_D": "数据的逻辑结构在计算机中的表示",
	"subject_answer": "D",
	"analysis": "数据的存储结构是指数据结构(数据的逻辑结构)在计算机中的表示，又称物理结构。数据的存储结构主要有两种：顺序存储结构和链式存储结构。"
}, {
	"subject_title": "Object类中的方法public int hashCode[]，在其子类中覆盖该方法时，其方法修饰符可以是（　　）。",
	"subject_choice_A": "protected",
	"subject_choice_B": "public",
	"subject_choice_C": "private",
	"subject_choice_D": "缺省",
	"subject_answer": "B",
	"analysis": "所有的类都是Object的子类，如果要覆盖Object的equals方法则必须覆盖hasCode方法，覆盖时的属性是public。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "有一个以上根结点的数据结构不一定是非线性结构",
	"subject_choice_B": "只有一个根结点的数据结构不一定是线性结构",
	"subject_choice_C": "循环链表是非线性结构",
	"subject_choice_D": "双向链表是非线性结构",
	"subject_answer": "D",
	"analysis": "线性表的特点是：在数据元素的非空有限集合中；存在唯一的一个被称为“第一个”的数据元素；存在唯一一个被称为“最后一个”的数据元素；除第一个以外，集合中的每个数据元素均只有一个后继；除最后一个以外，集合中的每个数据元素均只有一个后继。因此，双向表是非线性结构。"
}, {
	"subject_title": "用于设置组件大小的方法是（　　）。",
	"subject_choice_A": "paint()",
	"subject_choice_B": "setSize()",
	"subject_choice_C": "getSize()",
	"subject_choice_D": "repaint()",
	"subject_answer": "B",
	"analysis": "在构件类的方法中，paint()方法是绘制构件，setSize()方法是设置组件大小，getSize()方法是获得组件大小，repaint()方法是重新绘制构件。"
}, {
	"subject_title": "破坏死锁的4个必要条件之一就可以预防死锁。假如规定一个进程在请求新资源之前首先释放已占有的资源则是破坏了（　　）条件。",
	"subject_choice_A": "互斥使用",
	"subject_choice_B": "部分分配",
	"subject_choice_C": "不可剥夺",
	"subject_choice_D": "环路等待",
	"subject_answer": "B",
	"analysis": "若一个进程请求新资源之前首先释放已占有的资源，这破坏了部分分配条件。"
}, {
	"subject_title": "软件详细设计产生的图如下。该图是（　　）。\n　\n　",
	"subject_choice_A": "N-S图",
	"subject_choice_B": "PAD图",
	"subject_choice_C": "程序流程图",
	"subject_choice_D": "E-R图",
	"subject_answer": "C",
	"analysis": "N-S图(也称为盒图或CHAPIN图)和PAD(问题分析图)及PFD(程序流程图)是详细设计阶段的常用工具，E-R图即实体一联系图是数据库设计的常用工具。从题中图可以看出该图属于程序流程图。"
}, {
	"subject_title": "下列选项中，是软件调试技术的是（　　）。",
	"subject_choice_A": "错误推断",
	"subject_choice_B": "集成测试",
	"subject_choice_C": "回溯法",
	"subject_choice_D": "边界值分析",
	"subject_answer": "C",
	"analysis": "软件调试技术包括强行排错法、回溯法和原因排除法。边界值分析、错误推断都是黑盒测试的方法。"
}, {
	"subject_title": "下列关于JDK目录结构的说法，错误的是（　　）。",
	"subject_choice_A": "bin目录下有许多工具",
	"subject_choice_B": "demo目录下有各种演示例子",
	"subject_choice_C": "include目录下都是库文件",
	"subject_choice_D": "jre目录是Java程序运行环境的根目录",
	"subject_answer": "C",
	"analysis": "本题考查JDK目录结构。bin目录下有编译器、解释器和各种工具，如服务器工具、IDLpackage工具和jdb等。jre目录是Java程序运行环境的根目录，它下面有bin子目录，包括平台所用工具和库的可执行文件和DLL文件；lib子目录包括java运行环境的代码库。lib目录下都是库文件。demo目录下有各种演示例子。include目录下是Win32子目录，都是本地方法文件，选项C错误。"
}, {
	"subject_title": "下列Java组件中，不属于容器的是（　　）。",
	"subject_choice_A": "Panel",
	"subject_choice_B": "Window",
	"subject_choice_C": "Frame",
	"subject_choice_D": "Label",
	"subject_answer": "D",
	"analysis": "本题考查对Java组件中容器的基本知识的理解。选项A错误，Panel类派生自容器类Container，属于容器的一种；选项B错误。Window类也派生自容器类Container，也属于容器的一种；选项C错误，Frame类派生自Window类，也是一种容器；选项D正确，Label组件是标签组件，不属于容器。故本题答案选项是D。"
}, {
	"subject_title": "设R是一个2元关系，S是一个3元关系，则下列运 算中正确的是（　　）。",
	"subject_choice_A": "R-S",
	"subject_choice_B": "R×S",
	"subject_choice_C": "RnS",
	"subject_choice_D": "RUS",
	"subject_answer": "B",
	"analysis": "关系的交(n)、并(U)和差(一)运算要求两个关系是同元的，显然作为二元的R和三元S只能做笛卡儿积运算。"
}, {
	"subject_title": "Java语言使用的字符码集是（　　）。",
	"subject_choice_A": "ASCII",
	"subject_choice_B": "BCD",
	"subject_choice_C": "DCB",
	"subject_choice_D": "Unicode",
	"subject_answer": "D",
	"analysis": "Java语言使用的是Unicode字符集。而ASCII是国际上使用最广泛的字符编码；BCD是一种数字压缩存储编码方法。"
}, {
	"subject_title": "下列为窗口事件的是（　　）。",
	"subject_choice_A": "MouseEvent",
	"subject_choice_B": "WindowEvent",
	"subject_choice_C": "ActionEvent",
	"subject_choice_D": "KeyEvent",
	"subject_answer": "B",
	"analysis": "MouseEvent是鼠标事件，ActionEvent是组件事件，KeyEvent是键盘事件。"
}, {
	"subject_title": "当一个应用程序的所有非守护线程终止运行时，但仍然有守护线程在运行，应用程序将（　　）。",
	"subject_choice_A": "运行",
	"subject_choice_B": "阻塞",
	"subject_choice_C": "终止",
	"subject_choice_D": "休眠",
	"subject_answer": "C",
	"analysis": "本题考查线程的机制。守护线程是一类特殊的线程．它和普通线程的区别在于它并不是应用程序的核心部分，当一个应用程序的所有非守护线程终止运行时，即使仍然有守护线程在运行，应用程序也将终止；反之，只要有一个非守护线程在运行，应用程序就不会终止。守护线程一般被用于在后台为其他线程提供服务。可以通过调用方法isDaemon()来判断一个线程是否是守护线程，也可以调用方法setDaemon()来将一个线程设为守护线程。"
}, {
	"subject_title": "每个Java小应用程序必须定义为（　　）。",
	"subject_choice_A": "Applet类或JApplet类的子类",
	"subject_choice_B": "JFrame类的子类",
	"subject_choice_C": "Frame的子类",
	"subject_choice_D": "Window的子类",
	"subject_answer": "A",
	"analysis": "本题考查Applet的基本知识。Applel类定义了小应用程序(Applet)与其运行环境之间的一个接口；JApplet是Applet类的扩展，它继承了Applet的方法和执行机制，同时也增加了对Swing构件的支持。每个Jaw小应用程序都必须是Applet类或JApplet类的子类。因此，本题的正确答案是A。"
}, {
	"subject_title": "软件测试目的是（　　）。",
	"subject_choice_A": "评估软件可靠性",
	"subject_choice_B": "发现并改正程序中的错误",
	"subject_choice_C": "改正程序中的错误",
	"subject_choice_D": "发现程序中的错误",
	"subject_answer": "D",
	"analysis": "软件测试的目的主要是在于发现软件错误，希望在软件开发生命周期内尽可能早地发现尽可能多的bug。"
}, {
	"subject_title": "类变量必须带有的修饰符是（　　）。",
	"subject_choice_A": "static",
	"subject_choice_B": "final",
	"subject_choice_C": "public",
	"subject_choice_D": "volatile",
	"subject_answer": "A",
	"analysis": "类变量用static修饰。"
}, {
	"subject_title": "下述关于数据库系统的叙述中，正确的是（　　）。",
	"subject_choice_A": "数据库系统减少了数据冗余",
	"subject_choice_B": "数据库系统避免了一切冗余",
	"subject_choice_C": "数据库系统中数据的一致性是指数据类型一致",
	"subject_choice_D": "数据库系统比文件系统能管理更多的数据",
	"subject_answer": "A",
	"analysis": "数据库系统会减少数据冗余，但不可能避免所有冗余。"
}, {
	"subject_title": "下列程序的功能是将一个整数数组写入二进制文件，在程序的下画线处应填入的选项是（　　）。\nimport java．io．*；\npublic class XieShuzu{\npublic static void main(String[]a){\nint[]myArray=(10，20，30，40)；\ntry{\nDataOutputStream dos=\nnew DataOutputStream(new\nFileOutput Stream(\"ints．dat\"))；\nfor(int i=0；i<MYARRAY．LENGTH；I++)\ndos． (myArray[i])；\ndos．close()；\nSystem．OUt．println(\"已经将整数数组写入二进\n制文件：ints．dat\")；\n}catch(IOException ioe)\n{System．OUt．println(\"IO Exeepr_on\")；)\n}\n}",
	"subject_choice_A": "writeArray",
	"subject_choice_B": "writeByte",
	"subject_choice_C": "writeInt",
	"subject_choice_D": "writeDouble",
	"subject_answer": "C",
	"analysis": "向流中写入整数数组，用writeInt方法。"
}, {
	"subject_title": "当一个Applet被下载到本地环境时，不发生的操作是（　　）。",
	"subject_choice_A": "产生一个Applet主类的实例",
	"subject_choice_B": "对Applet自身进行初始化",
	"subject_choice_C": "启动Applet运行",
	"subject_choice_D": "Applet并不显示出来",
	"subject_answer": "D",
	"analysis": "本题考查Applet的加载。当一个Applet下载到本地系统时，将发生以下操作：产生一个Applet主类的实例；对Applet自身进行初始化；启动Applet运行，将Applet完全显示出来。由此可见，选项D说法符合题意。"
}, {
	"subject_title": "数据独立性是数据库技术的重要特点之一。所谓数据独立性是指（　　）。",
	"subject_choice_A": "数据与程序独立存放",
	"subject_choice_B": "不同的数据被存放在不同的文件中",
	"subject_choice_C": "不同的数据只能被对应的应用程序所使用",
	"subject_choice_D": "以上三种说法都不对",
	"subject_answer": "D",
	"analysis": "数据独立性是数据库系统的一个最重要的目标之一，它使数据能独立于应用程序。数据独立性包括数据的物理独立性和逻辑独立性。物理独立性是指用户的应用程序与存储在磁盘上的数据库中数据是相互独立的。即数据在磁盘上怎样存储由DBMS管理，用户程序不需要了解，应用程序要处理的只是数据的逻辑结构，这样当数据的物理存储改变了，应用程序不用改变。逻辑独立性是指用户的应用程序与数据库的逻辑结构是相互独立的，即当数据的逻辑结构改变时，用户程序也可以不变。"
}, {
	"subject_title": "使新创建的线程参与运行调度的方法是（　　）。",
	"subject_choice_A": "run()",
	"subject_choice_B": "start()",
	"subject_choice_C": "init()",
	"subject_choice_D": "resume()",
	"subject_answer": "B",
	"analysis": "start()方法使线程参与运行调度。"
}, {
	"subject_title": "在创建线程时可以显式地指定线程组，此时可供选择的线程构造方法有（　　）种。",
	"subject_choice_A": "1",
	"subject_choice_B": "2",
	"subject_choice_C": "3",
	"subject_choice_D": "4",
	"subject_answer": "C",
	"analysis": "线程组是由java．lang包中的ThreadGroup类实现的。在创建线程时可以显式地指定线程组，此时需要从如下三种线程构造方法中选择一种：public Thread(ThreadGroup group，Runnable target)； public Thread(ThreadGroup group，String name)； public Thread(ThreadGroup group，Runnable target，String name)。"
}, {
	"subject_title": "JDK中，用（　　）命令对其源文件进行编译，生成字节码文件。",
	"subject_choice_A": "java．exe",
	"subject_choice_B": "javac．exe",
	"subject_choice_C": "javadoc．exe",
	"subject_choice_D": "javap．exe",
	"subject_answer": "B",
	"analysis": "本题考查JDK实用工具的使用。选项A错误，java．exe是Java语言解释器，直接从类文件执行Java应用程序字节代码，可接受class文件并启动Java虚拟机执行；选项B正确，javac．exe是Java语言编译器，将Java源代码转换成字节码；选项C错误，javadoc．exe是根据Java源代码及说明语句生成HTML，文档；选项D错误，javap．exe是反汇编器，显示编译类文件中的可访问功能和数据，同时显示字节代码含义。"
}, {
	"subject_title": "设A为已定义的类名，则下列声明A类的对象a的语句中正确的是（　　）。",
	"subject_choice_A": "public A a=new A()",
	"subject_choice_B": "public A a=A()",
	"subject_choice_C": "A a=new class()；",
	"subject_choice_D": "a A；",
	"subject_answer": "A",
	"analysis": "对象的生成包括声明、实例化和初始化3个方面的内容，一般格式是先定义一个对象变量，再用关键字new生成一个对象，并为该对象变量赋值。"
}, {
	"subject_title": "下列各项说法中错误的是（　　）。",
	"subject_choice_A": "共享数据的所有访问都必须使用synchronized加锁",
	"subject_choice_B": "共享数据的访问不一定全部使用synchronized加锁",
	"subject_choice_C": "所有的对共享数据的访问都是临界区",
	"subject_choice_D": "临界区必须使用synchronized加锁",
	"subject_answer": "B",
	"analysis": "共享数据的所有访问一定要作为临界区，用synchronized标识，这样保证了所有的对共享数据的操作都通过对象锁的机制进行控制。"
}, {
	"subject_title": "设某循环队列的容量为50，如果头指针front=45(指向队头元素的前一位置)，尾指针rear=10(指向队尾元素)，则该循环队列中共有元素个数为（　　）。",
	"subject_choice_A": "5",
	"subject_choice_B": "15",
	"subject_choice_C": "35",
	"subject_choice_D": "40",
	"subject_answer": "B",
	"analysis": "队列个数=rear-front+容量。"
}, {
	"subject_title": "下面程序段的输出结果为（　　）。 \npackage test； \npublic class ClassA\n{\nint x=20： \nstatic int y=6； \npublic static void main(String args[])\n{\nClassB b=new ClassB()；\ngo(10)； \nSystem．out．println(\"x=\"+b．x)； \n}\n}\nclass ClassB\n{\nint X； \nvoid go(int y)\n{\nClassA a=new ClassA()； \nx=a．Y ； \n}\n}",
	"subject_choice_A": "x=10",
	"subject_choice_B": "x=20",
	"subject_choice_C": "x=6",
	"subject_choice_D": "编译不通过",
	"subject_answer": "C",
	"analysis": "本题考查在Java中静态变量(类变量)的用法。在题目程序段中生成了一个staticint y=6类变量，在ClassA中调用的b．go(10)，只不过是在ClassB中的一个局部变量，通过调用ClassB中的90方法可以生成一个ClassA对象，并给这个新生成的对象赋以ClassA中的类变量Y的值。从main()方法作为入口执行程序，首先生成一个ClassB的对象，然后b．go(10)会调用ClassA，会给X和Y赋值，X=a．Y后，X值为6，再返回去执行System．out．println(&quot;x=&quot;+b．x)语句，输出为x=6，可见，正确答案为选项C。"
}, {
	"subject_title": "下列关于线程和进程的说法正确的是（　　）。",
	"subject_choice_A": "进程结构的所有成分都在用户空间内",
	"subject_choice_B": "用户程序能够直接访问进程涉及的数据",
	"subject_choice_C": "线程是内核级的实体",
	"subject_choice_D": "线程结构驻留在用户空间中",
	"subject_answer": "D",
	"analysis": "本题考查线程和进程的概念。线程与进程在概念上是相关的，进程由代码、数据、内核状态和一组寄存器组成，而线程是由表示程序运行状态的寄存器，如程序计数器、栈指针以及堆栈组成，线程不包括进程地址空间中的代码和数据，线程是计算过程在某一时刻的状态。进程是一个内核级的实体，进程结构的所有成分都在内核空间中，一个用户程序不能直接访问这些数据。线程是一个用户级的实体，线程结构驻留在用户空间中，能够被普通的用户级方法直接访问。"
}, {
	"subject_title": "阅读下列程序 \npublic class VariableUse\n{\npublic static void main(String[]args)\n{\nint a； if(a= =8)\n{\nint b=9； System．OUt．println(\"a=\"+a)： \nSystem．out．println(\"b=\"+b)； \n}\nSystem．Out．println(\"a=\"+a)： \nSystem．OUt．println(\"b=\"+b)； \n}\n}\n该程序在编译时的结果是（　　）。",
	"subject_choice_A": "变量a未赋值",
	"subject_choice_B": "第二个System．out．println(\"b=\"+b)语句中，变量b作用域有错",
	"subject_choice_C": "第二个System．out．println(\"a=\"+a)语句中，变量a作用域有错",
	"subject_choice_D": "第一个System．out．println(\"b=\"+b)语句中，变量b作用域有错",
	"subject_answer": "B",
	"analysis": "局部变量b是在if(a==8){}里定义的，作用域也只在这个if语句范围内，第二个System．out．println(&quot;b=&quot;+b)语句中，变量b超出了作用域。"
}, {
	"subject_title": "AWT中用来表示对话框的类是（　　）。",
	"subject_choice_A": "Font",
	"subject_choice_B": "Color",
	"subject_choice_C": "Panel",
	"subject_choice_D": "Dialog",
	"subject_answer": "D",
	"analysis": "Font和Color是构件的字体和外观颜色，Panel是面板容器，Dialog是对话框的类。"
}, {
	"subject_title": "下列变量定义中，不合法的是（　　）。",
	"subject_choice_A": "int SX；",
	"subject_choice_B": "int_123；",
	"subject_choice_C": "int Summer 2010_gross_sale；",
	"subject_choice_D": "int#dim；",
	"subject_answer": "D",
	"analysis": "Java中标识符的命名规则为：①区分大小写，例如a和A是两个变量；②标识符由字母、下画线、美元符号和数字组成，并且第一个字符不能是数字。"
}, {
	"subject_title": "Class类的对象由（　　）自动生成，隐藏在．class文件中，它在运行时为用户提供信息。",
	"subject_choice_A": "Java编译器",
	"subject_choice_B": "Java解释器",
	"subject_choice_C": "Java new关键字",
	"subject_choice_D": "Java类分解器",
	"subject_answer": "A",
	"analysis": "class文件是由编译器生成的。"
}, {
	"subject_title": "将E—R图转换为关系模式时，实体和联系都可以表示为（　　）。",
	"subject_choice_A": "属性",
	"subject_choice_B": "键",
	"subject_choice_C": "关系",
	"subject_choice_D": "域",
	"subject_answer": "C",
	"analysis": "将E-R图转换为关系模式时，实体和联系都可以表示为关系。"
}, {
	"subject_title": "软件设计中模块划分应遵循的准则是（　　）。",
	"subject_choice_A": "低内聚低耦合",
	"subject_choice_B": "高内聚低耦合",
	"subject_choice_C": "低内聚高耦合",
	"subject_choice_D": "高内聚高耦合",
	"subject_answer": "B",
	"analysis": "耦合性和内聚性是模块独立性的两个定性标准，软件设计应该遵循高内聚低耦合的准则。"
}, {
	"subject_title": "在学生管理的关系数据库中，存取一个学生信息的数据单位是（　　）。",
	"subject_choice_A": "文件",
	"subject_choice_B": "数据库",
	"subject_choice_C": "字段",
	"subject_choice_D": "记录",
	"subject_answer": "D",
	"analysis": "一个数据库由一个文件或文件集合组成。这些文件中的信息可分解成一个个记录。"
}, {
	"subject_title": "下列代码的执行结果是（　　）。 \npublic  class Test\n{\npublic  static void main(String args[])\n{\nSystem．out．println(5／2)； \nSystem．OUt．println(100％3．O)\n}\n}",
	"subject_choice_A": "2和1",
	"subject_choice_B": "2和1．0",
	"subject_choice_C": "2．5和1",
	"subject_choice_D": "2．5和1．0",
	"subject_answer": "B",
	"analysis": "由于5和2都是int型，所以语句System．out．println(5／2)的输出为2。由于操作数3．0为double型(Java语言中浮点数的默认值为double型)，所以结果为double型，即1．0。"
}, {
	"subject_title": "在程序的下画线处应填入的选项是（　　）。 public class Test<u>                </u>{public static void main(String args[]){Test t=new Test()； Thread tt=new Thread(t)； tt．start()； }public void run(){for(int i=0；i&lt;5；i++){System．OUt．println(\"i=\"+i)； }}}",
	"subject_choice_A": "implements Runnable",
	"subject_choice_B": "extends Thread",
	"subject_choice_C": "implements Thread",
	"subject_choice_D": "extends Runnable",
	"subject_answer": "A",
	"analysis": "Test类实现了Runnable接口。"
}, {
	"subject_title": "下列关于Java多线程并发控制机制的叙述中，错误的是（　　）。",
	"subject_choice_A": "Java中对共享数据操作的并发控制是采用加锁技术",
	"subject_choice_B": "线程之间的交互，提倡采用suspend()／resume()方法",
	"subject_choice_C": "共享数据的访问权限都必须定义为private",
	"subject_choice_D": "Java中没有提供检测与避免死锁的专门机制，但程序员可以采用某些策略防止死锁的发生",
	"subject_answer": "B",
	"analysis": "本题考查多线程的并发控制机制。Java中对共享数据操作的并发控制采用传统的加锁技术，也就是给对象加锁，选项A说法正确。线程之间的交互，提倡采用wait()和notify()方法，这两个方法是java．lang．object类的方法，是实现线程通信的两个方法，不提倡使用suspend()和resume()方法，它们容易造成死锁，所以选项B说法错误。共享数据的访问权限都必须定义为private，不能为public或其他，选项C说法正确。Java中没有提供检测与避免死锁的专门机制，因此完全由程序进行控制，但程序员可以采用某些策略防止死锁的发生，选项D说法正确。"
}, {
	"subject_title": "为了提高软件模块的独立性，模块之间最好是（　　）。",
	"subject_choice_A": "控制耦合",
	"subject_choice_B": "公共耦合",
	"subject_choice_C": "内容耦合",
	"subject_choice_D": "高内聚低耦合",
	"subject_answer": "D",
	"analysis": "耦合性与内聚性是模块独立性的两个定性标准，一般的程序设计都会尽量做到高内聚、低耦合，有利于提高模块的独立性。"
}, {
	"subject_title": "数据库管理系统是（　　）。",
	"subject_choice_A": "操作系统的一部分",
	"subject_choice_B": "在操作系统支持下的系统软件",
	"subject_choice_C": "一种编译系统",
	"subject_choice_D": "一种操作系统",
	"subject_answer": "B",
	"analysis": "数据库系统属于系统软件的范畴。"
}, {
	"subject_title": "下列叙述中，错误的是（　　）。",
	"subject_choice_A": "Applet的默认布局管理器是FlowLayout",
	"subject_choice_B": "JApplet中增加构件是加到JApplet的内容面板上，不是直接加到JApplet中",
	"subject_choice_C": "JApplet的内容面板的默认布局管理器是Border-Layout",
	"subject_choice_D": "JApplet的内容面板的默认布局管理器是FlowLay-out",
	"subject_answer": "D",
	"analysis": "FlowLayout布局管理器是Panel类和Applet类默认的布局管理器。向JApplet中增加构件，是把构件添加到Japplet的内容面板中，而不是直接添加到JApplet中。JApplet的内容面板的默认布局管理器是BorderLayout，而Applet默认的布局管理器是FlowLayout。"
}, {
	"subject_title": "以下（　　）命令能为远程对象生成stub和skeleton。",
	"subject_choice_A": "rmiregistry",
	"subject_choice_B": "serialver",
	"subject_choice_C": "rmic",
	"subject_choice_D": "rmid",
	"subject_answer": "C",
	"analysis": "本题考查J2SDK的RMl命令。rmiregistry命令是在当前主机的指定端口上启动远程对象注册服务程序；serialver命令是返回serialVersionUID的值；rmic命令为远程对象生成stub和skeleton；rmid命令可以激活系统守候进程，以便能够在Java虚拟机上注册和激活对象。"
}, {
	"subject_title": "如果线程调用下列方法，不能保证使该线程停止运行的是（　　）。",
	"subject_choice_A": "sleep()",
	"subject_choice_B": "stop()",
	"subject_choice_C": "yield()",
	"subject_choice_D": "wait()",
	"subject_answer": "C",
	"analysis": "线程的方法中sleep()方法的作用是使比当前线程优先级低的线程运行。该方法使一个线程暂停运行一段固定时间。在休眠时间内，线程将不运行，低优先级的线程将有机会运行。yield()方法为只让给同等优先级的线程运行。如果没有同等优先级的线程是可运行状态，yield()方法将什么也不做，即线程将继续运行。stop()方法是强行终止线程。wait()方法是线程间交互的方法，是使一个线程停止运行，进入等待状态。"
}, {
	"subject_title": "Thread类的方法中用于修改线程名字的方法是（　　）。",
	"subject_choice_A": "setName()",
	"subject_choice_B": "reviseName()",
	"subject_choice_C": "getName()",
	"subject_choice_D": "checkAccess()",
	"subject_answer": "A",
	"analysis": "Thread类的其他方法有setName()、getName()、activeCount()和setDaemon()等。其中，用于修改线程名字的方法是setName()。"
}, {
	"subject_title": "下列叙述中，错误的是（　　）。",
	"subject_choice_A": "父类不能替代子类",
	"subject_choice_B": "子类能够替代父类",
	"subject_choice_C": "子类继承父类",
	"subject_choice_D": "父类包含子类",
	"subject_answer": "D",
	"analysis": "本题考查继承的概念。继承性是面向对象方法的一个重要基本特征，它使代码可重用，可降低程序的复杂性。对一个类的继承也就是构建了一个子类，子类继承了父类的方法和状态，同时还可以向新类中增添新的方法和状态。重点掌握两点：子类方法的访问权限比父类的访问权限高，因此父类不能替代子类，但子类能够代替父类，选项A和选项B说法正确；子类方法不能产生比父类更多的异常。选项D为正确答案。"
}, {
	"subject_title": "Applet的默认布局管理器是（　　）。",
	"subject_choice_A": "BorderLayout",
	"subject_choice_B": "FlowLayout",
	"subject_choice_C": "GridLayout",
	"subject_choice_D": "PanelLayout",
	"subject_answer": "B",
	"analysis": "Applet是一个面板容器，它默认使用Flow布局管理器，所以可以在Applet中设置并操作AWT构件。"
}, {
	"subject_title": "下列选项中不属于结构化程序设计原则的是（　　）。",
	"subject_choice_A": "可封装",
	"subject_choice_B": "自顶向下",
	"subject_choice_C": "模块化",
	"subject_choice_D": "逐步求精",
	"subject_answer": "A",
	"analysis": "结构化程序设计的主要原则概括为自顶向下，逐步求精，限制使用GOT0语句。"
}, {
	"subject_title": "下列数据结构中，能用二分法进行查找的是（　　）。",
	"subject_choice_A": "顺序存储的有序线性表",
	"subject_choice_B": "线性链表",
	"subject_choice_C": "二叉链表",
	"subject_choice_D": "有序线性链表",
	"subject_answer": "A",
	"analysis": "二分法查找只适用于顺序存储的有序线性表，对于顺序存储的非有序线性表和线性链表，都只能采用顺序查找。"
}, {
	"subject_title": "下列关于项目中“移出”文件的说法，正确的是（　　）。",
	"subject_choice_A": "被移出的文件将直接从磁盘中删除",
	"subject_choice_B": "被移出的文件将不能被任何项目添加",
	"subject_choice_C": "被移出的文件只是将文件移出项目，但文件保留在磁盘中",
	"subject_choice_D": "被移出的文件，以后不能再次添加到原项目中，但可以添加到其他项目中",
	"subject_answer": "C",
	"analysis": "在数据库中移除不代表删除，从项目中移除是指文件只是从项目中移除，但文件还保存在磁盘中，如果需要仍然可再次添加到此项目中。当在项目中删除文件后，文件才能被添加到其他的项目中。所以答案选择C。"
}, {
	"subject_title": "下列选项中，与成员变量共同构成一个类的是（　　）。",
	"subject_choice_A": "关键字",
	"subject_choice_B": "方法",
	"subject_choice_C": "运算符",
	"subject_choice_D": "表达式",
	"subject_answer": "B",
	"analysis": "在类体中定义的两种成员，数据成员和成员函数，其中数据成员就是成员变量，而成员函数就是通常说的方法。"
}, {
	"subject_title": "一个工作人员可以使用多台计算机，而一台计算机可被多个人使用，则实体工作人员与实体计算机之间的联系是（　　）。",
	"subject_choice_A": "一对一",
	"subject_choice_B": "一对多",
	"subject_choice_C": "多对多",
	"subject_choice_D": "多对一",
	"subject_answer": "C",
	"analysis": "一个工作人员对应多台计算机，一台计算机对应多个工作人员，则实体工作人员与实体计算机之间的联系是多对多。"
}, {
	"subject_title": "下列变量名的定义中，符合Java命名约定的是（　　）。",
	"subject_choice_A": "fieldname",
	"subject_choice_B": "super",
	"subject_choice_C": "Intnum",
	"subject_choice_D": "$number",
	"subject_answer": "A",
	"analysis": "Java命名约定全部小写，不得使用关键字，只有A符合。"
}, {
	"subject_title": "使得线程放弃当前分得的CPU时间，但不使线程阻塞，即线程仍处于可执行状态，随时可能再次分得CPU时间的方法是（　　）。",
	"subject_choice_A": "time()",
	"subject_choice_B": "yield()",
	"subject_choice_C": "load()",
	"subject_choice_D": "min()",
	"subject_answer": "B",
	"analysis": "本题考查线程阻塞的概念。yield()方法使得线程放弃当前分得的CPU时间，但是不使线程阻塞，印线程仍处于可执行状态，随时可能再次分得CPU时间。调用yield()的效果等价于调度程序认为该线程已执行了足够的时间从而转到另一个线程。"
}, {
	"subject_title": "对建立良好的程序设计风格，下列描述中正确的是（　　）。",
	"subject_choice_A": "程序应该简单、清晰、可读性好",
	"subject_choice_B": "符号名的命名只需要符合语法",
	"subject_choice_C": "充分考虑程序的执行效率",
	"subject_choice_D": "程序的注释可有可无",
	"subject_answer": "A",
	"analysis": "”清晰第一，效率第二”，在考虑到程序的执行效率的同时，一定要保证程序清晰、可读；对符号名的命名，除了要符合语法要求外，还要具有一定的含义；程序的注释可以帮助程序员理解程序，不是可有可无的。"
}, {
	"subject_title": "在匹配器(Matcher)类中，用于寻找下一个模式匹配串的方法是（　　）。",
	"subject_choice_A": "static boolean matches()",
	"subject_choice_B": "boolean matcher．find()",
	"subject_choice_C": "int matcher．start()",
	"subject_choice_D": "int matcher．end()",
	"subject_answer": "A",
	"analysis": "本题考查考生对Java中的匹配器(Mateher)类的理解。Matcher类用于将一个输入字符串input和模式串pattern相比较。Booleanmateher．find()方法用于寻找下一个模式匹配串；int matcher．start()方法用于返回匹配串的一个起始索引整数值；int matcher．end()方法用于返回匹配串的一个终止索引整数值。而用于输入字符串与模式串比较的方法是static boolean matches()，选项A正确。"
}, {
	"subject_title": "在Applet生命周期中，下面方法中，在装载Applet时被调用的是（　　）。",
	"subject_choice_A": "stop()",
	"subject_choice_B": "init()",
	"subject_choice_C": "start()",
	"subject_choice_D": "destroy()",
	"subject_answer": "B",
	"analysis": "在JavaApplet的生命周期中，共有4种状态和4个方法：init()、start()、stop()和destroy()。在Applet装载时，由浏览器或appletviewer调用init()方法，通知该Applet已被加载到浏览器中，使Applet执行一些基本初始化。"
}, {
	"subject_title": "下列工具中为需求分析常用工具的是（　　）。",
	"subject_choice_A": "PAD",
	"subject_choice_B": "PFD",
	"subject_choice_C": "N-S",
	"subject_choice_D": "DFD",
	"subject_answer": "D",
	"analysis": "需求分析常用工具有数据流图(DFD)、数据字典(DD)、判定树和判定表。问题分析图(PAD)、程序流程图(PFD)、金式图(N-S)都是详细设计的常用工具，不是需求分析的工具。"
}, {
	"subject_title": "下列选项中不属于结构化程序设计方法的是（　　）。",
	"subject_choice_A": "自顶向下",
	"subject_choice_B": "逐步求精",
	"subject_choice_C": "模块化",
	"subject_choice_D": "可复用",
	"subject_answer": "D",
	"analysis": "结构化程序设计的主要原则概括为自顶向下，逐步求精，模块化。"
}, {
	"subject_title": "数据库设计中，用E-R图来描述信息结构但不涉及信息在计算机中的表示，它属于数据库设计的（　　）。",
	"subject_choice_A": "需求分析阶段",
	"subject_choice_B": "逻辑设计阶段",
	"subject_choice_C": "概念设计阶段",
	"subject_choice_D": "物理设计阶段",
	"subject_answer": "C",
	"analysis": "E-R(Entity-Relationship)图为实体一联系图，提供了表示实体型、属性和联系的方法，用来描述现实世界的概念模型。"
}, {
	"subject_title": "提供showDocument()方法，使Applet能够请求浏览器访问特定URL的类是（　　）。",
	"subject_choice_A": "Applet",
	"subject_choice_B": "AppletContext",
	"subject_choice_C": "JApplet",
	"subject_choice_D": "URL",
	"subject_answer": "B",
	"analysis": "AppletContext类是一个接口类，Applet通过AppletContext接口与环境进行通信。可以利用这个类从Applet环境获取信息，而这个环境一般是指浏览器。Applet使用AppletContext类的showDocument()方法可以通知浏览器在指定窗口中显示另一个URL的内容。因此，本题的正确答案是B。"
}, {
	"subject_title": "下列变量定义中，不合法的是（　　）。",
	"subject_choice_A": "int SX；",
	"subject_choice_B": "int_123；",
	"subject_choice_C": "int Summer 2010_gross_sale；",
	"subject_choice_D": "int#dim；",
	"subject_answer": "D",
	"analysis": "Java中标识符的命名规则为：①区分大小写，例如a和A是两个变量；②标识符由字母、下画线、美元符号和数字组成，并且第一个字符不能是数字。"
}, {
	"subject_title": "有三个关系R、S和T如下：\n　\n　\n则由关系R和S得到关系T的操作是（　　）。",
	"subject_choice_A": "自然连接",
	"subject_choice_B": "交",
	"subject_choice_C": "除",
	"subject_choice_D": "并",
	"subject_answer": "C",
	"analysis": "S中的关系全部出现在R中，只有做除法操作才会出现关系T。"
}, {
	"subject_title": "Java程序与数据库的连接机制是（　　）。",
	"subject_choice_A": "ODBC",
	"subject_choice_B": "JDBC",
	"subject_choice_C": "ODBCAPI",
	"subject_choice_D": "SQL／CLI",
	"subject_answer": "B",
	"analysis": "本题考查Java程序与数据库的连接。JDBC(JavaData Base Connectivity)是Java程序与数据库连接的一种机制。在Java虚拟机中有个特殊模块JDBC Driver Manager,既负责管理针对各种类型数据库软件的JDBC驱动程序，也负责和用户应用程序交互。"
}, {
	"subject_title": "程序流程图中的菱形框表示的是（　　）。",
	"subject_choice_A": "处理步骤",
	"subject_choice_B": "逻辑处理",
	"subject_choice_C": "物理处理",
	"subject_choice_D": "控制流向",
	"subject_answer": "B",
	"analysis": "程序流程图的主要元素：①方框：表示一个处理步骤；②菱形框：表示一个逻辑处理；③箭头：表示控制流向。"
}, {
	"subject_title": "要表示表格的数据，需要继承类（　　）。",
	"subject_choice_A": "AbstraceTableModel",
	"subject_choice_B": "TableModel",
	"subject_choice_C": "JTable",
	"subject_choice_D": "TableModelable",
	"subject_answer": "A",
	"analysis": "表格是Swing新增加的构件，主要功能是把数据以二维表格的形式显示出来。使用表格，依据M-V-C的思想，最好生成一个MyTableModel类型的对象来表示数据，这个类是从AbstractTableModel类继承来的。"
}, {
	"subject_title": "下面程序段的输出结果是（　　）。\npublic class Test{\npublic static void main(String args[]){\nint a，b；\nfor(a=1，b=1；a<=100；a++){\nif(b>=10)break；\nif(b％2= =1){\nb+=2：\ncontinue；\n}\n}\nSystem．OUt．println(a)；\n}\n}",
	"subject_choice_A": "5",
	"subject_choice_B": "6",
	"subject_choice_C": "7",
	"subject_choice_D": "101",
	"subject_answer": "B",
	"analysis": "本题考查for循环和if语句的嵌套以及break语句和continue语句的用法。第1个if语句的意义为：当b&gt;=10时退出for循环，第2个if语句的意义为：如果b％2=1，则b的值加2并退出本次循环。本程．序当b的值分别为l、3、5、7和9的时候执行5次循环，此时a=5，b=9，当执行第6次循环时，a的值为6，但b=11，所以退出循环，程序结束。"
}, {
	"subject_title": "下列方法中可以用来创建一个新线程的是（　　）。",
	"subject_choice_A": "实现java．lang．Runnable接口并重写start()方法",
	"subject_choice_B": "实现java．lang．Runnable接口并重写run()方法",
	"subject_choice_C": "继承java．lang．Thread类并重写run()方法",
	"subject_choice_D": "实现java．lang．Thread类并实现start()方法",
	"subject_answer": "C",
	"analysis": "本题考查考生对创建线程的使用。创建线程有两种方法：通过实现Runnable接口创建线程和通过继承Thread类创建线程。通过实现Runnable接口创建线程，当实现Runnable接口的类的对象用来创建线程以后，该线程的启动将使得对象的run()方法被调用。通过继承Thread类创建线程，可以通过继承Thread类，并重写其中的run()方法定义线程体，然后创建该子类的对象创建线程。线程创建是考试重点内容，请务必掌握。"
}, {
	"subject_title": "下列选项中属于字符串常量的是（　　）。",
	"subject_choice_A": "•abc•",
	"subject_choice_B": "\"abe\"",
	"subject_choice_C": "[abc]",
	"subject_choice_D": "(abc)",
	"subject_answer": "B",
	"analysis": "Java中字符串常量由双引号和其中间的字符所组成。"
}, {
	"subject_title": "软件工程的理论和技术性研究的内容主要包括软件开发技术和（　　）。",
	"subject_choice_A": "消除软件危机",
	"subject_choice_B": "软件工程管理",
	"subject_choice_C": "程序设计自动化",
	"subject_choice_D": "实现软件可重用",
	"subject_answer": "B",
	"analysis": "基于软件工程的目标，软件工程的理论和技术性研究的内容主要包括软件开发技术和软件工程管理。"
}, {
	"subject_title": "为使下列代码正常运行，应该在下画线处填入的选项是（　　）。\nint[]numbers=new int[n]；\nfor(int i=0；i<NUMBERS． ；i++)\nnumbers[i]=i+1：",
	"subject_choice_A": "size",
	"subject_choice_B": "length",
	"subject_choice_C": "dimension",
	"subject_choice_D": "measurement",
	"subject_answer": "B",
	"analysis": "length表示数组的长度。"
}, {
	"subject_title": "Java的反汇编命令是（　　）。",
	"subject_choice_A": "javap",
	"subject_choice_B": "javac",
	"subject_choice_C": "jdb",
	"subject_choice_D": "java",
	"subject_answer": "A",
	"analysis": "Javap命令是java反汇编命令，javac命令是java语言编译器，jdb是基于文本和命令行的调试工具，java命令是Java解释器。"
}, {
	"subject_title": "若变量a是String类型的数据，那么表达式(a+a)的类型是（　　）。",
	"subject_choice_A": "char",
	"subject_choice_B": "String",
	"subject_choice_C": "int",
	"subject_choice_D": "long",
	"subject_answer": "B",
	"analysis": "Java中允许两个String类型进行+运算，其结果仍旧是String类型。"
}, {
	"subject_title": "实现下列（　　）接口可以对TextField对象的事件进行监听和处理。",
	"subject_choice_A": "ActionListener",
	"subject_choice_B": "FocusListener",
	"subject_choice_C": "MouseMotionListener",
	"subject_choice_D": "WindowListener",
	"subject_answer": "A",
	"analysis": "文本框TextField可用于编辑单行文本，输入一个字符串，按&lt;Enter&gt;键就会激活一个文本框事件。对TextField对象的事件进行监听和处理可以实现接口ActionListener来进行．"
}, {
	"subject_title": "下列不属于表达式语句的是（　　）。",
	"subject_choice_A": "++i；",
	"subject_choice_B": "--j；",
	"subject_choice_C": "b#a；",
	"subject_choice_D": "b*=a；",
	"subject_answer": "C",
	"analysis": "前两项是自加减运算，最后一项是b=b*a。"
}, {
	"subject_title": "下列与数据元素有关的叙述中，不正确的是（　　）。",
	"subject_choice_A": "数据元素是数据的基本单位，即数据集合中的个体",
	"subject_choice_B": "数据元素是有独立含义的数据最小单位",
	"subject_choice_C": "数据元素又称为结点",
	"subject_choice_D": "数据元素又称为记录",
	"subject_answer": "B",
	"analysis": "数据元素是数据的基本单位，即数据集合中的个体。有些情况下也把数据元素称为结点、记录、表目等。一个数据元素可由一个或多个数据项组成，数据项是有独立含义的数据最小单位，其值能唯一确定一个数据元素的数据项。"
}, {
	"subject_title": "Java语青中，对当前对象的父类对象进行引用的关键字是（　　）。",
	"subject_choice_A": "case",
	"subject_choice_B": "super",
	"subject_choice_C": "char",
	"subject_choice_D": "break",
	"subject_answer": "B",
	"analysis": "当子类隐藏了父类的变量，并重写了父类方法后，又要使用父类变量或父类被重写的方法时，可以通过super来实现对父类变量的访问和对父类方法的调用。"
}, {
	"subject_title": "要串行化某些类的对象，这些类必须实现（　　）。",
	"subject_choice_A": "Serializable接口",
	"subject_choice_B": "java．i0．Exceptionlizable接口",
	"subject_choice_C": "java．i0．Datalnput接口",
	"subject_choice_D": "DataOutput接口",
	"subject_answer": "A",
	"analysis": "Java语言中一个类只有实现Serializable接口，它的对象才是可串行化的。"
}, {
	"subject_title": "下列可以获得构件前景色的方法是（　　）。",
	"subject_choice_A": "getsize()",
	"subject_choice_B": "getForeground()",
	"subject_choice_C": "getBaekground()",
	"subject_choice_D": "paint()",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "十进制数16的十六进制表示格式是（　　）。",
	"subject_choice_A": "0x10",
	"subject_choice_B": "0x16",
	"subject_choice_C": "0xA",
	"subject_choice_D": "016",
	"subject_answer": "A",
	"analysis": "本题考查Java语言中的进制换算。首先要清楚各种进制的表示方法。整型常量有3种书写格式：十进制整数，如156，-230，345；八进制整数，以0开头，如012表示十进制的l0；十六进制整数，以0x或OX开头，如0X123表示十进制数291。十进制数16相当于十六进制的10，所以选项A正确。"
}, {
	"subject_title": "对长度为n的线性表进行顺序查找，在最坏情况下需要比较的次数为（　　）。",
	"subject_choice_A": "125",
	"subject_choice_B": "n／2",
	"subject_choice_C": "n",
	"subject_choice_D": "n+1",
	"subject_answer": "C",
	"analysis": "对线性表进行顺序查找时，最坏情况下，要查找的元素是表的最后一个元素或查找失败，这两种情况都需要将这个元素与表中的所有元素进行比较，因此比较次数为n。"
}, {
	"subject_title": "要使下列程序能够正确运行，则横线处应填写的内容是（　　）。\nimport Java．awt．*；\nimport java．applet．*；\npublic class SayHi extends Applet{\npublic void (Graphics g){\n9.drawString(\"Hi!\"，20，20)；\n}\n}",
	"subject_choice_A": "int",
	"subject_choice_B": "start",
	"subject_choice_C": "paint",
	"subject_choice_D": "stop",
	"subject_answer": "C",
	"analysis": "Java中，继承applet类的子类需要实现以下方法：init()、start()、stop()、destroy()、paint(Graphicsg)方法。其中，paint(Graphics g)方法有一个参数g，是浏览器在运行Java Applet时产生的一个类Graphics的实例。"
}, {
	"subject_title": "数据库设计中反映用户对数据要求的模式是（　　）。",
	"subject_choice_A": "内模式",
	"subject_choice_B": "概念模式",
	"subject_choice_C": "外模式",
	"subject_choice_D": "设计模式",
	"subject_answer": "C",
	"analysis": "外模式，也称为用户模式。在一个数据库模式中，有N个外模式，每一个外模式对应一个用户。外模式保证数据的逻辑独立性。内模式属于物理模式，因此，一个数据库只有一个内模式；内模式规定了数据的存储方式、规定了数据操作的逻辑、规定了数据的完整性、规定了数据的安全性、规定了数据的存储性能。"
}, {
	"subject_title": "某二叉树共有60个叶子结点与50个度为1的结点，则该二叉树中的总结点数为（　　）。",
	"subject_choice_A": "148",
	"subject_choice_B": "169",
	"subject_choice_C": "182",
	"subject_choice_D": "198",
	"subject_answer": "B",
	"analysis": "本题考查二叉树的性质。叶子结点即度为0的结点，它总是比度为2的结点多一个，所以，具有60个叶子结点的二叉树有59个度为2的结点。总结点数等于个叶子结点加上59个度为2的结点再加上50个度为1的结点的和，共l69个结点。"
}, {
	"subject_title": "对下列二叉树进行中序遍历的结果是（　　）。\n　\n　",
	"subject_choice_A": "DBXEAYFZC",
	"subject_choice_B": "XYZDEFBCA",
	"subject_choice_C": "ZYXFEDCBA",
	"subject_choice_D": "YZCFAXEDB",
	"subject_answer": "A",
	"analysis": "中序遍历的方法是：先遍历左子树，然后访问根结点，最后遍历右子树；并且，在遍历左、右子树时，仍然先遍历左子树，然后访问根结点，最后遍历右子树。所以中序遍历的结果是DBXEAYFZC"
}, {
	"subject_title": "软件(程序)调试的任务是（　　）。",
	"subject_choice_A": "诊断和改正程序中的错误",
	"subject_choice_B": "尽可能多地发现程序中的错误",
	"subject_choice_C": "发现并改正程序中的所有错误",
	"subject_choice_D": "确定程序中错误的性质",
	"subject_answer": "A",
	"analysis": "调试的目的是发现错误或导致程序失效的错误原因，并修改程序以修正错误。调试是测试之后的活动。"
}, {
	"subject_title": "数据库管理系统中负责数据模式定义的语言是（　　）。",
	"subject_choice_A": "数据定义语言",
	"subject_choice_B": "数据管理语言",
	"subject_choice_C": "数据操纵语言",
	"subject_choice_D": "数据控制语言",
	"subject_answer": "A",
	"analysis": "数据模式是由数据定义语言(DataDeftnition Language，DDL)来描述、定义的，体现、反映了数据库系统的整体观。"
}, {
	"subject_title": "下列关于顺序存储结构的叙述中，错误的是（　　）。",
	"subject_choice_A": "存储密度大",
	"subject_choice_B": "某些非线性结构也可以采用顺序方法存储",
	"subject_choice_C": "结点中只有自身信息域，没有链接信息域",
	"subject_choice_D": "便于进行插入、删除等运算操作",
	"subject_answer": "D",
	"analysis": "顺序结构每个结点只包含自身的信息域，且逻辑上相邻的结点物理上也是相邻的。因此其存储密度大，但插入、删除运算操作不方便，需移动大量的结点。"
}, {
	"subject_title": "如果线程正处于阻塞状态，不能够使线程直接进入可运行状态的情况是（　　）。",
	"subject_choice_A": "sleep()方法的时间到",
	"subject_choice_B": "获得了对象的锁",
	"subject_choice_C": "线程在调用t．join()方法后，线程t结束",
	"subject_choice_D": "wait()方法结束",
	"subject_answer": "D",
	"analysis": "wait()会使线程放弃对象锁，进入等待此对象的等待锁定池。"
}, {
	"subject_title": "算法的空间复杂度是指（　　）。",
	"subject_choice_A": "算法在执行过程中所需要的计算机存储空间",
	"subject_choice_B": "算法所处理的数据量",
	"subject_choice_C": "算法程序中的语句或指令条数",
	"subject_choice_D": "算法在执行过程中所需要的临时工作单元数",
	"subject_answer": "A",
	"analysis": "一个算法的空间复杂度一般是指执行这个算法所需的存储空间。一个算法所占用的存储空间包括算法程序所占用的空间，输入的初始数据所占用的存储空间及算法执行过程中所需要的额外空间。"
}, {
	"subject_title": "负责数据库中查询操作的数据库语言是（　　）。",
	"subject_choice_A": "数据定义语言",
	"subject_choice_B": "数据管理语言",
	"subject_choice_C": "数据操纵语言",
	"subject_choice_D": "数据控制语言",
	"subject_answer": "C",
	"analysis": "数据库操纵语言专门负责查询、增加和删除等数据操作。"
}, {
	"subject_title": "阅读下面代码\nif(x= =0){System．OUt．println(\"冠军\")；}\nelseif(x>-3){System．OUt．println(\"亚军\")；)\nelse{System．Out．println(\"季军\")；)\n若要求打印字符串”季军”，则变量X的取值范围是( )。",
	"subject_choice_A": "x=0&x<= -3",
	"subject_choice_B": "x>0",
	"subject_choice_C": "x>-3",
	"subject_choice_D": "x<=-3",
	"subject_answer": "D",
	"analysis": "本题考查的是条件分支语句if-else。if-else根据判定条件的真假来执行两种操作中的一种。当条件为真时，执行if语句后面的代码块；当条件为假时，执行else后面的代码块。题目中的代码段是一个if-else的嵌套语句，根据if-else语句的执行过程来进行分析。当x的值为0时，布尔表达式&quot;x==0&quot;的结果为真，就输出&quot;冠军&quot;；当x的值不为0时，则执行else语句中的内容。else语句中的代码又是一个if-else语句，还是和上面一样进行分析。当x的值不等于0且大干-3时，布尔表达式&quot;x&gt;-3&quot;的结果为真，输出&quot;亚军&quot;；当x的值不等于0且不大于-3，也就是x的值不等于0同时x的值小于等于-3时，则输出&quot;季军&quot;。经过上述分析可知，要想输出&quot;季军&quot;，x所满足的条件为x!=0&amp;x&lt;=-3，但是当x&lt;=-3时，x的值一定不会为0。所以，x所满足的条件可以简写为x&lt;=-3．因此，本题的正确答案为D。"
}, {
	"subject_title": "使用白盒测试法时，确定测试数据应该根据（　　）和指定的覆盖标准。",
	"subject_choice_A": "程序的内部逻辑",
	"subject_choice_B": "程序的复杂结构",
	"subject_choice_C": "使用说明书",
	"subject_choice_D": "程序的功能",
	"subject_answer": "A",
	"analysis": "白盒测试是把测试对象看做一个打开的盒子，允许测试人员利用程序内部的逻辑结构及相关信患来设计或选择测试用例，对程序所有的逻辑路径进行测试。"
}, {
	"subject_title": "设计程序时，应采纳的原则之一是（　　）。",
	"subject_choice_A": "程序的结构应有助于读者的理解",
	"subject_choice_B": "不限制goto语句的使用",
	"subject_choice_C": "减少或取消注释行",
	"subject_choice_D": "程序越短越好",
	"subject_answer": "A",
	"analysis": "程序设计的风格主要强调程序的简单、清晰和可理解性，以便读者理解。程序滥用goto语句将使程序流程无规律，可读性差；添加注释行有利于对程序的理解，程序的长短要依据实际的需要而定，并不是越短越好。"
}, {
	"subject_title": "在多线程程序设计中，如果采用继承Thread类的方式创建线程，则需要重写Thread类的（　　）方法。",
	"subject_choice_A": "start",
	"subject_choice_B": "local",
	"subject_choice_C": "interrupt",
	"subject_choice_D": "run",
	"subject_answer": "D",
	"analysis": "Thread类本身实现了Runnable接口，所以可以通过继承Thread类，并重写run()方法定义线程体，然后创建该子类的对象创建线程。"
}, {
	"subject_title": "下列代码的下画线处应填入的方法名是（　　）。\nimport java．awt．*；\nimport java．applet．*；\npublic class Hello extends Applet{\npublic void (Graphics g){\n9.drawstring(\"How are you!\"，l0，10)；\n}\n}",
	"subject_choice_A": "repaint",
	"subject_choice_B": "println",
	"subject_choice_C": "paint",
	"subject_choice_D": "show",
	"subject_answer": "C",
	"analysis": "这里使用一个继承自Applet的类来显示字符。主要方法是在paint()方法中使用System．out．println()显示。"
}, {
	"subject_title": "以下不是APPLET标记的选项是（　　）。",
	"subject_choice_A": "PARAM",
	"subject_choice_B": "BODY",
	"subject_choice_C": "CODEBASE",
	"subject_choice_D": "ALT",
	"subject_answer": "B",
	"analysis": "&lt;APPLET&gt;标记的一般格式是：&lt;APPLET<br>\n[CODEBASE=codebaseURL]<br>\nCODE=appletFile [ALT=alternateText]<br>\n[NAME=appletlnstanceName]<br>\nWIDTH=pixels<br>\nHEIGHT=pixels<br>\n[ALIGN=alignment]<br>\n[VSPACE=pixels]<br>\n[HSPACE=pixels]<br>\n[ARCHIVE=archiveFiles]<br>\n&gt;<br>\n[&lt;PARAM NAME=appletParameterl VALUE=val-ue&gt;]<br>\n[&lt;PARAM NAME=appletParameter2 vALuE=val-ue&gt;]<br>\n[alternateHTML]<br>\n因此可以看出，选项B不是APPLET标记。"
}, {
	"subject_title": "Java中的抽象类Reader和Writer所处理的流是（　　）。",
	"subject_choice_A": "图像流",
	"subject_choice_B": "对象流",
	"subject_choice_C": "字节流",
	"subject_choice_D": "字符流",
	"subject_answer": "D",
	"analysis": "Reader／Writer所处理的流是字符流，InputStream／OutputStream的处理对象是字节流。"
}, {
	"subject_title": "设a=8，则表达式a>>>2的值是（　　）。",
	"subject_choice_A": "1",
	"subject_choice_B": "2",
	"subject_choice_C": "3",
	"subject_choice_D": "4",
	"subject_answer": "B",
	"analysis": "本题具体考查对位运算符中无符号右移运算符的掌握。无符号右移运算符”&gt;&gt;&gt;”用于将一个数的各二进制位全部无符号右移若干位，与运算符”&gt;&gt;”不同的是左补0。在本题中，8的二进制表示l000，右移两位后变成了0010，对应的十进制数是2。"
}, {
	"subject_title": "有三介关系R、S和T如下：\n　\n　\n则由关系R和S得到关系T的操作是（　　）。",
	"subject_choice_A": "自然连接",
	"subject_choice_B": "交",
	"subject_choice_C": "投影",
	"subject_choice_D": "并",
	"subject_answer": "A",
	"analysis": "自然连接是将表中具有相同名称的列自动进行记录匹配。"
}, {
	"subject_title": "Java对文件类提供了许多操作方法，能获得文件对象父路径名的方法是（　　）。",
	"subject_choice_A": "getAbsolutePath()",
	"subject_choice_B": "getParentFile()",
	"subject_choice_C": "getAbsoluteFile()",
	"subject_choice_D": "getName()",
	"subject_answer": "B",
	"analysis": "本题考查File类的基本知识。File类是通过文件名列表来描述一个文件对象的属性，通过File类提供的方法，可以获得文件的名称、长度、所有路径等信息，还可以改变文件的名称、删除文件等。"
}, {
	"subject_title": "16根地址总线的寻址范围是（　　）。",
	"subject_choice_A": "531KB",
	"subject_choice_B": "64KB",
	"subject_choice_C": "640KB",
	"subject_choice_D": "1MB",
	"subject_answer": "B",
	"analysis": "假设地址总线有n条，内存的寻址范围是2n。"
}, {
	"subject_title": "关于集合类描述正确的是（　　）。\nⅠ．集合类中容纳的都是指向Object类对象的指针\nⅡ．集合类容纳的对象都是Object的类例\nⅢ．只能容纳对象\nIV．只能容纳基本数据类型",
	"subject_choice_A": "Ⅰ、Ⅱ、Ⅲ",
	"subject_choice_B": "Ⅰ、Ⅱ",
	"subject_choice_C": "Ⅰ、Ⅲ",
	"subject_choice_D": "Ⅰ、Ⅱ、Ⅲ、IV",
	"subject_answer": "A",
	"analysis": "本题主要考查集合类的特点。选项A正确，集合类是用来存放某类对象的。集合类有一个共同特点，就是它们只容纳对象。如果集合类中想使用简单数据类型，又想利用集合类的灵活性，可以把简单数据类型变成该数据类型类的对象，然后放入集合中处理，这表示集合类不能容纳基本数据类型，所以IV是不正确的选项B错误，集合只容纳对象；选项C错误，该选项少选了Ⅱ；选项D错误，错误原因同选项B。"
}, {
	"subject_title": "在switch(expression)语句中，expression的数据类型不能是（　　）。",
	"subject_choice_A": "double",
	"subject_choice_B": "char",
	"subject_choice_C": "byte",
	"subject_choice_D": "short",
	"subject_answer": "A",
	"analysis": "本题考查考生对switch(expression)语句的理解。表达式expression只能返回int、byte、short和char，题目中的double是不正确的。同时还要注意，多分支结构中，case子句的值必须是常量，而且所有case子句中的值应是不同的，default子句是任选的。"
}, {
	"subject_title": "下列叙述中，不属于测试的特征的是（　　）。",
	"subject_choice_A": "测试的挑剔性",
	"subject_choice_B": "完全测试的不可能性",
	"subject_choice_C": "测试的可靠性",
	"subject_choice_D": "测试的经济性",
	"subject_answer": "C",
	"analysis": "软件测试的目标是在精心控制的环境下执行程序，以发现程序中的错误，给出程序可靠性的鉴定。软件测试有3个重要特征：测试的挑剔性、完全测试的不可能性及测试的经济性。"
}, {
	"subject_title": "下列程序的运行结果是（　　）。\nPublic class sun\n{\nPublic static void main(String args[])\n{\nint x=4，y=0；\nif(Math．pow(X，2)= =16)\ny—x ；\nif(Math．pow(X，2)<15)\ny—l／x；\nif(Math．pow(X，2)>15)\ny=(int)Math．pow(X，2)+1；\nsystem．out．println(y)；\n}\n}",
	"subject_choice_A": "4",
	"subject_choice_B": "17",
	"subject_choice_C": "18",
	"subject_choice_D": "0．25",
	"subject_answer": "B",
	"analysis": "本题是考查对if-else分支结构和几个标准函数的理解。pow(x，y)方法是X的Y次幂，程序中pow(x，2)满足第1个if语句和第3个if语句，条件变量y将被赋值两次，但对于同一个变量来说，只能存储最后一个所赋的值。"
}, {
	"subject_title": "软件(程序)调试的任务是( )。",
	"subject_choice_A": "诊断和改正程序中的错误",
	"subject_choice_B": "尽可能多地发现程序中的错误",
	"subject_choice_C": "发现并改正程序中的所有错误",
	"subject_choice_D": "确定程序中错误的性质",
	"subject_answer": "A",
	"analysis": "调试的目的是发现错误或导致程序失效的错误原因，并修改程序以修正错误。调试是测试之后的活动"
}, {
	"subject_title": "在一个线程中调用下列方法，不会改变该线程运行状态的是（　　）。",
	"subject_choice_A": "yield方法",
	"subject_choice_B": "另一个线程的join方法",
	"subject_choice_C": "sleep方法",
	"subject_choice_D": "一个对象的notify方法",
	"subject_answer": "B",
	"analysis": "另一个线程的join方法是使得另一个线程等待，直到本线程结束为止，另一个线程恢复到可运行状态，不会改变本线准的运行状态。"
}, {
	"subject_title": "如果应用程序要在Applet上显示输出，则必须重写的方法是( )。",
	"subject_choice_A": "Graphics．drawString()",
	"subject_choice_B": "repaint()",
	"subject_choice_C": "paint()",
	"subject_choice_D": "update()",
	"subject_answer": "C",
	"analysis": "paint()是绘制Applet界面的基本方法。"
}, {
	"subject_title": "耦合性和内聚性是对模块独立性度量的两个标准，下列叙述中正确的是（　　）。",
	"subject_choice_A": "提高耦合性降低内聚性有利于提高模块的独立性",
	"subject_choice_B": "降低耦合性提高内聚性有利于提高模块的独立性",
	"subject_choice_C": "耦合性是指一个模块内部各个元素间彼此结合的紧密程度",
	"subject_choice_D": "内聚性是指模块闻互相连接的紧密程度",
	"subject_answer": "B",
	"analysis": "耦合是指模块间相互连接的紧密程度，内聚性是指在一个模块内部各个元素间彼此之间接合的紧密程序。高内聚、低耦合有利于模块的独立性。"
}, {
	"subject_title": "下列不属于接口WindowListener的方法是（　　）。",
	"subject_choice_A": "windowClosing()",
	"subject_choice_B": "windowClosed()",
	"subject_choice_C": "windowMinimized()",
	"subject_choice_D": "windowOpened()",
	"subject_answer": "C",
	"analysis": "接口WindowListener包括以下方法：windowActivated、windowDeactivated、windowClosing、windowClosed、windowlconified、windowDeieonified windowOpened方法。所以选C。"
}, {
	"subject_title": "执行下列程序时，会产生什么异常（　　）。\npublic class Test{\npublic static void main(String args[]){\nint d=101；\nint b=220：\nlong a=321；\nSystem．OUt．println((a-b)／(a-b-d))；\n}\n}",
	"subject_choice_A": "ArraylndexOutOfBoundsException",
	"subject_choice_B": "NumberFormatException",
	"subject_choice_C": "ArithmeticException",
	"subject_choice_D": "EOFExeeption",
	"subject_answer": "C",
	"analysis": "本题考查异常的概念。首先应该掌握题目选项中给出的都是什么类型的异常。选项A是当访问数组中非法元素时引发，出现数组负下标异常。选项B是格式化数字异常。选项C是算术异常，如程序触发分母为0，或用0取模时出现。选项D是文件已结束异常。当Java执行这个算术表达式的时候，由于求模运算的分母是a-b-d=0，就会构造一个ArithmetieException的异常对象来使程序停下来并处理这个错误的情况，在运行时抛出这个异常。默认的处理器打印出Exception的相关信息和发生异常的地点。"
}, {
	"subject_title": "关于Applet执行的操作，下面说法正确的是（　　）。",
	"subject_choice_A": "在运行时调用其他程序",
	"subject_choice_B": "可以进行文件读／写操作",
	"subject_choice_C": "不能装载动态连接库和调用任何本地方法",
	"subject_choice_D": "试图打开一个socket进行网络通信，但是所连接的主机并不是提供Applet的主机",
	"subject_answer": "C",
	"analysis": "本题考查Applet的概念。Java虚拟机为Applet提供能够良好运行的沙箱，一旦它们试图离开沙箱则会被禁止。由于Applet是通过网络传递的，这就不可避免地使人想到会发生安全问题。例如，有人编写恶意程序通过小应用程序读取用户密码并散播到网络上，这将会是一件非常可怕的事情。所以，必须对小应用程序进行限制。浏览器禁止Applet运行任何本地可运行程序，选项A错误。禁止加载本地库或方法，Applet只能使用自身的代码或Applet浏览器提供的JavaAPl，不允许装载动态连接库和调用任何本地方法，选项C正确。禁止读／写本地计算机的文件系统，选项B错误。禁止与没有提供Applet的任何主机建立网络连接，如果Applet试图打开一个socket进行网络通信，所连接的主机必须是提供Applet的主机，选项D错误。"
}, {
	"subject_title": "下列属于合法的Java标识符的是（　　）。",
	"subject_choice_A": "_cat",
	"subject_choice_B": "5books",
	"subject_choice_C": "+static",
	"subject_choice_D": "-3．14159",
	"subject_answer": "A",
	"analysis": "本题考查Java标识符的命名规则，是考试的重点内容。Java中标识符的命名规则是标识符以字母、下画线或美元符作为首字符的字符串序列，；标识符是区分大小写的；标识符的字符数没有限制。留此可见，Java中标识符不能以数字开头，所以选项B错误，不能以“+”开头，选项C错误，不能以“-”开头，选项D错误，只有选项是正确答案。"
}, {
	"subject_title": "单击窗口内的按钮时，产生的事件是（　　）。",
	"subject_choice_A": "MouseEvent",
	"subject_choice_B": "WindowEvent",
	"subject_choice_C": "ActionEvent",
	"subject_choice_D": "KeyEvent",
	"subject_answer": "C",
	"analysis": "在构件的事件类中，MouseEvent事件是鼠标事件，包括鼠标单击，移动；WindowEvent事件是窗口事件，包括关闭窗口，窗口闭合。图标化；ActionEvent事件是动作事件，包括按钮按下；TextField中按&lt;Enter&gt;键；KeyEvent事件是键盘事件，包括键按下、释放。"
}, {
	"subject_title": "下列程序的功能是统计字符串中“array”的个数，在程序的空白处应填入的正确选项是（　　）。\npublic class FindKeyWords(\npublic static void main(sring[]args){\nsting text=\n\"An array is a data structur that stores a eollection of\"\n+\"values of the same type．You access each individu-\nal value\"\n+\"through an integer index．For example．if a is an\narray\"\n+\"of inergers，then all]is the ith integer in the ar-\nray．\"；\nInt arrayCount=0；\nInt idex=-l；\nSting arrarStr=\"array\"：\nIndex=text．indexof(arrayStr)；\nWhile(index 0){\n++arrayCount：\nIndex+=arrayStr．1ength()；\nIndex=text．indexof(arrayStr，index)；\n}\nSystem．OUt．println\n(\"the text contains\"+arrayCount+\"arrays\")；\n}\n}",
	"subject_choice_A": "<",
	"subject_choice_B": "=",
	"subject_choice_C": "<=",
	"subject_choice_D": ">=",
	"subject_answer": "D",
	"analysis": "在字符串中查询指定的字符或子串，可用indexof()方法，如查询成功，返回所查字符的位置。如不成功，返回-l，从下面程序可以看出，While条件应为查询成功。"
}, {
	"subject_title": "下列选项中属于字符串常量的是（　　）。",
	"subject_choice_A": "•abc•",
	"subject_choice_B": "\"abe\"",
	"subject_choice_C": "[abc]",
	"subject_choice_D": "(abc)",
	"subject_answer": "B",
	"analysis": "Java中字符串常量由双引号和其中间的字符所组成。"
}, {
	"subject_title": "下列叙述中，错误的是（　　）。",
	"subject_choice_A": "内部类的名称与定义它的类的名称可以相同",
	"subject_choice_B": "内部类可用abstract修饰",
	"subject_choice_C": "内部类可作为其他类的成员",
	"subject_choice_D": "内部类可访问它所在类的成员",
	"subject_answer": "A",
	"analysis": "内部类与外部类的名称不能相同。"
}, {
	"subject_title": "能向内部直接写入数据的流是（　　）。",
	"subject_choice_A": "FileOutputStream",
	"subject_choice_B": "FileInputStream",
	"subject_choice_C": "ByteArrayOutputStream",
	"subject_choice_D": "ByteArraylnputStream",
	"subject_answer": "C",
	"analysis": "本题考查Java的内存读写。在java．io中，还提供了ByteArrayInputStream、ByteArrayoutputStream和StringBufferInputStream类可直接访问内存，它们是InputStream和OutputStream的子类。用ByteArrayOutputStream可向字节数组写入数据；ByteArrayInputStream可从字节数组中读取数据。"
}, {
	"subject_title": "下列程序的输出结果是（　　）。\npublic class Test{\npublic static void main(String[]args){\nint[]array=(2，4，6，8，lO)；\nint size=6；\nint result =-1：\ntry{\nfor(int i=0；i(size 8L&result= = -1；)\nif(array[i]= =20)result=i：\n}\ncatch(ArithmeticException e){\nSystem．out．println(\"Catch- - -l\")；\n}\ncatch(ArraylndexOutOfBoundsException e){\nSystem．out．println(\"Catch- - -2\")；\n}\ncatch(Exception e){\nSystem．out．println(\"Catch- - -3\")；)\n}\n}",
	"subject_choice_A": "Catch- - -1",
	"subject_choice_B": "Catch- - -2",
	"subject_choice_C": "Catch- - -3",
	"subject_choice_D": "以上都不对",
	"subject_answer": "B",
	"analysis": "由题可知先判断i&lt;size&amp;&amp;resuh==-1，结果为真，则执行if语句array数组中的任何数都不等于20，并且i从0开始一直到i=5时发生越界，则输出Cateh= =-2，结果为B。"
}, {
	"subject_title": "下列类中属于字节输入抽象类的是（　　）。",
	"subject_choice_A": "FileInputStream",
	"subject_choice_B": "ObjectInputStream",
	"subject_choice_C": "FiterInputStream",
	"subject_choice_D": "InputStream",
	"subject_answer": "D",
	"analysis": "在Java中定义了两种类型的流，字节型和字符型，这两种流分别用4个抽象类表示：InputStream，OutputStream，Reader，Writer，其中InptutStream和OutStream表示字节流，Reader和Reader是表示字符流，所以字节输入抽象类为InptutStream。"
}, {
	"subject_title": "如果应用程序要在Applet上显示输出，则必须重写的方法是（　　）。",
	"subject_choice_A": "Graphics．drawstring()",
	"subject_choice_B": "repaint()",
	"subject_choice_C": "paint()",
	"subject_choice_D": "update()",
	"subject_answer": "C",
	"analysis": "paint()是画Applet界面的基本方法。"
}, {
	"subject_title": "下列Java语句从指定网址读取html文件，在下画线处应填上的选项是（　　）。\nReader in=new——(new URL(urlString)．\nopenStream())；",
	"subject_choice_A": "Reader",
	"subject_choice_B": "DataOutputStream",
	"subject_choice_C": "ByteArray InputStream",
	"subject_choice_D": "InputStreamReader",
	"subject_answer": "A",
	"analysis": "创建一个Reader流的对象in。"
}, {
	"subject_title": "阅读下列Java语句：\nObjectOutputStream OUt=new ObjeetOutputStream\n(new (\"employee．dat\"))；\n在下画线处，应填的正确选项是（　　）。",
	"subject_choice_A": "File",
	"subject_choice_B": "FileWriter",
	"subject_choice_C": "FileOutputStream",
	"subject_choice_D": "Outputstream",
	"subject_answer": "C",
	"analysis": "ObjeetOutputStream即继承了0utputStream抽象类，又实现了ObjectOutput接口，这是Java用接口技术代替双重继承的例子，其构造方法参数是串行化了的对象。所以，此处应为串行化的文件输出流。"
}, {
	"subject_title": "以下叙述中不属于Java语言特点的是（　　）。",
	"subject_choice_A": "面向对象",
	"subject_choice_B": "可移植性",
	"subject_choice_C": "多线程",
	"subject_choice_D": "宏定义",
	"subject_answer": "D",
	"analysis": "本题考查Java语言的基本特点。选项A正确，Java最大的特点之一是跨平台、面向对象；选项B正确，解释同A；选项C正确，多线程是Java的一个主要特性，它使可执行程序具有同时保持几个线程执行的能力；选项D错误，Java不支持宏定义。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "对长度为n的有序链表进行查找，最坏情况下需要的比较次数为n",
	"subject_choice_B": "对长度为n的有序链表进行对分查找，最坏情况下需要的比较次数为(n／Z)",
	"subject_choice_C": "对长度为n的有序链表进行对分查找，最坏情况下需要的比较次数为(log2n)",
	"subject_choice_D": "对长度为n的有序链表进行对分查找，最坏情况下需要的比较次数为(nlog2n)",
	"subject_answer": "C",
	"analysis": "二分法查找只适用于顺序存储的有序表，对于长度为n的有序线性表，最坏情况只需比较log2n次。"
}, {
	"subject_title": "Java类库中，将信息写入内存的类是（　　）。",
	"subject_choice_A": "java．io．FileOutputStream",
	"subject_choice_B": "java．io．ByteArrayOutputStream",
	"subject_choice_C": "java．io．BufferedOutputStream",
	"subject_choice_D": "java．io．DataOutputStream",
	"subject_answer": "B",
	"analysis": "在java．i0中，提供了ByteArrayInputStream、ByteArrayOutputStream和StringBuffednputStream类可以直接访问内存，其中用ByteArrayOutputStream可以向字节数组(缓冲区)写入数据。"
}, {
	"subject_title": "下列各项中代表八进制整数的是（　　）。",
	"subject_choice_A": "0XA6",
	"subject_choice_B": "0144",
	"subject_choice_C": "1840",
	"subject_choice_D": "-lE3",
	"subject_answer": "B",
	"analysis": "Java语言中八进制整数为整型常量中的一种，以0开始，后加数字0～7组成。故只有B选项0144符合要求。"
}, {
	"subject_title": "用链表表示线性表的优点是（　　）。",
	"subject_choice_A": "便于随机存取",
	"subject_choice_B": "花费的存储空间较顺序存储少",
	"subject_choice_C": "便于插入和删除操作",
	"subject_choice_D": "数据元素的物理顺序与逻辑顺序相同",
	"subject_answer": "C",
	"analysis": "数据结构是相互之间存在一种或多种特定关系的数据元素的集合。”关系”描述的是数据元素之间的逻辑关系，因此又称数据的逻辑结构。数据的存储结构是指数据结构(数据的逻辑结构)在计算机中的表示，又称物理结构。数据的存储结构有顺序存储结构和链式存储结构两种。不同存储结构的数据处理效率不同。由于链表采用链式存储结构，元素的物理顺序并不连续，对于插入和删除无需移动元素，很方便，当查找元素时就需要逐个元素查找，因此查找的时间相对更长。"
}, {
	"subject_title": "能打印出一个双引号的语句是（　　）。",
	"subject_choice_A": "System．out．println{\"\"}；",
	"subject_choice_B": "System．out．println{\"*\"}；",
	"subject_choice_C": "System．OUt．println{¨／\"}；",
	"subject_choice_D": "System．OUt．println(¨＼¨\"}；",
	"subject_answer": "D",
	"analysis": "双引号字符的输出应使用转义字符。"
}, {
	"subject_title": "Java程序默认引用的包是（　　）。",
	"subject_choice_A": "java．text包",
	"subject_choice_B": "java．awt包",
	"subject_choice_C": "java．1an9包",
	"subject_choice_D": "java．util包",
	"subject_answer": "C",
	"analysis": "java．lang包提供Java编程语言进行程序设计的基础类。java．lang包是编译器自动导入的。"
}, {
	"subject_title": "下列数据结构中，能用二分法进行查找的是（　　）。",
	"subject_choice_A": "顺序存储的有序线性表",
	"subject_choice_B": "线性链表",
	"subject_choice_C": "二叉链表",
	"subject_choice_D": "有序线性链表",
	"subject_answer": "A",
	"analysis": "二分法查找只适用于顺序存储的有序线性表，对于顺序存储的非有序线性表和线性链表，都只能采用顺序查找。"
}, {
	"subject_title": "阅读下面代码\nif(x= =0){System．out．println(\"冠军\")；)\nelseif(x>一3){System．Out．println(\"亚军\")；}\nelse{System．out．println(\"季军\")；}\n若要求打印字符串”季军”，则变量X的取值范围是（　　）。",
	"subject_choice_A": "x=d&x<=-3",
	"subject_choice_B": "x>O",
	"subject_choice_C": "x>-3",
	"subject_choice_D": "x<=-3",
	"subject_answer": "D",
	"analysis": "本题考查的是条件分支语句if-else。if-else根据判定条件的真假来执行两种操作中的一种。当条件为真时，执行if语句后面的代码块；当条件为假时，执行else后面的代码块。题目中的代码段是一个if-else的嵌套语句，根据if-else语句的执行过程来进行分析。当x的值为0时，布尔表达式&quot;x==0&quot;的结果为真，就输出”冠军”；当x的值不为0时，则执行else语句中的内容。else语句中的代码又是一个if-else语句，还是和上面一样进行分析。当X的值不等于0且大于-3时，布尔表达式”x&gt;-3”的结果为真，输出&quot;亚军&quot;；当x的值不等于0且不大干-3，也就是X的值不等于0同时x的值小于等于-3时，则输出&quot;季军&quot;。经过上述分析可知，要想输出&quot;季军&quot;，x所满足的条件为x!=O&amp;x&lt;=-3，但是当x&lt;=-3时，x的值一定不会为0。所以，X所满足的条件可以简写为x&lt;=-3。因此，本题的正确答案为D。"
}, {
	"subject_title": "当Applet程序中的init()方法为下列代码时，运行后用户界面会出现的情况，以下描述正确的是（　　）。\npublic void init()\n{\nsetlLayout(new BorderLayout())；\nadd(”North”，new TextField(10))：\nadd(”Center”，new Button(”help”))：\n}",
	"subject_choice_A": "文本框将会出现在Applet的顶上，且有l0个字符的宽度",
	"subject_choice_B": "按钮将会出现在Applet的正中间，且尺寸为正好能够包容help的大小",
	"subject_choice_C": "文本框将会出现在Applet的顶上，从最左边一直延伸到最右边；按钮将会出现在Applet的正中间，覆盖除文本框外的所有空间",
	"subject_choice_D": "按钮与文本框的布局依赖于Applet的尺寸",
	"subject_answer": "C",
	"analysis": "该题考查对容器布局策略的理解。边界布局管理器BorderLayout将容器按上北下南左西右东划分为东、南、西、北、中5部分，分别用英文单词East，South，North，West，Center来表示。其中，东、西、南、北4个方向的组件宽度为恰好能够包容组件的内容，而长度为延伸到该容器边界的长度；而对于中间的组件，它会扩充到除四边以外的整个容器区域。本题的具体情况是：文本框将会出现在applet的顶上，长度为整个applet的宽度；按钮将会出现在applet的正中央，覆盖除文本框外的所有空间。"
}, {
	"subject_title": "下列事件监听器中，无法对TextField对象进行事件监听和处理的是（　　）。",
	"subject_choice_A": "ActionListener",
	"subject_choice_B": "FocusListener",
	"subject_choice_C": "MouseMotionListener",
	"subject_choice_D": "ChangeListener",
	"subject_answer": "D",
	"analysis": "本题考查AWT事件处理。事件就是发生在用户界面上的用户交互行为所产生的一种效果。每类事件都有对应的事件监听器，监听器就是接口。在单行文本输入区(TextField)构件上可能发生的事件包括：FocusEvent焦点事件——焦点的获得和丢失，这类事件所对应的事件监听器是FocusListener；ActionEvent动作事件——按钮按下、TextField中按&lt;Enter&gt;键，这类事件所对应的事件监听器是ActionListener；MouseEvent鼠标事件——鼠标单击、释放、拖动、移动，这类事件所对应的事件监听器是MousetMotionListener。虽然还包括其他一些监听器，但是在所有事件及其所对应的事件监听器中，并不包括ChangeListener这样一个事件监听器。因此，本题的正确答案是D。"
}, {
	"subject_title": "某二叉树共有7个结点，其中叶子结点只有l个，则该二叉树的深度为(假设根结点在第1层)（　　）。",
	"subject_choice_A": "3",
	"subject_choice_B": "4",
	"subject_choice_C": "6",
	"subject_choice_D": "7",
	"subject_answer": "D",
	"analysis": "对于任意一棵二叉树T，如果叶子结点数为n0，度为2的结点数为n2，二者之间的关系是n0=n2+1，该题中度为2的结点数为0，且只有一个叶子结点，因此，树中度为l的结点有6个，很容易想到树的高度为7。"
}, {
	"subject_title": "若定义int a=2，b一2，下列表达式中值不为4的是（　　）。",
	"subject_choice_A": "a*(++b)",
	"subject_choice_B": "a*(b++)",
	"subject_choice_C": "a+b",
	"subject_choice_D": "a*b",
	"subject_answer": "A",
	"analysis": "++b，先自加，再计算，即a*(++b)等价于b=b+1；a*b。"
}, {
	"subject_title": "下面for循环语句的执行结果是（　　）。\n　\n　",
	"subject_choice_A": "6 3",
	"subject_choice_B": "7 4",
	"subject_choice_C": "6 2",
	"subject_choice_D": "7 3",
	"subject_answer": "B",
	"analysis": "该题考查对for循环的理解。①当j＝10时，满足条件j&gt;3，由于for循环中j－－执行了1次，j的值为9，执行if语句，j％3＝0不满足条件，继续向下执行2次－－j，j的值为7：②当j＝7时，满足条件j&gt;3，由于for循环中j－－执行了1次，j的值为6，执行if语句，i％3＝0不满足条件，继续向下执行2次－－j，j的值为4。"
}, {
	"subject_title": "向Applet传递参数的正确描述是（　　）。",
	"subject_choice_A": "  ",
	"subject_choice_B": "  ",
	"subject_choice_C": "  ",
	"subject_choice_D": "  ",
	"subject_answer": "A",
	"analysis": "&lt;Applet&gt;标记的参数部分－般格式是[&lt;PARAMNAME＝appletParameter VALUE＝value&gt;]。"
}, {
	"subject_title": "以下叙述中不属于Java语言特点的是（　　）。",
	"subject_choice_A": "面向对象",
	"subject_choice_B": "可移植性",
	"subject_choice_C": "多线程",
	"subject_choice_D": "宏定义",
	"subject_answer": "D",
	"analysis": "本题考查Java语言的基本特点。选项A正确，Java最大的特点之一是跨平台、面向对象；选项B正确，解释同A；选项C正确，多线程是Java的一个主要特性，它使可执行程序具有同时保持几个线程执行的能力；选项D错误，Java不支持宏定义。"
}, {
	"subject_title": "下列选项默认的布局管理器不是BorderLayout的是（　　）。",
	"subject_choice_A": "Window",
	"subject_choice_B": "Panel",
	"subject_choice_C": "Frame",
	"subject_choice_D": "Dialog",
	"subject_answer": "B",
	"analysis": "本题考查Java中的布局管理器。Panel和Applet默认的布局管理器是FlowLayout，构件在容器中放置规律是从上到下、从左到右进行放置；BorderLayout是Window、Frame和Dialog的默认布局管理器，在BorderLay—out布局管理器中构件分成5个区域North、South、East、West和Center，每个区域只能放置一个构件。考生应注意区分各个布局管理器的区别和联系，以及各个布局管理器的特点。"
}, {
	"subject_title": "SQL语言又称为（　　）。",
	"subject_choice_A": "结构化定义语言",
	"subject_choice_B": "结构化控制语言",
	"subject_choice_C": "结构化查询语言",
	"subject_choice_D": "结构化操纵语言",
	"subject_answer": "C",
	"analysis": "SQL语言的全称为StructuredQueryLanguage，它是－种介于关系代数与关系演算之间的结构化查询语言，是－种面向数据库的通用数据处理语言规范。它包含数据查询语言、数据操纵语言、数据定义语言和数据控制语言4个部分。"
}, {
	"subject_title": "在对象流中，对象的传送首先要将所传送的对象串行化，也就是实现Serializable接口。下列代码中必须实现Serializable接口的类是（　　）。\n　\n　",
	"subject_choice_A": "Employee",
	"subject_choice_B": "Input",
	"subject_choice_C": "Staff",
	"subject_choice_D": "Stream",
	"subject_answer": "A",
	"analysis": "－个对象能够实现序列化的前提是实现Serializable接口，Serializable接口没有方法，更像是－个标记，有了这个标记的Class才能被序列化机制处理。"
}, {
	"subject_title": "下列方法与Applet显示无关的是（　　）。",
	"subject_choice_A": "paint（　　）",
	"subject_choice_B": "update（　　）",
	"subject_choice_C": "draw（　　）",
	"subject_choice_D": "repaint（　　）",
	"subject_answer": "C",
	"analysis": "本题考查Applet的基本概念。Applet显示相关的方法主要有3个。paint（）方法，具体执行Applet的绘制，定义为：publicvoid paint(Graphics g)；update（）方法，定义为：public void update(Graphics g)，主要用于更新Applet的显示；repaint（）方法，定义为：public void repaint（），主要用于Applet的重新显示，它调用update（）方法实现对Applet的更新。而draw（）方法与显示无关。故选C。"
}, {
	"subject_title": "在文件类提供的方法中，用于创建目录的方法是（　　）。",
	"subject_choice_A": "mkdir（　　）",
	"subject_choice_B": "mkdirs（　　）",
	"subject_choice_C": "list（　　）",
	"subject_choice_D": "listRoots（　　）",
	"subject_answer": "A",
	"analysis": "本题考查文件类提供的方法。mkdir（）是为目录操作提供的方法，用来创建目录；mkdirs（）也是为目录操作提供的方法，创建包含父目录的目录；list（）是对文件名操作提供的方法，返回－个字符串数组，为该文件所在目录下的所有文件名列表；listRoots是为目录提供的方法，返回根目录结构。由此可见，只有选项A满足题目要求。"
}, {
	"subject_title": "int型public成员变量MAX_LENGTH，该值保持为常数100，则定义这个变量的语句是（　　）。",
	"subject_choice_A": "public int MAX_LENGTH＝1 00",
	"subject_choice_B": "final int MAX_LENGTH＝100",
	"subject_choice_C": "public const int MAX_LENGTH＝100",
	"subject_choice_D": "public final int MAX_LENGTH＝100",
	"subject_answer": "D",
	"analysis": "本题考查Java中变量的声明。选项A虽然按照题目要求定义了一个变量，但没有满足保持为常数的要求，该变量可以被改变；选项B没有满足题目要求的public成员变量；选项C与C语言混淆，const是C语言用来定义常值变量的关键字；Java中定义常值变量使用的是fi—nal属性，说明该值赋值以后永不改变，所以选项D为正确答案。"
}, {
	"subject_title": "按照Java的标识符命名规则，下列表示－个类的标识符正确的是（　　）。",
	"subject_choice_A": "Helloworld",
	"subject_choice_B": "HelloWorld",
	"subject_choice_C": "helloworld",
	"subject_choice_D": "helloWorld",
	"subject_answer": "B",
	"analysis": "本题考查Java类名的命名规则。类名与接口名都采用完整的英文描述，并且所有单词的第一个字母大写；包采用完整的英文描述符，都是由小写字母组成的；类的变量采用完整的英文描述，第一个字母小写，任何中间单词的首字母大写；常量名全部采用大写字母，单词之间用下画线分隔。应该掌握命名规则，不仅因为它是考试重点，同时也是养成良好编程习惯的基础。"
}, {
	"subject_title": "下面程序段的输出结果是（　　）。\n　\n　",
	"subject_choice_A": "37",
	"subject_choice_B": "31",
	"subject_choice_C": "33",
	"subject_choice_D": "35",
	"subject_answer": "C",
	"analysis": "本题是对for循环语句和数组的综合考查。题中共定义了两个数组：a[]和p[]，共用了3次for循环；第1个for语句对数组a[i]赋值；第2个for语句对数组p[i]赋值；第3个for语句计算k的值。3次循环分别得到：5，15和33。正确答案为选项C。"
}, {
	"subject_title": "有下列二叉树，对此二叉树前序遍历的结果为（　　）。\n　\n　",
	"subject_choice_A": "ACBEDGFH",
	"subject_choice_B": "ABDGCEHF",
	"subject_choice_C": "HGFEDCBA",
	"subject_choice_D": "ABCDEFGH",
	"subject_answer": "B",
	"analysis": "二叉树的前序遍历是指，先访问根结点，再访问左子树，最后访问右子树。并且在访问左右子树时，也是先访问其根结点，再访问左右子树。"
}, {
	"subject_title": "软件详细设计产生的图如下。该图是（　　）。\n　\n　",
	"subject_choice_A": "N—S图",
	"subject_choice_B": "PAD图",
	"subject_choice_C": "程序流程图",
	"subject_choice_D": "E—R图",
	"subject_answer": "C",
	"analysis": "N—S图(也称h盒图或CHAPIN图)和PAD(问题分析图)及PFD(程序流程图)是详细设计阶段的常用工具，E—R图即实体－联系图是数据库设计的常用工具。从题中图可以看出该图属于程序流程图。"
}, {
	"subject_title": "顺序存储结构的优点是（　　）。",
	"subject_choice_A": "删除运算方便",
	"subject_choice_B": "存储空间利用率高",
	"subject_choice_C": "插人运算方便",
	"subject_choice_D": "可以方便地运用到各种逻辑结构的存储表中",
	"subject_answer": "B",
	"analysis": "顺序结构逻辑上相邻的结点物理上也是相邻的。因此，其存储密度大，存储空间利用率高，但插入、删除运算操作不方便，需移动大量的结点。"
}, {
	"subject_title": "下列选项中属于字符串常量的是（　　）。",
	"subject_choice_A": "•abc•",
	"subject_choice_B": "”abc”",
	"subject_choice_C": "[abc]",
	"subject_choice_D": "(abc)",
	"subject_answer": "B",
	"analysis": "Java中字符串常量由双引号和其中间的字符所组成。"
}, {
	"subject_title": "算法的空间复杂度是指（　　）。",
	"subject_choice_A": "算法程序的长度",
	"subject_choice_B": "算法程序中的指令条数",
	"subject_choice_C": "算法程序所占的存储空间",
	"subject_choice_D": "算法执行过程中所需要的存储空间",
	"subject_answer": "D",
	"analysis": "算法的空间复杂度，是指执行这个算法所需的存储空间。算法所占用的存储空间包括算法程序所占用的空间、输入的初始数据所占用的存储空间及算法执行过程中所需要的额外空间。"
}, {
	"subject_title": "如果线程正处于运行状态，则它可能到达的下－个状态是（　　）。",
	"subject_choice_A": "只有终止状态",
	"subject_choice_B": "只有阻塞状态和终止状态",
	"subject_choice_C": "可运行状态、阻塞状态、终止状态",
	"subject_choice_D": "其他所有状态",
	"subject_answer": "C",
	"analysis": "下－个状态可以是可运行状态、阻塞状态、终止状态中的任－种。"
}, {
	"subject_title": "下列方法中可以用来创建一个新线程的是（　　）。",
	"subject_choice_A": "实现java．lang．Runnable接口并重写start（　　）方法",
	"subject_choice_B": "实现java．lang．Runnable接口并重写run（　　）方法",
	"subject_choice_C": "继承java．lang．Thread类并重写run（　　）方法",
	"subject_choice_D": "实现java．lang．Thread类并实现start（　　）方法",
	"subject_answer": "C",
	"analysis": "题考查考生对创建线程的使用。创建线程有两种方法：通过实现Runnable接口创建线程和通过继承Thread类创建线程。通过实现Runnable接口创建线程，当实现Runnable接口的类的对象用来创建线程以后，该线程的启动将使得对象的run（）方法被调用。通过继承Thread类创建线程，可以通过继承Thread类，并重写其中的run（）方法定义线程体，然后创建该子类的对象创建线程。线程创建是考试重点内容，请务必掌握。"
}, {
	"subject_title": "－棵二叉树的中序遍历结果为DBEAFC，前序遍历结果为ABDECF．则后序历结果为（　　）。",
	"subject_choice_A": "ACFBED",
	"subject_choice_B": "DFBECA",
	"subject_choice_C": "ABCDEF",
	"subject_choice_D": "DEBFCA",
	"subject_answer": "D",
	"analysis": "这类题型－般通过前序遍历的结果来找根结点，用中序遍历的结构找分支结点，通过画出该二叉树可得到结果。"
}, {
	"subject_title": "下列数据结构中，能用二分法进行查找的是（　　）。",
	"subject_choice_A": "顺序存储的有序线性表",
	"subject_choice_B": "线性链表",
	"subject_choice_C": "二叉链表",
	"subject_choice_D": "有序线性链表",
	"subject_answer": "A",
	"analysis": "二分法查找只适用于顺序存储的有序线性表，对于顺序存储的非有序线性表和线性链表，都只能呆用顺序查找。"
}, {
	"subject_title": "下列选项中，是软件调试技术的是（　　）。",
	"subject_choice_A": "错误推断",
	"subject_choice_B": "集成测试",
	"subject_choice_C": "回溯法",
	"subject_choice_D": "边界值分析",
	"subject_answer": "C",
	"analysis": "软件调试技术包括强行排错法、回溯法和原因排除法。边界值分析、错误推断都是黑盒测试的方法。"
}, {
	"subject_title": "在程序读人字符文件时，能够以该文件作为直接参数的类是（　　）。",
	"subject_choice_A": "FileReader",
	"subject_choice_B": "BufferedReader",
	"subject_choice_C": "FileInputStream",
	"subject_choice_D": "ObjeetInputStream",
	"subject_answer": "A",
	"analysis": "FileReader、BufferedReader是字符类输入流。FileInputStream是字节输入流。对象串行化时，需要使用ObjectInputStream类中提供的方法从对象流中读取对象。所以，在程序读入字符文件时，要使用字符流Fil—eReader或BufferedReader。但是FileReader的参数是读入的文件，而BufferedReader的参数是FileReader流的一个对象。因此，本题的正确答案是A。"
}, {
	"subject_title": "能够支持javadoc命令的注释语句是（　　）。",
	"subject_choice_A": "|**…//",
	"subject_choice_B": "/*…*/",
	"subject_choice_C": "//",
	"subject_choice_D": "/**…*/",
	"subject_answer": "D",
	"analysis": "本题考查Java中的注释语句。注释是程序设计的重要组成部分，应熟练掌握。Java中有三类注释语句：文档注释/**…*/，被javadoc处理，可以建立类的一个外部说明性文件，所以本题正确答案是选项D；C语言注释风格/*…*/，用于去掉当前不再使用但仍想保留的代码等；单行注释//，格式上要求注释符//后必须紧跟一个空格，然后才是注释信息。"
}, {
	"subject_title": "通常我们使用（　　）方法来为一个部件注册事件监听器。",
	"subject_choice_A": "add×××Listener",
	"subject_choice_B": "×××Listener",
	"subject_choice_C": "Listener×××",
	"subject_choice_D": "×××Listeneradd",
	"subject_answer": "A",
	"analysis": "本题考查事件监听器的概念。每类事件都有对应的事件监听器，监听器是接口，根据动作来定义方法。AwT的构件类中提供注册和注销监听器的方法。注册监听器：publicvoid add&lt;ListenerType&gt;(&lt;Listener—Type&gt;listener)；注销监听器：public void removed Listener—Type&gt;(&lt;ListenerType&gt;listener)。由此可见，选项A正确。"
}, {
	"subject_title": "下面排序算法中，平均排序速度最快的是（　　）。",
	"subject_choice_A": "冒泡排序法",
	"subject_choice_B": "选择排序法",
	"subject_choice_C": "交换排序法",
	"subject_choice_D": "堆排序法",
	"subject_answer": "D",
	"analysis": "在各种排序方法中，快速排序法和堆排序法的平均速度是最快的，因为它们的时间复杂度都是O(nlog2n)，其他的排序算法的时间复杂度大都是O(n2)。"
}, {
	"subject_title": "下列代码的执行结果是（　　）。",
	"subject_choice_A": "9．9",
	"subject_choice_B": "3",
	"subject_choice_C": "false",
	"subject_choice_D": "true",
	"subject_answer": "C",
	"analysis": "此题后半部分除数是0，按常理说应该报异常，且不会得出结果。但是在计算＆＆运算时采用了部分结果方法，即先运算前半部分，如果前半部分为假，则不必计算后半部分，整个结构为假，如果前半部分为真，这时才计算后半部分的值，在此，前部分已经为假，所以结果就不用计算后半部分。"
}, {
	"subject_title": "下列关于JavaApplication与Applet的说法中，正确的是（　　）。",
	"subject_choice_A": "都包含main（　　）方法",
	"subject_choice_B": "都通过“appletviewer”命令执行",
	"subject_choice_C": "都通过“javac”命令编译",
	"subject_choice_D": "都嵌入在HTML文件中执行",
	"subject_answer": "C",
	"analysis": "本题考查JavaApplication与Applet的区别。Applet与Application的主要区别在执行方式上，Ap—plication以main（）方法为入口点运行，Applet要在浏览器或appletviewer中运行，运行过程比Application更复杂。两者都是通过”javac”命令编译，所以只有选项C说法正确。"
}, {
	"subject_title": "下列选项中，不属于模块问耦合的是（　　）。",
	"subject_choice_A": "数据耦合",
	"subject_choice_B": "标记耦合",
	"subject_choice_C": "异构耦合",
	"subject_choice_D": "公共耦合",
	"subject_answer": "C",
	"analysis": "模块之间的耦合程度反映了模块的独立性，也反映了系统分解后的复杂程度。按照耦合程度从弱到强，可以将其分成7级，分别是非直接耦合、数据耦合、标记耦合、控制耦合、外部耦合、公共耦合和内容耦合。其中没有异构耦合这种方式。"
}, {
	"subject_title": "下列语句中，可以作为无限循环语句的是（　　）。",
	"subject_choice_A": "for(；；){}",
	"subject_choice_B": "for(int i＝0；i<10000；i＋＋){}",
	"subject_choice_C": "while(false){}",
	"subject_choice_D": "do{}while(false)",
	"subject_answer": "A",
	"analysis": "B的循环终止条件为l0000，C、D的终止条件为常量false，都不能无限循环。"
}, {
	"subject_title": "若数组a定义为int[][]a＝new int[3][4]，则a是（　　）。",
	"subject_choice_A": "－维数组",
	"subject_choice_B": "二维数组",
	"subject_choice_C": "三维数组",
	"subject_choice_D": "四维数组",
	"subject_answer": "B",
	"analysis": "二维数组有两种定义方式：①typear—rayName[][]；②type[][]arrayName；从题目中的语句可以看出，本题定义了一个二维数组。"
}, {
	"subject_title": "在设计程序时，应采纳的原则之－是（　　）。",
	"subject_choice_A": "不限制go to语句的使用",
	"subject_choice_B": "减少或取消注解行",
	"subject_choice_C": "程序越短越好",
	"subject_choice_D": "程序结构应有助于渎者理解",
	"subject_answer": "D",
	"analysis": "程序设计中，程序不要求长度，以结构清晰、易于理解为标准，程序员可以添加注释来助于理解，同时要尽量少用goto语句，否则会破坏程序的结构。"
}, {
	"subject_title": "阅读下列Java语句：\n　\n　\n在下画线处，应填的正确选项是（　　）。",
	"subject_choice_A": "File",
	"subject_choice_B": "FileWriter",
	"subject_choice_C": "FileOutputStream",
	"subject_choice_D": "Outputstream",
	"subject_answer": "C",
	"analysis": "ObjectOutputStream即继承了0utput－Stream抽象类，又实现了0bjectOutput接口，这是Java用接口技术代替双重继承的例子，其构造方法参数是串行化了的对象。所以，此处应为串行化的文件输出流。"
}, {
	"subject_title": "sum的值为0，则result＝sum＝＝0?1：num/sum的值为（　　）。",
	"subject_choice_A": "0",
	"subject_choice_B": "1",
	"subject_choice_C": "01",
	"subject_choice_D": "无法输出",
	"subject_answer": "B",
	"analysis": "本题考查条件运算符“?”的用法。该运算符是三元运算符，－般形式为：表达式?语句l：语句2。其中，表达式的值为－个布尔值，如果这个值为true，就执行语句1，否则执行语句2。此外语句1和语句2需要返回相同的数据类型，而且该类型不能是void。本题中sum＝＝0成立，故值为1。"
}, {
	"subject_title": "二维数组A[0，…，8][0，…，9]，其每个元素占2字节。从首地址400开始，按行优先顺序存储，则元素A[8][5]的存储地址为（　　）。",
	"subject_choice_A": "570",
	"subject_choice_B": "506",
	"subject_choice_C": "410",
	"subject_choice_D": "482",
	"subject_answer": "A",
	"analysis": "A[8]Es]元素存储的位置在第9行第6列，所以AE8]Es]之前存储的个数应为8×10＋5＝85，这些元素占用的空间为85×2字节＝170字节，所以A[8][5]的存储位置为400＋170＝570。"
}, {
	"subject_title": "在学生管理的关系数据库中，存取－个学生信息的数据单位是（　　）。",
	"subject_choice_A": "文件",
	"subject_choice_B": "数据库",
	"subject_choice_C": "字段",
	"subject_choice_D": "记录",
	"subject_answer": "D",
	"analysis": "－个数据库由－个文件或文件集合组成。这些文件中的信息可分解成－个个记录。"
}, {
	"subject_title": "下列程序的功能是统计字符串中“array”的个数，在程序的空白处应填入的正确选项是（　　）。\n　\n　\n　\n　",
	"subject_choice_A": "<",
	"subject_choice_B": "＝",
	"subject_choice_C": "<＝",
	"subject_choice_D": ">＝",
	"subject_answer": "D",
	"analysis": "在字符串中查询指定的字符或子串，可用indexof（）方法，如查询成功，返回所查字符的位置。如不成功，返回－l，从下面程序可以看出，While条件应为查询成功。"
}, {
	"subject_title": "String、StingBuffer都是（　　）类，都不能被继承。",
	"subject_choice_A": "static",
	"subject_choice_B": "abstract",
	"subject_choice_C": "final",
	"subject_choice_D": "private",
	"subject_answer": "C",
	"analysis": "final为最终类，该类不能有子类。"
}, {
	"subject_title": "下列命令中用于激活系统守候进程以便能够在Java虚拟机上注册和激活对象的是（　　）。",
	"subject_choice_A": "rmic",
	"subject_choice_B": "rmiregistry",
	"subject_choice_C": "rmid",
	"subject_choice_D": "serialver",
	"subject_answer": "C",
	"analysis": "Java语言的RMl包括：rmic、rmiregis－try、rmid、serialver。其中，命令rmid用于激活系统守候进程，以便能够在Java虚拟机上注册和激活对象。"
}, {
	"subject_title": "当启动Applet程序时，首先调用的方法是（　　）。",
	"subject_choice_A": "stop（　　）",
	"subject_choice_B": "init（　　）",
	"subject_choice_C": "start（　　）",
	"subject_choice_D": "destroy（　　）",
	"subject_answer": "B",
	"analysis": "本题考查Applet程序的运行方式。在Applet运行时，首先由浏览器调用init（）方法，所以选项B正确。初始化完成后，将调用start（）方法使Applet成为激活状态。当Applet被覆盖时，可用stop（）方法停止线程。关闭浏览器时调用destroy（），彻底终止Apptet，从内存中卸载并释放该Applet的所有资源。Applet的生命周期及其运行方式是考试重点，应该牢记。"
}, {
	"subject_title": "有下列二叉树，对此二叉树前序遍历的结果为（　　）。\n　\n　",
	"subject_choice_A": "XZCYAB",
	"subject_choice_B": "XYZABC",
	"subject_choice_C": "XYABCZ",
	"subject_choice_D": "XYAZBC",
	"subject_answer": "D",
	"analysis": "对二叉树的前序遍历是指：先访问根结点，然后访问左子树，最后访问右子树，并且，在访问左、右子树时，先访问根结点，再依次访问其左、右子树。"
}, {
	"subject_title": "下列特点中不属于Java的是（　　）。",
	"subject_choice_A": "多线程",
	"subject_choice_B": "多重继承",
	"subject_choice_C": "跨平台",
	"subject_choice_D": "动态性",
	"subject_answer": "B",
	"analysis": "Java不支持多重继承(子类只能有一个父类)。"
}, {
	"subject_title": "Component类中用于刷新组件的方法是（　　）。",
	"subject_choice_A": "getFont（　　）",
	"subject_choice_B": "getName（　　）",
	"subject_choice_C": "update（　　）",
	"subject_choice_D": "paint（　　）",
	"subject_answer": "C",
	"analysis": "getFont方法用来获取字体，getName方法用于获取组件的名字，paint方法用于绘制组件，update方法用于刷新组件。"
}, {
	"subject_title": "下列程序从标准输入设备－－键盘读入－个字符，然后输出到屏幕。要想完成此功能，画线处应该填入的语句为（　　）。\n　\n　",
	"subject_choice_A": "ch＝System．in．read（　　）；",
	"subject_choice_B": "ch＝(char)System．in．read（　　）；",
	"subject_choice_C": "ch＝(char)System．in．readln（　　）；",
	"subject_choice_D": "ch＝(int)System．in．read（　　）；",
	"subject_answer": "B",
	"analysis": "此题程序通过调用系统的标准输入流System．in的read（）方法，从键盘读入－个字符，由于read（）方法的返回值是int类型，而变量ch是字符类型，不能直接转换，因此需要进行强制类型转换，应该填入的正确语句是ch＝(char)System．In．read（）。"
}, {
	"subject_title": "下列叙述中，正确的是（　　）。",
	"subject_choice_A": "声明变量时必须指定－个类型",
	"subject_choice_B": "Java认为变量number与Number相同",
	"subject_choice_C": "Java中唯－的注释方式是“／／”",
	"subject_choice_D": "源文件中public类可以有0个或多个",
	"subject_answer": "A",
	"analysis": "本题考查Java的基本概念。Java的基本概念是考试重点，应该重视。在Java中，声明变量时，必须指定类型，否则将会出错，所以选项A说法正确。Java标识符是区分大小写的，变量number和Number对Java来说是不同的，选项B说法错误。Java中有三种注释方式：文档注释／**…*／，被javadoc处理，可以建立类的－个外部说明性文件；C语言注释风格／*…*／，用于去掉当前不再使用但仍想保留的代码等；单行注释／／，格式上要求注释符／／后必须紧跟－个空格，然后才是注释信息，选项C说法错误。源文件中public类可以有0个或l个，不能多于1个，选项D说法错误。"
}, {
	"subject_title": "软件测试目的是（　　）。",
	"subject_choice_A": "评估软件可靠性",
	"subject_choice_B": "发现并改正程序中的错误",
	"subject_choice_C": "改正程序中的错误",
	"subject_choice_D": "发现程序中的错误",
	"subject_answer": "D",
	"analysis": "软件测试的目的主要是在于发现软件错误，希望在软件开发生命周期内尽可能早的发现尽可能多的bug。"
}, {
	"subject_title": "以下（　　）命令能为远程对象生成stub和skelmon。",
	"subject_choice_A": "rmiregistry",
	"subject_choice_B": "serialver",
	"subject_choice_C": "rmic",
	"subject_choice_D": "rmid",
	"subject_answer": "C",
	"analysis": "本题考查J2SDK的RMI命令。rmiregistry命令是在当前主机的指定端口上启动远程对象注册服务程序；serialver命令是返回serialVersionUID的值；rmic命令为远程对象生成stub和skeleton；rmid命令可以激活系统守候进程，以便能够在Java虚拟机上注册和激活对象。"
}, {
	"subject_title": "如果应用程序要在Applet上显示输出，则必须重写的方法是（　　）。",
	"subject_choice_A": "Graphics．drawstring（　　）",
	"subject_choice_B": "repaint（　　）",
	"subject_choice_C": "paint（　　）",
	"subject_choice_D": "update（　　）",
	"subject_answer": "C",
	"analysis": "paint（）是绘制Applet界面的基本方法。"
}, {
	"subject_title": "下列不属于表达式语句的是（　　）。",
	"subject_choice_A": "＋＋i；",
	"subject_choice_B": "－－J；",
	"subject_choice_C": "b#a；",
	"subject_choice_D": "b*＝a；",
	"subject_answer": "C",
	"analysis": "前两项是自加减运算，最后－项是b＝b*a"
}, {
	"subject_title": "阅读下列程序片段。\n　\n　\n如果sayHello（　　）方法正常运行，则test（　　）方法的运行结果将是（　　）。",
	"subject_choice_A": "Hello",
	"subject_choice_B": "ArrayIndexOutOfBondsException",
	"subject_choice_C": "ExceptionFinally",
	"subject_choice_D": "HelloFinally",
	"subject_answer": "D",
	"analysis": "sayHello（）方法正常运行则程序不抛出异常，并执行finally，所以为符合选项D。"
}, {
	"subject_title": "阅读下列代码段。\n　\n　\n上述代码的编译结果是（　　）。",
	"subject_choice_A": "程序通过编译并且run（　　）方法可以正常输出递增的i值",
	"subject_choice_B": "程序通过编译，调用run（　　）方法将不显示任何输出",
	"subject_choice_C": "程序不能通过编译，因为while的循环控制条件不能为“true”",
	"subject_choice_D": "程序不能通过编译，因为run（　　）方法的返回值类型不是void",
	"subject_answer": "D",
	"analysis": "while的循环控制条件可以为true，run（）方法没有返回值，所以不能是int型，故此程序不能通过编译。"
}, {
	"subject_title": "下列程序的输出结果是（　　）。\n　\n　",
	"subject_choice_A": "编译未通过",
	"subject_choice_B": "编译通过，但运行错误",
	"subject_choice_C": "可以运行，但有错误",
	"subject_choice_D": "以上都不对",
	"subject_answer": "B",
	"analysis": "这是－道考查数组引用的题，目的是考查如何在程序中引用初始化后的数组。引用的方式为arrayName[index]，其中index为数组的下标，可以为整数、变量和表达式，范围从0开始，－直到数组的长度减l。在Java语言中，是要对数组下标进行检查的。因此。当程序运行到数组的长度值时，就发生了越界现象。"
}, {
	"subject_title": "栈s最多能容纳4个元素，现有6个元素按A、B、C、D、E、F的顺序进栈，下列（　　）序列不是可能的出栈序列。",
	"subject_choice_A": "C、B、E、D、A、F",
	"subject_choice_B": "C、D、B、F、E、A",
	"subject_choice_C": "A、D、E、C、B、F",
	"subject_choice_D": "A、F、E、D、C、B",
	"subject_answer": "D",
	"analysis": "栈的特性为后进先出，而栈S只能容纳4个元素。当F进栈时。说明栈中有已有B、C、D、E四个元素，所以F无法进栈。"
}, {
	"subject_title": "Java中的抽象类Reader和Writer所处理的流是（　　）。",
	"subject_choice_A": "图像流",
	"subject_choice_B": "对象流",
	"subject_choice_C": "字节流",
	"subject_choice_D": "字符流",
	"subject_answer": "D",
	"analysis": "Reader/Writer所处理的流是字符流，InputStream/OutputStream的处理对象是字节流。"
}, {
	"subject_title": "耦合性和内聚性是对模块独立性度量的两个标准，下列叙述中正确的是（　　）。",
	"subject_choice_A": "提高耦合性降低内聚性有利于提高模块的独立性",
	"subject_choice_B": "降低耦合性提高内聚性有利于提高模块的独立性",
	"subject_choice_C": "耦合性是指－个模块内部各个元素间彼此结合的紧密程度",
	"subject_choice_D": "内聚性是指模块间互相连接的紧密程度",
	"subject_answer": "B",
	"analysis": "耦合是指模块间相互连接的紧密程度，内聚性是指在－个模块内部各个元素间彼此之间接合的紧密程序。高内聚、低耦合有利于模块的独立性。"
}, {
	"subject_title": "Java语言中所有的简单数据类型都被包含在（　　）中。",
	"subject_choice_A": "java．sql",
	"subject_choice_B": "java．awt",
	"subject_choice_C": "java．lang",
	"subject_choice_D": "java．math",
	"subject_answer": "C",
	"analysis": "Java语言中，所有的简单数据类型都被包含在包Java．lang中。"
}, {
	"subject_title": "下面程序段的输出结果是（　　）。\n　\n　",
	"subject_choice_A": "01",
	"subject_choice_B": "12",
	"subject_choice_C": "10",
	"subject_choice_D": "21",
	"subject_answer": "B",
	"analysis": "本题考查switch-case-break的用法。每个分支语句后面必须有break语句，否则程序向下执行，直到遇到break语句或程序结束。所以该题i＝1时执行casel分支语句，而casel分支语句后没有break语句，程序继续向下执行case2分支语句，case2语句后有break语句，故程序不执行default分支语句。"
}, {
	"subject_title": "阅读下列代码片段\n　\n　\n在下画线处，应填的正确选项是（　　）。",
	"subject_choice_A": "Implementation",
	"subject_choice_B": "Inheritance",
	"subject_choice_C": "implements",
	"subject_choice_D": "extends",
	"subject_answer": "D",
	"analysis": "继承父类应使用的关键词为extends。"
}, {
	"subject_title": "下列关于boolean类型的叙述中，正确的是（　　）。",
	"subject_choice_A": "可以将boolean类型的数值转换为int类型的数值",
	"subject_choice_B": "可以将boolean类型的数值转换为字符串",
	"subject_choice_C": "可以将boolean类型的数值转换为char类型的数值",
	"subject_choice_D": "不能将boolean类型的数值转换为其他基本数据类型",
	"subject_answer": "D",
	"analysis": "由于基本数据类型中boolean类型不是数字型，所以基本数据类型的转换是除了boolean类型以外的其他7种类型之间的转换。"
}, {
	"subject_title": "在编写Java程序的时候，如果不为类的成员变量定义初始值，Java会给它们设置默认值，下列说法中不正确的是（　　）。",
	"subject_choice_A": "Byte的默认值是0",
	"subject_choice_B": "int的默认值是0",
	"subject_choice_C": "long的默认值是0．0L",
	"subject_choice_D": "float的默认值是0．0f",
	"subject_answer": "C",
	"analysis": "Long类型的默认值为OL，而不是0．0L。"
}, {
	"subject_title": "Class类的对象由（　　）自动生成，隐藏在．class文件中，它在运行时为用户提供信息。",
	"subject_choice_A": "Java编译器",
	"subject_choice_B": "Java解释器",
	"subject_choice_C": "Java new关键字",
	"subject_choice_D": "Java类分解器",
	"subject_answer": "A",
	"analysis": "．class文件是由编译器生成的。"
}, {
	"subject_title": "请阅读下列程序代码，然后将程序的执行结果补充完整。横线处应填写的内容是（　　）。\n程序代码：\n　\n　\n执行结果：\nIn Situation 0\nno Exception caught\nin Proc finally",
	"subject_choice_A": "In Situation 1",
	"subject_choice_B": "In Situation",
	"subject_choice_C": "with Catch",
	"subject_choice_D": "int iArray 1",
	"subject_answer": "A",
	"analysis": "本题考查考生阅读Java程序的能力。题目程序看似复杂，但流程非常简单。程序的public类是throwsException，类中定义了Proc(intsel)方法。程序入口是main（）方法，使用try-catch-finally来捕获Arithmet-icException和ArrayIndexoutOfBoundsException异常，这两个异常是关于算术异常或数组索引越界的异常。执行Proc(O)时，输出In Situation0和no Exception caught两条信息；执行Proe(1)时，输出In Situationl和in Proe finally两条信息。整个程序并未发生异常。"
}, {
	"subject_title": "Object类中的方法public int hashCode[]，在其子类中覆盖该方法时，其方法修饰符可以是（　　）。",
	"subject_choice_A": "protected",
	"subject_choice_B": "public",
	"subject_choice_C": "private",
	"subject_choice_D": "缺省",
	"subject_answer": "B",
	"analysis": "所有的类都是Object的子类，如果要覆盖Object的equals方法则必须覆盖hasCode方法，覆盖时的属性是public。"
}, {
	"subject_title": "当检索一个压缩文件时，首先要建立压缩文件输入流对象，该对象（　　）。",
	"subject_choice_A": "以选中的压缩文件为参数",
	"subject_choice_B": "以FileInputStream对象为参数",
	"subject_choice_C": "以InputStreamReader对象为参数",
	"subject_choice_D": "以BufferedReader对象为参数",
	"subject_answer": "B",
	"analysis": "本题考查压缩文件流的概念。当输入一个ZIP文件时要将ZIP文件作为FileInputStream构造方法的参数，所以选项B正确。而FileInputStream对象又作为ZiplnputStream构造方法的参数出现。这里的ZipInputStream对象在将压缩文件内的输入项作为字符文本读出时即作为InputStreamReader的构造方法参数出现。最后，In—putStreamReader对象作为BufferedReader的构造方法的参数，并且使用readLine（）方法将压缩文件输入项作为文本读出。"
}, {
	"subject_title": "下面程序段的输出结果为（　　）。\n　\n　",
	"subject_choice_A": "x＝10",
	"subject_choice_B": "x＝20",
	"subject_choice_C": "x＝6",
	"subject_choice_D": "编译不通过",
	"subject_answer": "C",
	"analysis": "本题考查在Java中静态变量(类变量)的用法。在题目程序段中生成了－个staticint y＝6类变量，在ClassA中调用的b．go(10)，只不过是在ClassB中的－个局部变量，通过调用ClassB中的go方法可以生成－个classA对象，并给这个新生成的对象赋以ClassA中的类变量y的值。从main（）方法作为入口执行程序，首先生成－个ClassB的对象，然后b．go(10)会调用ClassA，会给x和y赋值，x＝a．y后，x值为6，再返回去执行System．out．println(”x＝”＋b．x)语句，输出为x＝6，可见，正确答案为选项C。"
}, {
	"subject_title": "下列程序片段中，能通过编译的是（　　）。",
	"subject_choice_A": "public abstract class Animal{",
	"subject_choice_B": "public abstract class Animal{",
	"subject_choice_C": "public class Animal{",
	"subject_choice_D": "public abstract class Animal{",
	"subject_answer": "A",
	"analysis": "Java中一个类是一个abstract类的子类，它必须具体实现父类的abstract方法。如果一个类中含有abstract方法，那么这个类必须用abstract来修饰(abstract类也可以没有abstract方法)。有abstract方法的父类只声明，由继承他的子类实现。所以选A。"
}, {
	"subject_title": "Java语言中，对当前对象的父类对象进行引用的关键字是（　　）。",
	"subject_choice_A": "case",
	"subject_choice_B": "super",
	"subject_choice_C": "char",
	"subject_choice_D": "break",
	"subject_answer": "B",
	"analysis": "当子类隐藏了父类的变量，并重写了父类方法后，又要使用父类变量或父类被重写的方法时，可以通过super来实现对父类变量的访问和对父类方法的调用。"
}, {
	"subject_title": "在学生管理的关系数据库中，存取一个学生信息的数据单位是（　　）。",
	"subject_choice_A": "文件",
	"subject_choice_B": "数据库",
	"subject_choice_C": "字段",
	"subject_choice_D": "记录",
	"subject_answer": "D",
	"analysis": "一个数据库由一个文件或文件集合组成。这些文件中的信息可分解成一个个记录。"
}, {
	"subject_title": "自定义异常类的父类可以是（　　）。",
	"subject_choice_A": "Error",
	"subject_choice_B": "VirtuaMachineError",
	"subject_choice_C": "Exception",
	"subject_choice_D": "Tbread",
	"subject_answer": "C",
	"analysis": "自定义异常类都是Throwable及其子集，所以只有c选项可以做它的父类。"
}, {
	"subject_title": "下列代码的下画线处应填入的方法名是（　　）。\n　\n　",
	"subject_choice_A": "repaint",
	"subject_choice_B": "println",
	"subject_choice_C": "paint",
	"subject_choice_D": "show",
	"subject_answer": "C",
	"analysis": "这里使用－个继承自Applet的类来显示字符。主要方法是在paint（）方法中使用System．out．println（）显示。"
}, {
	"subject_title": "Java的反汇编命令是（　　）。",
	"subject_choice_A": "javap",
	"subject_choice_B": "javac",
	"subject_choice_C": "jdb",
	"subject_choice_D": "java",
	"subject_answer": "A",
	"analysis": "Javap命令是java反汇编命令，javac命令是java语言编译器，jdb是基于文本和命令行的调试工具，java命令是Java解释器。"
}, {
	"subject_title": "当－个Applet所在的Web页面被其他页面覆盖后，不可能被调用的Applet方法是（　　）。",
	"subject_choice_A": "destroy（　　）",
	"subject_choice_B": "init（　　）",
	"subject_choice_C": "stop（　　）",
	"subject_choice_D": "start（　　）",
	"subject_answer": "B",
	"analysis": "在javaApplet的生命周期中，共有4种状态，即4个3－法init（）、start（）、stop（）和destroy（）。在Applet装载时，调用init（）通知该Applet已被加载到浏览器中，使Applet执行－些基本初始化操作。"
}, {
	"subject_title": "按运算符的功能划分，运算符”＋＝”的类型是（　　）。",
	"subject_choice_A": "算术运算符",
	"subject_choice_B": "关系运算符",
	"subject_choice_C": "逻辑运算符",
	"subject_choice_D": "赋值运算符",
	"subject_answer": "D",
	"analysis": "本题考查Java中的运算符。按照功能划分，运算符可以分为算术运算符：＋、、*、/、％、＋＋、－－；关系运算符：&gt;、&lt;、&gt;＝、&lt;＝、＝＝、!＝；布尔逻辑运算符：!、＆＆、||；位运算符：&gt;&gt;、&lt;&lt;、&gt;&gt;&gt;、&amp;、|、＾、～；赋值运算符：＝、＋＝、－＝、8＝、/＝等；条件运算符：?：；其他：分量运算符、下标运算符[]等。"
}, {
	"subject_title": "下列描述中，正确的是（　　）。",
	"subject_choice_A": "在Serializable接口中定义了抽象方法",
	"subject_choice_B": "在Serializable接日中定义了常量",
	"subject_choice_C": "在Serializable接口中没有定义抽象方法，也没有定义常量",
	"subject_choice_D": "在Serializable接口中定义了成员方法",
	"subject_answer": "C",
	"analysis": "在java．io包中，接口Serializable是实现对象串行化的工具。实际上，Serializable接口是一个空接口，它里面既没有定义抽象方法，也没有定义常量。Serializ—able接口的目的只是简单地标识一个类的对象是可以被串行化的。"
}, {
	"subject_title": "下列代码中，将引起编译错误的行是（　　）。\n1)public class Exercise{\n2)public static void main(String args[]){\n3)floatf＝0．0；\n4)f＋＝1．0；\n5)}\n6)}",
	"subject_choice_A": "第2行",
	"subject_choice_B": "第3行",
	"subject_choice_C": "第4行",
	"subject_choice_D": "第6行",
	"subject_answer": "B",
	"analysis": "本题考查Java中的数据类型，应该掌握Java中的简单数据类型，以及相关运算。floatf＝0．0这个语句，想要定义一个浮点型变量f，并且初值为0．0，但由于Java认为如果数字后没有任何字母，则默认为double类型，而double是不能转换为float的，所以该语句错误，如果改为floatf＝0．Of，即可正确运行。"
}, {
	"subject_title": "当－个应用程序的所有非守护线程终止运行时，但仍然有守护线程在运行，应用程序将（　　）。",
	"subject_choice_A": "运行",
	"subject_choice_B": "阻塞",
	"subject_choice_C": "终止",
	"subject_choice_D": "休眠",
	"subject_answer": "C",
	"analysis": "本题考查线程的机制。守护线程是－类特殊的线程，它和普通线程的区别在于它并不是应用程序的核心部分，当一个应用程序的所有非守护线程终止运行时，即使仍然有守护线程在运行，应用程序也将终止；反之，只要有一个非守护线程在运行，应用程序就不会终止。守护线程－般被用于在后台为其他线程提供服务。可以通过调用方法isDaemon（）来判断一个线程是否是守护线程，也可以调用方法setDaemon（）来将一个线程设为守护线程。"
}, {
	"subject_title": "下列包中，包含JOptionPane类的是（　　）。",
	"subject_choice_A": "javax．swing",
	"subject_choice_B": "java．1ang",
	"subject_choice_C": "java．util",
	"subject_choice_D": "java．applet",
	"subject_answer": "A",
	"analysis": "Swing中提供了JOptionPane类来实现类似Windows平台下的MessageBox的功能，利用JOption－Pane类中的各个static方法来生成各种标准的对话框，实现显示出信息、提出问题、警告、用户输入参数等功能，且这些对话框都是模式对话框。"
}, {
	"subject_title": "设a＝8，则表达式a>>>2的值是（　　）。",
	"subject_choice_A": "1",
	"subject_choice_B": "2",
	"subject_choice_C": "3",
	"subject_choice_D": "4",
	"subject_answer": "B",
	"analysis": "本题具体考查对位运算符中无符号右移运算符的掌握。无符号右移运算符”&gt;&gt;&gt;”用于将－个数的各二进制位全部无符号右移若干位，与运算符”&gt;&gt;”不同的是左补0。在本题中，8的二进制表示l000，右移两位后变成了0010，对应的十进制数是2。"
}, {
	"subject_title": "以下各选项中能正确声明－个表示50个值为null的字符串数组的是（　　）。",
	"subject_choice_A": "string[]a；",
	"subject_choice_B": "string a[]；",
	"subject_choice_C": "char a[50][3]",
	"subject_choice_D": "string a[]＝new string[50]",
	"subject_answer": "D",
	"analysis": "本题考查对字符串数组变量声明的掌握。在Java语言中，typearrayName[]和type[]arrayName的效果－样，都表示声明－个数组。所以选项A和选项B的效果是－样的，对于本题来说都是不正确的，因为它们没有指明数组所包含的元素的个数；选项c是－个二维的字符数组，Java语言跟C语言不－样，在C语言中，－个二维的字符数组就可以表示－个－维的字符串数组。而在Java中，字符char是基本数据类型，字符串string则是以对象的形式来表示的。所以，char a[][]并不等价于stringa[]。而且，c选项并没有指明数组的长度；选项D正确地声明了－个长度为50的空字符串数组。"
}, {
	"subject_title": "软件(程序)调试的任务是（　　）。",
	"subject_choice_A": "诊断和改正程序中的错误",
	"subject_choice_B": "尽可能多地发现程序中的错误",
	"subject_choice_C": "发现并改正程序中的所有错误",
	"subject_choice_D": "确定程序中错误的性质",
	"subject_answer": "A",
	"analysis": "调试的目的是发现错误或导致程序失效的错误原因，并修改程序以修正错误。调试是测试之后的活动。"
}, {
	"subject_title": "阅读下面程序\n　\n　\n如果输出结果的第二行为bb＝a，那么第－行的输出结果是（　　）。",
	"subject_choice_A": "aa＝I",
	"subject_choice_B": "aa＝204",
	"subject_choice_C": "aa＝v",
	"subject_choice_D": "aa＝156",
	"subject_answer": "B",
	"analysis": "本题考查的是Java的基本数据类型及其运算。程序开始生成了一个字符型变量a和3个整型变量i、j、aa。而整型变量aa的初始值是a＋i，其中a是一个字符型变量。如何进行加法运算呢?Java语言规定，char型数据可以自动转换成int类型，转换的结果就是该字符的ASCIl码值。因此，整型变量aa的初始值为字符”h”的ASCIl码值加上l00。如果记住h的ASCIl码值是104，则直接就确定aa的初始值是204，选项B为正确答案。如果记不得h的ASCIl码，题目中则给出提示。题目中说”输出结果的第二行为bb＝a”，也就是字符bb的值为字符a，bb的生成语句是charbb＝(char)j，是把整型变量j的值强制转换为字符型。同样，把ASCIl码值为j(97)所对应的字符赋值给bb。显然，字符a的ASCIl码值为97，字符b的ASCIl码值为98，依次类推，字符b的ASCIl码为l04。因此．本题的正确答案是B。"
}, {
	"subject_title": "JDK中提供的文档生成器是（　　）。",
	"subject_choice_A": "javado",
	"subject_choice_B": "javap．exe",
	"subject_choice_C": "exe",
	"subject_choice_D": "javaprof．exe",
	"subject_answer": "A",
	"analysis": "在JDK中：javadoc．exe是文档生成器，将Java源代码和包以MML格式生成AP文档；java．exe是Java解释器；javap．exe是Java反汇编器；javaprof．exe是Java剖析工具，提供解释器剖析信息。"
}, {
	"subject_title": "在Java中，负责对字节代码解释执行的是（　　）。",
	"subject_choice_A": "垃圾回收器",
	"subject_choice_B": "虚拟机",
	"subject_choice_C": "编译器",
	"subject_choice_D": "多线程机制",
	"subject_answer": "B",
	"analysis": "本题考查Java语言的虚拟机。Java语言的执行模式是半编译半解释型。Java编写好的程序首先由编译器转换为标准字节代码，然后由Java虚拟机去解释执行。字节代码是－种二进制文件，但不能直接在操作系统上运行，可看做虚拟机的机器码。虚拟机把字节码程序与各操作系统和硬件分开，使Java程序独立于平台。Java中的虚拟机是非常重要的概念，是Java语言的基础，掌握后有助于理解Java语言的实现。"
}, {
	"subject_title": "在Java中，若要使用－个包中的类时，首先要求对该包进行导入，其关键字是（　　）。",
	"subject_choice_A": "import",
	"subject_choice_B": "package",
	"subject_choice_C": "include",
	"subject_choice_D": "packet",
	"subject_answer": "A",
	"analysis": "定义－个包要用package关键字，使用－个包中的类时，首先要使用import导入这些类所在的包。include为C语言的包含头文件的关键字，不是Java的。"
}, {
	"subject_title": "能打印出－个双引号的语句是（　　）。",
	"subject_choice_A": "System．out．println{\"\")；",
	"subject_choice_B": "System．out．println{\"*\")；",
	"subject_choice_C": "System．out．println{\"／\"}；",
	"subject_choice_D": "System．out．println{\"＼\"\")；",
	"subject_answer": "D",
	"analysis": "双引号字符的输出应使用转义字符。"
}, {
	"subject_title": "Java中的字符变量在内存中占位(bit)为（　　）。",
	"subject_choice_A": "4",
	"subject_choice_B": "8",
	"subject_choice_C": "16",
	"subject_choice_D": "24",
	"subject_answer": "C",
	"analysis": "字符变量在内存中占16位二进制数位，int变量在内存中占32位二进制数位。"
}, {
	"subject_title": "数据库应用系统中的核心问题是（　　）。",
	"subject_choice_A": "数据库设计",
	"subject_choice_B": "数据库系统设计",
	"subject_choice_C": "数据库维护",
	"subject_choice_D": "数据库管理员培训",
	"subject_answer": "A",
	"analysis": "数据库设计的目的是设计－个能满足用户要求，性能良好的数据库。所以数据库设计的核心是数据库应用。"
}, {
	"subject_title": "在Java中，线程是（　　）。",
	"subject_choice_A": "分时的",
	"subject_choice_B": "抢占式的",
	"subject_choice_C": "非抢占式的",
	"subject_choice_D": "非分时的",
	"subject_answer": "B",
	"analysis": "本题考查线程的调度。Java的线程调度策略是－种基于优先级的抢占式调度，选项B正确。Java这种抢占式调度可能是分时的，即每个等待池中的线程轮流执行，也可以不是，即线程逐个运行，具体呆用哪种方式，由具体JVM而定。线程－般通过使用sleep（）等方法保证给其他线程运行时间。"
}, {
	"subject_title": "JDK中，用（　　）命令对其源文件进行编译，生成字节码文件。",
	"subject_choice_A": "java．exe",
	"subject_choice_B": "javac．exe",
	"subject_choice_C": "javadoc．exe",
	"subject_choice_D": "javap．exe",
	"subject_answer": "B",
	"analysis": "本题考查JDK实用工具的使用。选项A错误，java．exe是Java语言解释器，直接从类文件执行Java应用程序字节代码，可接受class文件并启动Java虚拟机执行；选项B正确，javac．exe是Java语言编译器，将Java源代码转换成字节码；选项C错误，javadoc．exe是根据Java源代码及说明语句生成HTML，文档；选项D错误，javap．exe是反汇编器，显示编译类文件中的可访问功能和数据，同时显示字节代码含义。"
}, {
	"subject_title": "栈和队列的共同点是（　　）。",
	"subject_choice_A": "都是先进先出",
	"subject_choice_B": "都是先进后出",
	"subject_choice_C": "只允许在端点处插入和删除元素",
	"subject_choice_D": "没有共同特点",
	"subject_answer": "C",
	"analysis": "栈是只允许在表的－端进行插入和删除的操作，队列是允许在表的－端进行插入，另－端进行删除的操作。"
}, {
	"subject_title": "若特快订单是－种订单，则特快订单类和订单类的关系是（　　）。",
	"subject_choice_A": "使用关系",
	"subject_choice_B": "包含关系",
	"subject_choice_C": "继承关系",
	"subject_choice_D": "无关系",
	"subject_answer": "C",
	"analysis": "继承是允许将一个类定义为一个更通用类的特例。特殊类称为子类，通用类称为父类。除了订单类的属性外，特快订单类可能还有其他－些特殊属性。显然，订单类是通用类，即父类；而特快订单类是定单类的一个特例，是子类。订单类和特快订单类是继承关系。"
}, {
	"subject_title": "软件需求分析－般应确定的是用户对软件的（　　）。",
	"subject_choice_A": "功能需求",
	"subject_choice_B": "非功能需求",
	"subject_choice_C": "性能需求",
	"subject_choice_D": "功能需求和非功能需求",
	"subject_answer": "D",
	"analysis": "软件需求分析中需要构造－个完全的系统逻辑模型，理解用户提出的每－功能与性能要求，使用户明确自己的任务。因此，需求分析应确定用户对软件的功能需求和非功能需求。"
}, {
	"subject_title": "常常使用内部类来实现监听器接口，这是接口和内部类相结合的－个较为典型的例子，它属于（　　）。",
	"subject_choice_A": "整数处理",
	"subject_choice_B": "浮点数处理",
	"subject_choice_C": "事件处理",
	"subject_choice_D": "数据处理",
	"subject_answer": "C",
	"analysis": "常常使用内部类来实现监听器接口，这是接口和内部类相结合的－个较为典型的例子，它属于事件处理。"
}, {
	"subject_title": "下列方法中能完成主类实例初始化工作的是（　　）。",
	"subject_choice_A": "start（　　）",
	"subject_choice_B": "stop（　　）",
	"subject_choice_C": "init（　　）",
	"subject_choice_D": "paint（　　）",
	"subject_answer": "C",
	"analysis": "本题考查对Applet必须要重载的几个方法的理解。选项A错误，start（）方法使得程序从初始态进入运行态，当浏览器从图标状态恢复为窗口时，或者当用户离开包含Applet的主页后又再返回时，系统都会自动再执行－遍start（）方法；选项B错误，stop（）方法是和start（）方法相对应的，当浏览器变成图标或者是用户离开Apple*所在页面时，浏览器都会调用slop（）方法，该方法也是可以被多次调用的；选项c正确，当创建JavaApplet且第－次使用支持java的浏览器载入该Applet时，就会执行init（）方法，通常在这方法中执行－次性的初始化操作；选项D错误，paint（）方法是画图时必须要重载的方法。"
}, {
	"subject_title": "AWT中用来表示颜色的类是（　　）。",
	"subject_choice_A": "Font",
	"subject_choice_B": "Color",
	"subject_choice_C": "Panel",
	"subject_choice_D": "Dialog",
	"subject_answer": "B",
	"analysis": "AWT中Font是表示字体的类，Color是表示颜色的类，Panel是表示面板的类，Dialog是表示对话框的类。"
}, {
	"subject_title": "在软件开发中，需求分析阶段可以使用的工具是（　　）。",
	"subject_choice_A": "N—S图",
	"subject_choice_B": "DFD图",
	"subject_choice_C": "PAD图",
	"subject_choice_D": "程序流程图",
	"subject_answer": "B",
	"analysis": "在软件开发中，需求分析阶段常使用的工具有数据流图(DFD)、数据字典(DD)、判断树和判断表。"
}, {
	"subject_title": "下列事件监听器中，无法对TextField对象进行事件监听和处理的是（　　）。",
	"subject_choice_A": "ActionListener",
	"subject_choice_B": "FocusListener",
	"subject_choice_C": "MouseMotionListener",
	"subject_choice_D": "ChangeListener",
	"subject_answer": "D",
	"analysis": "本题考查AWT事件处理。事件就是发生在用户界面上的用户交互行为所产生的－种效果。每类事件都有对应的事件监听器，监听器就是接口。在单行文本输入区(TextField)构件上可能发生的事件包括：Fo-cusEvent焦点事件——焦点的获得和丢失，这类事件所对应的事件监听器是FocusListener；ActionEvent动作事件——按钮按下、TextField中按&lt;Enter&gt;键，这类事件所对应的事件监听器是ActionListener；MouseEvent鼠标事件——鼠标单击、释放、拖动、移动，这类事件所对应的事件监听器是MousetMotionListener。虽然还包括其他－些监听器，但是在所有事件及其所对应的事件监听器中，并不包括ChangeListener这样一个事件监听器。因此，本题的正确答案是D。"
}, {
	"subject_title": "下列选项中为单精度数的是（　　）。",
	"subject_choice_A": "2",
	"subject_choice_B": "5．2",
	"subject_choice_C": "0．2f",
	"subject_choice_D": "023",
	"subject_answer": "C",
	"analysis": "Java中单精度常量以f或F结尾。"
}, {
	"subject_title": "在方法内部使用，代表对当前对象自身引用的关键字是（　　）。",
	"subject_choice_A": "super",
	"subject_choice_B": "This",
	"subject_choice_C": "Super",
	"subject_choice_D": "this",
	"subject_answer": "D",
	"analysis": "super关键字为实现对父类变量的访问和对父类方法的调用。对当前对象自身的引用应使用this关键字。"
}, {
	"subject_title": "Java中用于提供Java语言、Java虚拟机的核心的类和接口的包是（　　）。",
	"subject_choice_A": "java．io包",
	"subject_choice_B": "java．applet包",
	"subject_choice_C": "java．lang包",
	"subject_choice_D": "java．net包",
	"subject_answer": "C",
	"analysis": "本题考查考生对Java语言中的类和接口的理解。java．lang包提供了构成Java语言、Java虚拟机核心的类和接口。例如，类object、类String和类Thread等。对任何一个Java程序来说，这些类几乎都是必不可少的。java．lang还包含了许多由Java虚拟机发出的异常，这些异常也是”类”的－种。另外，java．lang包还包含－些用于访问系统资源的类，如ClassLoader等。java．lang包具有极其重要的作用，在程序开头可以不必明文编写装载它的代码。"
}, {
	"subject_title": "要使下列程序能够正确运行，则横线处应填写的内容是（　　）。\n　\n　",
	"subject_choice_A": "int",
	"subject_choice_B": "start",
	"subject_choice_C": "paint",
	"subject_choice_D": "stop",
	"subject_answer": "C",
	"analysis": "Java中，继承applet类的子类需要实现以下方法：init（）、start（）、stop（）、destroy（）、paint(Graphicsg)方法。其中，paint(Graphics g)方法有－个参数g，是浏览器在运行Java Applet时产生的－个类Graphics的实例。"
}, {
	"subject_title": "数据独立性是数据库技术的重要特点之－。所谓数据独立性是指（　　）。",
	"subject_choice_A": "数据与程序独立存放",
	"subject_choice_B": "不同的数据被存放在不同的文件中",
	"subject_choice_C": "不同的数据只能被对应的应用程序所使用",
	"subject_choice_D": "以上三种说法都不对",
	"subject_answer": "D",
	"analysis": "数据独立性是数据库系统的一个最重要的目标之一，它使数据能独立于应用程序。数据独立性包括数据的物理独立性和逻辑独立性。物理独立性是指用户的应用程序与存储在磁盘上的数据库中数据是相互独立的。即数据在磁盘上怎样存储由DBMS管理，用户程序不需要了解，应用程序要处理的只是数据的逻辑结构，这样当数据的物理存储改变了，应用程序不用改变。逻辑独立性是指用户的应用程序与数据库的逻辑结构是相互独立的，即当数据的逻辑结构改变时，用户程序也可以不变。"
}, {
	"subject_title": "下列各项中属于合法标识符的是（　　）。",
	"subject_choice_A": "myid/2",
	"subject_choice_B": "＋void",
	"subject_choice_C": "－5",
	"subject_choice_D": "_vacl",
	"subject_answer": "D",
	"analysis": "Java语言的标识符是以字母、下画线和符号$为首字符的字符串，首字符后面可以跟字母、下画线、$和数字，且标识符是区分大小写的，标识符的字符数没有限制。A选项中含有非法符号”/”，故是错误的：B选项是以符号”＋”开始的字符串也不符合规则；同理，c选项也是错误的。"
}, {
	"subject_title": "下列选项中，与成员变量共同构成一个类的是（　　）。",
	"subject_choice_A": "关键字",
	"subject_choice_B": "方法",
	"subject_choice_C": "运算符",
	"subject_choice_D": "表达式",
	"subject_answer": "B",
	"analysis": "在类体中定义的两种成员，数据成员和成员函数，其中数据成员就是成员变量，而成员函数就是通常说的方法。"
}, {
	"subject_title": "数据库设计中，用E—R图来描述信息结构但不涉及信息在计算机中的表示，它属于数据库设计的（　　）。",
	"subject_choice_A": "需求分析阶段",
	"subject_choice_B": "逻辑设计阶段",
	"subject_choice_C": "概念设计阶段",
	"subject_choice_D": "物理设计阶段",
	"subject_answer": "C",
	"analysis": "E—R(Entity—Relationship)图为实体－联系图，提供了表示实体型、属性和联系的方戈．用来描述现实世界的概念模型。"
}, {
	"subject_title": "下列选项成员变量声明正确的是（　　）。",
	"subject_choice_A": "public protected final int i；",
	"subject_choice_B": "abstract ClaSS Fl{…}",
	"subject_choice_C": "private double height；",
	"subject_choice_D": "double weight{}",
	"subject_answer": "C",
	"analysis": "本题考查对成员变量的声明。成员变量的声明格式为：修饰符type变量名；其中type可以是java语言中的任意数据类型，而修饰符可以是public、protected，private，static，final，transient，volatile等。选项A错误，成员变量不能同时声明成public和protected。选项B是类的声明格式，并不是成员变量的声明。成员变量声明应以“；”结尾，选项D错误。选项c声明了－个私有的double型成员变量，为正确答案。"
}, {
	"subject_title": "用来导人已定义好的类或包的语句是（　　）。",
	"subject_choice_A": "main",
	"subject_choice_B": "import",
	"subject_choice_C": "public class",
	"subject_choice_D": "class",
	"subject_answer": "B",
	"analysis": "本题考查Java中的import语句。Java中使用import语句来导入已定义好的类或包，需要注意Ja－va语言的java．lang包是编译器自动导入的，编程时如果使用该包中的类，可省去import导入，如果要使用其他包中的类，必须用import导入。"
}, {
	"subject_title": "面向对象方法中，继承是指（　　）。",
	"subject_choice_A": "－组对象所具有的相似性质",
	"subject_choice_B": "一个对象具有另一个对象的性质",
	"subject_choice_C": "各对象之间的共同性质",
	"subject_choice_D": "类之间共享属性和操作的机制",
	"subject_answer": "D",
	"analysis": "继承：在程序设计中，继承是指子类自动享用父类的属性和方法，并可以增加新的属性和方法的－种机制。它是实现代码共享的重要手段，可以使软件更具有开放性、可扩充性，这是信息组织与分类的行之有效的方法，也是面向对象的主要优点之一。继承又分为单重继承和多重继承，单重继承是指子类只能继承一个父类的属性和操作；而多重继承是指子类可以继承了多个父类的属性和操作。Java是－种单重继承语言，而c＋＋是－种多重继承语言。"
}, {
	"subject_title": "下列关于数据的存储结构的叙述中，正确的是（　　）。",
	"subject_choice_A": "数据的存储结构是数据间关系的抽象描述",
	"subject_choice_B": "数据的存储结构是逻辑结构在计算机存储器中的实现",
	"subject_choice_C": "数据的存储结构分为线性结构和非线性结构",
	"subject_choice_D": "数据的存储结构对数据的具体实现没有影响",
	"subject_answer": "B",
	"analysis": "数据的存储结构是逻辑结构在计算机存储器中的实现。为了全面表示一个逻辑结构，它在存储器中的影响包括数据元素自身值的表示和数据元素的表示两方面。"
}, {
	"subject_title": "在堆栈类Sharedstack的定义中，为了保证堆栈在并发操作中数据的正确性，应在下画线处填人的修饰符是(两个下画线的填写内容相同)（　　）。\n　\n　",
	"subject_choice_A": "puhlic",
	"subject_choice_B": "不使用修饰符",
	"subject_choice_C": "private",
	"subject_choice_D": "protected",
	"subject_answer": "C",
	"analysis": "堆栈中为了保证访问数据的－致性，应该对类的数据进行封装，而实现类数据封装的级别是private。"
}, {
	"subject_title": "下面程序段的输出结果为（　　）。\n　\n　",
	"subject_choice_A": "a＝100 b＝200",
	"subject_choice_B": "a＝12 b＝45",
	"subject_choice_C": "a＝12 b＝200",
	"subject_choice_D": "a＝100 b＝45",
	"subject_answer": "B",
	"analysis": "本题考查构造方法及构造方法重载。Test类有两个构造方法，即使用了方法重载技术。不带参数的构造方法对类的实例变量进行特定数值的赋值，而带参数的构造方法根据参数对类的实例变量进行赋值。TestObil＝newTest(12，45)语句调用的是Test(intx，inty)，而TestObj2＝newTest（）调用的是Test（），注意根据参数个数来区分。"
}, {
	"subject_title": "下列有关接口的说法，正确的是（　　）。",
	"subject_choice_A": "接口与抽象类是相同的概念",
	"subject_choice_B": "实现－个接口必须实现接口的所有方法",
	"subject_choice_C": "接口之间不能有继承关系",
	"subject_choice_D": "－个类不可实现多个接口",
	"subject_answer": "B",
	"analysis": "ava的接口是为实现多继承并简化其复杂性。接口与抽象类非常相似，它将抽象推进到更深层次。－个类可实现许多接口，但只有同－个父类。所以只有选项B正确。"
}, {
	"subject_title": "在数据管理技术发展的三个阶段中，数据共享最好的是（　　）。",
	"subject_choice_A": "人工管理阶段",
	"subject_choice_B": "文件系统阶段",
	"subject_choice_C": "数据库系统阶段",
	"subject_choice_D": "3个阶段相同",
	"subject_answer": "C",
	"analysis": "数据管理技术的发展经历了3个阶段：人工管理阶段、文件系统阶段和数据库系统阶段。人工管理阶段无共享，冗余度大；文件管理阶段共享性差，冗余度大；数据库系统管理阶段共享性大，冗余度小。"
}, {
	"subject_title": "在创建线程时可以显式地指定线程组，此时可供选择的线程构造方法有（　　）种。",
	"subject_choice_A": "1",
	"subject_choice_B": "2",
	"subject_choice_C": "3",
	"subject_choice_D": "4",
	"subject_answer": "C",
	"analysis": "线程组是由java．lang包中的Thread－Group类实现的。在创建线程时可以显式地指定线程组，此时需要从如下三种线程构造方法中选择－种；publicThread(ThreadGroup group，Runnable target)；public Thread(ThreadGroup group，String name)；public Thread(ThreadGroup group，Runnable target，String name)。"
}, {
	"subject_title": "用下列4种排序方法，对一个已排好序(由小到大)的序列进行由小到大排序时，选择（　　）方法最好。",
	"subject_choice_A": "冒泡排序",
	"subject_choice_B": "直接选择排序",
	"subject_choice_C": "直接插入排序",
	"subject_choice_D": "归并排序",
	"subject_answer": "C",
	"analysis": "直接插入排序的基本算法是：当插入第i(i&gt;＝1)个对象时，前面的V[0]，V[1]，…，V[i－1]已经排好序，这时，用VEi]的关键码与V[i－1]，[i－2]…的关键码顺序进行比较，找到插入位置即将V[i]插入，原来位置上的对象则向后移。由此可知，直接插入排序法的关键码比较次数与对象的初始排列有关。在本题中，序列已经排好序，所以其i的取值达到了最大，也就是序列中元素的个数，其实根本无需比较和交换，所以这种方法是最佳的。"
}, {
	"subject_title": "下列关于HTML标记的说法，正确的是（　　）。",
	"subject_choice_A": "URLgetDocumentBase（　　）返回Applet主类的URL",
	"subject_choice_B": "URLgetCOdeBase（　　）返回包含Applet的HTML文件的URL",
	"subject_choice_C": "在HTML中不说明String getParameter(string name)的参数，该方法将返回”0”",
	"subject_choice_D": "HTML标记方法用于获取HTML文件中关于Applet的信息",
	"subject_answer": "D",
	"analysis": "本题考查Applet中HTML标记方法。URLgetDocumentBase（）返回包含Applet的HTML文件的URL，而不是返回Applet主类的URL，选项A错误。URLgetCOdeBase（）返回Applet主类的URL，而不是返回包含Applet的HTML文件的URL．选项B错误。StringgetParameter(slringname)返回定义在HTML文件的指定参数，如果指定参数在HTML中无说明，该方法将返回”null”，而不是”0”，因此选项C错误。"
}, {
	"subject_title": "关系数据库管理系统能实现的专门关系运算包括（　　）。",
	"subject_choice_A": "排序、索引、统计",
	"subject_choice_B": "选择、投影、连接",
	"subject_choice_C": "关联、更新、排序",
	"subject_choice_D": "显示、打印、制表",
	"subject_answer": "B",
	"analysis": "关系数据库管理系统能实现的专门关系运算包括选择、投影、连接。"
}, {
	"subject_title": "下列叙述中，正确的是（　　）。",
	"subject_choice_A": "Reader是－个读取字符文件的接口",
	"subject_choice_B": "Reader是－个读取数据文件的抽象类",
	"subject_choice_C": "Reader是－个读取字符文件的抽象类",
	"subject_choice_D": "Reader是－个读取字节文件的－般类",
	"subject_answer": "C",
	"analysis": "本题考查Reader类的概念。首先应该明确，Reader是－个抽象类，字符输入流都是抽象类Reader类的子类，它是用来读取字符文件的类。字符输出流都是Writer抽象类的子类。"
}, {
	"subject_title": "表达式(10*49．3)的类型是（　　）。",
	"subject_choice_A": "double",
	"subject_choice_B": "char",
	"subject_choice_C": "long",
	"subject_choice_D": "float",
	"subject_answer": "A",
	"analysis": "运算中自动类型转换按优先关系从低级数据转换成高级数据。规定的优先次序是byte，short，char→int→long→float→double。"
}, {
	"subject_title": "下列关于Java语言特点的叙述中，错误的是（　　）。",
	"subject_choice_A": "Java是面向过程的编程语言",
	"subject_choice_B": "Java支持分布式计算",
	"subject_choice_C": "Java是跨平台的编程语言",
	"subject_choice_D": "Java支持多线程",
	"subject_answer": "A",
	"analysis": "Java是新－代编程语言，具有很多特点：简单易学；利用面向对象技术；分布式计算；健壮性(鲁棒性)；安全性；跨平台(即体系结构中立)；可移植性；解释执行；高性能；多线程；动态性。因此，本题的正确答案是A。"
}, {
	"subject_title": "下列说法正确的是（　　）。",
	"subject_choice_A": "类FilelnputStream和FileOutputStream用来进行文件1/O处理，由它们所提供的方法可以打开本地主机上的文件，并进行顺序的读/写",
	"subject_choice_B": "通过类File的实例或者一个表示文件名称的字符串可以生成文件输人/输出流，在流对象生成的同时，文件被打开，但还不能进行文件读/写",
	"subject_choice_C": "对于InputStream和OutputStream来说，它们的实例都是是非顺序访问流，即只能进行顺序的读/写",
	"subject_choice_D": "当从标准输人流读取数据时，从键盘输人的数据直接输入到程序中",
	"subject_answer": "A",
	"analysis": "本题是考查对文件输入、输出流的理解。通过类File的实例或者一个表示文件名称的字符串可以生成文件输入/输出流，在流对象生成的同时，文件被打开，然后就可以进行文件读/写，选项B说法错误。对于InputStream和OutputStream来说，它们的实例都是顺序访问流，即只能进行顺序的读/写，选项C说法错误。当从标准输入流读取数据时，从键盘输入的数据被缓冲，按&lt;Enter&gt;键时，程序才会得到输入数据，选项D说法错误。"
}, {
	"subject_title": "已知－个有序线性表为(13，18，24，35，47，50，62，83，90，115，134)，当用二分法查找值为90的元素时，查找成功的比较次数为（　　）。",
	"subject_choice_A": "1",
	"subject_choice_B": "2",
	"subject_choice_C": "3",
	"subject_choice_D": "9",
	"subject_answer": "B",
	"analysis": "根据二分法查找需要两次：首先将90与表中间的元素50进行比较，由于90大于50，所以在线性表的后半部分查找；第二次比较的元素是后半部分的中间元素，即90，这时两者相等，即查找成功。"
}, {
	"subject_title": "下列关于Java语言中线程的叙述中，正确的是（　　）。",
	"subject_choice_A": "线程由代码、数据、内核状态和－组寄存器组成",
	"subject_choice_B": "线程间的数据是不共享的",
	"subject_choice_C": "用户只能通过创建Thread类的实例或者定义和创建Thread子类的实例，建立和控制自己的线程",
	"subject_choice_D": "因多线程并发执行而引起的执行顺序的不确定性可能造成执行结果的不确定",
	"subject_answer": "D",
	"analysis": "本题考查线程的基本知识。线程与进程在概念上是相关的，线程是由表示程序运行状态的寄存器、程序计数器、栈指针以及堆栈组成，它不包含进程地址空间中的代码和数据。代码所操作的数据是Java线程模型中的一个组成部分，数据与代码是独立的。数据可以被多个线程共享，也可不共享。Java语言中提供两种创建线程的方法，－种是通过继承Thread类创建线程，另－种是通过实现Runnable接口来创建线程。"
}, {
	"subject_title": "JDK中用于存放Java类库文件的文件夹是（　　）。",
	"subject_choice_A": "bin",
	"subject_choice_B": "include",
	"subject_choice_C": "lib",
	"subject_choice_D": "demo",
	"subject_answer": "C",
	"analysis": "本题考查JDK的文件夹结构。bin文件夹下存放可执行文件。include存放Java标准类的源代码。demo文件夹存放Java例子程序。"
}, {
	"subject_title": "下列程序的输出结果是（　　）。\n　\n　",
	"subject_choice_A": "The value is 8",
	"subject_choice_B": "The value is 9",
	"subject_choice_C": "The value is 10",
	"subject_choice_D": "The value is ll",
	"subject_answer": "C",
	"analysis": "此题考查的是do－while循环和“－－”操作符的知识。do－while最少执行－次，在执行完do中的内容后，判断while中的条件是否为true。如果为true，就再执行do中的内容，然后进行判断。以此类推，直到while的判断为false时退出循环，执行循环后面的内容。而“－－”操作符的规则是，变量右边的“－”将先进行运算，然后才使变量的值减－。而在变量左边的“－－”，则先将变量的值减1再运算。本程序中i的值为10，当程序运行到do－while循环时，程序先执行－次循环，然后判断，因此选C。"
}, {
	"subject_title": "为了支持压栈线程与弹栈线程之间的交互与同步，在程序的下画线处依次填入的语句是（　　）。\n　\n　",
	"subject_choice_A": "synchronized（　　）",
	"subject_choice_B": "synchronized",
	"subject_choice_C": "synchronized",
	"subject_choice_D": "Serializable",
	"subject_answer": "B",
	"analysis": "在Synchronized块中等待共享数据的状态改变时调用wait（）方法，这样该线程进入等待状态暂时释放共享数据对象的锁。"
}, {
	"subject_title": "下列关于顺序存储结构的叙述中，错误的是（　　）。",
	"subject_choice_A": "存储密度大",
	"subject_choice_B": "某些非线性结构也可以采用顺序方法存储",
	"subject_choice_C": "结点中只有自身信息域，没有链接信息域",
	"subject_choice_D": "便于进行插入、删除等运算操作",
	"subject_answer": "D",
	"analysis": "顺序结构每个结点只包含自身的信息域，且逻辑上相邻的结点物理上也是相邻的。因此其存储密度大，但插入、删除运算操作不方便，需移动大量的结点。"
}, {
	"subject_title": "软件按功能可以分为应用软件、系统软件和支撑软件(或工具软件)。下面属于应用软件的是（　　）。",
	"subject_choice_A": "调试程序",
	"subject_choice_B": "操作系统",
	"subject_choice_C": "教务管理系统",
	"subject_choice_D": "汇编程序",
	"subject_answer": "C",
	"analysis": "编译程序和汇编程序属于开发工具，操作系统属于系统软件，而教务管理系统属于应用软件。"
}, {
	"subject_title": "使用如下（　　）保留字可以使只有在定义该类的包中的其他类才能访问该类。",
	"subject_choice_A": "abstract",
	"subject_choice_B": "private",
	"subject_choice_C": "protected",
	"subject_choice_D": "不使用保留字",
	"subject_answer": "D",
	"analysis": "本题考查类的修饰符。类的默认访问控制策略是不使用保留字来定义类，这会限制其他包中的类访问该类，该类只能被同－个包的类访问和引用，也不能用import语句引用，选项D正确。protected保留字不起作用，具有protected成员的类的子类可以在包外访问这些被保护的成员。abstract修饰符修饰的类被称为抽象类，没有具体对象的概念类，不满足题意。private修饰符修饰的类只能被该类自身访问和修改，而不能被任何其他类获取和引用，不满足题意。可见本题正确答案为选项D。"
}, {
	"subject_title": "下列关于Applet的安全限制的叙述中，错误的是（　　）。",
	"subject_choice_A": "通常情况下，禁止Applet读、写本地文件系统",
	"subject_choice_B": "通常情况下，禁止Applet向Applet源主机之外的任何主机建立网络连接",
	"subject_choice_C": "通常情况下，禁止Applet读取系统信息",
	"subject_choice_D": "通常情况下，禁止Applet加载本地库或方法",
	"subject_answer": "C",
	"analysis": "本题考查Applet的安全限制。许多浏览器为了保护本地主机，－般情况下，对Applet作了如下安全限制：Applet不能运行任何本地可执行程序；禁止Applet读、写本地计算机的文件系统；禁止加载本地库或方法。Applet只能使用自身的代码或Applet浏览器提供的JavaAPl；禁止向提供Applet之外的任何主机建立网络连接；不能读取某些系统信息。除了Java版本号、操作系统名等－些简单信息外，Applet不能获得与本地计算机有关的任何信息。根据上述介绍可知，Applet只能读取有限的系统信息，但不是－点几都不能读取。因此，本题的正确答案是C。"
}, {
	"subject_title": "支持子程序调用的数据结构是（　　）。",
	"subject_choice_A": "栈",
	"subject_choice_B": "树",
	"subject_choice_C": "队列",
	"subject_choice_D": "二叉树",
	"subject_answer": "A",
	"analysis": "根据栈的定义，栈是－种限定在－端进行插入与删除的线性表。在主函数调用子函数时，主函数会保持当前状态，然后转去执行子函数，把子函数的运行结果返回到主函数，主函数继续向下执行，这种过程符合栈的特点。所以－般采用栈式存储方式。"
}, {
	"subject_title": "能向内部直接写入数据的流是（　　）。",
	"subject_choice_A": "FileOutputStream",
	"subject_choice_B": "FileInputStream",
	"subject_choice_C": "ByteArrayOutputStream",
	"subject_choice_D": "ByteArrayInputStream",
	"subject_answer": "C",
	"analysis": "本题考查Java的内存读写。在java．io中，还提供了ByteArrayInputStream、ByteArrayOutput－Stream和StringBufferInputStream类可直接访问内存，它们是InputStream和OutputStream的子类。用ByteArrayOut-putStream可向字节数组写入数据；ByteArraylnputStream可从字节数组中读取数据。"
}, {
	"subject_title": "在长度为z的有序线性表中进行二分查找，最坏情况下需要比较的次数是（　　）。",
	"subject_choice_A": "（　　）(n)",
	"subject_choice_B": "（　　）(n2)",
	"subject_choice_C": "（　　）(log2n)",
	"subject_choice_D": "（　　）(nlog2n)",
	"subject_answer": "C",
	"analysis": "对于长度为n的有序线性表，在最坏情况下，二分法查找只需比较log2n次，而顺序查找需要比较n次。"
}, {
	"subject_title": "模块独立性是软件模块化所提出的要求，衡量模块独立性的度量标准是模块的（　　）。",
	"subject_choice_A": "抽象和信息隐蔽",
	"subject_choice_B": "局部化和封装化",
	"subject_choice_C": "内聚性和耦合性",
	"subject_choice_D": "激活机制和控制方法",
	"subject_answer": "C",
	"analysis": "模块的独立性是评价设计好坏的重要度量标准。衡量软件的模块独立性使用耦合性和内聚性两个定性的度量标准。"
}, {
	"subject_title": "在多线程程序设计中，如果采用继承Thread类的方式创建线程，则需要重写Thread类的（　　）方法。",
	"subject_choice_A": "start",
	"subject_choice_B": "10cal",
	"subject_choice_C": "interrupt",
	"subject_choice_D": "run",
	"subject_answer": "D",
	"analysis": "Thread类本身实现了Runnable接口，所以可以通过继承Thread类，并重写run（）方法定义线程体，然后创建该子类的对象创建线程。"
}, {
	"subject_title": "下面程序段的输出结果为（　　）。\n　\n　",
	"subject_choice_A": "a＝true b＝false",
	"subject_choice_B": "a＝true b＝false",
	"subject_choice_C": "a＝true b＝true",
	"subject_choice_D": "a＝false b＝false",
	"subject_answer": "C",
	"analysis": "本题考查关系运算符&lt;和＝＝。题目中a＝(3&lt;5)；比较3和5的大小，因为，3&lt;5，返回true给a；b＝(a＝＝true)；判断a是否为真，因为a确实为真，返回true给b；c＝(b＝＝false)；判断h是否为假，因为b不为假，返回false给c。最后结果a＝true，b＝true，b＝true，C＝false，选项C正确。"
}, {
	"subject_title": "一个栈的初始状态为空。现将元素1、2、3、4、5、A、B、c、D、E依次人栈，然后再依次出栈，则元素出栈的顺序是（　　）。",
	"subject_choice_A": "12345ABCDE",
	"subject_choice_B": "EDCBA54321",
	"subject_choice_C": "ABCDE12345",
	"subject_choice_D": "54321EDCBA",
	"subject_answer": "B",
	"analysis": "栈是按照“先进后出”或“后进先出”的原则组织数据的，所以出栈顺序是EDCBA54321。"
}, {
	"subject_title": "下列程序的运行结果是（　　）。",
	"subject_choice_A": "errorl：10．5",
	"subject_choice_B": "error2",
	"subject_choice_C": "errorl：10．5 error2",
	"subject_choice_D": "以上都不对",
	"subject_answer": "C",
	"analysis": "try-catch块是可以嵌套分层的，并且通过异常对象的数据类型来进行匹配，以找到正确的catchblock异常错误处理代码。以下是通过异常对象的数据类型来进行匹配找到正确的catchblock的过程。①首先在抛出异常的try－catch块中查找catch block，按顺序先与第一个catch block块匹配，如果抛出的异常对象的数据类型与catch block中传入的异常对象的临时变量(就是catch语句后面参数)的数据类型完全相同，或是它的子类型对象，则匹配成功，进入到catch block中执行，否则到第2步：②如果有两个或更多的catch block，则继续查找匹配第二个、第三个，直至最后一个catch block，如匹配成功，则进入到对应的catch block中执行，否则到第3步；③返回到上－级的trycatch块中，按规则继续查找对应的catch block。如果找到，进入到对应的catch block中执行，否则到第4步；④再到上上级的try—catch块中，如此不断递归，直到匹配到顶级的try—catch块中的最后一个catch block，如果找到，进入到对应的catch block中执行；否则程序将会执行terminate（）退出。所以本题选C。"
}, {
	"subject_title": "Java中的抽象类Reader和Writer所处理的流是（　　）。",
	"subject_choice_A": "图像流",
	"subject_choice_B": "对象流",
	"subject_choice_C": "字节流",
	"subject_choice_D": "字符流",
	"subject_answer": "D",
	"analysis": "Reader/Writer所处理的流是字符流，InputStream/Out put Stream的处理对象是字节流。"
}, {
	"subject_title": "下列选项中为单精度数的是（　　）。",
	"subject_choice_A": "2",
	"subject_choice_B": "5．2",
	"subject_choice_C": "0．2f",
	"subject_choice_D": "023",
	"subject_answer": "C",
	"analysis": "Java中单精度常量以f或F结尾。"
}, {
	"subject_title": "软件工程的理论和技术性研究的内容主要包括软件开发技术和（　　）。",
	"subject_choice_A": "消除软件危机",
	"subject_choice_B": "软件工程管理",
	"subject_choice_C": "程序设计自动化",
	"subject_choice_D": "实现软件可重用",
	"subject_answer": "B",
	"analysis": "基于软件工程的目标，软件工程的理论和技术性研究的内容主要包括软件开发技术和软件工程管理。"
}, {
	"subject_title": "为使下列代码正常运行，应该在下画线处填入的选项是（　　）。\n　\n　",
	"subject_choice_A": "size",
	"subject_choice_B": "length",
	"subject_choice_C": "dimension",
	"subject_choice_D": "measurement",
	"subject_answer": "B",
	"analysis": "length表示数组的长度。"
}, {
	"subject_title": "Java语言和C＋＋语言相比，下面哪项内容是Java独有的（　　）。",
	"subject_choice_A": "面向对象",
	"subject_choice_B": "动态链接",
	"subject_choice_C": "有类库",
	"subject_choice_D": "跨平台",
	"subject_answer": "D",
	"analysis": "C＋＋语言和Java语言都是面向对象的程序设计语言；库文件(．dll)就是C＋＋语言的动态链接库，这两种语言都有类库，因为类是面向对象的最基本的概念；跨平台的特性是Java语言所特有的，在不同的操作系统上，只要装有JVM就可以解释执行Java程序，而C＋＋语言没有这种特性。"
}, {
	"subject_title": "下列关于Java布尔类型的描述中，正确的是（　　）。",
	"subject_choice_A": "－种基本的数据类型，它的类型名称为boolean",
	"subject_choice_B": "用int表示类型",
	"subject_choice_C": "其值可以赋给int类型的变量",
	"subject_choice_D": "有两个值，l代表真，0代表假",
	"subject_answer": "A",
	"analysis": "布尔类型数据只有两个值：true(真)、false(假)，不对应任何数字，不能与数字进行转换，布尔类型数据－般用于逻辑判别。"
}, {
	"subject_title": "在读字符文件Employee．dat时，使用该文件作为参数的类是（　　）。",
	"subject_choice_A": "BufferedReader",
	"subject_choice_B": "DataInputStream",
	"subject_choice_C": "DataOutputStream",
	"subject_choice_D": "FilelnputStream",
	"subject_answer": "D",
	"analysis": "本题考查java．io包中的字符输入流。Java的输入输出包括字节流、文件流和对象流等，要注意区分不同流使用的不同类。字符类输入流都是抽象类InputStreamReader及其子类FileReader、BuIferedReader等。选项A中BufferedReader是把缓冲技术用于字符输入流，提高了字符传送的效率，但它不能处理文件流。选项B中DataInputStream类是用来处理字节流的，实现了DataInput接口，不能处理文件流。选项C中DataOutputStream类实现了DataOutput接口，不能处理文件流。选项D中FileInput－Stream可对－个磁盘文件涉及的数据进行处理，满足题目要求。"
}, {
	"subject_title": "为了提高软件模块的独立性，模块之间最好是（　　）。",
	"subject_choice_A": "控制耦合",
	"subject_choice_B": "公共耦合",
	"subject_choice_C": "内容耦合",
	"subject_choice_D": "高内聚低耦合",
	"subject_answer": "D",
	"analysis": "耦合性与内聚性是模块独立性的两个定性标准，－般的程序设计都会尽量做到高内聚、低耦合，有利于提高模块的独立性。"
}, {
	"subject_title": "在关系A(S，SN，D)和关系B(D，CN，NM)中，A的主关键字是s，B的主关键字是D，则关系A的外码是（　　）。",
	"subject_choice_A": "CN",
	"subject_choice_B": "SN",
	"subject_choice_C": "S",
	"subject_choice_D": "D",
	"subject_answer": "D",
	"analysis": "外码用于建立和加强两个关系之间的连接，通过将保存关系中主键值的－列或多列属性添加到另－个关系中，可建立两个关系之间的联系，这个列属性称为第二关系的外码。"
}, {
	"subject_title": "数据库技术的根本目标是要解决数据的（　　）。",
	"subject_choice_A": "存储问题",
	"subject_choice_B": "共享问题",
	"subject_choice_C": "安全问题",
	"subject_choice_D": "保护问题",
	"subject_answer": "B",
	"analysis": "在数据库系统中，需要对数据进行集合、统－的管理，以达到被多个应用程序共享的目标。"
}, {
	"subject_title": "相对于数据库系统，文件系统的主要缺陷有数据依赖、数据不一致性和（　　）。",
	"subject_choice_A": "可重用性差",
	"subject_choice_B": "安全性差",
	"subject_choice_C": "非持久性",
	"subject_choice_D": "冗余性",
	"subject_answer": "D",
	"analysis": "文件系统所管理的数据文件基本上是分散、相互独立的。因此相对于数据库系统，以此为基础的数据处理存在3个缺点：数据冗余大、数据的不－致性、程序与数据的相互依赖(简称为数据依赖)。"
}, {
	"subject_title": "下列代码中的内部类名是（　　）。\n　\n　",
	"subject_choice_A": "Timer",
	"subject_choice_B": "ActionListener",
	"subject_choice_C": "listener",
	"subject_choice_D": "匿名",
	"subject_answer": "B",
	"analysis": "内部类就是在类内部重新定义的新类，该类能连接外部类，但是不能和外部类进行通信。Actionl。－istenser有自己的类方法体，而Timer没有，只是实例化了－个Timer对象。"
}, {
	"subject_title": "－棵二叉树有10个度为l的结点，7个度为2的结点，则该二叉树共有结点个数为（　　）。",
	"subject_choice_A": "8",
	"subject_choice_B": "25",
	"subject_choice_C": "17",
	"subject_choice_D": "7",
	"subject_answer": "B",
	"analysis": "在任意－棵二叉树中，度数为0的结点(即叶子结点)总比度为2的结点多－个，因此该二叉树中叶子结点为7＋1＝8，8＋17＝25。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "顺序存储结构的存储－定是连续的，链式存储结构的存储空间不－定是连续的",
	"subject_choice_B": "顺序存储结构只针对线性结构。链式存储结构只针对非线性结构",
	"subject_choice_C": "顺序存储结构能存储有序表，链式存储结构不能存储有序表",
	"subject_choice_D": "链式存储结构比顺序存储结构节省存储空间",
	"subject_answer": "A",
	"analysis": "顺序存储方式主要用于线性数据结构，它把逻辑上相邻的数据元素存储在物理上相邻的存储单元里，结点之间的关系由存储单元的邻接关系来体现。链式存储结构的存储空间不－定是连续的。"
}, {
	"subject_title": "下列与算法有关的叙述中，不正确的是（　　）。",
	"subject_choice_A": "运算是数据结构的一个重要方面，运算的实现步骤用算法来描述",
	"subject_choice_B": "算法是精确定义的－系列规则，它指出怎样从给定的输入信息经过有限步骤产生所求的输出信息",
	"subject_choice_C": "算法的设计采用由粗到细，由抽象到具体的逐步求精的方法",
	"subject_choice_D": "对于算法的分析，指的是分析算法运行所要占用的机器时间，即算法的时间代价",
	"subject_answer": "D",
	"analysis": "算法是－系列解决问题的清晰指令，也就是说，能够对－定规范的输入，在有限时间内获得所要求的输出。算法常常含有重复的步骤和－些比较或逻辑判断。如果一个算法有缺陷，或不适合于某个问题，执行这个算法将不会解决这个问题。不同的算法可能用不同的时间、空间或效率来完成同样的任务。一个算法的优劣可以用空间复杂度与时间复杂度来衡量，也就是算法分析，因此选项D错误。算法设计－般采用由粗到细、由抽象到具体的初步求精的方法。"
}, {
	"subject_title": "下列关于线程优先级的说法中，正确的是（　　）。",
	"subject_choice_A": "线程的优先级是不能改变的",
	"subject_choice_B": "线程的优先级是在创建线程时设置的",
	"subject_choice_C": "在创建线程后的任何时候都可以设置",
	"subject_choice_D": "B和C",
	"subject_answer": "C",
	"analysis": "本题考查线程优先级的概念。首先应该了解Java的线程是有优先级的，并且可以控制其优先级，可以排除选项A；选项B和选项C本身就矛盾，故选项D是错误的，B和c不能同时选择。线程的优先级在创建线程时可以设置，也可以通过getPriority（）方法来获得线程的优先级，通过setPriority（）方法来设定线程的优先级。线程的优先级属于考试重点内容，应该重点掌握。"
}, {
	"subject_title": "JDBC是面向（　　）的。",
	"subject_choice_A": "过程",
	"subject_choice_B": "对象",
	"subject_choice_C": "应用",
	"subject_choice_D": "用户",
	"subject_answer": "B",
	"analysis": "JDBC中定义了－组标准的应用程序接口(API)，这些API是－种面向对象的封装和重新设计的接口，使得用户能够编写不依赖于数据库厂商的数据库应用程序。"
}, {
	"subject_title": "以下不是APPLET标记的选项是（　　）。",
	"subject_choice_A": "PARAM",
	"subject_choice_B": "BODY",
	"subject_choice_C": "CODEBASE",
	"subject_choice_D": "ALT",
	"subject_answer": "B",
	"analysis": "<IMG _djrealurl=\"/uploads/11/295185/images/201404/13980767293067.jpg\" src=\"https://img.examcoo.com/paper/295185/201404/13980767293067.jpg\">"
}, {
	"subject_title": "下面描述中，不属于软件危机表现的是（　　）。",
	"subject_choice_A": "软件过程不规范",
	"subject_choice_B": "软件开发生产率低",
	"subject_choice_C": "软件质量难以控制",
	"subject_choice_D": "软件成本不断提高",
	"subject_answer": "A",
	"analysis": "①对软件开发的进度和费用估计不准确；②用户对已完成的软件系统不满意的现象时常发生；③软件产品的质量往往靠不住；④软件常常是不可维护的；⑤软件通常没有适当的文档；⑥软件成本在计算机系统总成本中所占的比例逐年上升；⑦软件开发生产率提高的速度，远远跟不上计算机应用迅速普及深入的趋势。"
}, {
	"subject_title": "继承是面向对象编程的－个重要特征，它可降低程序的复杂性并使代码（　　）。",
	"subject_choice_A": "可读性好",
	"subject_choice_B": "可重用",
	"subject_choice_C": "可跨包访问",
	"subject_choice_D": "运行更安全",
	"subject_answer": "B",
	"analysis": "继承性是面向对象方法的－个重要基本特性，它使代码可重用，可降低程序复杂性。对－个类的继承是指在现有类(父类)的基础上构建－个新类(子类)，子类重用(继承)了父类的方法和状态，同时还可以向新类中增添新的方法和状态。"
}, {
	"subject_title": "下列说法中不正确的是（　　）。",
	"subject_choice_A": "Java语言中的事件都是继承自Java．awt．AW－TEvent类",
	"subject_choice_B": "AWTEvent类是Event（　　）bject类的子类",
	"subject_choice_C": "Java的AwT事件分为低级事件和高级事件",
	"subject_choice_D": "ActionEvent类是AWTEvent类的子类",
	"subject_answer": "A",
	"analysis": "Java中所有的AwT事件类是由Java．awt．AWTEvent类派生的。而Java中的事件类是继承自java．util．Event类，java．awt．AWTEvent是java．util．Event的子类。"
}, {
	"subject_title": "结构化程序设计的3种基本结构是（　　）。",
	"subject_choice_A": "过程、子程序和分程序",
	"subject_choice_B": "顺序、选择和重复",
	"subject_choice_C": "递归、堆栈和队列",
	"subject_choice_D": "调用、返回和转移",
	"subject_answer": "B",
	"analysis": "程序的三种基本控制结构包括：顺序、选择和重复(循环)，这三种结构就足以表达出各种其他形式的结构。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "栈是“先进先出”的线性表",
	"subject_choice_B": "队列是“先进后出”的线性表",
	"subject_choice_C": "循环队列是非线性结构",
	"subject_choice_D": "有序线性表既可以采用顺序存储结构，也可以采用链式存储结构",
	"subject_answer": "D",
	"analysis": "本题考查了栈、队列、循环队列的基本概念，栈的特点是先进后出，队列的特点是先进先出，根据数据结构中各数据元素之间的复杂程度，将数据结构分为线性结构与非线性结构两类。有序线性表既可以采用顺序存储结构，也可以采用链式存储结构。"
}, {
	"subject_title": "下列描述中，错误的是（　　）。",
	"subject_choice_A": "Java要求编程者管理内存",
	"subject_choice_B": "Java的安全性体现在多个层次上",
	"subject_choice_C": "Applet要求在支持Java的浏览器上运行",
	"subject_choice_D": "Java有多线程机制",
	"subject_answer": "A",
	"analysis": "为了充分利用资源，Java有一个系统级的线程，用来对内存的使用进行跟踪，它可以在系统空闲时对不用的内存空间进行回收，从而使程序员从繁忙的内存管理中解放出来。"
}, {
	"subject_title": "软件生命周期是指（　　）。",
	"subject_choice_A": "软件产品从提出、实现、使用维护到停止使用退役的过程",
	"subject_choice_B": "软件从需求分析、设计、实现到测试完成的过程，",
	"subject_choice_C": "软件的开发过程",
	"subject_choice_D": "软件的运行维护过程",
	"subject_answer": "A",
	"analysis": "软件生命周期(SDLC，SystemsDevelopment Life Cycle，SDLC)是软件的产生直到报废的生命周期，周期内有问题定义、可行性分析、总体描述、系统设计、编码、调试和测试、验收与运行、维护升级到废弃等阶段。"
}, {
	"subject_title": "下列包中，包含JOptionPane类的是（　　）。",
	"subject_choice_A": "javax．swing",
	"subject_choice_B": "java．iang",
	"subject_choice_C": "java．util",
	"subject_choice_D": "java．applet",
	"subject_answer": "A",
	"analysis": "Swing中提供了JOptionPane类来实现类似Windows平台下的MessageBox的功能，利用JOption-Pane类中的各个static方法来生成各种标准的对话框，实现显示信息、提出问题、警告、用户输入参数等功能，且这些对话框都是模式对话框。"
}, {
	"subject_title": "若干进程之间相互合作，共同完成－项任务，进程的这种协同工作关系称为（　　）。",
	"subject_choice_A": "异步",
	"subject_choice_B": "同步",
	"subject_choice_C": "并发",
	"subject_choice_D": "互斥",
	"subject_answer": "B",
	"analysis": "进程同步是指进程之间－种直接的协同工作关系，这些进程相互合作，共同完成－项任务。进程间的直接相互作用构成进程的同步。"
}, {
	"subject_title": "16根地址总线的寻址范围是（　　）。",
	"subject_choice_A": "531KB",
	"subject_choice_B": "64KB",
	"subject_choice_C": "640KB",
	"subject_choice_D": "1MB",
	"subject_answer": "B",
	"analysis": "假设地址总线有n条，内存的寻址范围是2n。"
}, {
	"subject_title": "结构化程序所要求的基本结构不包括（　　）。",
	"subject_choice_A": "顺序结构",
	"subject_choice_B": "GOT0跳转",
	"subject_choice_C": "选择(分支)结构",
	"subject_choice_D": "重复(循环)结构",
	"subject_answer": "B",
	"analysis": "结构化程序设计的三种结构是顺序、分支和循环，不包括GOT（）跳转，它只是分支结构的－种，也是－个关键字。"
}, {
	"subject_title": "下列关于域名和I P地址的叙述中，不正确的是（　　）。",
	"subject_choice_A": "在Internet中访问一台主机必须使用它的主机名",
	"subject_choice_B": "200．201．202．203是一个C类I P地址",
	"subject_choice_C": "I P地址采用的是分层结构",
	"subject_choice_D": "主机名与I P地址是一一对应的",
	"subject_answer": "A",
	"analysis": "每台直接连接到Internet上的计算机、路由器都必须有唯－的IP地址。IP地址是Internet赖以工作的基础。Internet中的计算机与路由器的IP地址采用分层结构，它是由网络地址与主机地址两部分组成。对于C类地址。其网络地址空间长度为21位，主机地址空间长度为8位，C类IP地址范围从：l92．0．0．0～223．255．255．255。主机名与它的IP地址－－对应，因此在Internet上访问－台主机既可以使用它的主机名，也可以使用它的IP地址。"
}, {
	"subject_title": "在switch(expression)语句中，expression的数据类型不能是（　　）。",
	"subject_choice_A": "double",
	"subject_choice_B": "char",
	"subject_choice_C": "byte",
	"subject_choice_D": "short",
	"subject_answer": "A",
	"analysis": "本题考查考生对switch(expression)语句的理解。表达式expression只能返回int、byte、short和char，题目中的double是不正确的。同时还要注意，多分支结构中，case子句的值必须是常量，而且所有case子句中的值应是不同的，default子句是任选的。"
}, {
	"subject_title": "阅读下列程序\n　\n　\n该程序在编译时的结果是（　　）。",
	"subject_choice_A": "变量a未赋值",
	"subject_choice_B": "第二个System．out．println(”b＝”＋b)语句中，变量b作用域有错",
	"subject_choice_C": "第二个System．out．println(”a＝”＋a)语句中，变量a作用域有错",
	"subject_choice_D": "第－个System．out．println(”b＝”＋b)语句中，变量b作用域有错",
	"subject_answer": "B",
	"analysis": "局部变量b是在if(a＝8){}里定义的，作用域也只在这个if语句范围内，第二个System．out．println(”b＝”＋b)语句中，变量b超出了作用域。"
}, {
	"subject_title": "在HTML文件的标志中作为可选属性的是（　　）。",
	"subject_choice_A": "Apple*主类的文件名",
	"subject_choice_B": "Applet显示区域的宽度",
	"subject_choice_C": "Applet主类的路径",
	"subject_choice_D": "Applet显示区域的高度",
	"subject_answer": "A",
	"analysis": "通过使用&lt;Applet&gt;标记，至少要指定Applet子类的位置以及浏览器中Applet的显示大小。"
}, {
	"subject_title": "算法的有穷性是指（　　）。",
	"subject_choice_A": "算法程序的运行时间是有限的",
	"subject_choice_B": "算法程序所处理的数据量是有限的",
	"subject_choice_C": "算法程序的长度是有限的",
	"subject_choice_D": "算法只能被有限的用户使用",
	"subject_answer": "A",
	"analysis": "算法的有穷性是指算法必须在执行有限的步骤后终止。"
}, {
	"subject_title": "下列不属于表达式语句的是（　　）。",
	"subject_choice_A": "＋＋i；",
	"subject_choice_B": "－－j；",
	"subject_choice_C": "b#a；",
	"subject_choice_D": "b*＝a：",
	"subject_answer": "C",
	"analysis": "前两项是自加减运算，最后－项是b＝b*a"
}, {
	"subject_title": "在下列程序的空白处，应填入的正确选项是（　　）。\n　\n　",
	"subject_choice_A": "WriterObject",
	"subject_choice_B": "Writer",
	"subject_choice_C": "BufferedWriter",
	"subject_choice_D": "writerObject",
	"subject_answer": "D",
	"analysis": "本题考查的是输入／输出及文件操作，writerObject方法是向数据流中写入数据。"
}, {
	"subject_title": "能将程序补充完整的选项是（　　）。\n　\n　",
	"subject_choice_A": "i＝m",
	"subject_choice_B": "i＝b",
	"subject_choice_C": "i＝p．a",
	"subject_choice_D": "i＝P．change(50)",
	"subject_answer": "D",
	"analysis": "本题考查类的声明。选项A中m没有被声明过，不能使用；选项B中虽然b是类Teacher的pub—lic成员变量，但在静态方法中，不能使用类中的非静态成员；选项C中a是类Person的private成员，在类外不能直接引用；选项D中change(intm)方法是public方法，并且返回一个int型值，可以通过类的实例变量P引用并赋值给一个int型变量。"
}, {
	"subject_title": "有下列二叉树，对此二叉树进行后序遍历的结果为（　　）。\n　\n　",
	"subject_choice_A": "ACBEDGFH",
	"subject_choice_B": "GDBHEFCA",
	"subject_choice_C": "HGFEDCBA",
	"subject_choice_D": "ABCDEFGH",
	"subject_answer": "B",
	"analysis": "对二叉树的后序遍历是指：先访问左子树，然后访问右子树，最后访问根结点，并且在访问其左、右子树时先访问其左、右子树，最后访问根结点。"
}, {
	"subject_title": "Java中，线程必须属于－个进程，线程是程序运行中的（　　）。",
	"subject_choice_A": "字节流",
	"subject_choice_B": "字符流",
	"subject_choice_C": "对象流",
	"subject_choice_D": "执行流",
	"subject_answer": "D",
	"analysis": "－个进程的执行过程中会产生多个线程即执行流。"
}, {
	"subject_title": "软件需求分析阶段的工作，可以分为4个方面：需求获取、需求分析、编写需求规格说明书以及（　　）。",
	"subject_choice_A": "阶段性报告",
	"subject_choice_B": "需求评审",
	"subject_choice_C": "总结",
	"subject_choice_D": "都不正确",
	"subject_answer": "B",
	"analysis": "需求分析是软件定义时期的最后一个阶段。可以概括为四个方面：需求获取；需求分析；编写需求规格说明书；需求评审。"
}, {
	"subject_title": "每个Java小应用程序必须定义为（　　）。",
	"subject_choice_A": "Applet类或JApplet类的子类",
	"subject_choice_B": "JFrame类的子类",
	"subject_choice_C": "Frame的子类",
	"subject_choice_D": "Window的子类",
	"subject_answer": "A",
	"analysis": "本题考查Applet的基本知识。Applet类定义了小应用程序(Applet)与其运行环境之间的一个接口；JApplet是Applet类的扩展，它继承了Applet的方法和执行机制，同时也增加了对Swing构件的支持。每个Java小应用程序都必须是Applet类或jApplet类的子类。因此，本题的正确答案是A。"
}, {
	"subject_title": "下列属于合法的Java标识符是（　　）。",
	"subject_choice_A": "”ABC”",
	"subject_choice_B": "&5678",
	"subject_choice_C": "＋rriwo",
	"subject_choice_D": "saler",
	"subject_answer": "D",
	"analysis": "Java中标识符的命名规则是：标识符以字母、下画线、美元符作为首字符的字符串序列；标识符是区分大小写的；标识符的字符数没有限制。由此可见，Java中标识符不能以“””开头，所以选项A错误，不能以“＆”开头，选项B错误，不能以“＋”开头，选项C错误，只有选项D是正确答案。"
}, {
	"subject_title": "数据库设计中反映用户对数据要求的模式是（　　）。",
	"subject_choice_A": "内模式",
	"subject_choice_B": "概念模式",
	"subject_choice_C": "外模式",
	"subject_choice_D": "设计模式",
	"subject_answer": "C",
	"analysis": "外模式，也称为用户模式。在一个数据库模式中，有n个外模式，每一个外模式对应一个用户。外模式保证数据的逻辑独立性。内模式属于物理模式，因此，一个数据库只有一个内模式。内模式规定了数据的存储方式、规定了数据操作的逻辑、规定了数据的完整性、规定了数据的安全性、规定了数据存储性能。"
}, {
	"subject_title": "grid[9][5]描述的是（　　）。",
	"subject_choice_A": "二维数组",
	"subject_choice_B": "－维数组",
	"subject_choice_C": "五维数组",
	"subject_choice_D": "九维数组",
	"subject_answer": "A",
	"analysis": "这是－个二维数组，[]中的数字是每－维的大小。"
}, {
	"subject_title": "Java程序与数据库的连接机制是（　　）。",
	"subject_choice_A": "（　　）DBC",
	"subject_choice_B": "JDBC",
	"subject_choice_C": "（　　）DBCAPI",
	"subject_choice_D": "SQl/CLI",
	"subject_answer": "B",
	"analysis": "本题考查Java程序与数据库的连接。JDBC(JavaData Base Connectivity)是Java程序与数据库连接的－种机制。在Java虚拟机中有个特殊模块JDBC Driv—er Manager，既负责管理针对各种类型数据库软件的JDBC驱动程序，也负责和用户应用程序交互。"
}, {
	"subject_title": "下列各项说法中错误的是（　　）。",
	"subject_choice_A": "共享数据的所有访问都必须使用synchronized加锁",
	"subject_choice_B": "共享数据的访问不－定全部使用synchronized加锁",
	"subject_choice_C": "所有的对共享数据的访问都是临界区",
	"subject_choice_D": "临界区必须使用synchronized加锁",
	"subject_answer": "B",
	"analysis": "共享数据的所有访问－定要作为临界区，用synchronized标识，这样保证了所有的对共享数据的操作都通过对象锁的机制进行控制。"
}, {
	"subject_title": "单击窗口内的按钮时，产生的事件是（　　）。",
	"subject_choice_A": "MouseEvent",
	"subject_choice_B": "WindowEvent",
	"subject_choice_C": "ActionEvent",
	"subject_choice_D": "KeyEvent",
	"subject_answer": "C",
	"analysis": "在构件的事件类中，MouseEvem事件是鼠标事件，包括鼠标单击，移动；WindowEvent事件是窗口事件，包括关闭窗口，窗口闭合，图标化；ActionEvent事件是动作事件，包括按钮按下；TextField中按&lt;Enter&gt;键；KeyEvent事件是键盘事件，包括键按下、释放。"
}, {
	"subject_title": "在Java中，实现用户界面功能的包是（　　）。",
	"subject_choice_A": "java．applet",
	"subject_choice_B": "javax．transaction",
	"subject_choice_C": "java．util",
	"subject_choice_D": "java．awt",
	"subject_answer": "D",
	"analysis": "本题考查考生对Java包功能的理解。选项A中java．applet包是为Applet提供执行需要的所有类，主要访问Applet内容的通信类；选项B中transaction包是属于javax而不是java，javax．transaction包是提供事务处理所需要的包；选项C中java．util包提供使用程序类和集合类，如系统特性定义和使用、日期函数类、集合Collection、Map、List、Array等常用工具类；java．awt包是封装抽象窗口工具包，提供构建和管理用户图形界面功能，为本题正确答案。"
}, {
	"subject_title": "下列选项中属于字符串常量的是（　　）。",
	"subject_choice_A": "•abc•",
	"subject_choice_B": "\"abc\"",
	"subject_choice_C": "[abc]",
	"subject_choice_D": "(abc)",
	"subject_answer": "B",
	"analysis": "Java中字符串常量由双引号和其中间的字符所组成．"
}, {
	"subject_title": "类Panel默认的布局管理器是（　　）。",
	"subject_choice_A": "GridLayout",
	"subject_choice_B": "BorderLayout",
	"subject_choice_C": "FlowLayout",
	"subject_choice_D": "CardLayout",
	"subject_answer": "C",
	"analysis": "本题考查Java中的布局管理器。Flow－Layout是Pane和Applet默认的布局管理器，构件在容器中从上到下、从左到右进行放置，所以选项C为正确答案。BorderLayout是Window、Frame和Dial09的默认布局管理器，在BorderLayout布局管理器中构件分成5个区域，每个区域只能放置－个构件。OridLayout使容器中各个构件呈网状布局，平均占据容器的空间。OardLayout把容器分成许多层，每层只能放置－个构件。"
}, {
	"subject_title": "下列线程状态转换序列，在线程实际运行中可能出现的序列是（　　）。",
	"subject_choice_A": "新建－运行－阻塞－终止",
	"subject_choice_B": "……运行－阻塞－可运行－终止．",
	"subject_choice_C": "……可运行－运行－阻塞－运行……",
	"subject_choice_D": "新建－可运行－运行－阻塞－可运行……",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列工具中为需求分析常用工具的是（　　）。",
	"subject_choice_A": "PAD",
	"subject_choice_B": "PFD",
	"subject_choice_C": "N～S",
	"subject_choice_D": "DFD",
	"subject_answer": "D",
	"analysis": "需求分析常用工具有数据流图(DFD)、数据字典(DD)、判定树和判定表。问题分析图(PAD)、程序流程图(PFD)、盒式图(N—s)都是详细设计的常用工具，不是需求分析的工具。"
}, {
	"subject_title": "当一个Applet所在的Web页面被其他页面覆盖后。不可能被调用的Applet方法是（　　）。",
	"subject_choice_A": "destroy（　　）",
	"subject_choice_B": "init（　　）",
	"subject_choice_C": "stop（　　）",
	"subject_choice_D": "start（　　）",
	"subject_answer": "B",
	"analysis": "在JavaApplet的生命周期中，共有4种状态，即4种方法：init（）、start（）、stop（）和destory（）。在Applet装载时，调用init（）通知该Applet已被加载到浏览器中，使Applet执行－些基本初始化操作。"
}, {
	"subject_title": "程序设计语言的基本成分是数据成分、运算成分、控制成分和（　　）。",
	"subject_choice_A": "对象成分",
	"subject_choice_B": "变量成分",
	"subject_choice_C": "语句成分",
	"subject_choice_D": "传输成分",
	"subject_answer": "D",
	"analysis": "程序设计语言的基本成分有：数据成分，用于描述程序所涉及的数据；运算成分，用于描述程序中所包含的运算；控制成分，用于描述程序中所包含的控制；传输成分，用于表达程序中数据的传输。"
}, {
	"subject_title": "下面代码段的输出是（　　）。\n　\n　",
	"subject_choice_A": "编译出错",
	"subject_choice_B": "5752",
	"subject_choice_C": "true",
	"subject_choice_D": "无任何输出",
	"subject_answer": "A",
	"analysis": "本题考查对位运算符和逻辑运算符的理解。位运算符”&amp;”和”|&quot;用于按位将两个数进行与和或的操作，两个操作数可以是整型、字节型、长整型和短整型，但不能是浮点型数据。逻辑运算符&amp;&amp;只能对两个布尔型的数据进行运算，返回的结果也是布尔型的。"
}, {
	"subject_title": "对鼠标单击按钮操作进行事件处理的接口是（　　）．",
	"subject_choice_A": "MouseListener",
	"subject_choice_B": "WindowListener",
	"subject_choice_C": "ActionListener",
	"subject_choice_D": "KeyListener",
	"subject_answer": "C",
	"analysis": "动作事件和按钮按下，以及在TeXtFieId中按&lt;Enter．&gt;键对应的事件为ActionEvent事件，进行处理的接口应为ActionListener。MouseListener是MouseEvent事件的实现接口，响应的是鼠标的移动、单击(不包括单击按钮)事件。"
}, {
	"subject_title": "下列特征中不是面向对象方法的主要特征的是（　　）。",
	"subject_choice_A": "多态性",
	"subject_choice_B": "继承",
	"subject_choice_C": "封装性",
	"subject_choice_D": "模块化",
	"subject_answer": "D",
	"analysis": "面向对象设计方法与面向过程设计方法有本质的不同，其基本原理是：使用现实世界的概念抽象地思考问题从而自然地解决问题。其特点包括：分类性、多态性、封装性、模块独立性、继承和多态性等。模块化是结构化程序设计的特点。"
}, {
	"subject_title": "Java的反汇编命令是（　　）。",
	"subject_choice_A": "javap",
	"subject_choice_B": "javac",
	"subject_choice_C": "jdb",
	"subject_choice_D": "java",
	"subject_answer": "A",
	"analysis": "javap命令是Java反汇编命令；javac命令是Java语言编译器，jdb是基于文本和命令行的调试工具，java命令是Java解释器。"
}, {
	"subject_title": "一个工作人员可以使用多台计算机，而一台计算机可被多个人使用，则实体工作人员与实体计算机之间的联系是（　　）。",
	"subject_choice_A": "一对一",
	"subject_choice_B": "一对多",
	"subject_choice_C": "多对多",
	"subject_choice_D": "多对一",
	"subject_answer": "C",
	"analysis": "一个工作人员对应多台计算机，－台计算机对应多个工作人员，则实体工作人员与实体计算机之间的联系是多对多。"
}, {
	"subject_title": "Frame默认的布局管理器是（　　）。",
	"subject_choice_A": "FlowLayout",
	"subject_choice_B": "BorderLayout",
	"subject_choice_C": "GridLayout",
	"subject_choice_D": "UpLayout",
	"subject_answer": "B",
	"analysis": "本题考查Java中的布局管理器。Flow－Layout是Pane和Applet默认的布局管理器，构件在容器中从上到下、从左到右进行放置；BorderLayout是Window、Frame和Dial09的默认布局管理器，在BorderLayout布局管理器中构件分成5个区域，每个区域只能放置－个构件；GridLayout使容器中各个构件呈网状布局，平均占据容器的空间；GardLayout把容器分成许多层，每层只能放置－个构件。"
}, {
	"subject_title": "某二叉树共有60个叶子结点与50个度为1的结点，则该二叉树中的总结点数为（　　）。",
	"subject_choice_A": "148",
	"subject_choice_B": "169",
	"subject_choice_C": "182",
	"subject_choice_D": "198",
	"subject_answer": "B",
	"analysis": "本题考查二叉树的性质。叶子结点即度为0的结点，它总是比度为2的结点多一个，所以，具有60个叶子结点的二叉树有59个度为2的结点。总结点数等于个叶子结点加上59个度为2的结点再加上50个度为l的结点的和，共169个结点。"
}, {
	"subject_title": "当浏览器重新返回Applet所在页面时，将调用Applet类的方法是（　　）。",
	"subject_choice_A": "start（　　）",
	"subject_choice_B": "ink（　　）",
	"subject_choice_C": "stop（　　）",
	"subject_choice_D": "destroy（　　）",
	"subject_answer": "A",
	"analysis": "本题考查Applet的运行方式。当init（）方法完成后，将调用start（）方法，使Applet成为激活状态。该方法在Applet每次显示时都要调用。例如，浏览器由最小化复原，或浏览器从一个URL返回该Applet所在的页面，－般常在start（）中启动动画或播放声音等的线程。"
}, {
	"subject_title": "在程序的下画线处应填入的选项是（　　）。\n　\n　",
	"subject_choice_A": "implements Runnable",
	"subject_choice_B": "extends Thread",
	"subject_choice_C": "implements Thread",
	"subject_choice_D": "extends Runnable",
	"subject_answer": "B",
	"analysis": "implements是实现接口，extends是继承类。Thread是类，Runnable是接口，所以只有A、B选项语法是正确的。而Runnable是不能返回Static值，所以答案选择B。"
}, {
	"subject_title": "假设用－个长度为50的数组(数组元素的下标从0到49)作为栈的存储空间，栈底指针bottom指向栈底元素，栈顶指针top指向栈顶元素，如果bottom＝49，top＝30(数组下标)，则栈中具有的元素个数为（　　）。",
	"subject_choice_A": "50",
	"subject_choice_B": "19",
	"subject_choice_C": "1",
	"subject_choice_D": "20",
	"subject_answer": "B",
	"analysis": "当前栈中的所有元素的个数就是用栈底指针减去栈顶指针。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "在栈中，栈中元素随栈底指针与栈顶指针的变化而动态变化",
	"subject_choice_B": "在栈中，栈顶指针不变，栈中元素随栈底指针的变化而动态变化",
	"subject_choice_C": "在栈中，栈底指针不变，栈中元素随栈顶指针的变化而动态变化",
	"subject_choice_D": "上述三种说法都不对",
	"subject_answer": "C",
	"analysis": "栈是限制仅在表的－端进行插入和删除的运算的线性表，通常称插入、删除的这－端为栈顶，另－端称为栈底。"
}, {
	"subject_title": "在Java语言中，0bjectOutputStream是指（　　）。",
	"subject_choice_A": "字节流",
	"subject_choice_B": "字符流",
	"subject_choice_C": "对象输出流",
	"subject_choice_D": "数据流",
	"subject_answer": "C",
	"analysis": "本题考查Java输入＼输出流的概念。Fil－eInputStream是字节流，BufferedWriter是字符流，Objec－tOutputStream是对象输出流，既继承了OutputStream抽象类，又实现了0bjectOutput接口，这是Java用接口技术代替双重继承的例子，其构造方法参数是串行化的对象。"
}, {
	"subject_title": "下列与数据元素有关的叙述中，不正确的是（　　）。",
	"subject_choice_A": "数据元素是数据的基本单位，即数据集合中的个体",
	"subject_choice_B": "数据元素是有独立含义的数据最小单位",
	"subject_choice_C": "数据元素又称为结点",
	"subject_choice_D": "数据元素又称为记录",
	"subject_answer": "B",
	"analysis": "数据元素是数据的基本单位，即数据集合中的个体。有些情况下也把数据元素称为结点、记录、表目等。一个数据元素可由一个或多个数据项组成，数据项是有独立含义的数据最小单位，其值能唯－确定一个数据元素的数据项。"
}, {
	"subject_title": "当－个Applet被加载，后续对Applet生命周期方法的调用中，可能存在的次序是（　　）。",
	"subject_choice_A": "start（　　），stop（　　），destroy（　　）",
	"subject_choice_B": "init（　　），start（　　），stop（　　），start（　　），stop（　　），destroy（　　）",
	"subject_choice_C": "start（　　），init（　　），stop（　　），destroy（　　）",
	"subject_choice_D": "init（　　），start（　　），destroy（　　）",
	"subject_answer": "B",
	"analysis": "init（）－般用来完成所有必需的初始化操作，start（）是在初始化之后Applet被加载时调用，stop（）在Applet停止执行时调用，destory（）是Applet从系统中撤出时调用。"
}, {
	"subject_title": "下列叙述中，错误的是（　　）。",
	"subject_choice_A": "内部类的名称与定义它的类的名称可以相同",
	"subject_choice_B": "内部类可用abstract修饰",
	"subject_choice_C": "内部类可作为其他类的成员",
	"subject_choice_D": "内部类可访问它所在类的成员",
	"subject_answer": "A",
	"analysis": "内部类与外部类的名称不能相同。"
}, {
	"subject_title": "最常用的－种基本数据模型是关系数据模型，它的表示应采用（　　）。",
	"subject_choice_A": "树",
	"subject_choice_B": "网络",
	"subject_choice_C": "图",
	"subject_choice_D": "二维表",
	"subject_answer": "D",
	"analysis": "关系数据模型是属于数据库的－种最重要的数据模型，在关系数据模型中，实体及实体间的联系都用二维表来表示。"
}, {
	"subject_title": "继承是Java语言的－个重要机制，所有的Java类都继承自根类（　　）。",
	"subject_choice_A": "Class",
	"subject_choice_B": "Object",
	"subject_choice_C": "String",
	"subject_choice_D": "Date",
	"subject_answer": "B",
	"analysis": "本题考查Java的继承机制。Class类封装了类和对象的属性特征，包含着解释Java类的信息；Object类处于Java类层次结构的最上层，是所有类的父类，也就是说，所有Java语言中的类都是直接或间接继承0bieet类得到的；String类是字符串类，用于构造字符串常量。Date类是日期类，提供了处理日期、时间的多种方法。"
}, {
	"subject_title": "下列叙述中，错误的是（　　）。",
	"subject_choice_A": "File类能够存储文件",
	"subject_choice_B": "File类能够读写文件",
	"subject_choice_C": "File类能够建立文件",
	"subject_choice_D": "File类能够获取文件目录信息",
	"subject_answer": "B",
	"analysis": "本题考查考生对Java中File类的理解。文件File是java．io包中的－个重要的非流类，以－种系统无关的方式表示－个文件对象的属性。通过File所提供的方法，可以得到文件或目录的描述信息(包括名字、路径、长度、可读和可写等)，也可以生成新文件、目录，修改文件和目录，查询文件属性，重命名文件或者删除文件。File描述了文件本身的属性，File类中封装了对文件系统进行操作的功能。简单说，File类所关心的是文件在磁盘上的存储，而要对文件进行读写，就是流类所关心的文件内容，应该掌握相关概念以及相关方法。"
}, {
	"subject_title": "负责数据库中查询操作的数据库语言是（　　）。",
	"subject_choice_A": "数据定义语言",
	"subject_choice_B": "数据管理语言",
	"subject_choice_C": "数据操纵语言",
	"subject_choice_D": "数据控制语言",
	"subject_answer": "C",
	"analysis": "数据库操纵语言专门负责查询、增加和删除等数据操作。"
}, {
	"subject_title": "下列程序段的输出结果是（　　）。\n　\n　",
	"subject_choice_A": "0",
	"subject_choice_B": "a",
	"subject_choice_C": "f",
	"subject_choice_D": "5",
	"subject_answer": "D",
	"analysis": "a和f的ASCⅡ值相差5。"
}, {
	"subject_title": "下列属于合法的Java标识符的是（　　）。",
	"subject_choice_A": "_cat",
	"subject_choice_B": "5books",
	"subject_choice_C": "＋static",
	"subject_choice_D": "－3．14159",
	"subject_answer": "A",
	"analysis": "本题考查Java标识符的命名规则，是考试的重点内容。Java中标识符的命名规则是标识符以字母、下画线或美元符作为首字符的字符串序列；标识符是区分大小写的；标识符的字符数没有限制。由此可见，Java中标识符不能以数字开头，所以选项B错误，不能以“＋”开头，选项C错误，不能以“－”开头，选项D错误，只有选项A是正确答案。"
}, {
	"subject_title": "下列Java组件中，不属于容器的是（　　）。",
	"subject_choice_A": "Panel",
	"subject_choice_B": "Window",
	"subject_choice_C": "Frame",
	"subject_choice_D": "Label",
	"subject_answer": "D",
	"analysis": "本题考查对Java组件中容器的：基本知识的理解。选项A错误，Panel类派生自容器类Container，属于容器的－种；选项B错误，Window类也派生自容器类Container，也属于容器的－种；选项C错误，Frame类派生自Window类，也是－种容器；选项D正确，Label组件是标签组件，不属于容器。故本题答案是D。"
}, {
	"subject_title": "下列与其他选项不相等的是（　　）。",
	"subject_choice_A": "15",
	"subject_choice_B": "0xF",
	"subject_choice_C": "015",
	"subject_choice_D": "OXF",
	"subject_answer": "C",
	"analysis": "本题考查Java语言中的迸制换算。考生首先要清楚各种进制的表示方法．整型常量有3种书写格式：十进制整数，如156，－230，345；八进制整数：以0开头，如Ol2表示十进制的l0；十六进制整数：以Ox或0X开头，如0X123表示十进制数291。选项A是十进制的15，选项B和选项D都是十六进制中的F相当于十进制的15，选项C为八进制，以0开头，此处015相当于十进制的13，与其他选项不同。"
}, {
	"subject_title": "设有字符序列(Q，H，C，Y，P，A，M，S，R，D，F，x)，则新序列(F，H，C，D，P，A，M，Q，R，S，Y，x)是下列（　　）排序算法－趟扫描的结果。",
	"subject_choice_A": "起泡排序",
	"subject_choice_B": "初始步长为4的希尔排序",
	"subject_choice_C": "二路归并排序",
	"subject_choice_D": "以第一个元素为分界元素的快速排序",
	"subject_answer": "D",
	"analysis": "根据快速排序的算法，新序列(F，H，C，D，P，A，M，Q，R，S，Y，X)为字符序列(Q，H，C，Y，P，A，M，S，R，D，F，X)经过快速排序的算法第－趟扫描后的结果。"
}, {
	"subject_title": "下列描述中正确的是（　　）。",
	"subject_choice_A": "软件工程只是解决软件项目的管理问题",
	"subject_choice_B": "软件工程主要解决软件产品的生产率问题",
	"subject_choice_C": "软件工程的主要思想是强调在软件开发过程中需要应用工程化原则",
	"subject_choice_D": "软件工程只是解决软件开发过程中的技术问题",
	"subject_answer": "C",
	"analysis": "软件工程是指将工程化的思想应用于软件的开发、应用和维护的过程，包括软件开发技术和软件工程管理。"
}, {
	"subject_title": "类变量必须带有的修饰符是（　　）。",
	"subject_choice_A": "static",
	"subject_choice_B": "final",
	"subject_choice_C": "public",
	"subject_choice_D": "volatile",
	"subject_answer": "A",
	"analysis": "类变量用static修饰。"
}, {
	"subject_title": "执行下面程序段后，2值为（　　）。\nint x＝1，y＝2，z＝3；\nz＝z/(float)(x/y)；",
	"subject_choice_A": "编译无法通过",
	"subject_choice_B": "6",
	"subject_choice_C": "3",
	"subject_choice_D": "2",
	"subject_answer": "A",
	"analysis": "本题考查Java的运算和类型转换。题目中变量X、y、z是int类型，由于括号的优先级要高，所以语句(float)(x/y)的结果为0．0，分母已经成为0，编译肯定无法通过。另外，由于z是int型，不能将float型强制转化为int型。"
}, {
	"subject_title": "设计软件结构是在软件生命周期的（　　）。",
	"subject_choice_A": "软件定义期",
	"subject_choice_B": "软件开发期",
	"subject_choice_C": "软件维护期",
	"subject_choice_D": "以上3个都不是",
	"subject_answer": "B",
	"analysis": "设计软件结构，是在软件概要设计阶段进行的，而概要设计属于软件开发期。"
}, {
	"subject_title": "用于输入压缩文件格式的ZiplnputStream类所属包是（　　）。",
	"subject_choice_A": "java．util",
	"subject_choice_B": "java．io",
	"subject_choice_C": "java．nio",
	"subject_choice_D": "java．util．zip",
	"subject_answer": "D",
	"analysis": "本题考查ZipInputStream类的基本概念。压缩文件输入流都是InflateInputStream的子类，是以字节压缩为特征的过滤流。主要有三类，应该有所了解。ZipInputStream类在java．util．zip包中，该类用于输入以gzip格式进行压缩的文件，是对输入文件类型的－种过滤。ZipInputStream类也在java．util．zip包中，用于输入zip格式的文件，这是对于文件类新格式的－种过滤。Jarlnput－Stream类在java．util．jar包中，是ZipInputStream的子类，用于输入jar文件。"
}, {
	"subject_title": "请阅读下面程序\n　\n　\n为使该程序正确执行，下画线处的语句应是（　　）。",
	"subject_choice_A": "t．sleep（　　）",
	"subject_choice_B": "t．yield（　　）",
	"subject_choice_C": "t．interrupt（　　）",
	"subject_choice_D": "t．start（　　）",
	"subject_answer": "D",
	"analysis": "程序中通过继承Thread类来创建线程，而Java中新创建的线程不会自动运行，必须调用线程的start（）方法，才能运行该线程。"
}, {
	"subject_title": "下列能够正确创建线程的方法是（　　）。\n①继承java．fang．Thread类，并重写run（　　）方法\n②继承java．lang．Runnable类，并重写start（　　）方法\n③实现java．lang．Thread接口，并实现run（　　）方法\n④实现java．lang．Runable接口，并实现run（　　）方法",
	"subject_choice_A": "①、③",
	"subject_choice_B": "②、④",
	"subject_choice_C": "②、③",
	"subject_choice_D": "①、④",
	"subject_answer": "D",
	"analysis": "用Thread类的构造方法Thread(Runnabletarget)创建线程对象时，构造方法中的参数必须是－个具体的对象，该对象称作线程的目标对象，创建目标对象的类必须要实现Runnable接口。"
}, {
	"subject_title": "在程序的下面线处应填人的选项是（　　）。\n　\n　",
	"subject_choice_A": "implements Runnable",
	"subject_choice_B": "extends Thread",
	"subject_choice_C": "implements Thread",
	"subject_choice_D": "extends Runnable",
	"subject_answer": "A",
	"analysis": "Test类实现了Runnable接口。"
}, {
	"subject_title": "如果线程正处于阻塞状态，不能够使线程直接进入可运行状态的情况是（　　）。",
	"subject_choice_A": "sleep（　　）方法的时间到",
	"subject_choice_B": "获得了对象的锁",
	"subject_choice_C": "线程在调t．join（　　）方法后，线程t结果",
	"subject_choice_D": "wait（　　）方法结束",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "Java对文件类提供了许多操作方法，能获得文件对象父路径名的方法是（　　）。",
	"subject_choice_A": "getAbsolutePath（　　）",
	"subject_choice_B": "getParentFile（　　）",
	"subject_choice_C": "getAbsoluteFile（　　）",
	"subject_choice_D": "getName（　　）",
	"subject_answer": "B",
	"analysis": "本题考查File类的基本知识。File类是通过文件名列表来描述一个文件对象的属性，通过File类提供的方法，可以获得文件的名称、长度、所有路径等信息，还可以改变文件的名称、删除文件等。"
}, {
	"subject_title": "下列不属于Swing的构件是（　　）。",
	"subject_choice_A": "JButton",
	"subject_choice_B": "JLabel",
	"subject_choice_C": "JFrame",
	"subject_choice_D": "JPane",
	"subject_answer": "D",
	"analysis": "Swing构件中JButton是按钮构件，JLa－bel为标签构件，JFrame为顶层窗体容器构件。中间容器面板应为JPanel，而不是JPane。"
}, {
	"subject_title": "AWT中用来表示对话框的类是（　　）。",
	"subject_choice_A": "Font",
	"subject_choice_B": "Color",
	"subject_choice_C": "Panel",
	"subject_choice_D": "Dialog",
	"subject_answer": "D",
	"analysis": "Font和Color是构件的字体和外观颜色，Panel是面板容器，Dialog是对话框的类。"
}, {
	"subject_title": "下列关于Java安全性的说法错误的是（　　）。",
	"subject_choice_A": "有严格的访问权限检查",
	"subject_choice_B": "对程序执行前要检查",
	"subject_choice_C": "不允许使用指针",
	"subject_choice_D": "可防止对内存的非法入侵",
	"subject_answer": "B",
	"analysis": "本题考查Java的安全性特点。面向网络、分布式的Java语言，对非法入侵的防范是非常重要的，Java语言提供充分的安全保障，在运行程序时，有严格的访问权限检查。对字节代码执行前要检查，不允许使用指针，可防止对内存的非法入侵，它是目前安全性最佳的语言。但是Java并不是对程序执行前检查，而是对字节代码进行检查，Java编写好的程序首先由编译器转换为标准字节代码，然后由Java虚拟机去解释执行。"
}, {
	"subject_title": "下列叙述中，错误的是（　　）。",
	"subject_choice_A": "Jbutton类和标签类可显示图标和文本",
	"subject_choice_B": "Button类和标签类可显示图标和文本",
	"subject_choice_C": "AWT构件能直接添加到顶层容器中",
	"subject_choice_D": "Swing构件不能直接添加到顶层容器中",
	"subject_answer": "B",
	"analysis": "Swing的按钮上还可以同时显示文字和图标，甚至只有图标都是可以的，这样就构成了图形按钮。而AWT中的Button类不能显示图标，只能显示文本。"
}, {
	"subject_title": "下列关于System类的叙述中，错误的是（　　）。",
	"subject_choice_A": "System类是一个final类",
	"subject_choice_B": "System类不能实例化",
	"subject_choice_C": "System类中没有定义属性",
	"subject_choice_D": "System类主要提供了系统环境参数的访问",
	"subject_answer": "C",
	"analysis": "本题考查System类的基本知识。Sys—tern类是一个final类，所有的方法都用类变量来调用，对System类不可能实例化。System类主要用来提供标准输入/输出和系统环境信息的访问设置。而System类的属性有：①publicstatic final InputStream in；标准输入；②publicstatic final OutputStream out；标准输出；③public static finalPrintStream err；标准错误输出。"
}, {
	"subject_title": "结构化程序设计的3种基本结构是（　　）。",
	"subject_choice_A": "过程、子程序和分程序",
	"subject_choice_B": "顺序、选择和循环",
	"subject_choice_C": "递归、堆栈和队列",
	"subject_choice_D": "调用、返回和转移",
	"subject_answer": "B",
	"analysis": "程序的基本控制结构包括顺序、选择和循环。"
}, {
	"subject_title": "在下列代码的下画线处应填入的内容是（　　）。\n　\n　",
	"subject_choice_A": "staff",
	"subject_choice_B": "double",
	"subject_choice_C": "int",
	"subject_choice_D": "String",
	"subject_answer": "D",
	"analysis": "这是学习Java语言接触的第－个程序，main函数的参数是StringargsE3。"
}, {
	"subject_title": "下列选项中不属于结构化程序设计原则的是（　　）。",
	"subject_choice_A": "可封装",
	"subject_choice_B": "自顶向下",
	"subject_choice_C": "模块化",
	"subject_choice_D": "逐步求精",
	"subject_answer": "A",
	"analysis": "结构化程序设计的主要原则概括为自顶向下，逐步求精，限制使用GOT（）语句。"
}, {
	"subject_title": "下列构造方法的调用方式中，正确的是（　　）。",
	"subject_choice_A": "按照－般方法调用",
	"subject_choice_B": "由用户直接调用",
	"subject_choice_C": "只能通过new自动调用",
	"subject_choice_D": "被系统调用",
	"subject_answer": "C",
	"analysis": "本题考查Java中的构造方法。构造方法在Java中占有非常重要的地位，务必掌握。构造方法是类中的－种特殊方法，是为对象初始化操作编写的方法，用来定义对象的初始状态。构造方法不能被程序调用，构造方法名必须与类名相同，没有返回值，用户不能直接调用，只能通过new自动调用，所以选项C正确。"
}, {
	"subject_title": "下列代表十六进制整数的是（　　）。",
	"subject_choice_A": "OXA6",
	"subject_choice_B": "1234L",
	"subject_choice_C": "－840",
	"subject_choice_D": "0144",
	"subject_answer": "A",
	"analysis": "本题考查Java语言中的整型常量。整型常量有3种书写格式：十进制整数、八进制整数和十六进制整数。十六进制整数以Ox或0X开头，如0X123表示十进制数291。选项A表示的是十六进制整数，选项B是long类型整型常量，选项C是十进制整数，选项D是八进制整数，因此选项A为本题正确选项。"
}, {
	"subject_title": "Java程序默认引用的包是（　　）。",
	"subject_choice_A": "java．text包",
	"subject_choice_B": "java．awt包",
	"subject_choice_C": "java．lang包",
	"subject_choice_D": "java．util包",
	"subject_answer": "C",
	"analysis": "java．lang包提供Java编程语言进行程序设计的基础类。java．lang包是编译器自动导入的。"
}, {
	"subject_title": "数据库管理系统中负责数据模式定义的语言是（　　）。",
	"subject_choice_A": "数据定义语言",
	"subject_choice_B": "数据管理语言",
	"subject_choice_C": "数据操纵语言",
	"subject_choice_D": "数据控制语言",
	"subject_answer": "A",
	"analysis": "数据模式是由数据定义语言(DataDefinition Language，DDL)来描述、定义的，体现、反映了数据库系统的整体观。"
}, {
	"subject_title": "要下列Java Applet程序完整并能够正确运行，横线处应填入的内容是（　　）。\n　\n　",
	"subject_choice_A": "extends Thread",
	"subject_choice_B": "extends Applet",
	"subject_choice_C": "extends Char",
	"subject_choice_D": "extends Float",
	"subject_answer": "B",
	"analysis": "本题是考查继承。继承了Applet类。"
}, {
	"subject_title": "下列程序的执行结果为（　　）。\n　\n　",
	"subject_choice_A": "1310",
	"subject_choice_B": "1211",
	"subject_choice_C": "1111",
	"subject_choice_D": "1212",
	"subject_answer": "A",
	"analysis": "程序是由if－else语句构成的流程，分析判断条件，变量i和j比较，得到条件表达式的值为true，然后执行i－1，现在变量i的值为12，而j的值为10；由于条件表达式为true，则执行i＋＋，因此i的值为13，并跳过else子句块，循环控制语句执行完毕，这时变量i和i的值分别为13和10。"
}, {
	"subject_title": "下列叙述中正确的是（　　）。",
	"subject_choice_A": "有－个以上根结点的数据结构不－定是非线性结构",
	"subject_choice_B": "只有－个根结点的数据结构不－定是线性结构",
	"subject_choice_C": "循环链表是非线性结构",
	"subject_choice_D": "双向链表是非线性结构",
	"subject_answer": "D",
	"analysis": "线性表的特点是：在数据元素的非空有限集合中；存在唯－的－个被称为“第－个”的数据元素；存在唯－－个被称为“最后－个”的数据元素；除第－个以外，集合中的每个数据元素均只有－个后继；除最后－个以外，集合中的每个数据元素均只有－个后继。因此，双向表是非线性结构。"
}, {
	"subject_title": "int类型的取值范围为（　　）。\n　\n　",
	"subject_choice_A": "  ",
	"subject_choice_B": "  ",
	"subject_choice_C": "  ",
	"subject_choice_D": "  ",
	"subject_answer": "B",
	"analysis": "本题考查int类型的取值范围。int类型是最常用的整数类型，存储时占32位bit，能表示的范围是－2的31次方至2的31次方－1，选项B正确。而short类型在存储时占l6位bit，能表示的范围是－2的16次方至2的16次方－1。long类型存储时占64位bit，数据范围是－2的64次方至2的64次方－1。正确答案为选项B。"
}, {
	"subject_title": "－个工作人员可以使用多台计算机，而－台计算机可被多个人使用，则实体工作人员与实体计算机之间的联系是（　　）。",
	"subject_choice_A": "－对－",
	"subject_choice_B": "－对多",
	"subject_choice_C": "多对多",
	"subject_choice_D": "多对－",
	"subject_answer": "C",
	"analysis": "－个工作人员对应多台计算机，－台计算机对应多个工作人员，则实体工作人员与实体计算机之间的联系是多对多。"
}, {
	"subject_title": "下列叙述中，正确的是（　　）。",
	"subject_choice_A": "Java语言的标识符是区分大小写的",
	"subject_choice_B": "源文件名与public类名可以不相同",
	"subject_choice_C": "源文件的扩展名为．jar",
	"subject_choice_D": "源文件中public类的数目不限",
	"subject_answer": "A",
	"analysis": "本题考查考生对Java语言概念的理解。这些属于考试重点内容。Java语言和C语言不同，它是区分大小写的，选项A正确。Java程序的源文件扩展名为．class，．jar文件是由归档工具jar生成的。源文件中的public类的数目只能有0个或l个，用来指定应用程序类名，也是源文件名。"
}, {
	"subject_title": "为使Java程序独立于平台，Java虚拟机把字节码与各个操作系统及硬件（　　）。",
	"subject_choice_A": "分开",
	"subject_choice_B": "结合",
	"subject_choice_C": "联系",
	"subject_choice_D": "融合",
	"subject_answer": "A",
	"analysis": "只有分开，才能做到独立于平台，与硬件无关。"
}, {
	"subject_title": "下列命令中，是Java编译命令的是（　　）。",
	"subject_choice_A": "javac",
	"subject_choice_B": "java",
	"subject_choice_C": "javadoc",
	"subject_choice_D": "appletviewer",
	"subject_answer": "A",
	"analysis": "本题考查Java中JDK工具。javac是Java的编译命令，能将源代码编译成字节码，以．class扩展名存入Java工作目录中。Java是Java解释器，执行字节码程序，该程序是类名所指的类，必须是－个完整定义的名字。javadoc是Java文档生成器，对Java源文件和包以XML格式生成API文档。appletviewer是JavaApplet浏览器。"
}, {
	"subject_title": "当使用SomeThread t＝new SomeThread（　　）创建一个线程时，下列叙述中正确的是（　　）。",
	"subject_choice_A": "SomeThread类是包含run（　　）方法的任意Java类",
	"subject_choice_B": "SomeThread类－定要实现Runnable接口",
	"subject_choice_C": "SomeThread类是Thread类的子类",
	"subject_choice_D": "SomeThread类是Thread类的子类并且要实现Run－nable接口",
	"subject_answer": "C",
	"analysis": "由SomeThreadt＝new SomeTharead（）可知此题是通过继承Thread类来创建线程的。"
}, {
	"subject_title": "按层次次序将一棵有n个结点的完全二叉树的所有结点从1～n编号，当i≤n/2时，编号为i的结点的左子树的编号是（　　）。",
	"subject_choice_A": "2i－1",
	"subject_choice_B": "2i",
	"subject_choice_C": "2i＋1",
	"subject_choice_D": "不确定",
	"subject_answer": "B",
	"analysis": "完全二叉树中除最下面－层外，各层都被结点充满了，每－层结点个数恰是上－层结点个数的2倍。因此，从一个结点的编号就可推知它的双亲及左、右子树结点的编号。当i≤n/2时，编号为i的结点的左子树的编号是2i，否则结点i没有左子树。当i≤(n1)/2时．编号为i的结点的右子树的编号是2i＋1，否则结点i没有右子树。当i≠1时，编号为i的结点的双亲是结点i/2。"
}, {
	"subject_title": "在软件开发中，需求分析阶段产生的主要文档是（　　）。",
	"subject_choice_A": "软件集成测试计划",
	"subject_choice_B": "软件详细设计说明书",
	"subject_choice_C": "用户手册",
	"subject_choice_D": "软件需求规格说明书",
	"subject_answer": "D",
	"analysis": "需求分析阶段只能产生需求分析规格说明数，A测试说明书是软件测试阶段生成的，B软件详细设计说明书是设计阶段生成的，C用户手册是软件发布时随软件－同交付给用户的。"
}, {
	"subject_title": "阅读下列代码后　\n　\n正确的说法是（　　）。",
	"subject_choice_A": "编译时将产生错误",
	"subject_choice_B": "编译时正确，运行时将产生错误",
	"subject_choice_C": "输出零",
	"subject_choice_D": "输出空",
	"subject_answer": "A",
	"analysis": "本题考查考生对Java中数组的定义及使用。intarr[]＝newint[10]表示数组arr是一个含有10个元素的整数数组。Java中的数据类型必须实例化后才能使用，但是有种情况例外，就是该成员是用static声明的。题目中对于数组并没有实例化，因此不能使用，所以选项A说法正确。如果加上static修饰符，改为static int arr[]＝new int[10]或者将该数组实例化即可，输出为0。"
}, {
	"subject_title": "下列代码中，将引起－个编译错误的行是（　　）。\n　\n　",
	"subject_choice_A": "第3行",
	"subject_choice_B": "第5行",
	"subject_choice_C": "第6行",
	"subject_choice_D": "第10行",
	"subject_answer": "D",
	"analysis": "本题考查考生对Java中构造方法的理解及应用。构造方法名必须与类名相同，没有返回值，用户不能直接调用，只能通过new自动调用。题目有两个构造方法Test（）和Test(inta)，按照参数决定调用哪个方法。tl＝newTest（）语句调用Test（）方法，而t2＝newTest(j，k)将会找不到相应的构造方法，程序编译出错在第10行，所以选项D正确。"
}, {
	"subject_title": "下列关于面向对象的论述中，正确的是（　　）。",
	"subject_choice_A": "面由对象是指以对象为中心，分析、设计和实现应用程序的机制",
	"subject_choice_B": "面向对象是指以功能为中心，分析、设计和实现应用程序的机制",
	"subject_choice_C": "面向对象仅适用于程序设计阶段",
	"subject_choice_D": "面向对象是－种程序设计语言",
	"subject_answer": "A",
	"analysis": "面向对象是－种程序设计方式，Java、C＋＋是面向对象设计的语言，而C是面向过程设计的语言。面向对象设计适应于设计、编码、实现、测试等－系列环节。"
}, {
	"subject_title": "在读取二进制数据文件的记录时，为了提高效率常常使用的－种辅助类是（　　）。",
	"subject_choice_A": "InputStream",
	"subject_choice_B": "FilelnputStream",
	"subject_choice_C": "StringBuffer",
	"subject_choice_D": "BufferedReader",
	"subject_answer": "C",
	"analysis": "本题考查Java语言的输入/输出流。InputStream类、FileInputStream类和BufferedReader类都是Java语言中和输入输出直接相关的类，不属于辅助类，因此可以直接判断出选项c为正确答案。"
}, {
	"subject_title": "下面叙述正确的是",
	"subject_choice_A": "算法的执行效率与数据的存储结构无关",
	"subject_choice_B": "算法的空间复杂度是指算法程序中指令（或语句）的条数",
	"subject_choice_C": "算法的有穷性是指算法必须能在执行有限个步骤之后终止",
	"subject_choice_D": "以上三种描述都不对",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "以下数据结构中不属于线性结构的是",
	"subject_choice_A": "队列",
	"subject_choice_B": "线性表",
	"subject_choice_C": "二叉树",
	"subject_choice_D": "栈",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "在一颗二叉树上第5层的结点数最多是",
	"subject_choice_A": "8",
	"subject_choice_B": "16",
	"subject_choice_C": "32",
	"subject_choice_D": "15",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下面描述中，符合结构化程序设计风格的是",
	"subject_choice_A": "使用顺序、选择和重复（循环）三种基本控制结构表示程序的控制逻辑",
	"subject_choice_B": "模块只有一个入口，可以有多个出口",
	"subject_choice_C": "注重提高程序的执行效率",
	"subject_choice_D": "不使用goto语句",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下面概念中，不属于面向对象方法的是",
	"subject_choice_A": "对象",
	"subject_choice_B": "继承",
	"subject_choice_C": "类",
	"subject_choice_D": "过程调用",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "在结构化方法中，用数据流程图（DFD）作为描述工具的软件开发阶段是",
	"subject_choice_A": "可行性分析",
	"subject_choice_B": "需求分析",
	"subject_choice_C": "详细设计",
	"subject_choice_D": "程序编码",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "在软件开发中，下面任务不属于设计阶段的是",
	"subject_choice_A": "数据结构设计",
	"subject_choice_B": "给出系统模块结构",
	"subject_choice_C": "定义模块算法",
	"subject_choice_D": "定义需求并建立系统模型",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "数据库系统的核心是",
	"subject_choice_A": "数据模型",
	"subject_choice_B": "数据库管理系统",
	"subject_choice_C": "软件工具",
	"subject_choice_D": "数据库",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列叙述中正确的是",
	"subject_choice_A": "数据库系统是一个独立的系统，不需要操作系统的支持",
	"subject_choice_B": "数据库设计是指设计数据库管理系统",
	"subject_choice_C": "数据库技术的根本目标是要解决数据共享的问题",
	"subject_choice_D": "数据库系统中，数据的物理结构必须与逻辑结构一致",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列模式中，能够给出数据库物理存储结构与物理存取方法的是",
	"subject_choice_A": "内模式",
	"subject_choice_B": "外模式",
	"subject_choice_C": "概念模式",
	"subject_choice_D": "逻辑模式",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "Java语言的类型是",
	"subject_choice_A": "面向对象语言",
	"subject_choice_B": "面向过程语言",
	"subject_choice_C": "汇编程序",
	"subject_choice_D": "形式语言",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "Frame默认的布局管理器是",
	"subject_choice_A": "FlowLayout",
	"subject_choice_B": "BorderLayout",
	"subject_choice_C": "GridLayout",
	"subject_choice_D": "CardLayout",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "保证Java语言可移植性的特征是",
	"subject_choice_A": "面向对象",
	"subject_choice_B": "安全性",
	"subject_choice_C": "分布式计算",
	"subject_choice_D": "可跨平台",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列有关Java语言的叙述中，正确的是",
	"subject_choice_A": "Java是不区分大小写的",
	"subject_choice_B": "源文件名与public类型的类名必须相同",
	"subject_choice_C": "源文件名其扩展名为.jar",
	"subject_choice_D": "源文件中public类的数目不限",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列哪个数代表八进制整数？",
	"subject_choice_A": "0XA6",
	"subject_choice_B": "-1E3",
	"subject_choice_C": "1840",
	"subject_choice_D": "0144",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "按运算符操作数的数目划分，运算符 ？ ：的类型是",
	"subject_choice_A": "三元",
	"subject_choice_B": "二元",
	"subject_choice_C": "四元",
	"subject_choice_D": "一元",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下列代码的执行结果是：\npublic class Test3{\npublic static void main(String args[]){\nSystem.out.println(100%3);\nSystem.out.print(\",\");\nSystem.out.println(100%3.0);\n}\n}",
	"subject_choice_A": "1,1",
	"subject_choice_B": "1,1.0",
	"subject_choice_C": "1.0,1",
	"subject_choice_D": "1.0,1.0",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列赋值语句中错误的是",
	"subject_choice_A": "float f=11.1f",
	"subject_choice_B": "double d=5.3E12;",
	"subject_choice_C": "char c='\\r';",
	"subject_choice_D": "byte bb=433;",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "给出下面程序段：\nif(x>0){System.out.println(\"Hello.\");}\nelse if(x>-3){System.out.println(\"Nice to meet you!\");}\nelse {System.out.println(\"How are you?\");}\n若打印字符串“How are you?”,则x的取值范围是",
	"subject_choice_A": "x>0",
	"subject_choice_B": "x>-3",
	"subject_choice_C": "x<=-3",
	"subject_choice_D": "x<=0&x>-3",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "属于main()方法的返回类型是",
	"subject_choice_A": "public",
	"subject_choice_B": "static",
	"subject_choice_C": "void",
	"subject_choice_D": "main",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列内部类的正确用途是\nbtnn.addActionListener(new //注册监听器\nActionListener()\n{ public void actionPerformed(ActionEvent event)\n{ String s=input.getText();\noutput.setText(\"Hello\"+s+\",Welcome You!\");\n}})",
	"subject_choice_A": "用于访问外部类的数据",
	"subject_choice_B": "用于进行事件处理",
	"subject_choice_C": "隐藏起来不被同一包中的其他类所见",
	"subject_choice_D": "生成事件适配器",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列数组 a 中，版本较新的能在程序运行时动态调整大小的是",
	"subject_choice_A": "int a[]",
	"subject_choice_B": "String[] a",
	"subject_choice_C": "a=new ArrayList()",
	"subject_choice_D": "a=new Array()",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列叙述中，错误的是",
	"subject_choice_A": "接口与类的层次无关",
	"subject_choice_B": "通过接口说明类所实现的方法",
	"subject_choice_C": "通过接口可了解对象的交互界面",
	"subject_choice_D": "接口与存储空间有关",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "阅读和理解下面程序段:\nclass Manager extends Employee\n{ public Manager(String n,double s,int year,int month,int day)\n{ super(n,s,year,month,day);\nbonus=0;}\npublic double getSalary()\n{ double baseSalary=super;getSalary();\nreturn baseSalary+bonus;}\npublic void setBonus(double b)\n{ bonus=b;}\nprivate double bonus;\n}\nManager是Employee的子类,其理由是",
	"subject_choice_A": "Manager的适用范围较宽",
	"subject_choice_B": "extends关键字声明",
	"subject_choice_C": "Manager的域减小了",
	"subject_choice_D": "雇员是一个经理",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "WindowListener中可以实现窗口关闭功能的方法是",
	"subject_choice_A": "public void windowOpened(WindowEvent e)",
	"subject_choice_B": "public void windowClosed(WindowEvent e)",
	"subject_choice_C": "public void windowClosing(WindowEvent e)",
	"subject_choice_D": "public void windowDeactivated(WindowEvent e)",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列关于Applet的叙述中，错误的是",
	"subject_choice_A": "Applet是Java类，所以可以由JDK中的解释器java.exe直接解释运行",
	"subject_choice_B": "Applet应该定义为java.applet.Applet类或javax.swing.Japplet类的子类",
	"subject_choice_C": "Applet与Applicationg的主要区别在执行方式上",
	"subject_choice_D": "通过在HTML文件中采用标记可以向Applet传递参数",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "与Applet生命周期相关的方法的数量是",
	"subject_choice_A": "4种",
	"subject_choice_B": "3种",
	"subject_choice_C": "2种",
	"subject_choice_D": "5种",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下列属于正则表达式的是",
	"subject_choice_A": "一个数组",
	"subject_choice_B": "一组二进制数据",
	"subject_choice_C": "一个字符串",
	"subject_choice_D": "一个公式",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列关于线程调度的叙述中,错误的是",
	"subject_choice_A": "调用线程的sleep()方法，可以使比当前线程优先级低的线程获得运行机会",
	"subject_choice_B": "调用线程的yeild()方法，只会使与当前线程相同优先级的线程获得运行机会",
	"subject_choice_C": "当有比当前线程的优先级高的线程出现时，高优先级线程将抢占CPU并运行",
	"subject_choice_D": "具有相同优先级的多个线程的调度一定是分时的",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "调用线程的下列方法，不会改变该线程在生命周期中状态的方法是",
	"subject_choice_A": "yeild()",
	"subject_choice_B": "wait()",
	"subject_choice_C": "sleep()",
	"subject_choice_D": "isAlive()",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "Java application中的主类需包含main方法，以下哪项是main方法的正确形参？（    ）",
	"subject_choice_A": "String  args",
	"subject_choice_B": "String  args[]",
	"subject_choice_C": "Char  arg",
	"subject_choice_D": "StringBuffer args[]",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列的哪个选项可以正确用以表示八进制值8？（    ）",
	"subject_choice_A": "0x8",
	"subject_choice_B": "0x10",
	"subject_choice_C": "08",
	"subject_choice_D": "010",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "设 int x=1,float y=2，则表达式 x / y的值是：（    ）",
	"subject_choice_A": "0",
	"subject_choice_B": "1",
	"subject_choice_C": "2",
	"subject_choice_D": "以上都不是",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "若有定义：byte[] x={11,22,33,-66};\n其中0≤k≤3，则对x数组元素错误的引用是（  ）",
	"subject_choice_A": "x[5-3]",
	"subject_choice_B": "x[k]",
	"subject_choice_C": "x[k+5]",
	"subject_choice_D": "x[0]",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "Java Applet在被浏览器加载的时候首先被执行且在applet整个生命周期中只被运行一次的方法是（    ）？",
	"subject_choice_A": "init()",
	"subject_choice_B": "start()",
	"subject_choice_C": "opreationcrawl()",
	"subject_choice_D": "reader()",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "在浏览器中执行applet 程序，以下选项中的哪个方法将被最先执行（    ）。",
	"subject_choice_A": "init()",
	"subject_choice_B": "start()",
	"subject_choice_C": "destroy()",
	"subject_choice_D": "stop()",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "在Java中，一个类可同时定义许多同名的方法，这些方法的形式参数的个数、类型或顺序各不相同，传回的值也可以不相同。这种面向对象程序特性称为（    ）",
	"subject_choice_A": "隐藏",
	"subject_choice_B": "重写",
	"subject_choice_C": "重载",
	"subject_choice_D": "Java不支持此特性",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "以下有关构造方法的说法，正确的是：（    ）",
	"subject_choice_A": "一个类的构造方法可以有多个",
	"subject_choice_B": "构造方法在类定义时被调用",
	"subject_choice_C": "构造方法只能由对象中的其它方法调用。",
	"subject_choice_D": "构造方法可以和类同名，也可以和类名不同",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "类Parent、Child定义如下：\n1\\．    public class  Parent\n2\\．{ public  float  aFun(float a, float b)  throws\n3\\．  IOException {      }\n4\\．}\n5\\．public  class  Child  extends  Parent{\n6\\．\n7\\．}\n将以下哪种方法插入行6是不合法的。（    ）",
	"subject_choice_A": "float  aFun(float  a,  float  b){ }",
	"subject_choice_B": "public  int  aFun(int a, int b)throws  Exception{ }",
	"subject_choice_C": "public  float  aFun(float  p,  float q){ }",
	"subject_choice_D": "public  int  aFun(int a,  int  b)throws IOException{ }",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "给出下面代码，关于该程序以下哪个说法是正确的？（    ）\npublic class Person{\nstatic int arr[] = new int[5];\npublic static void main(String a[])\n{\nSystem.out.println(arr[0]);　}\n}",
	"subject_choice_A": "编译时将产生错误",
	"subject_choice_B": "编译时正确，运行时将产生错误",
	"subject_choice_C": "输出零",
	"subject_choice_D": "输出空",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "在编写Java  Applet程序时，需在程序的开头写上（    ）语句。",
	"subject_choice_A": "import  java.awt.* ;",
	"subject_choice_B": "import  java.applet.Applet ;",
	"subject_choice_C": "import  java.io.* ;",
	"subject_choice_D": "import  java.awt.Graphics ;",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列类定义中哪些是合法的抽象类的定义？（    ）",
	"subject_choice_A": "abstract Animal{abstract void growl();}",
	"subject_choice_B": "class abstract Animal{abstract void growl();}",
	"subject_choice_C": "abstract class Animal{abstract void growl();}",
	"subject_choice_D": "abstract class Animal{abstrac t void growl(){System.out.println(“growl”);};}",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "在使用interface声明一个接口时，只可以使用（    ）修饰符修饰该接口。",
	"subject_choice_A": "private",
	"subject_choice_B": "protected",
	"subject_choice_C": "private  protected",
	"subject_choice_D": "public",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "在使用interface声明一个接口时，只可以使用（    ）修饰符修饰该接口。",
	"subject_choice_A": "private",
	"subject_choice_B": "protected",
	"subject_choice_C": "private  protected",
	"subject_choice_D": "public",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "以下哪项可能包含菜单条（    ）。",
	"subject_choice_A": "Panel",
	"subject_choice_B": "Frame",
	"subject_choice_C": "Applet",
	"subject_choice_D": "Dialog",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列哪一项不属于Swing的顶层容器？（    ）",
	"subject_choice_A": "JApplet",
	"subject_choice_B": "JTree",
	"subject_choice_C": "JDialog",
	"subject_choice_D": "JFrame",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "给定下列表达式\nInteger I= new Integer(42);\nLong  L= new Long(42);\nDouble D= new Double(42.0);\n则下列表达式输出为true的是_____",
	"subject_choice_A": "(I==L)",
	"subject_choice_B": "(I==D)",
	"subject_choice_C": "(D==L)",
	"subject_choice_D": "(I.equals (D))",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "请问所有的异常类皆继承哪一个类？（  ）。",
	"subject_choice_A": "java.io.Exception",
	"subject_choice_B": "java.lang.Throwable",
	"subject_choice_C": "java.lang.Exception",
	"subject_choice_D": "java.lang.Error",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "数据的存储结构是指____。",
	"subject_choice_A": "存储在外存中的数据",
	"subject_choice_B": "数据所占的存储空间",
	"subject_choice_C": "数据在计算机中的顺序存储方式",
	"subject_choice_D": "数据的逻辑结构在计算机中的表示",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列关于栈的描述中错误的是：____。",
	"subject_choice_A": "栈是先进后出的线性表",
	"subject_choice_B": "栈只能顺序存储",
	"subject_choice_C": "栈具有记忆作用",
	"subject_choice_D": "对栈的插入与删除操作中，不需要改变栈底指针",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "对于长度为n的线性表，在最坏情况下，下列各排序法所对应的比较次数中正确的是____。",
	"subject_choice_A": "冒泡排序为n/2",
	"subject_choice_B": "冒泡排序为n",
	"subject_choice_C": "快速排序为n",
	"subject_choice_D": "快速排序为n(n-1)/2",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "对长度为n的线性表进行顺序查找，在最坏情况下所需要的比较次数为____。",
	"subject_choice_A": "log2n",
	"subject_choice_B": "n/2",
	"subject_choice_C": "n",
	"subject_choice_D": "n+1",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列对于线性链表的描述中正确的是____。",
	"subject_choice_A": "存储空间不一定是连续，且各元素的存储顺序是任意的",
	"subject_choice_B": "存储空间不一定是连续，且前件元素一定存储在后件元素的前面",
	"subject_choice_C": "存储空间必须连续，且前件元素一定存储在后件元素的前面",
	"subject_choice_D": "存储空间必须连续，且各元素的存储顺序是任意的",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下列对于软件测试的描述中正确的是____。",
	"subject_choice_A": "软件测试的目的是证明程序是否正确",
	"subject_choice_B": "软件测试的目的是使程序运行结果正确",
	"subject_choice_C": "软件测试的目的是尽可能多地发现程序中的错误",
	"subject_choice_D": "软件测试的目的是使程序符合结构化原则",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "为了使模块尽可能独立，要求____。",
	"subject_choice_A": "模块的内聚程度要尽量高，且各模块间的耦合程度要尽量强",
	"subject_choice_B": "模块的内聚程度要尽量高，且各模块间的耦合程度要尽量弱",
	"subject_choice_C": "模块的内聚程度要尽量低，且各模块间的耦合程度要尽量弱",
	"subject_choice_D": "模块的内聚程度要尽量低，且各模块间的耦合程度要尽量强",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列描述中正确的是____。",
	"subject_choice_A": "程序就是软件",
	"subject_choice_B": "软件开发不受计算机系统的限制",
	"subject_choice_C": "软件既是逻辑实体，又是物理实体",
	"subject_choice_D": "软件是程序、数据与相关文档的集合",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "数据独立性是数据技术的重要特点之一。所谓数据独立性是指____。",
	"subject_choice_A": "数据与程序独立存放",
	"subject_choice_B": "不同的数据被存放在不同的文件中",
	"subject_choice_C": "不同的数据只能被对应的应用程序所使用",
	"subject_choice_D": "以上三种说法都不对",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "用树形结构表示实体之间联系的模型是____。",
	"subject_choice_A": "关系模型",
	"subject_choice_B": "网状模型",
	"subject_choice_C": "层次模型",
	"subject_choice_D": "以上三个都是",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "在Java中，负责对字节代码解释执行的是____。",
	"subject_choice_A": "垃圾回收器",
	"subject_choice_B": "虚拟机",
	"subject_choice_C": "编译器",
	"subject_choice_D": "多线程机制",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列叙述中,正确的是____。",
	"subject_choice_A": "Java语言的标识符是区分大小写的",
	"subject_choice_B": "源文件名与public类名可以不相同",
	"subject_choice_C": "源文件名其扩展名为.jar",
	"subject_choice_D": "源文件中public类的数目不限",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下列属于合法的Java标识符是____。",
	"subject_choice_A": "_cat",
	"subject_choice_B": "5books",
	"subject_choice_C": "+static",
	"subject_choice_D": "-3.14159",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "在 Java 中，表示换行符的转义字符是____。",
	"subject_choice_A": "\\n",
	"subject_choice_B": "\\f",
	"subject_choice_C": "'n'",
	"subject_choice_D": "\\dd",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "在 Java 中，由Java编译器自动导入，而无需在程序中用import导入的包是____。",
	"subject_choice_A": "java.applet",
	"subject_choice_B": "java.awt",
	"subject_choice_C": "java.util",
	"subject_choice_D": "java.lang",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "在 Java 中，所有类的根类是____。",
	"subject_choice_A": "java.lang.Objet",
	"subject_choice_B": "java.lang.Class",
	"subject_choice_C": "java.applet.Applet",
	"subject_choice_D": "java.awt.Frame",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "在 Java 中，用 package 语句说明一个包时，该包的层次结构必须是____。",
	"subject_choice_A": "与文件的结构相同",
	"subject_choice_B": "与文件目录的层次相同",
	"subject_choice_C": "与文件类型相同",
	"subject_choice_D": "与文件大小相同",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "在读字符文件 Employee.dat 时，使用该文件作为参数的类是____。",
	"subject_choice_A": "BufferedReader",
	"subject_choice_B": "DataInputStream",
	"subject_choice_C": "DataOutputStream",
	"subject_choice_D": "FileInputStream",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列构造方法的调用方式中，正确的是____。",
	"subject_choice_A": "按照一般方法调用",
	"subject_choice_B": "由用户直接调用",
	"subject_choice_C": "只能通过 new 自动调用",
	"subject_choice_D": "被系统调用",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "类 Panel 默认的布局管理器是____。",
	"subject_choice_A": "GridLayout",
	"subject_choice_B": "BorderLayout",
	"subject_choice_C": "FlowLayout",
	"subject_choice_D": "GardLayout",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "在 Java 中，能实现多重继承效果的方式是____。",
	"subject_choice_A": "内部类",
	"subject_choice_B": "适配器",
	"subject_choice_C": "接口",
	"subject_choice_D": "同步",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "char 类型的取值范围是____。",
	"subject_choice_A": "2-7～27-1",
	"subject_choice_B": "0～216-1",
	"subject_choice_C": "-215～215-1",
	"subject_choice_D": "0～28-1",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "能够支持 javadoc 命令的注释语句是____。",
	"subject_choice_A": "/**...//",
	"subject_choice_B": "/*...*/",
	"subject_choice_C": "//",
	"subject_choice_D": "/**...*/",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "十进制数16的16进制表示格式是____。",
	"subject_choice_A": "0x10",
	"subject_choice_B": "0x16",
	"subject_choice_C": "0xA",
	"subject_choice_D": "016",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "int 型 public 成员变量 MAX_LENGTH，该值保持为常数100，则定义这个变量的语句是____。",
	"subject_choice_A": "public int MAX_LENGTH=100",
	"subject_choice_B": "final int MAX_LENGTH=100",
	"subject_choice_C": "public const int MAX_LENGTH=100",
	"subject_choice_D": "public final int MAX_LENGTH=100",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列不是 InputStream 子类的是____。",
	"subject_choice_A": "文件输入流 FileInputStream",
	"subject_choice_B": "对象输入流 ObjectInputStream",
	"subject_choice_C": "字符输入流 CharInputStream",
	"subject_choice_D": "压缩文件输入流 ZipInputStream",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列方法中可以用来创建一个新线程的是____。",
	"subject_choice_A": "实现java.lang.Runnable 接口并重写 start()方法",
	"subject_choice_B": "实现java.lang.Runnable 接口并重写 run()方法",
	"subject_choice_C": "继承java.lang.Thread 类并重写 run()方法",
	"subject_choice_D": "实现java.lang.Thread 类并实现 start()方法",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列关于 Java Application 与 Applet 的说法中，正确的是____。",
	"subject_choice_A": "都包含 main() 方法",
	"subject_choice_B": "都通过“appletviewer”命令执行",
	"subject_choice_C": "都通过“javac”命令编译",
	"subject_choice_D": "都嵌入在 HTML 文件中执行",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "当启动 Applet 程序时，首先调用的方法是____。",
	"subject_choice_A": "stop()",
	"subject_choice_B": "init()",
	"subject_choice_C": "start()",
	"subject_choice_D": "destroy()",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列叙述中正确的是（    ）。",
	"subject_choice_A": "对长度为n的有序链表进行查找，最坏情况下需要的比较次数为n",
	"subject_choice_B": "对长度为n的有序链表进行对分查找，最坏情况下需要的比较次数为(n／2)",
	"subject_choice_C": "对长度为n的有序链表进行对分查找，最坏情况下需要的比较次数为(log2(下标)n)",
	"subject_choice_D": "对长度为n的有序链表进行对分查找，最坏情况—卜需要的比较次数为(nlog2(下标)n)",
	"subject_answer": "C",
	"analysis": "二分法查找只适用于顺序存储的有序表，对于长度为n的有序线性表，最坏情况只需比较log2n次。"
}, {
	"subject_title": "算法的时间复杂度是指（    ）。",
	"subject_choice_A": "算法的执行时间",
	"subject_choice_B": "算法所处理的数据量",
	"subject_choice_C": "算法程序中的语句或指令条数",
	"subject_choice_D": "算法在执行过程中所需要的基本运算次数",
	"subject_answer": "D",
	"analysis": "算法的时间复杂度是指算法需要消耗的时间资源。一般来说，计算机算法是问题规模n的函数f(n)，算法的时间复杂度也因此记做T(n)=O(f(n))因此，问题的规模n越大，算法执行的时间的增长率与f(n)的增长率正相关，称作渐进时间复杂度(AsymptoticTimeComplexity)。简单来说就是算法在执行过程中所需要的基本运算次数。"
}, {
	"subject_title": "软件按功能可以分为：应用软件、系统软件和支撑软件(或工具软件)，下面属于系统软件的是（    ）。",
	"subject_choice_A": "编辑软件",
	"subject_choice_B": "操作系统",
	"subject_choice_C": "教务管理系统",
	"subject_choice_D": "浏览器",
	"subject_answer": "B",
	"analysis": "编辑软件和浏览器属于工具软件，教务系统是应用软件。"
}, {
	"subject_title": "软件(程序)调试的任务是（    ）。",
	"subject_choice_A": "诊断和改正程序中的错误",
	"subject_choice_B": "尽可能多地发现程序中的错误",
	"subject_choice_C": "发现并改正程序中的所有错误",
	"subject_choice_D": "确定程序中错误的性质",
	"subject_answer": "A",
	"analysis": "调试的目的是发现错误或导致程序失效的错误原因，并修改程序以修正错误。调试是测试之后的活动"
}, {
	"subject_title": "数据流程图(DFD图)是（    ）。",
	"subject_choice_A": "软件概要设计的工具",
	"subject_choice_B": "软件详细设计的工具",
	"subject_choice_C": "结构化方法的需求分析工具",
	"subject_choice_D": "面向对象方法的需求分析工具",
	"subject_answer": "D",
	"analysis": "数据流程图是一种结构化分析描述模型，用来对系统的功能需求进行建模。"
}, {
	"subject_title": "软件生命周期可分为定义阶段，开发阶段和维护阶段。详细设计属于（    ）。",
	"subject_choice_A": "定义阶段",
	"subject_choice_B": "开发阶段",
	"subject_choice_C": "维护阶段",
	"subject_choice_D": "上述三个阶段",
	"subject_answer": "B",
	"analysis": "开发阶段在开发初期分为需求分析、总体设计、详细设计3个阶段了，在开发后期分为编码、测试两个子阶段。"
}, {
	"subject_title": "数据库管理系统中负责数据模式定义的语言是（    ）。",
	"subject_choice_A": "数据定义语言",
	"subject_choice_B": "数据管理语言",
	"subject_choice_C": "数据操纵语言",
	"subject_choice_D": "数据控制语言",
	"subject_answer": "C",
	"analysis": "模式描述语言(DaraDescriptionLanguage，DDL)来描述、定义的，体现、反映了数据库系统的整体观。"
}, {
	"subject_title": "在学生管理的关系数据库中，存取一个学生信息的数据单位是（    ）。",
	"subject_choice_A": "文件",
	"subject_choice_B": "数据库",
	"subject_choice_C": "字段",
	"subject_choice_D": "记录",
	"subject_answer": "D",
	"analysis": "一个数据库由一个文件或文件集合组成。这些文件中的信息可分解成一个个记录。"
}, {
	"subject_title": "数据库设计中，用E-R图来描述信息结构但不涉及信息在计算机中的表示，它属于数据库设计的（    ）。",
	"subject_choice_A": "需求分析阶段",
	"subject_choice_B": "逻辑设计阶段",
	"subject_choice_C": "概念设计阶段",
	"subject_choice_D": "物理设计阶段",
	"subject_answer": "C",
	"analysis": "实体联系图Entity-RelationshipE-R图为实体-联系图，提供了表示实体型、属性和联系的方法，用来描述现实世界的概念模型。"
}, {
	"subject_title": "有两个关系R和T如下：\n \n \n则由关系R得到关系T的操作是(    )。",
	"subject_choice_A": "选择",
	"subject_choice_B": "投影",
	"subject_choice_C": "交",
	"subject_choice_D": "并",
	"subject_answer": "D",
	"analysis": "选择是建立一个含有与原始关系相同列数的新表，但是行只包括那些满足某些特定标准的原始关系行。"
}, {
	"subject_title": "Java中定义常量的保留字是（    ）。",
	"subject_choice_A": "const",
	"subject_choice_B": "final",
	"subject_choice_C": "finally",
	"subject_choice_D": "native",
	"subject_answer": "B",
	"analysis": "fmal是最终的修饰符，其修饰的是常量。"
}, {
	"subject_title": "下列关于Java布尔类型的描述中，正确的是（    ）。",
	"subject_choice_A": "一种基本的数据类型，它的类型名称为boolean",
	"subject_choice_B": "用int表示类型",
	"subject_choice_C": "其值可以赋给int类型的变量",
	"subject_choice_D": "有两个值，1代表真，0代表假",
	"subject_answer": "A",
	"analysis": "布尔类型数据只有两个值：true(真)、false(假)，不对应任何数字，不能与数字进行转换，布尔类型数据一般用于逻辑判别。"
}, {
	"subject_title": "Java中所有类的父类是（    ）。",
	"subject_choice_A": "Father",
	"subject_choice_B": "Dang",
	"subject_choice_C": "Exception",
	"subject_choice_D": "Object",
	"subject_answer": "D",
	"analysis": "ObJeot是所有类的根。"
}, {
	"subject_title": "下列程序段的输出结果是（    ）。\nintdata=0；\nchark='a'，p='f'\ndata=p-k；\nSystem.out.printlln(data)；",
	"subject_choice_A": "0",
	"subject_choice_B": "a",
	"subject_choice_C": "f",
	"subject_choice_D": "5",
	"subject_answer": "D",
	"analysis": "a和f的ASCII值相差5。"
}, {
	"subject_title": "下列数中为八进制的是（    ）。",
	"subject_choice_A": "27",
	"subject_choice_B": "0x25",
	"subject_choice_C": "026",
	"subject_choice_D": "028",
	"subject_answer": "C",
	"analysis": "采用0，1，2，3，4，5，6，7八个数码，逢八进位，并且开头一定要以数字0开头的为八进制。"
}, {
	"subject_title": "下列方法中，不属于Throwable类的方法是（    ）。",
	"subject_choice_A": "printMessage",
	"subject_choice_B": "getMessage",
	"subject_choice_C": "toString",
	"subject_choice_D": "fillStackTrace",
	"subject_answer": "C",
	"analysis": "toString是Object类的方法，所有类都从Object类继承。"
}, {
	"subject_title": "下列程序的输出结果是（    ）。\nPublicclassTest{\nPublicstaticvoidmain(String[]args){\nint[]array=(2，4，6，8，10)；\nintsize=6；\nintresult=-1；\ntry{\nfor(inti=0；i＜size&&result==-1；)\nif(array[i]==20)result=i；\n}\ncatch(ArithmeticExceptione){\nSystem.out.println(\"Catch---1\")；\n}\ncatch(Array IndexOutOfBoundsExceptione){\nSystem.out.println(\"Catch---2\")；\n}\ncatch(Exceptione){\nSystem.out.println(\"Catch---3\")；\n}\n}",
	"subject_choice_A": "Catch---1",
	"subject_choice_B": "Catch---2",
	"subject_choice_C": "Catch---3",
	"subject_choice_D": "以上都不对",
	"subject_answer": "B",
	"analysis": "略"
}, {
	"subject_title": "下列包中，包含JoptionPane类的是（    ）。",
	"subject_choice_A": "javax.swing",
	"subject_choice_B": "java.lang",
	"subject_choice_C": "java.util",
	"subject_choice_D": "java.applet",
	"subject_answer": "A",
	"analysis": "Swing中提供了JOptionPane类来实现类似Windows平台下的MessageBox的功能，利用JOptionPane类中的各个staUc方法来生成各种标准的对话框，实现显示出信息、提出问题、警告、用户输入参数等功能。且这些对话框都是模式对话框。"
}, {
	"subject_title": "下列选项中，与成员变量共同构成一个类的是（    ）。",
	"subject_choice_A": "关键字",
	"subject_choice_B": "方法",
	"subject_choice_C": "运算符",
	"subject_choice_D": "表达式",
	"subject_answer": "B",
	"analysis": "类体中定义的两种成员，数据成员和成员函数。"
}, {
	"subject_title": "下列程序的功能是将一个整数数组写入二进制文件，在程序的下划线处应填入的选项是（    ）。\nimportjava.io.*；\npublicclassXieShuzu{\npublicstaticvoidmain(String[]a){\nint[]myArray=(10，20，30，40)；\ntry{\nDataOutputStreamdos=\nnewDataOu中utStream(new\nFileOutputStream(\"ints.dat\"))；\nfor(inti=O；i＜myArray.length；i++)\ndos.______(myArray[])；\ndos.close()；\nSystem.out.println(\"已经将整数数组写入二进制文件：ints.dat\")：\n}catch(IOExceptionioe)\n{System.out.println(\"IOExcepr_on\")；}\n}\n}",
	"subject_choice_A": "writeArray",
	"subject_choice_B": "writeByte",
	"subject_choice_C": "writeInt",
	"subject_choice_D": "writeDouble",
	"subject_answer": "C",
	"analysis": "向流中写入整数数组，用WrinteInt方法。"
}, {
	"subject_title": "Java中的抽象类Reader和Writer所处理的流是（    ）。，",
	"subject_choice_A": "图像流",
	"subject_choice_B": "对象流",
	"subject_choice_C": "字节流",
	"subject_choice_D": "字符流",
	"subject_answer": "D",
	"analysis": "Reader／Writer所处理的流是字符流，InputStream／OutputStream的处理对象是字节流。"
}, {
	"subject_title": "下列叙述中，错误的是（    ）。",
	"subject_choice_A": "内部类的名称与定义它的类的名称可以相同",
	"subject_choice_B": "内部类可用abstract修饰",
	"subject_choice_C": "内部类可作为其他类的成员",
	"subject_choice_D": "内部类可访问它所在类的成员",
	"subject_answer": "A",
	"analysis": "内部类与外部类的名称不能相同。"
}, {
	"subject_title": "用于在子类中调用被重写父类方法的关键字是（    ）。",
	"subject_choice_A": "this",
	"subject_choice_B": "super",
	"subject_choice_C": "This",
	"subject_choice_D": "Super",
	"subject_answer": "B",
	"analysis": "super可用于调用被重写的父类方法，注意Java的大小写敏感。"
}, {
	"subject_title": "下列Java语句从指定网址读取html文件，在下划线处应填上的选项是（    ）。\nReaderin=new_______(newURL(urlString).openStream())；",
	"subject_choice_A": "Reader",
	"subject_choice_B": "DataOutputStream",
	"subject_choice_C": "ByteArraylnputStream",
	"subject_choice_D": "InputStreamReader",
	"subject_answer": "A",
	"analysis": "创建一个Reader流的对象in。"
}, {
	"subject_title": "下列不属于表达式语句的是（    ）。",
	"subject_choice_A": "++i；",
	"subject_choice_B": "--j；",
	"subject_choice_C": "b#a；",
	"subject_choice_D": "b*=a；",
	"subject_answer": "C",
	"analysis": "前两项是自加减运算，最后一项是b=b*a。"
}, {
	"subject_title": "下列为窗口事件的是（    ）。",
	"subject_choice_A": "MouseEvent",
	"subject_choice_B": "WindowEvent",
	"subject_choice_C": "ActionEvent",
	"subject_choice_D": "KeyEvent",
	"subject_answer": "B",
	"analysis": "MouseEvent鼠标事件，AcfionEvent组件事件，KeyEvent键盘事件。"
}, {
	"subject_title": "用鼠标点击菜单项(Menultem)产生的事件是（    ）。",
	"subject_choice_A": "MenuEvent",
	"subject_choice_B": "ActionEvent",
	"subject_choice_C": "KeyEvent",
	"subject_choice_D": "MouseEvent",
	"subject_answer": "B",
	"analysis": "ActionEvent组件事件，当特定于组件的动作(比如被按下)发生时，由组件(比如Button)生成此高级别事件。事件被传递给每一个ActionListener对象，这些对象是使用组件的addActionListener方法注册的，用以接收这类事件。"
}, {
	"subject_title": "下列不属于逻辑运算符的是（    ）。",
	"subject_choice_A": "t",
	"subject_choice_B": "||",
	"subject_choice_C": "&&",
	"subject_choice_D": "I",
	"subject_answer": "D",
	"analysis": "!是逻辑非，||是逻辑或，&amp;&amp;是逻辑与，|是按位或。"
}, {
	"subject_title": "当使用SomeThread t=new SomeThread（    ）创建一个线程时，下列叙述中正确的是(    )。",
	"subject_choice_A": "SomeThread类是包含run()方法的任意Java类",
	"subject_choice_B": "SomeThread类一定要实现Runnable接口",
	"subject_choice_C": "SomeThread类是Thread类的子类",
	"subject_choice_D": "SomeThread类是Thread类的子类并且要实现Runnable接口",
	"subject_answer": "C",
	"analysis": "由SomeThreadtead=newSomeThread()可知此题是通过继承Thread类来创建线程的。"
}, {
	"subject_title": "在程序的下划线处应填入的选项是（    ）。\npublicclassTest________{\npublicstaticvoidmain(Stringargs[]){\nTestt=newTest()\nThreadtt=newThread(t)；\ntt.start()；\n}\npublicvoidmn(){\nfor(inti=0；i＜5；i++){\nSystem.out.println(\"i=\"+i)；\n}\n}\n}",
	"subject_choice_A": "implementsRunnable",
	"subject_choice_B": "extendsThread",
	"subject_choice_C": "implementsThread",
	"subject_choice_D": "extendsRunnable",
	"subject_answer": "A",
	"analysis": "Test类实现了Runnable接口。"
}, {
	"subject_title": "下列数据结构中，属于非线性结构的是",
	"subject_choice_A": "循环队列",
	"subject_choice_B": "带链队列",
	"subject_choice_C": "二叉树",
	"subject_choice_D": "带链栈",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列数据结构中，能够按照“先进后出”原则存取数据的是",
	"subject_choice_A": "循环队列",
	"subject_choice_B": "栈",
	"subject_choice_C": "队列",
	"subject_choice_D": "二叉树",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "对于循环队列，下列叙述中正确的是",
	"subject_choice_A": "队头指针是固定不变的",
	"subject_choice_B": "队头指针一定大于队尾指针",
	"subject_choice_C": "队头指针一定小于队尾指针",
	"subject_choice_D": "队头指针可以大于队尾指针，也可以小于队尾指针",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "算法的空间复杂度是指",
	"subject_choice_A": "算法在执行过程中所需要的计算机存储空间",
	"subject_choice_B": "算法所处理的数据量",
	"subject_choice_C": "算法程序中的语句或指令条数",
	"subject_choice_D": "算法在执行过程中所需要的临时工作单元数",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "软件设计中划分模块的一个准则是",
	"subject_choice_A": "低内聚低耦合",
	"subject_choice_B": "高内聚低耦合",
	"subject_choice_C": "低内聚高耦合",
	"subject_choice_D": "高内聚高耦合",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列选项中不属于结构化程序设计原则的是",
	"subject_choice_A": "可封装",
	"subject_choice_B": "自顶向下",
	"subject_choice_C": "模块化",
	"subject_choice_D": "逐步求精",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "软件详细设计产生的图如下：\n \n \n该图是",
	"subject_choice_A": "N-S图",
	"subject_choice_B": "PAD图",
	"subject_choice_C": "程序流程图",
	"subject_choice_D": "E-R图",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "数据库管理系统是",
	"subject_choice_A": "操作系统的一部分",
	"subject_choice_B": "在操作系统支持下的系统软件",
	"subject_choice_C": "一种编译系统",
	"subject_choice_D": "一种操作系统",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "在E-R图中，用来表示实体联系的图形是",
	"subject_choice_A": "椭圆图",
	"subject_choice_B": "矩形",
	"subject_choice_C": "菱形",
	"subject_choice_D": "三角形",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "有三个关系R，S和T如下：\n其中关系T由关系R和S通过某种操作得到，该操作为",
	"subject_choice_A": "选择",
	"subject_choice_B": "投影",
	"subject_choice_C": "交",
	"subject_choice_D": "并",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "用于设置组件大小的方法是",
	"subject_choice_A": "paint( )",
	"subject_choice_B": "setSize( )",
	"subject_choice_C": "getSize( )",
	"subject_choice_D": "repaint( )",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "点击窗口内的按钮时，产生的事件是",
	"subject_choice_A": "MouseEvent",
	"subject_choice_B": "WindowEvent",
	"subject_choice_C": "ActionEvent",
	"subject_choice_D": "KeyEvent",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "AWT中用来表示对话框的类是",
	"subject_choice_A": "Font",
	"subject_choice_B": "Color",
	"subject_choice_C": "Panel",
	"subject_choice_D": "Dialog",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列运算符中，优先级最高的是",
	"subject_choice_A": "+=",
	"subject_choice_B": "= =",
	"subject_choice_C": "&&",
	"subject_choice_D": "++",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列运算结果为1的是",
	"subject_choice_A": "8>>1",
	"subject_choice_B": "4>>>2",
	"subject_choice_C": "8<<1",
	"subject_choice_D": "4<<<2",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列语句中，可以作为无限循环语句的是",
	"subject_choice_A": "for(;;) {}",
	"subject_choice_B": "for(int i=0; i<10000;i++) {}",
	"subject_choice_C": "while(false) {}",
	"subject_choice_D": "do {} while(false)",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下列表达式中，类型可以作为int型的是",
	"subject_choice_A": "“abc”+”efg”",
	"subject_choice_B": "“abc”+’efg’",
	"subject_choice_C": "‘a’+’b’",
	"subject_choice_D": "3+”4”",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "阅读下列程序\nPublic class Test implements Runnable{\nPrivate int x=0;\nPrivate int y=o;\nboolean flag=true;\nPublic static void main(string[ ] args) {\nTest  r =new Test( );\nThead t1=new Thead(r);\nThead t2=new Thead(r);\nt1.start( );\nt2.start( );\n}\nPublic void run(){\nWhile(flag) {\nx++;\ny++;\nsystem.out.println(“(” +x_ “,”+y+”)”);\nif (x>=10)\nflag=false;\n}\n}\n}\n下列对程序运行结果描述的选项中，正确的是",
	"subject_choice_A": "每行的（x,y）中，可能有；每一对（x,y）值都出现两次。",
	"subject_choice_B": "每行的（x,y）中，可能有；每一对（x,y）值仅出现一次。",
	"subject_choice_C": "每行的（x,y）中，可能有x=y；每一对（x,y）值都出现两次。",
	"subject_choice_D": "每行的（x,y）中，可能有x=y；每一对（x,y）值都出现一次。",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "如果线程正处于运行状态，则它可能到达的下一个状态是",
	"subject_choice_A": "只有终止状态",
	"subject_choice_B": "只有阻塞状态和终止状态",
	"subject_choice_C": "可运行状态，阻塞状态，终止状态",
	"subject_choice_D": "其他所有状态",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "在下列程序的空白处，应填入的正确选项是\nimport java.io.*;\nPublic class writeInt{\nPublic static void main(string[ ] a) {\nInt[ ] myArray = {10,20,30,40};\ntry{\nDataOutputSystem dos= new DataOutputSystem\n（new FileOutputSystem(“ints.dat”)）;\nfor  （int i=0；I<myArray.length；i++）\ndos。writeInt（myArray[i]）;\ndos.\nSystem.out.println\n(“Have written binary file ints.dat”);\n}\nCatch(IOException ioe)\n{    System.out.println(“IO Exception”);\n}\n}\n}",
	"subject_choice_A": "start( )",
	"subject_choice_B": "close( )",
	"subject_choice_C": "read( )",
	"subject_choice_D": "write( )",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "在一个线程中调用下列方法，不会改变该线程运行状态的是",
	"subject_choice_A": "yield方法",
	"subject_choice_B": "另一个线程的join方法",
	"subject_choice_C": "sleep方法",
	"subject_choice_D": "一个对象的notify方法",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "在关闭浏览器时调用，能够彻底终止Applet并释放该Applet所有资源的方法是",
	"subject_choice_A": "stop( )",
	"subject_choice_B": "destroy( )",
	"subject_choice_C": "paint( )",
	"subject_choice_D": "start( )",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "为了将HelloApplet(主类名为HelloApplet.class)嵌入在greeting.html文件中，应该在下列greeting.html文件的横线处填入的代码是\n<HTML>\n<HEAD>\n<TITLE> Greetings </TITLE>\n</HEAD>\n<BODY>\n<APPLET ______>\n</APPLET>\n</BODY>\n</HTML>",
	"subject_choice_A": "ＨelloApplet.class",
	"subject_choice_B": "CODE=” ＨelloApplet.class”",
	"subject_choice_C": "CODE=” ＨelloApplet.class” WIDTH=150 HEIGHT=25",
	"subject_choice_D": "CODE=” ＨelloApplet.class” WIDTH=10 HEIGHT=10",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列变量名的定义中，符合Java命名约定的是",
	"subject_choice_A": "fieldname",
	"subject_choice_B": "super",
	"subject_choice_C": "Intnum",
	"subject_choice_D": "$number",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "自定义异常类的父类可以是",
	"subject_choice_A": "Error",
	"subject_choice_B": "VirtuaMachineError",
	"subject_choice_C": "Exception",
	"subject_choice_D": "Thread",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "阅读下列程序片段\nPublic void test(){\nTry{\nsayHello();\nsystem.out.println(“hello”);\n} catch (ArrayIndexOutOfBoundException e) {\nSystem.out.println(“ArrayIndexOutOfBoundException”);\n}catch(Exception e){\nSystem.out.println(“Exception”);\n}finally {\nSystem.out.println(“finally”);\n}\n}\n如果sayHello( )方法正常运行，则test( )方法的运行结果将是",
	"subject_choice_A": "Hello",
	"subject_choice_B": "ArrayIndexOutOfBondsException",
	"subject_choice_C": "Exception",
	"subject_choice_D": "Hello",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "为使Java程序独立于平台，Java虚拟机把字节码与各个操作系统及硬件",
	"subject_choice_A": "分开",
	"subject_choice_B": "结合",
	"subject_choice_C": "联系",
	"subject_choice_D": "融合",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "Java中的基本数据类型int在不同的操作系统平台的字长是",
	"subject_choice_A": "不同的",
	"subject_choice_B": "32位",
	"subject_choice_C": "64位",
	"subject_choice_D": "16位",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "String、StingBuffer都是______类，都不能被继承。",
	"subject_choice_A": "static",
	"subject_choice_B": "abstract",
	"subject_choice_C": "final",
	"subject_choice_D": "private",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列程序的功能是统计字符串中“array”的个数，在程序的空白处应填入的正确选项是\npublic class FindKeyWords{\npublic static void main(sring[] args){\nsting text=\n“ An array is a data structur that stores a collection of”\n+ “values of the same type . You access each individual value”\n+ “through an integer index . For example,if a is an array”\n+ “of inergers, then a[i] is the ith integer in the array.”;\nInt arrayCount =0;\nInt idex = -1;\nSting arrarStr =”array”;\nIndex = text.indexof(arrayStr);\nWhile(index          0) {\n++arrayCount;\nIndex += arrayStr.length();\nIndex = text.indexof(arrayStr,index);\n}\nSystem.out.println\n(“the text contains” + arrayCount + “arrays”);\n}\n}",
	"subject_choice_A": "<",
	"subject_choice_B": "=",
	"subject_choice_C": "<=",
	"subject_choice_D": ">=",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列叙述中正确的是",
	"subject_choice_A": "栈是“先进先出”的线性表",
	"subject_choice_B": "队列是“先进先出”的线性表",
	"subject_choice_C": "循环队列是非线性结构",
	"subject_choice_D": "有序性表既可以采用顺序存储结构，也可以采用链式存储结构",
	"subject_answer": "B",
	"analysis": "在队列这种数据结构中，最先插入在元素将是最先被删除；反之最后插入的元素将最后被删除，因此队列又称为“先进先出”（FIFO—first in first out）的线性表。"
}, {
	"subject_title": "支持子程序调用的数据结构是",
	"subject_choice_A": "栈",
	"subject_choice_B": "树",
	"subject_choice_C": "队列",
	"subject_choice_D": "二叉树",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "某二叉树有5个度为2的结点，则该二叉树中的叶子结点数是",
	"subject_choice_A": "10",
	"subject_choice_B": "8",
	"subject_choice_C": "6",
	"subject_choice_D": "4",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列排序方法中，最坏情况下比较次数最少的是",
	"subject_choice_A": "冒泡排序",
	"subject_choice_B": "简单选择排序",
	"subject_choice_C": "直接插入排序",
	"subject_choice_D": "堆排序",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "软件按功能可以分为：应用软件、系统软件和支撑软件（或工具软件）。下面属于应用软件的是",
	"subject_choice_A": "编译软件",
	"subject_choice_B": "操作系统",
	"subject_choice_C": "教务管理系统",
	"subject_choice_D": "汇编程序",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下面叙述中错误的是",
	"subject_choice_A": "软件测试的目的是发现错误并改正错误",
	"subject_choice_B": "对被调试的程序进行“错误定位”是程序调试的必要步骤",
	"subject_choice_C": "程序调试通常也称为Debug",
	"subject_choice_D": "软件测试应严格执行测试计划，排除测试的随意性",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "耦合性和内聚性是对模块独立性度量的两个标准。下列叙述中正确的是",
	"subject_choice_A": "提高耦合性降低内聚性有利于提高模块的独立性",
	"subject_choice_B": "降低耦合性提高内聚性有利于提高模块的独立性",
	"subject_choice_C": "耦合性是指一个模块内部各个元素间彼此结合的紧密程度",
	"subject_choice_D": "内聚性是指模块间互相连接的紧密程度",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "数据库应用系统中的核心问题是",
	"subject_choice_A": "数据库设计",
	"subject_choice_B": "数据库系统设计",
	"subject_choice_C": "数据库维护",
	"subject_choice_D": "数据库管理员培训",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "有两个关系R，S如下：\nR\nA    B    C\na    3    2\nb    0    1\nc    2    1\nS\nA    B\na    3\nb    0\nc    2\n由关系R通过运算得到关系S，则所使用的运算为",
	"subject_choice_A": "选择",
	"subject_choice_B": "投影",
	"subject_choice_C": "插入",
	"subject_choice_D": "连接",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "将E-R图转换为关系模式时，实体和联系都可以表示为",
	"subject_choice_A": "属性",
	"subject_choice_B": "键",
	"subject_choice_C": "关系",
	"subject_choice_D": "域",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "Java虚拟机(JVM)运行Java代码时，不会进行的操作时",
	"subject_choice_A": "加载代码",
	"subject_choice_B": "校验代码",
	"subject_choice_C": "编译代码",
	"subject_choice_D": "执行代码",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "Java程序的并发机制是",
	"subject_choice_A": "多线程",
	"subject_choice_B": "多接口",
	"subject_choice_C": "多平台",
	"subject_choice_D": "多态性",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "在方法内部使用，代表对当前对象自身引用的关键字是",
	"subject_choice_A": "super",
	"subject_choice_B": "This",
	"subject_choice_C": "Super",
	"subject_choice_D": "this",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "阅读下列程序\npublic class VariableUse{\npublic static void main (String[] args) {\nint a;\nif (a==8) {\nint b=9;\nSystem.out.println(“a = ”+a);\nSystem.out.println(“b = ”+b);\n}\nSystem.out.println(“a = ”+a);\nSystem.out.println(“b = ”+b);\n}\n}\n该程序在编译时的结果是",
	"subject_choice_A": "变量a未赋值",
	"subject_choice_B": "第二个System.out.println(“b = ”+b)语句中，变量b作用域有错",
	"subject_choice_C": "第二个System.out.println(“a = ”+a)语句中，变量a作用域有错",
	"subject_choice_D": "第一个System.out.println(“b = ”+b)语句中，变量b作用域有错",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列不属于Swing的构件是",
	"subject_choice_A": "JButton",
	"subject_choice_B": "JLabel",
	"subject_choice_C": "JFrame",
	"subject_choice_D": "JPane",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "对鼠标点击按钮操作进行事件处理的接口是",
	"subject_choice_A": "MouseListener",
	"subject_choice_B": "WindowsListener",
	"subject_choice_C": "ActionListener",
	"subject_choice_D": "KeyListener",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "AWT中用来表示颜色的类是",
	"subject_choice_A": "Font",
	"subject_choice_B": "Color",
	"subject_choice_C": "Panel",
	"subject_choice_D": "Dialog",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列运算符中，优先级最高的是",
	"subject_choice_A": "++",
	"subject_choice_B": "+",
	"subject_choice_C": "*",
	"subject_choice_D": ">",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下列运算中属于跳转语句的是",
	"subject_choice_A": "try",
	"subject_choice_B": "catch",
	"subject_choice_C": "finally",
	"subject_choice_D": "break",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "阅读下列利用递归来求n!的程序\nClass FactorialTest{\nStatic long Factorial (int n) { //定义Factorial ()方法\nIf (n==1)\nReturn 1;\nElse\nReturn n* Factorial(_____);\n}\nPublic static void main (String a[]) { // main ()方法\nInt n=8;\nSystem.out.println{n+”! = ”+Factorial (n)};\n}\n}\n为保证程序正确运行，在下划线处应该填入的参数是",
	"subject_choice_A": "n-1",
	"subject_choice_B": "n-2",
	"subject_choice_C": "n",
	"subject_choice_D": "n+1",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "阅读下列代码\nPublic class Person{\nStatic int arr[ ] = new int (10);\nPublic static void main (String args  []) {\nSystem.out.println(arr[9]);\n}\n}\n该代码运行的结果是",
	"subject_choice_A": "编译时将产生错误",
	"subject_choice_B": "编译时正确，运行时将产生错误",
	"subject_choice_C": "输出0",
	"subject_choice_D": "输出空",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "在Java中，若要使用一个包中的类时，首先要求对该包进行导入，其关键字是",
	"subject_choice_A": "import",
	"subject_choice_B": "package",
	"subject_choice_C": "include",
	"subject_choice_D": "packet",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "继承是面向对象编程的一个重要特征，它可降低程序的复杂性并使代码",
	"subject_choice_A": "可读性好",
	"subject_choice_B": "可重用",
	"subject_choice_C": "可跨包访问",
	"subject_choice_D": "运行更安全",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "阅读下列代码片段\nClass InterestTest________ActionListener{\nPublic void actionPerformed (ActionEvent event) {\nDouble interest = balance * rate/100;\nBalance += interest;\nNumber Format format =\nNumber Format.getCurrencyInstance ();\nSystem.out.printlb{“balance = ”+\nFormatter.format (balance)};\n}\nPrivate double rate;\n}\n在下划线处，应填的正确选项是",
	"subject_choice_A": "Implementation",
	"subject_choice_B": "Inneritance",
	"subject_choice_C": "implements",
	"subject_choice_D": "extends",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列方法中，不属于类String的方法是",
	"subject_choice_A": "tolowerCase ()",
	"subject_choice_B": "valueof ()",
	"subject_choice_C": "charAt ()",
	"subject_choice_D": "append ()",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "grid (9)[5]描述的是",
	"subject_choice_A": "二维数组",
	"subject_choice_B": "一维数组",
	"subject_choice_C": "五维数组",
	"subject_choice_D": "九维数组",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "Java类库中，将信息写入内存的类是",
	"subject_choice_A": "java.io.FileOutputStream",
	"subject_choice_B": "java.io.ByteArrayOutputStream",
	"subject_choice_C": "java.io.BufferedOutputStream",
	"subject_choice_D": "java.io.DataOutputStream",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "阅读下列Java语句\nObjectOutputStream out\nNew ObjectOutputStream {new_______(“employee.dat”)};\n在下划线处，应填的正确选项是",
	"subject_choice_A": "File",
	"subject_choice_B": "FileWriter",
	"subject_choice_C": "FileOutputStream",
	"subject_choice_D": "OutputStream",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "使新创建的线程参与运行调度的方法是",
	"subject_choice_A": "run ()",
	"subject_choice_B": "start ()",
	"subject_choice_C": "init ()",
	"subject_choice_D": "resume ()",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "Java中的线程模型由三部分组成，与线程模型组成无关的是",
	"subject_choice_A": "虚拟的CPU",
	"subject_choice_B": "程序代码",
	"subject_choice_C": "操作系统的内核状态",
	"subject_choice_D": "数据",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列叙述中正确的是",
	"subject_choice_A": "算法的效率只与问题的规模有关，而与数据的存储结构无关",
	"subject_choice_B": "算法的时间复杂度是指执行算法所需要的计算工作量",
	"subject_choice_C": "数据的逻辑结构与存储结构是一一对应的",
	"subject_choice_D": "算法的时间复杂度与空间复杂度一定相关",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "在结构化程序设计中，模块划分的原则是",
	"subject_choice_A": "各模块应包括尽量多的功能",
	"subject_choice_B": "各模块的规模应尽量大",
	"subject_choice_C": "各模块之间的联系应尽量紧密",
	"subject_choice_D": "模块内具有高内聚度、模块间具有低耦合度",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "下列叙述中正确的是",
	"subject_choice_A": "软件测试的主要目的是发现程序中的错误",
	"subject_choice_B": "软件测试的主要目的是确定程序中错误的位置",
	"subject_choice_C": "为了提高软件测试的效率，最好由程序编制者自己来完成软件测试的工作",
	"subject_choice_D": "软件测试是证明软件没有错误",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下面选项中不属于面向对象程序设计特征的是",
	"subject_choice_A": "继承性",
	"subject_choice_B": "多态性",
	"subject_choice_C": "类比性",
	"subject_choice_D": "封装性",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列对队列的叙述正确的是",
	"subject_choice_A": "队列属于非线性表",
	"subject_choice_B": "队列按“先进后出”原则组织数据",
	"subject_choice_C": "队列在队尾删除数据",
	"subject_choice_D": "队列按“先进先出”原则组织数据",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "对下列二叉树\n \n \n进行前序遍历的结果是",
	"subject_choice_A": "DYBEAFCZX",
	"subject_choice_B": "YDEBFZXCA",
	"subject_choice_C": "ABDYECFXZ",
	"subject_choice_D": "ABCDEFXYZ",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "某二叉树中有n个度为2的结点，则该二叉树中的叶子结点数为",
	"subject_choice_A": "n+1",
	"subject_choice_B": "n-1",
	"subject_choice_C": "2n",
	"subject_choice_D": "n/2",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "在下列关系运算中，不改变关系表中的属性个数但能减少元组个数的是",
	"subject_choice_A": "并",
	"subject_choice_B": "交",
	"subject_choice_C": "投影",
	"subject_choice_D": "笛卡儿乘积",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "在E-R图中，用来表示实体之间联系的图形是",
	"subject_choice_A": "矩形",
	"subject_choice_B": "椭圆形",
	"subject_choice_C": "菱形",
	"subject_choice_D": "平行四边形",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列叙述中错误的是",
	"subject_choice_A": "在数据库系统中，数据的物理结构必须与逻辑结构一致",
	"subject_choice_B": "数据库技术的根本目标是要解决数据的共享问题",
	"subject_choice_C": "数据库设计是指在已有数据库管理系统的基础上建立数据库",
	"subject_choice_D": "数据库系统需要操作系统的支持",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "Java语言与C++语言相比，最突出的特点是",
	"subject_choice_A": "面向对象",
	"subject_choice_B": "高性能",
	"subject_choice_C": "跨平台",
	"subject_choice_D": "有类库",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列叙述中，错误的是",
	"subject_choice_A": "Java提供了丰富的类库\\TAB",
	"subject_choice_B": "Java最大限度地利用网络资源",
	"subject_choice_C": "Java支持多线程\\TAB",
	"subject_choice_D": "Java不支持TCP/IP协议",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "在下列Java语言的包中，提供图形界面构件的包是",
	"subject_choice_A": "java.io",
	"subject_choice_B": "javax.swing",
	"subject_choice_C": "java.net",
	"subject_choice_D": "java.rmi",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列叙述中，错误的是",
	"subject_choice_A": "javac.exe是Java的编译器",
	"subject_choice_B": "javadoc.exe是Java的文档生成器",
	"subject_choice_C": "javaprof.exe是Java解释器的剖析工具",
	"subject_choice_D": "javap.exe是Java的解释器",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "在执行Java程序时，将应用程序连接到调试器的选项是",
	"subject_choice_A": "-D",
	"subject_choice_B": "-debug",
	"subject_choice_C": "-vexbosegs",
	"subject_choice_D": "-mx",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "请阅读下面程序\nimport　java.io.*;\npublic　class　TypeTransition{\npublic　static　void　main(String　args[]){\nchar　a　=　'a';\nint　i　=　100;\nlong　y　=　456L;\nint　aa　=　a　+　i;\nlong　yy　=　y-aa;\nSystem.out.print(\"aa　=　\"+aa);\nSystem.out.print(\"yy　=　\"+yy);\n}\n}\n程序运行结果是",
	"subject_choice_A": "aa　=　197　　yy　=　259",
	"subject_choice_B": "aa　=　177　　yy　=　259",
	"subject_choice_C": "aa　=　543　　yy　=　288\\TAB",
	"subject_choice_D": "aa　=　197　　yy　=　333\\TAB　\\TAB",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "请阅读下面程序\npublic　class　OperatorsAndExpressions　{\nvoid　residual(){\nint　i=100,j=30;\nfloat　m=563.5f,n=4.0f;\nSystem.out.println(i%j);\nSystem.out.println(m%n);\n}\npublic　static　void　main(String　args[]){\nOperatorsAndExpressions　OperAndExp=new　OperatorsAndExpressions();\n//取模运算符在整数和浮点数中的应用\nOperAndExp.residual();\n}\n}\n程序运行结果是",
	"subject_choice_A": "10",
	"subject_choice_B": "20",
	"subject_choice_C": "10",
	"subject_choice_D": "20",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "请阅读下面程序\npublic　class　ForLoopStatement　{\npublic　static　void　main(String[]　args)　{\nint　i,j;\nfor(i=1;i<5;i++){　　\\TAB　　　　　//i循环\nfor(j=1;j<=i;j++)　　\\TAB　//j循环\nSystem.out.print(i+\"×\"+j+\"=\"+i*j+\"　　\");\nSystem.out.println();\n}\n}\n}\n程序完成后，i循环和j循环执行的次数分别是",
	"subject_choice_A": "4，10",
	"subject_choice_B": "8，9",
	"subject_choice_C": "9，8",
	"subject_choice_D": "10，10\\TAB",
	"subject_answer": "A",
	"analysis": ""
}, {
	"subject_title": "下列叙述中，错误的是",
	"subject_choice_A": "Java中，方法的重载是指多个方法可以共享同一个名字",
	"subject_choice_B": "Java中，用abstract修饰的类称为抽象类，它不能实例化\\TAB",
	"subject_choice_C": "Java中，接口是不包含成员变量和方法实现的抽象类",
	"subject_choice_D": "Java中，构造方法可以有返回值",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "请阅读下面程序\npublic　class　ExampleStringBuffer{\npublic　static　void　main(String[]　args){\nStringBuffer　sb=new　StringBuffer　(\"test\");\nSystem.out.println(\"buffer　=\"+sb);\nSystem.out.println(\"length　=\"+sb.length());\n}\n}\n程序运行结果中在\"length=\"后输出的值是",
	"subject_choice_A": "10",
	"subject_choice_B": "4",
	"subject_choice_C": "20",
	"subject_choice_D": "30",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "请阅读下面程序\nimport　java.io.*;\npublic　class　ExceptionCatch{\npublic　static　void　main(String　args[]){\ntry{\nFileInputStream　fis=new　FileInputStream(\"text\");\nSystem.out.println(\"content　of　text　is:\");\n}\ncatch(FileNotFoundException　e){\nSystem.out.println(e);\nSystem.out.println(\"message:\"+e.getMessage());\ne.printStackTrace(System.out);\n}____________________{\nSystem.out.println(e);\n}\n}\n}\n为保证程序正确运行，程序中下划线处的语句应是",
	"subject_choice_A": "catch(FileInputStream　fis)",
	"subject_choice_B": "e.printStackTrace()\\TAB",
	"subject_choice_C": "catch(IOException　e)",
	"subject_choice_D": "System.out.println(e)",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列叙述中，错误的是",
	"subject_choice_A": "所有的字节输入流都从InputStream类继承",
	"subject_choice_B": "所有的字节输出流都从OutputStream类继承",
	"subject_choice_C": "所有的字符输出流都从OutputStreamWriter类继承",
	"subject_choice_D": "所有的字符输入流都从Reader类继承",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列叙述中，正确的是",
	"subject_choice_A": "线程与进程在概念上是不相关的\\TAB",
	"subject_choice_B": "一个线程可包含多个进程\\TAB",
	"subject_choice_C": "一个进程可包含多个线程\\TAB",
	"subject_choice_D": "Java中的线程没有优先级",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "请阅读下面程序\npublic　class　ThreadTest{\npublic　static　void　main(String　args[　]){\\TAB\nThread　t1　=　new　Thread(　new　Hello(　)　);\nThread　t2　=　new　Thread(　new　Hello(　)　);\\TAB\nt1.start(　);\nt2.start(　);\n}\n}\nclass　Hello　implements　Runnable{\nint　i　;\npublic　void　run(　){\nwhile(　true){\nSystem.out.println(\"Hello\"+i++);\nif　(i==5)　　break　;\n}\n}\n}\n该程序创建线程使用的方法是",
	"subject_choice_A": "继承Thread类",
	"subject_choice_B": "实现Runnable接口\\TAB",
	"subject_choice_C": "t1.start()",
	"subject_choice_D": "t2.start()",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "Java对I/O访问所提供的同步处理机制是",
	"subject_choice_A": "字节流",
	"subject_choice_B": "过滤流",
	"subject_choice_C": "字符流",
	"subject_choice_D": "压缩文件流",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "Java对文件类提供了许多操作方法，能获得文件对象父路径名的方法是",
	"subject_choice_A": "getAbsolutePath()",
	"subject_choice_B": "getParentFile()\\TAB",
	"subject_choice_C": "getAbsoluteFile()",
	"subject_choice_D": "getName()",
	"subject_answer": "B",
	"analysis": ""
}, {
	"subject_title": "下列叙述中，错误的是",
	"subject_choice_A": "Java中没有检测和避免死锁的专门机制",
	"subject_choice_B": "程序中多个线程互相等待对方持有的锁，可能形成死锁",
	"subject_choice_C": "为避免死锁，Java程序中可先定义获得锁的顺序，解锁是按加锁的反序释放",
	"subject_choice_D": "为避免死锁，Java程序中可先定义获得锁的顺序，解锁是按加锁的正序释放",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "请阅读下面程序\npublic　class　ThreadTest　{\npublic　static　void　main(String　args[　])　throws　Exception{\nint　i=0;\nHello　t　=　new　Hello(　);\n__________________;\nwhile(　true){\nSystem.out.println(\"Good　Morning\"+i++);\nif　(i　==　2　&&　t.isAlive()){\nSystem.out.println(\"Main　waiting　for　Hello!\");\nt.join();　　//等待t运行结束\n}\nif　(i==5)　　break　;}\n}\n}\nclass　Hello　extends　Thread{\nint　i　;\npublic　void　run(　){\nwhile(　true){\nSystem.out.println(\"Hello\"+i++);\nif　(i==5)　　break　;}}}\n为使该程序正确执行，下划线处的语句应是",
	"subject_choice_A": "t.sleep()",
	"subject_choice_B": "t.yield()",
	"subject_choice_C": "t.interrupt()",
	"subject_choice_D": "t.start()",
	"subject_answer": "D",
	"analysis": ""
}, {
	"subject_title": "Panel类的默认布局管理器是",
	"subject_choice_A": "BorderLayout",
	"subject_choice_B": "CardLayout",
	"subject_choice_C": "FlowLayout",
	"subject_choice_D": "GridBagLayout",
	"subject_answer": "C",
	"analysis": ""
}, {
	"subject_title": "下列叙述中，错误的是",
	"subject_choice_A": "JButton类和标签类可显示图标和文本\\TAB",
	"subject_choice_B": "Button类和标签类可显示图标和文本",
	"subject_choice_C": "AWT构件能直接添加到顶层容器中",
	"subject_choice_D": "Swing构件不能直接添加到顶层容器中",
	"subject_answer": "B",
	"analysis": ""
}]