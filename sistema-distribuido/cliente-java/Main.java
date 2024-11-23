import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        try {
            Connection conn = DriverManager.getConnection("jdbc:postgresql://slave2:5432/slave2_db", "user", "password");
            Random random = new Random();
            while (true) {
                int id = random.nextInt(1000) + 1;
                String usuario = "User_" + random.nextInt(100);
                String cargo = "Cargo_" + random.nextInt(10);
                String query = "INSERT INTO tabla_y (id, usuario, cargo) VALUES (" + id + ", '" + usuario + "', '" + cargo + "')";
                Statement stmt = conn.createStatement();
                stmt.executeUpdate(query);
                System.out.println("Dato insertado: " + query);
                Thread.sleep(2000); // Pausa de 2 segundos
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
