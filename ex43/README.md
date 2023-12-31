# 面向对象的分析和设计基础
过程如下：
1. 把问题写或者划下来。
2. 提炼出关键概念，并进行研究。
3. 为这些概念创建一个类的层级和对象关系图。
4. 写下这些类的代码，并测试运行。
5. 重复和改进。

## 1. 写或画出这个问题
“外星人入侵了一艘宇宙飞船，我们的英雄必须穿过迷宫般的房间打败他们，这样他才能逃到逃生舱去到下面的星球。游戏更像是 Zork 之类的文字冒险游戏，并且有着很有意思的死亡方式。这款游戏的引擎会运行一张满是房间或场景的地图。当玩家进入游戏时，每个房间都会打印自己的描述，然后告诉引擎下一步该运行地图中的哪个房间。”
死亡（Death）：玩家死的时候，会非常有意思。 中央走廊（Central Corridor）：这是起点，已经有一个哥顿人站在那里，在继续之前，玩家必须用一个笑话来击败他。 激光武器军械库（Laser Weapon Armory）：这是英雄在到达逃生舱之前用中子弹炸毁飞船的地方。这里有一个键盘，英雄必须猜出数字。 桥（The Bridge）：另一个和哥顿人战斗的场景，英雄在这里放置了炸弹。 逃生舱（Escape Pod）：英雄逃脱的地方，前提是他猜出正确的逃生舱。
到这一步我可能会画一幅映射图，或者为每个房间写更多的描述——反正就是当我探究这个问题的时候，任何我脑子里冒出的想法

## 2. 抽取关键概念并予以研究
我现在有足够的信息来提取其中的名词，并分析他们的类层级结构。首先，我会做一个所有名词的列表：
* Alien（外星人）
* Player（玩家）
* Ship（飞船）
* Maze（迷宫）
* Room（房间）
* Scene（场景）
* Gothon（哥特人）
* Escape Pod（逃生舱）
* Planet（行星）
* Map（地图）
* Engine（引擎）
* Death（死亡）
* Central Corridor（中央走廊）
* Laser Weapon Armory（激光武器军械库）
* The Bridge（桥）
还应浏览一遍所有的动词，看它们适不适合作为函数名，但是我会先暂时跳过这一步。

现在你可能也会研究一下每个概念以及任何你不明白的东西。比如，我会玩几个同类型的游戏，确保我知道它们是如何工作的。我可能还会研究船是如何设计的或者炸弹是怎么用的。还有一些技术性问题，比如如何把游戏状态储存在数据库中。当我完成这些研究，我可能会基于这些新信息从第一步开始，重新写我的描述，并做概念提取。

## 为这些概念创建类的层级结构和对象地图
我通过询问“什么与其他东西类似?”、“什么基本上就是另一个东西的另一个词?”来把我已经有的东西转换成类的层级结构。

很快我就发现“房间”（“Room”）和“场景”（“Scene”）基本上是同一种东西，取决于我想用它们来做什么。在这个游戏中我选择用“场景”。然后我意识到所有特定的房间比如“中央走廊”其实就是“场景”。我还发现“死亡”（“Death”）也可以说是场景，这确认了我选择“场景”而不是“房间”的正确性，因为你可以说“死亡”是一种场景，但如果说它是一个“房间”就有点奇怪了。“迷宫”（“Maze”）和“地图”（“Map”）也基本上是同一种东西，我会选择用“地图”，因为我更常用它。我不想做一个战斗系统，所以我会暂时忽略“外星人”（“Alien”）和“玩家”（“Player”）这两个东西，先保存起来以备后用。“行星”（“Planet”）也可以是另一种场景，而不是其他特定的东西。

经过上述思考过程，我开始创建一个看起来像这样的类的层级结构：

* Map
* Engine
* Scene
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod
然后我会浏览一遍，基于我描述里面的东西，想想看每个类下面需要些什么动作。例如，我从描述里知道，我需要一种方式来“运行”这个引擎，从地图“到达下一个场景”，到达“开场”，并“进入”一个场景，我会像这样把这些动作加上：
* Map - next_scene - opening-scene
* Engine - play
* Scene - enter
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod

## 编写类代码并通过测试来运行
一旦我有了这个类和函数的树状图，我在我的编辑器里面打开一个源文件，试着写它们的代码。通常我就是把树状图里的东西复制粘贴到源文件里，然后把它们编辑成类。下面是它们最开始的样子，文件最后放了一个小测试
1   class Scene(object):
2
3       def enter(self):
4           pass
5
6
7   class Engine(object):
8
9       def __init__(self, scene_map):
10          pass
11
12      def play(self):
13          pass
14
15  class Death(Scene):
16
17      def enter(self):
18          pass
19
20  class CentralCorridor(Scene):
21
22      def enter(self):
23          pass
24
25  class LaserWeaponArmory(Scene):
26
27      def enter(self):
28          pass
29
30  class TheBridge(Scene):
31
32      def enter(self):
33          pass
34
35  class EscapePod(Scene):
36
37      def enter(self):
38          pass
39
40
41  class Map(object):
42
43      def __init__(self, start_scene):
44          pass
45
46      def next_scene(self, scene_name):
47          pass
48
49      def opening_scene(self):
50          pass
51
52
53  a_map = Map('central_corridor')
54  a_game = Engine(a_map)
55  a_game.play()

## 重复和改进
过程的最后一步准确来说不是一个步骤，而像是一个 while 循环。你不可能一次完成这个过程。相反，你会再次回顾整个过程，并根据你从后续步骤中学到的信息对其进行改进。有时我会进入第三步，然后意识到我需要再回到第一步和第二步，那我就会停下来，回到前面去做。有时我会灵光一闪，跳到最后，把脑子里的解决方案代码敲出来，然后再回过头来做前面的步骤，以确保我涵盖了所有可能的情况。

在这个过程中你需要注意的另一个问题是，它不仅仅是你在一个单一层面上做的事，而是当你遇到一个特定的问题时，你可以在每个层面上做的事情。假设我不知道怎么写 Engine.play 这个方法。我可以停下来，把整个过程专注在这一个函数上来弄明白代码应该怎么写。

# 自上而下 VS自下而上
这个过程通常被称为“自上而下”，因为它从最抽象的概念（上）开始，然后一直向下到实际的应用。我希望你能从现在开始分析这本书里遇到的问题时使用我刚才描述的这个过程，但是你应该知道编程中还有另一种解决问题的方式，那就是，从写代码开始，然后逐渐“上升”到抽象的概念，这种方式被称为“自下而上”。它的步骤大致如下：

* 从问题中拿出一小部分，开始写简单的能运行的代码
* 然后用类和自动化测试来把代码改进地更正式一些
* 抽象出你所使用的关键概念，试着探究一下它们
* 针对正在发生的事情写一段描述
* 回过头去继续改进代码，也可能把之前写的删掉重新开始
* 转到这个问题的其他部分，然后重复以上步骤
  
这个过程只有在你对编程已经比较熟练并且面对问题能够自然使用编程思维的情况下才会更好，同时，当你知道整个工程的一小部分、却对全局概念的信息掌握不全的时候，这个方法也很好用。你可以将整个过程拆解成很多小块，然后边写代码边探索，这样可以帮助你一点一点地钻研这个问题，直到整个问题都得到解决。但是，请记住，你的解决方案很可能会曲折而怪异，所以我才把回顾、研究以及基于你所学到的东西对代码进行改进和清理这些步骤加入到我的过程描述中。