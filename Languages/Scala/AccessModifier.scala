object AccessModifier {
    // Access modifers : private, protected, no modifier
  class Animal{
      private def eat = println("Animal eats")
  }

  class Cat extends Animal{
      protected def catEats = println("I eat/drink milk !!")
  }

  class Dog extends Animal{
      def dogEats = println("I chew bone !!")
  }
}
