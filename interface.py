import tkinter as tk
from tkinter import ttk
from database import execute_query, fetch_data
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuração da interface gráfica
        self.title("Buy Corner - Loja de Produtos Esportivos")
        self.geometry("1920x1080")
        self.configure(bg='#FF0000')

        # Cabeçalho
        header = tk.Label(self, text="BUY CORNER - LOJA DE PRODUTOS ESPORTIVOS", font=('Impact', 30), bg='#FF0000', fg='black')
        header.pack(pady=10)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Estilo da aplicação
        style = ttk.Style()
        style.configure('TNotebook', background='#FF0000')
        style.configure('TNotebook.Tab', background='#3e3e3e', foreground='black', padding=10)
        style.configure('TFrame', background='#2e2e2e')

        # Aba Produtos
        self.create_products_tab(notebook)

        # Aba Fornecedores
        self.create_suppliers_tab(notebook)

        # Aba Clientes
        self.create_clients_tab(notebook)

        # Aba Vendas
        self.create_sales_tab(notebook)

        self.mainloop()

    def create_products_tab(self, notebook):
        aba_produtos = ttk.Frame(notebook)
        notebook.add(aba_produtos, text="Produtos")

        frame_produtos = ttk.Frame(aba_produtos, padding=10, relief=tk.GROOVE, borderwidth=2)
        frame_produtos.grid(row=0, column=0, sticky='nsew')

        tk.Label(frame_produtos, text="Código de Barras:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=0, column=0, sticky='e', pady=5)
        self.entry_cod_barras = tk.Entry(frame_produtos, width=40, font=('Arial', 12))
        self.entry_cod_barras.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_produtos, text="Nome:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=1, column=0, sticky='e', pady=5)
        self.entry_name = tk.Entry(frame_produtos, width=40, font=('Arial', 12))
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_produtos, text="Categoria:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=2, column=0, sticky='e', pady=5)
        self.entry_category = tk.Entry(frame_produtos, width=40, font=('Arial', 12))
        self.entry_category.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_produtos, text="Descrição:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=3, column=0, sticky='e', pady=5)
        self.entry_description = tk.Entry(frame_produtos, width=40, font=('Arial', 12))
        self.entry_description.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame_produtos, text="Preço:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=4, column=0, sticky='e', pady=5)
        self.entry_price = tk.Entry(frame_produtos, width=40, font=('Arial', 12))
        self.entry_price.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(frame_produtos, text="Quantidade em Estoque:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=5, column=0, sticky='e', pady=5)
        self.entry_quantity = tk.Entry(frame_produtos, width=40, font=('Arial', 12))
        self.entry_quantity.grid(row=5, column=1, padx=10, pady=5)

        btn_add_product = tk.Button(frame_produtos, text="Adicionar Produto", command=self.add_product, bg='#4caf50', fg='white')
        btn_add_product.grid(row=6, column=1, pady=10)

        btn_delete_product = tk.Button(frame_produtos, text="Excluir Produto", command=self.delete_product, bg='#f44336', fg='white')
        btn_delete_product.grid(row=6, column=0, pady=10)

        self.tree_products = ttk.Treeview(frame_produtos, columns=("Código de Barras", "Nome", "Categoria", "Descrição", "Preço", "Quantidade em Estoque"), show='headings')
        self.tree_products.grid(row=7, column=0, columnspan=2, pady=10)
        for col in self.tree_products["columns"]:
            self.tree_products.heading(col, text=col)

        self.load_products()

    def load_products(self):
        query = "SELECT * FROM Produto"
        for row in fetch_data(query):
            self.tree_products.insert("", "end", values=row)

    def add_product(self):
        query = "INSERT INTO Produto (Cod_Barras, Nome, Categoria, Descrição, Preço, Quantidade_Em_Estoque) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            self.entry_cod_barras.get(),
            self.entry_name.get(),
            self.entry_category.get(),
            self.entry_description.get(),
            float(self.entry_price.get()),
            int(self.entry_quantity.get())
        )
        execute_query(query, params)
        self.tree_products.delete(*self.tree_products.get_children())
        self.load_products()
        self.clear_product_entries()

    def delete_product(self):
        selected_item = self.tree_products.selection()
        if selected_item:
            item = self.tree_products.item(selected_item)
            query = "DELETE FROM Produto WHERE Cod_Barras = %s"
            execute_query(query, (item['values'][0],))
            self.tree_products.delete(selected_item)

    def clear_product_entries(self):
        self.entry_cod_barras.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def create_suppliers_tab(self, notebook):
        aba_fornecedores = ttk.Frame(notebook)
        notebook.add(aba_fornecedores, text="Fornecedores")

        frame_fornecedores = ttk.Frame(aba_fornecedores, padding=10, relief=tk.GROOVE, borderwidth=2)
        frame_fornecedores.grid(row=0, column=0, sticky='nsew')

        tk.Label(frame_fornecedores, text="CNPJ:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=0, column=0, sticky='e', pady=5)
        self.entry_supplier_cnpj = tk.Entry(frame_fornecedores, width=40, font=('Arial', 12))
        self.entry_supplier_cnpj.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_fornecedores, text="Nome:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=1, column=0, sticky='e', pady=5)
        self.entry_supplier_name = tk.Entry(frame_fornecedores, width=40, font=('Arial', 12))
        self.entry_supplier_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_fornecedores, text="Endereço:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=2, column=0, sticky='e', pady=5)
        self.entry_supplier_address = tk.Entry(frame_fornecedores, width=40, font=('Arial', 12))
        self.entry_supplier_address.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_fornecedores, text="Telefone:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=3, column=0, sticky='e', pady=5)
        self.entry_supplier_phone = tk.Entry(frame_fornecedores, width=40, font=('Arial', 12))
        self.entry_supplier_phone.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame_fornecedores, text="Email:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=4, column=0, sticky='e', pady=5)
        self.entry_supplier_email = tk.Entry(frame_fornecedores, width=40, font=('Arial', 12))
        self.entry_supplier_email.grid(row=4, column=1, padx=10, pady=5)

        btn_add_supplier = tk.Button(frame_fornecedores, text="Adicionar Fornecedor", command=self.add_supplier, bg='#4caf50', fg='white')
        btn_add_supplier.grid(row=5, column=1, pady=10)

        btn_delete_supplier = tk.Button(frame_fornecedores, text="Excluir Fornecedor", command=self.delete_supplier, bg='#f44336', fg='white')
        btn_delete_supplier.grid(row=5, column=0, pady=10)

        self.tree_suppliers = ttk.Treeview(frame_fornecedores, columns=("CNPJ", "Nome", "Endereço", "Telefone", "Email"), show='headings')
        self.tree_suppliers.grid(row=6, column=0, columnspan=2, pady=10)
        for col in self.tree_suppliers["columns"]:
            self.tree_suppliers.heading(col, text=col)

        self.load_suppliers()

    def load_suppliers(self):
        query = "SELECT * FROM Fornecedor"
        for row in fetch_data(query):
            self.tree_suppliers.insert("", "end", values=row)

    def add_supplier(self):
        query = "INSERT INTO Fornecedor (Cnpj_Fornecedor, Nome, Endereço, Telefone, Email) VALUES (%s, %s, %s, %s, %s)"
        params = (
            self.entry_supplier_cnpj.get(),
            self.entry_supplier_name.get(),
            self.entry_supplier_address.get(),
            self.entry_supplier_phone.get(),
            self.entry_supplier_email.get()
        )
        execute_query(query, params)
        self.tree_suppliers.delete(*self.tree_suppliers.get_children())
        self.load_suppliers()
        self.clear_supplier_entries()

    def delete_supplier(self):
        selected_item = self.tree_suppliers.selection()
        if selected_item:
            item = self.tree_suppliers.item(selected_item)
            query = "DELETE FROM Fornecedor WHERE Cnpj_Fornecedor = %s"
            execute_query(query, (item['values'][0],))
            self.tree_suppliers.delete(selected_item)

    def clear_supplier_entries(self):
        self.entry_supplier_cnpj.delete(0, tk.END)
        self.entry_supplier_name.delete(0, tk.END)
        self.entry_supplier_address.delete(0, tk.END)
        self.entry_supplier_phone.delete(0, tk.END)
        self.entry_supplier_email.delete(0, tk.END)

    def create_clients_tab(self, notebook):
        aba_clientes = ttk.Frame(notebook)
        notebook.add(aba_clientes, text="Clientes")

        frame_clientes = ttk.Frame(aba_clientes, padding=10, relief=tk.GROOVE, borderwidth=2)
        frame_clientes.grid(row=0, column=0, sticky='nsew')

        tk.Label(frame_clientes, text="CPF:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=0, column=0, sticky='e', pady=5)
        self.entry_client_cpf = tk.Entry(frame_clientes, width=40, font=('Arial', 12))
        self.entry_client_cpf.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_clientes, text="Nome:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=1, column=0, sticky='e', pady=5)
        self.entry_client_name = tk.Entry(frame_clientes, width=40, font=('Arial', 12))
        self.entry_client_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_clientes, text="Endereço:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=2, column=0, sticky='e', pady=5)
        self.entry_client_address = tk.Entry(frame_clientes, width=40, font=('Arial', 12))
        self.entry_client_address.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_clientes, text="Telefone:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=3, column=0, sticky='e', pady=5)
        self.entry_client_phone = tk.Entry(frame_clientes, width=40, font=('Arial', 12))
        self.entry_client_phone.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame_clientes, text="Email:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=4, column=0, sticky='e', pady=5)
        self.entry_client_email = tk.Entry(frame_clientes, width=40, font=('Arial', 12))
        self.entry_client_email.grid(row=4, column=1, padx=10, pady=5)

        btn_add_client = tk.Button(frame_clientes, text="Adicionar Cliente", command=self.add_client, bg='#4caf50', fg='white')
        btn_add_client.grid(row=5, column=1, pady=10)

        btn_delete_client = tk.Button(frame_clientes, text="Excluir Cliente", command=self.delete_client, bg='#f44336', fg='white')
        btn_delete_client.grid(row=5, column=0, pady=10)

        self.tree_clients = ttk.Treeview(frame_clientes, columns=("CPF", "Nome", "Endereço", "Telefone", "Email"), show='headings')
        self.tree_clients.grid(row=6, column=0, columnspan=2, pady=10)
        for col in self.tree_clients["columns"]:
            self.tree_clients.heading(col, text=col)

        self.load_clients()

    def load_clients(self):
        query = "SELECT * FROM Cliente"
        for row in fetch_data(query):
            self.tree_clients.insert("", "end", values=row)

    def add_client(self):
        query = "INSERT INTO Cliente (Cpf_Cliente, Nome, Endereço, Telefone, Email) VALUES (%s, %s, %s, %s, %s)"
        params = (
            self.entry_client_cpf.get(),
            self.entry_client_name.get(),
            self.entry_client_address.get(),
            self.entry_client_phone.get(),
            self.entry_client_email.get()
        )
        execute_query(query, params)
        self.tree_clients.delete(*self.tree_clients.get_children())
        self.load_clients()
        self.clear_client_entries()

    def delete_client(self):
        selected_item = self.tree_clients.selection()
        if selected_item:
            item = self.tree_clients.item(selected_item)
            query = "DELETE FROM Cliente WHERE Cpf_Cliente = %s"
            execute_query(query, (item['values'][0],))
            self.tree_clients.delete(selected_item)

    def clear_client_entries(self):
        self.entry_client_cpf.delete(0, tk.END)
        self.entry_client_name.delete(0, tk.END)
        self.entry_client_address.delete(0, tk.END)
        self.entry_client_phone.delete(0, tk.END)
        self.entry_client_email.delete(0, tk.END)

    def create_sales_tab(self, notebook):
        aba_vendas = ttk.Frame(notebook)
        notebook.add(aba_vendas, text="Vendas")

        frame_vendas = ttk.Frame(aba_vendas, padding=10, relief=tk.GROOVE, borderwidth=2)
        frame_vendas.grid(row=0, column=0, sticky='nsew')

        tk.Label(frame_vendas, text="CPF Cliente:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=1, column=0, sticky='e', pady=5)
        self.entry_sale_client_cpf = tk.Entry(frame_vendas, width=40, font=('Arial', 12))
        self.entry_sale_client_cpf.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_vendas, text="Data:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=2, column=0, sticky='e', pady=5)
        self.entry_sale_date = tk.Entry(frame_vendas, width=40, font=('Arial', 12))
        self.entry_sale_date.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_vendas, text="Total Venda:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=3, column=0, sticky='e', pady=5)
        self.entry_sale_total = tk.Entry(frame_vendas, width=40, font=('Arial', 12))
        self.entry_sale_total.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame_vendas, text="Código de Barras:", font=('Arial', 12), bg='#2e2e2e', fg='white').grid(row=4, column=0, sticky='e', pady=5)
        self.entry_sale_product_code = tk.Entry(frame_vendas, width=40, font=('Arial', 12))
        self.entry_sale_product_code.grid(row=4, column=1, padx=10, pady=5)

        btn_add_sale = tk.Button(frame_vendas, text="Adicionar Venda", command=self.add_sale, bg='#4caf50', fg='white')
        btn_add_sale.grid(row=5, column=1, pady=10)

        btn_delete_sale = tk.Button(frame_vendas, text="Excluir Venda", command=self.delete_sale, bg='#f44336', fg='white')
        btn_delete_sale.grid(row=5, column=0, pady=10)

        self.tree_sales = ttk.Treeview(frame_vendas, columns=("ID da Venda", "Data", "CPF do Cliente", "Total da Venda", "Código de Barras"), show='headings')
        self.tree_sales.grid(row=6, column=0, columnspan=2, pady=10)
        for col in self.tree_sales["columns"]:
            self.tree_sales.heading(col, text=col)

        self.load_sales()

    def load_sales(self):
        query = "SELECT * FROM Venda"
        for row in fetch_data(query):
            self.tree_sales.insert("", "end", values=row)

    def add_sale(self):
        from datetime import datetime

        data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO Venda (Data, CPF_Cliente, Total_Venda, Cod_Barras) VALUES (%s, %s, %s, %s)"
        params = (
            data_venda,
            self.entry_sale_client_cpf.get(),
            float(self.entry_sale_total.get()),  
            self.entry_sale_product_code.get()
        )
        execute_query(query, params)
        self.tree_sales.delete(*self.tree_sales.get_children())
        self.load_sales()
        self.clear_sale_entries()

    def delete_sale(self):
        selected_item = self.tree_sales.selection()
        if selected_item:
            item = self.tree_sales.item(selected_item)
            query = "DELETE FROM Venda WHERE ID_Venda = %s"
            execute_query(query, (item['values'][0],))
            self.tree_sales.delete(selected_item)

    def clear_sale_entries(self):
        self.entry_sale_client_cpf.delete(0, tk.END)
        self.entry_sale_date.delete(0, tk.END)
        self.entry_sale_total.delete(0, tk.END)
        self.entry_sale_product_code.delete(0, tk.END)


if __name__ == "__main__":
    app = Application()
