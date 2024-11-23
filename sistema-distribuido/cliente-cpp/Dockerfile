FROM gcc:latest
WORKDIR /app

RUN apt-get update && apt-get install -y libpqxx-dev
COPY Main.cpp .
RUN g++ -o cliente Main.cpp -lpqxx -lpq

CMD ["./cliente"]
