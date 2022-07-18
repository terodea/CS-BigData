package builder.caseClass

object PersonCaseClassExample {

  def main(args: Array[String]): Unit = {
    val person1 = Person(
      firstName = "Akshay",
      lastName = "Terode",
      age = 27
    )

    val person2 = Person(
      firstName = "Swayam"
    )

    System.out.println(s"Person 1: ${person1}")
    System.out.println(s"Person 2: ${person2}")
  }
}
