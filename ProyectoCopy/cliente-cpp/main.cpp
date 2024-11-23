#include <iostream>
#include <pqxx/pqxx> 

int main() {
    try {
        pqxx::connection conn("dbname=ppal_db user=postgres password=admin host=ppal-db");
        pqxx::work W(conn);

        std::string sql = "INSERT INTO data_table (id, name) VALUES (1, 'C++ Client');";
        W.exec(sql);
        W.commit();

        std::cout << "Data inserted successfully!" << std::endl;
    } catch (const std::exception &e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }
    return 0;
}
