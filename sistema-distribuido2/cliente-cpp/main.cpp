#include <iostream>
#include <pqxx/pqxx>
#include <thread>
#include <chrono>
#include <cstdlib>
#include <ctime>

std::string generateRandomString(const std::string& prefix) {
    return prefix + std::to_string(rand() % 1000);
}

int main() {
    srand(time(0));

    try {
        pqxx::connection C("dbname=ppal_db user=user password=password host=slave1 port=5432");

        while (true) {
            pqxx::work W(C);
            std::string usuario = generateRandomString("UsuarioCPP_");
            std::string cargo = generateRandomString("Cargo_");

            W.exec("INSERT INTO tabla_x (usuario, cargo) VALUES ('" + usuario + "', '" + cargo + "');");
            W.commit();

            std::cout << "Registro insertado: Usuario = " << usuario << ", Cargo = " << cargo << std::endl;

            std::this_thread::sleep_for(std::chrono::seconds(2));
        }
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
    