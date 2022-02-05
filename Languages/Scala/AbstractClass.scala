object AbstractClass {
  abstract class Animal{
      def eat: Unit
      val creatureType: String
  }

  class Dog extends Animal{
      val creatureType: String = "canine"
      def eat: Unit = println("I chew bone")
  }

  val dogObj = new Dog
  dogObj.eat
  dogObj.creatureType
}
