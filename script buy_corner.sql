CREATE DATABASE buy_corner;
USE buy_corner;

CREATE TABLE Fornecedor (
    Cnpj_Fornecedor VARCHAR(14) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Endereço VARCHAR(200),
    Telefone VARCHAR(20),
    Email VARCHAR(100)
);

CREATE TABLE Produto (
    Cod_Barras VARCHAR(13) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50),
    Descrição TEXT,
    Preço DECIMAL(10,2),
    Quantidade_Em_Estoque INT,
    Cnpj_Fornecedor VARCHAR(14),
    FOREIGN KEY (Cnpj_Fornecedor) REFERENCES Fornecedor(Cnpj_Fornecedor)
);

CREATE TABLE Cliente (
    Cpf_Cliente VARCHAR(11) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Endereço VARCHAR(200),
    Telefone VARCHAR(20),
    Email VARCHAR(100)
);

CREATE TABLE Venda (
    ID_Venda INT AUTO_INCREMENT PRIMARY KEY,
    Data DATE,
    Cpf_Cliente VARCHAR(11),
    Total_Venda DECIMAL(10,2),
    Cod_Barras VARCHAR(13),
    FOREIGN KEY (Cpf_Cliente) REFERENCES Cliente(Cpf_Cliente),
    FOREIGN KEY (Cod_Barras) REFERENCES Produto(Cod_Barras)
);

INSERT INTO Fornecedor (Cnpj_Fornecedor, Nome, Endereço, Telefone, Email) VALUES
('12345678000195', 'Atacadão Sports', 'Rua das Palmeiras, 123', '(11) 1111-1111', 'atacadao@exemplo.com'),
('12345678000196', 'Sportiva Brasil', 'Avenida das Nações, 234', '(11) 2222-2222', 'sportiva@exemplo.com'),
('12345678000197', 'Futebol Mania', 'Rua do Futebol, 345', '(11) 3333-3333', 'futebolmania@exemplo.com'),
('12345678000198', 'Camisas e Cia', 'Praça da Alegria, 456', '(11) 4444-4444', 'camisasecia@exemplo.com'),
('12345678000199', 'Lojas do Torcedor', 'Avenida da Liberdade, 567', '(11) 5555-5555', 'lojastorcedor@exemplo.com'),
('12345678000200', 'SportShop Brasil', 'Rua do Comércio, 678', '(11) 6666-6666', 'sportshop@exemplo.com'),
('12345678000201', 'Estilo e Esporte', 'Avenida das Flores, 789', '(11) 7777-7777', 'estiloeesporte@exemplo.com'),
('12345678000202', 'Camisetas do Futebol', 'Rua da Vitória, 890', '(11) 8888-8888', 'camisetafutebol@exemplo.com'),
('12345678000203', 'Futebol & Cia', 'Rua das Acácias, 901', '(11) 9999-9999', 'futebolecia@exemplo.com'),
('12345678000204', 'Camisas Top', 'Avenida do Povo, 123', '(11) 1010-1010', 'camiastop@exemplo.com'),
('12345678000205', 'Estádio das Compras', 'Rua do Lazer, 234', '(11) 1111-1212', 'estadiocompras@exemplo.com'),
('12345678000206', 'Esporte Fashion', 'Rua da Cultura, 345', '(11) 1212-1313', 'esportefashion@exemplo.com'),
('12345678000207', 'Gol de Placa', 'Praça do Futebol, 456', '(11) 1313-1414', 'godeplaca@exemplo.com'),
('12345678000208', 'Copa & Cia', 'Rua da Amizade, 567', '(11) 1414-1515', 'copacia@exemplo.com'),
('12345678000209', 'Atitude Esportiva', 'Avenida do Trabalho, 678', '(11) 1515-1616', 'atitude@exemplo.com');

