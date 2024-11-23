#include <pqxx/pqxx> // Librería para PostgreSQL
#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib> // Para números aleatorios

std::string generate_random_data() {
    int random_id = rand() % 1000 + 1; // ID aleatorio entre 1 y 1000
    std::string random_user = "User_" + std::to_string(rand() % 100);
    std::string random_cargo = "Cargo_" + std::to_string(rand() % 10);
    return "'" + std::to_string(random_id) + "', '" + random_user + "', '" + random_cargo + "'";
}

int main() {
    try {
        pqxx::connection conn("dbname=ppal_db user=user password=password host=slave1");
        while (true) {
            std::string data = generate_random_data();
            pqxx::work txn(conn);
            txn.exec("INSERT INTO tabla_x (id, usuario, cargo) VALUES (" + data + ");");
            txn.commit();
            std::cout << "Dato insertado: " << data << std::endl;
            std::this_thread::sleep_for(std::chrono::seconds(2)); // Pausa de 2 segundos
        }
    } catch (const std::exception &e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }
}
