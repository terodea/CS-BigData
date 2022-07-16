trait Computer{
    def getRAM():String
    def getHDD():String
    def getCPU():String

    override def toString = "RAM= " + getRAM +", HDD=" + getHDD + ", CPU=" + getCPU
}