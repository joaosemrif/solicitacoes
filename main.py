from os import write
import streamlit as st
import controllers.ClienteController as ClienteController
import model.Cliente as cliente
import model.Produto as produto

st.sidebar.title('Menu')
paginaselecionada=st.sidebar.selectbox('Selecione a pagina',['incluir_cliente', 'Incluir Produto', 'Solicitacoes'])

if paginaselecionada == 'incluir_cliente':
    st.title('Incluir Cliente')
    with st.form(key="incluir_cliente"):
        input_name = st.text_input(label="Insira o seu nome")
        input_email = st.text_input(label="Insira seu email")
        input_telefone= st.text_input(label="Insira o seu telefone")
        input_occupation = st.selectbox("Selecione sua ocupação", ["Cliente", "Funcionario"])
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        cliente.nome = input_name
        cliente.email = input_email
        cliente.telefone = input_telefone
        cliente.profissao = input_occupation

        ClienteController.Incluir(cliente)
        st.success = ('Cliente Incluido com sucesso')

elif paginaselecionada == 'Incluir Produto':
    st.title('Cadastro Produto')

    with st.form(key="incluir_produto"):
        input_Descricao = st.text_input(label="Informe o nome do produto")
        input_preco= st.number_input(label="Insira o preço")
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        produto.descricao= input_Descricao
        produto.preco = input_preco
        []

        ClienteController.Incluir(produto)
        st.success = ('Produto Incluido com sucesso')

    
elif paginaselecionada == 'Solicitacoes':
    st.title('Solicitacoes')