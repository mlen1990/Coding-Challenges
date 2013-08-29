/* MySQLDatabase.java */

import java.sql.*;

/**
 *  This class is intended to setup the connection to the MySQL database
 *  and enable the insertion of file entries.
 **/
public class MySQLDatabase {

  // Driver and URL
  public static final String driver = "com.mysql.jdbc.Driver";
  public static final String url = "jdbc:mysql://localhost:3306/";

  // username and password
  public static final String user = "root";
  public static final String password = "goodjob123";

  // The connection to the mysql database
  private Connection mysql;

  /**
   *  MySQLDatabase() constructor.
   **/
  public MySQLDatabase() {}

  /**
   *  connectToDatabase() register the Java mysql driver and establish a
   *  connection to the database.
   **/
  public void connectToDatabase() {
    try {
      Class.forName(driver);
      mysql = DriverManager.getConnection(url, user, password);
    } catch (SQLException e) {
      System.out.println(e);
    } catch (ClassNotFoundException e) {
      System.out.println(e);
    }
  }

  /**
   *  closeConnection() close the connection to the database.
   **/
  public void closeConnection() {
    try {
      mysql.close();
    } catch (SQLException e) {
      System.out.println(e);
    }
  }

  /**
   *  setup() sets up the database table files and creates a files table to
   *  store the entries.
   *
   *  Note: only use this method if the database hasn't already been set up.
   **/
  public void setup() {
    Statement stmt = null;
    try {
      stmt = mysql.createStatement();
      String sql = "CREATE DATABASE FILES";
      stmt.executeUpdate(sql);
      sql = "USE FILES";
      stmt.executeUpdate(sql);
      sql = "CREATE TABLE FILES " +
                    "(timestamp TIMESTAMP, " +
                    "filename VARCHAR(30), " +
                    "top_level VARCHAR(30), " +
                    "thread_id INT)";
      stmt.executeUpdate(sql);
    } catch (SQLException e) {
      System.out.println(e);
    } finally {
      try {
        stmt.close();
      } catch (SQLException e) {
        System.out.println(e);
      }
    }
  }

  /**
   *  addEntry() adds a new entry to the database.
   *  @param mysql the connection to the mysql database.
   *  @param entry a sql statement in the the form of a string.
   *
   *  The sql statement should have this format:
   *  "insert into files values(now(), "filename", "top_level", thread_id)"
   **/
  public synchronized void addEntry(String entry) {
    Statement stmt = null;
    try {
      stmt = mysql.createStatement();
      stmt.executeUpdate(entry);
    } catch (SQLException e) {
      System.out.println(e);
    }
  }
}
