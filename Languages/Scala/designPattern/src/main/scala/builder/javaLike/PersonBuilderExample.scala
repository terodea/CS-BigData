package builder.javaLike

object PersonBuilderExample {
  /**
   * Avoid such implementation of builder pattern in scala.
   * @param args
   */
  def main(args: Array[String]): Unit = {
    val person: Person = new PersonBuilder().setFirstName("Akshay").setLastName("Terode").setAge(27).build()
    System.out.println(s"Person: ${person.firstName} ${person.lastName} Age: ${person.age}")
  }
}
