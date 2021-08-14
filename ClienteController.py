import services.database as db

def Incluir(cliente):
    count = db.cursor.execute("""INSERT INTO Pessoas (Pnome, Pemail, Ptelefone, Pprofissao) VALUES (?,?,?,?)""",
    cliente.nome, cliente.email, cliente.telefone, cliente.profissao).rowcount
    db.cnxn.commit()
