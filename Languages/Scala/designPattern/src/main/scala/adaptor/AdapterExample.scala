package adaptor

object AdapterExample {
  def main(args: Array[String]): Unit = {
    val logger = new AppLogger()
    logger.info("This is an info message.")
    logger.debug("Debug something here.")
    logger.error("Show an error message.")
    logger.warning("About to finish.")
    logger.info("Bye!")
  }
}
