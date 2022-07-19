package adaptor

trait Log {
  def info(message: String): Unit
  def debug(message: String): Unit
  def warning(message: String): Unit
  def error(message: String): Unit
}
