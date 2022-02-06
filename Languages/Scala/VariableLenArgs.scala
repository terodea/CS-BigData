object VariableLenArgs extends App{
    // App is a trait that has already defined main method, which helps in creating scala code as a runnable file.
    def printArgs(name: String*) = {
        for(i <- name){
            println(i)
        }
    }
    printArgs("hello", "I'm", "variable", "length args")

    // Null is a trait
    def tryNull(name: Null): Unit = {println("Successfully run!!")}
    tryNull(Null) // avoid this can lead to null pointer exception.

    // Nil
    val c = Nil
    prinlnt(c) // Nil is an empty list

    // Nothing: there was an error and nothing was returned.

    def fun: Nothing = {
        throw new Exception
    }

    // Option: Used in case of an ivalid return value
    // How do you deal with Nones in your code, use Option
    def getAStringMayBe(num: Int): Option[String] = {
        if(num > 0) Some("A positive number !")
        else None
    }

    def printResult(num: Int) = {
        getAStringMayBe(num) match {
            case Some(str) => println(str)
            case None => println("No String!!")
        }
    }

    printResult(10)
    printResult(-10)

    case class Address (city: String, state: String, zip:String)
    /*
    class User(email:String, password: String){
        var fName: String = _
        var lName: String = _
        var address: Address = _
    }

    val user = new User("terodea@gmail.com", "xyz")
    println(user.fName.length) // NullPointer Exception*/

    class User(email:String, password: String){
        var fName: Option[String] = None
        var lName: Option[String] = None
        var address: Option[Address] = None
    }

    val user = new User("terodea@gmail.com", "xyz")
    println(user.fName.getOrElse("Not Assigned"))
    
    user.fName = Some("Akshay")
    user.lName = Some("Terode")
    user.address = Some(Address("Nagpur", "Maharashtra", "442401"))

    println(user.fName.getOrElse("Not Assigned"))
}
