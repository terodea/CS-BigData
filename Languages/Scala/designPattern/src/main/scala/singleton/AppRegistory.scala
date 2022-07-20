package singleton
import scala.collection.concurrent.{TrieMap, Map}

object AppRegistry {
  System.out.println("Registry initialization block called.")
  private val users: Map[String, String] = TrieMap.empty

  def addUser(id: String, name: String): Unit = {
    users.put(id, name)
  }

  def removeUser(id: String): Unit = {
    users.remove(id)
  }

  def isUserRegistered(id: String): Boolean =
    users.contains(id)

  def getAllUserNames(): List[String] =
    users.map(_._2).toList
}