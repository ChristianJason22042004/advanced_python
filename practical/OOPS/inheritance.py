# 🧬 Inheritance Demonstration in Python
# --------------------------------------
# This program demonstrates all types of inheritance in Python:
# 1️⃣ Single Inheritance
# 2️⃣ Multilevel Inheritance
# 3️⃣ Multiple Inheritance
# 4️⃣ Hierarchical Inheritance
# 5️⃣ Hybrid Inheritance
# 6️⃣ Using super() Function

# ==========================================================
# 1️⃣ SINGLE INHERITANCE
# ==========================================================

class Parent:
    def show_parent(self):
        print("👨 Parent Class: This is the parent class.")


class Child(Parent):
    def show_child(self):
        print("🧒 Child Class: Inherited from Parent.")


print("\n🔹 SINGLE INHERITANCE")
obj_single = Child()
obj_single.show_parent()
obj_single.show_child()


# ==========================================================
# 2️⃣ MULTILEVEL INHERITANCE
# ==========================================================

class GrandParent:
    def feature1(self):
        print("👴 GrandParent: Base generation feature.")


class Parent(GrandParent):
    def feature2(self):
        print("👨 Parent: Middle generation feature.")


class Child(Parent):
    def feature3(self):
        print("🧒 Child: Youngest generation feature.")


print("\n🔹 MULTILEVEL INHERITANCE")
obj_multi = Child()
obj_multi.feature1()
obj_multi.feature2()
obj_multi.feature3()


# ==========================================================
# 3️⃣ MULTIPLE INHERITANCE
# ==========================================================

class Father:
    def skill_father(self):
        print("👨‍💻 Father: Coding skills.")


class Mother:
    def skill_mother(self):
        print("👩‍🎨 Mother: Designing skills.")


class Son(Father, Mother):
    def skill_son(self):
        print("👦 Son: Combines both skills.")


print("\n🔹 MULTIPLE INHERITANCE")
obj_multiple = Son()
obj_multiple.skill_father()
obj_multiple.skill_mother()
obj_multiple.skill_son()


# ==========================================================
# 4️⃣ HIERARCHICAL INHERITANCE
# ==========================================================

class Parent:
    def show_parent(self):
        print("👨 Parent class property.")


class Child1(Parent):
    def feature_child1(self):
        print("🧒 Child1 inherits from Parent.")


class Child2(Parent):
    def feature_child2(self):
        print("🧑 Child2 also inherits from Parent.")


print("\n🔹 HIERARCHICAL INHERITANCE")
obj1 = Child1()
obj2 = Child2()
obj1.show_parent()
obj1.feature_child1()
obj2.show_parent()
obj2.feature_child2()


# ==========================================================
# 5️⃣ HYBRID INHERITANCE (Combination)
# ==========================================================

class A:
    def showA(self):
        print("🅰️ Class A: Base class.")


class B(A):
    def showB(self):
        print("🅱️ Class B: Inherits from A.")


class C(A):
    def showC(self):
        print("🇨 Class C: Inherits from A.")


class D(B, C):
    def showD(self):
        print("🇩 Class D: Inherits from both B and C (Hybrid).")


print("\n🔹 HYBRID INHERITANCE")
obj_hybrid = D()
obj_hybrid.showA()
obj_hybrid.showB()
obj_hybrid.showC()
obj_hybrid.showD()


# ==========================================================
# 6️⃣ USING super() FUNCTION
# ==========================================================

class Parent:
    def greet(self):
        print("👋 Hello from Parent class.")


class Child(Parent):
    def greet(self):
        super().greet()  # Calls the Parent's greet()
        print("🙋 Hello from Child class (via super()).")


print("\n🔹 super() FUNCTION IN INHERITANCE")
obj_super = Child()
obj_super.greet()


# ==========================================================
# 🏁 PROGRAM END
# ==========================================================
print("\n🎯 All inheritance types demonstrated successfully!")
