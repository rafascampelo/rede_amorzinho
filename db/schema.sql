-- db/schema.sql
CREATE DATABASE IF NOT EXISTS amorzinho_rede;
USE amorzinho_rede;

CREATE TABLE IF NOT EXISTS relacionamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_casal VARCHAR(100),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    relacionamento_id INT,
    FOREIGN KEY (relacionamento_id) REFERENCES relacionamentos(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS mensagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    conteudo VARCHAR(100) NOT NULL,
    usuario_id INT NOT NULL,
    relacionamento_id INT NOT NULL,
    data_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        ON DELETE CASCADE,
    FOREIGN KEY (relacionamento_id) REFERENCES relacionamentos(id)
        ON DELETE CASCADE
);