INSERT INTO Produto (Cod_Barras, Nome, Categoria, Descrição, Preço, Quantidade_Em_Estoque, Cnpj_Fornecedor) VALUES
('7891234567890', 'Camisa Flamengo 2023', 'Roupas', 'Camisa oficial do Flamengo, modelo 2023', 249.90, 100, '12345678000195'),
('7891234567891', 'Camisa Palmeiras 2023', 'Roupas', 'Camisa oficial do Palmeiras, modelo 2023', 249.90, 80, '12345678000196'),
('7891234567892', 'Camisa São Paulo 2023', 'Roupas', 'Camisa oficial do São Paulo, modelo 2023', 249.90, 75, '12345678000197'),
('7891234567893', 'Camisa Santos 2023', 'Roupas', 'Camisa oficial do Santos, modelo 2023', 249.90, 60, '12345678000198'),
('7891234567894', 'Camisa Corinthians 2023', 'Roupas', 'Camisa oficial do Corinthians, modelo 2023', 249.90, 90, '12345678000199'),
('7891234567895', 'Camisa Vasco 2023', 'Roupas', 'Camisa oficial do Vasco, modelo 2023', 249.90, 50, '12345678000200'),
('7891234567896', 'Camisa Atlético Mineiro 2023', 'Roupas', 'Camisa oficial do Atlético Mineiro, modelo 2023', 249.90, 70, '12345678000201'),
('7891234567897', 'Camisa Cruzeiro 2023', 'Roupas', 'Camisa oficial do Cruzeiro, modelo 2023', 249.90, 40, '12345678000202'),
('7891234567898', 'Camisa Grêmio 2023', 'Roupas', 'Camisa oficial do Grêmio, modelo 2023', 249.90, 55, '12345678000203'),
('7891234567899', 'Camisa Internacional 2023', 'Roupas', 'Camisa oficial do Internacional, modelo 2023', 249.90, 65, '12345678000204'),
('7891234567800', 'Camisa Bahia 2023', 'Roupas', 'Camisa oficial do Bahia, modelo 2023', 249.90, 85, '12345678000205'),
('7891234567801', 'Camisa Sport 2023', 'Roupas', 'Camisa oficial do Sport, modelo 2023', 249.90, 45, '12345678000206'),
('7891234567802', 'Camisa Fortaleza 2023', 'Roupas', 'Camisa oficial do Fortaleza, modelo 2023', 249.90, 30, '12345678000207'),
('7891234567803', 'Camisa Atlético Goianiense 2023', 'Roupas', 'Camisa oficial do Atlético Goianiense, modelo 2023', 249.90, 25, '12345678000208'),
('7891234567804', 'Camisa Ceará 2023', 'Roupas', 'Camisa oficial do Ceará, modelo 2023', 249.90, 20, '12345678000209');

INSERT INTO Cliente (Cpf_Cliente, Nome, Endereço, Telefone, Email) VALUES
('12345678901', 'Lucas Silva', 'Rua São Paulo, 123', '(11) 98765-4321', 'lucas.silva@exemplo.com'),
('12345678902', 'Mariana Santos', 'Avenida Brasil, 234', '(11) 98876-5432', 'mariana.santos@exemplo.com'),
('12345678903', 'Roberto Almeida', 'Rua das Acácias, 345', '(11) 97987-6543', 'roberto.almeida@exemplo.com'),
('12345678904', 'Fernanda Oliveira', 'Praça da República, 456', '(11) 97098-7654', 'fernanda.oliveira@exemplo.com'),
('12345678905', 'Carlos Pereira', 'Avenida das Nações, 567', '(11) 96123-4567', 'carlos.pereira@exemplo.com'),
('12345678906', 'Juliana Costa', 'Rua do Comércio, 678', '(11) 96234-5678', 'juliana.costa@exemplo.com'),
('12345678907', 'Gabriel Martins', 'Avenida dos Trabalhadores, 789', '(11) 96345-6789', 'gabriel.martins@exemplo.com'),
('12345678908', 'Ana Beatriz', 'Rua da Amizade, 890', '(11) 96456-7890', 'ana.beatriz@exemplo.com'),
('12345678909', 'Thiago Rodrigues', 'Rua do Lazer, 901', '(11) 96567-8901', 'thiago.rodrigues@exemplo.com'),
('12345678910', 'Sofia Mendes', 'Rua das Flores, 123', '(11) 96678-9012', 'sofia.mendes@exemplo.com'),
('12345678911', 'Renato Lima', 'Avenida do Futuro, 234', '(11) 96789-0123', 'renato.lima@exemplo.com'),
('12345678912', 'Marcos Vinícius', 'Praça do Sol, 345', '(11) 96890-1234', 'marcos.vinicius@exemplo.com'),
('12345678913', 'Tatiane Dias', 'Rua do Morumbi, 456', '(11) 96901-2345', 'tatiane.dias@exemplo.com'),
('12345678914', 'Eduardo Gomes', 'Rua das Palmeiras, 567', '(11) 97012-3456', 'eduardo.gomes@exemplo.com'),
('12345678915', 'Larissa Ribeiro', 'Avenida da Liberdade, 678', '(11) 97123-4567', 'larissa.ribeiro@exemplo.com');

INSERT INTO Venda (Data, Cpf_Cliente, Total_Venda, Cod_Barras) VALUES
('2024-01-01', '12345678901', 249.90, '7891234567890'),
('2024-01-02', '12345678902', 249.90, '7891234567891'),
('2024-01-03', '12345678903', 249.90, '7891234567892'),
('2024-01-04', '12345678904', 249.90, '7891234567893'),
('2024-01-05', '12345678905', 249.90, '7891234567894'),
('2024-01-06', '12345678906', 249.90, '7891234567895'),
('2024-01-07', '12345678907', 249.90, '7891234567896'),
('2024-01-08', '12345678908', 249.90, '7891234567897'),
('2024-01-09', '12345678909', 249.90, '7891234567898'),
('2024-01-10', '12345678910', 249.90, '7891234567899'),
('2024-01-11', '12345678911', 249.90, '7891234567800'),
('2024-01-12', '12345678912', 249.90, '7891234567801'),
('2024-01-13', '12345678913', 249.90, '7891234567802'),
('2024-01-14', '12345678914', 249.90, '7891234567803'),
('2024-01-15', '12345678915', 249.90, '7891234567804');