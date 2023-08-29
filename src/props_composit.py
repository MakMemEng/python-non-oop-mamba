from abc import ABC, abstractmethod


# 抽象クラス
#  * 抽象基底クラス(ABC)を継承したクラスを抽象クラスという
#  * 抽象クラス自体はインスタンス化することはできない
class MyAbstractClass(ABC):
    # 抽象メソッド
    #  * 抽象メソッドはメソッドのシグネチャ(名前と引数)は定義されているが
    #    具体的な実装(メソッドの本体)は存在しない
    #  * 抽象クラスを継承する全ての子クラスは抽象メソッドをオーバーライドして
    #    具体的な実装を提供する必要がある
    @abstractmethod
    def my_method(self):
        print("+++ abstract method +++")


# !Error my_abstract_class = MyAbstractClass()


# 具象クラス
#  * 具象クラスは抽象クラスを継承し，抽象メソッドを全てオーバーライドして
#    具体的な実装を提供するクラスである
#  * 具象クラスはインスタンス化することができる
class MyConcreteClass(MyAbstractClass):
    # 抽象メソッドのオーバーライド
    def my_method(self):
        super().my_method()
        print("*** implement ***")


obj = MyConcreteClass()
obj.my_method()
