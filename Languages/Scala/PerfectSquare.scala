import scala.io.StdIn._

object PerfectScala{
    // 7
    // 10 20 16 25 30 40 36

    def main(args: Array[String]): Unit = {
        val numCustomers: Int = readInt()
        val billAmount: String = readLine()

        val billAmt: Array[Int] = billAmount.split(" ").map(x => x.toInt)

        var count = 0

        for(i <- billAmt){
            val sqrt = Math.sqrt(i)
            if(sqrt.ceil - sqrt == 0){
                count += 1
            }
        }
        println(count)
    }
}