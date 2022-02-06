import scala.io.StdIn._

object StringReversals {

    def main(args: Array[String]): Unit = {

        val input = readLine()
        println(input.reverse)
        println(input.split(" ").map(_.reverse).mkString(" "))
        println(input.split(" ").reverse.mkString(" "))
    }
}
