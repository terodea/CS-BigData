object Inheritance{
    // child class inhereting from parent class
    // Scala doesn't support multiple inheritence, i.e. can't extend from two parent class

    class Animal{
        def eat = println("Animals eat a lot")
    }

    class Cat extends Animal{
        eat
        def prefferedMeal = println("Milk")
    }


}