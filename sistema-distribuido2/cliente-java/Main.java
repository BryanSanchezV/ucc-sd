import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.util.Random;

public class Main {

    public static String generateRandomString(String prefix) {
        Random random = new Random();
        return prefix + random.nextInt(1000);
    }

    public static void main(String[] args) {
        try {
            Connection conn = DriverManager.getConnection(
                "jdbc:postgresql://slave2:5432/slave2_db", "user", "password");
            System.out.println("Conexión establecida con PostgreSQL.");

            while (true) {
                Statement stmt = conn.createStatement();
                String usuario = generateRandomString("UsuarioJava_");
                String cargo = generateRandomString("Cargo_");

                stmt.executeUpdate(
                    "INSERT INTO tabla_x_slave (usuario, cargo) VALUES ('" + usuario + "', '" + cargo + "');");
                System.out.println("Registro insertado: Usuario = " + usuario + ", Cargo = " + cargo);

                Thread.sleep(2000);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
