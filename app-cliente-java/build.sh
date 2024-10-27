javac -d build src/main/java/co/edu/ucc/sd/*.java
jar cfm app-cliente-java.jar resources/META-INF/MANIFEST.MF -C build/ .