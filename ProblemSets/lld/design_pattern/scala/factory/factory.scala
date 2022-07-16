import PC.PC
import Server.Server

object ComputerFactory{
    def apply(compType:String, ram:String, hdd:String, cpu:String) = compType.toUpperCase match {
        case "PC" => new PC(ram,hdd,cpu)
        case "SERVER" => new Server(ram,hdd,cpu)
    }
}