object DefaultArgs extends App{

    def add(num: Int, incrementBy: Int=1) = {
        num + incrementBy
    }

    println(add(7)) // num = 7 & incrementBy = 1
    println(add(num=7, incrementBy=2)) // num = 7 & incrementBy = 2
}
