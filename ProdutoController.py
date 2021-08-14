import services.database as db

def Incluir(produto):
    count = db.cursor.execute("""INSERT INTO Produto (Pdescricao, Ppreco) VALUES (?,?)""",
    produto.descricao, produto.preco).rowcount
    db.cnxn.commit()