package adaptor

class AppLogger extends Logger with Log {
  override def info(message: String): Unit = log(message, "info")
  override def warning(message: String): Unit = log(message, "warning")
  override def error(message: String): Unit = log(message, "error")
  override def debug(message: String): Unit = log(message, "debug")
}
