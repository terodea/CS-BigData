import scala.io.StdIn._
import scala.util.control.Breaks._
import scala.util.control._
object BelowTarget {
    // Find all the numbers in an array that are less than target

    def main(args: Array[String]) : Unit = {

        val num1 = readLine()
        val numArr: Array[Int] = num1.split(" ").map(_.toInt)

        val num2 = readLine()
        val num2Arr: Array[Int] = num2.split(" ").map(_.toInt)

        val target = numArr(1)

        var count = 0
        loop.breakable{
            for(i <- num2Arr){
                if (i < target){
                    count += 1
                }
                else{
                    loop.break
                }
            }
        }
        count = 0
        for(i <- num2Arr){
            if (i < target){
                count += 1
            }
            else{
                break()
            }
        }
        println(count)
    }
}
