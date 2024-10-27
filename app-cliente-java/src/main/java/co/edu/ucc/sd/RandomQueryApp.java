package co.edu.ucc.sd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Random;
import java.util.concurrent.TimeUnit;

public class RandomQueryApp {

    private static final String DB_URL = "jdbc:postgresql://localhost:5432/postgres";
    private static final String USER = "postgres";
    private static final String PASS = "postgres";

    public static void main(String[] args) {
        System.out.println("Cliente Java Bryan Sanchez");
        try {
            Connection connection = DriverManager.getConnection(DB_URL, USER, PASS);
            Statement statement = connection.createStatement();
            Random random = new Random();

            while (true) {
                int waitTime = random.nextInt(10) + 1; // Espera aleatoria entre 1 y 10 segundos
                TimeUnit.SECONDS.sleep(waitTime);

                String query = "SELECT id, name FROM public.dummy";
                ResultSet resultSet = statement.executeQuery(query);

                while (resultSet.next()) {
                    System.out.println("Java Resultado: " + resultSet.getString("id") + " " + resultSet.getString("name"));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
