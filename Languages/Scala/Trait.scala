object Trait {
    // Way to add multiple inheritance in scaala is using traits
    // traits are behaviour
    // trait doesn't have constructor paramter
    // traits can have partial implementation
    abstract class Animal{
        def eat: Unit
        val creatureType: String
    }

    trait Carnivore{
        val creatureType: String
        def prefferedMeal: Unit
    }

    trait ColdBlodded

    class Crocodile extends Animal with Carnivore with ColdBlodded{
        val creatureType: String = "canine"
        def eat = println("I eat flesh")
        def prefferedMeal = println("I like sea food")
    }

    val croc = new Crocodile
    croc.eat
    croc.creatureType
    croc.prefferedMeal
}
