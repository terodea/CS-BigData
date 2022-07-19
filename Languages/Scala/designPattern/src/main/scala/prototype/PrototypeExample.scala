package prototype

object PrototypeExample {
  /**
   * What it is good for?
   * The prototype design pattern is useful when performance is important.
   * Using the copy method, we can get instances that otherwise take time to create.
   * The slowness could be caused by some calculations performed during creation,
   * a database call that retrieves data, and so on.
   *
   * What it is not so good for?
   * Mistakes and side effects could be caused using shallow copies of objects,
   * where the actual references point to the original instances.
   * Also, avoiding constructors could lead to bad code.
   * The prototype design pattern should be really used in cases where there
   * might be a massive performance impact without it.
   */
  def main(args: Array[String]): Unit = {
    val initCell = Cell("abcd", List("protein1", "protein2"))
    val copy1 = initCell.copy()
    val copy2 = initCell.copy()
    val copy3 = initCell.copy(dna = "1234")

    System.out.println(s"The prototype is : ${initCell}")
    System.out.println(s"Cell 1: ${copy1}")
    System.out.println(s"Cell 2: ${copy2}")
    System.out.println(s"Cell 3: ${copy3}")
    System.out.println(s"1 and 2 are equal: ${copy1 == copy2}")
    System.out.println(s"1 and 3 are equal: ${copy1 == copy3}")
  }
}
