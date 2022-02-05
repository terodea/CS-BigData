object CaseDemo{
    // Class parameters are automatically promoted to fields i.e formal params are treated as instance variables.
    // Companion objects are created automatically.
    // By default immutable
    // case class are serializable i.e can be sent over a network, very usefull in distributed computing.

    case class Person(name: String, age:Int)

    val personObj1 = new Person("Akshay", 26)
    val personObj2 = new Person("Akshay", 26)

    // Case classes have toString
    println(personObj1.toString)
    println(personObj1.age)
    println(personObj1.name)

    // Equals and hashCode methods already implemented
    println(personObj1 == personObj2)

    val personObj3 = Person.apply("Jahangir", 30)
    println(personObj3)

    // copy method already present
    val personObj4 = personObj3.copy(age=37)
    println(personObj4.age)
    println(personObj4)

}