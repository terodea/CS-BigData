import Computer.Computer

private class Server(val ram:String, val hdd:String, val cpu:String) extends Computer{
    def getRAM():String =  ram
    def getHDD():String = hdd
    def getCPU():String = cpu
}