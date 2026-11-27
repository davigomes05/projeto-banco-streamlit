
import streamlit as st
import banco

st.title("Loja Esportiva")
st.write("Cadastro de Produtos Esportivos")

with st.form("cadastro", clear_on_submit=True):
    nome = st.text_input("Nome do Produto")

    categoria = st.selectbox(
        "Categoria",
        ["Futebol", "Basquete", "Vôlei", "Academia", "Corrida", "Acessórios"]
    )

    preco = st.number_input(
        "Preço R$",
        min_value=0.0,
        step=0.50
    )

    enviar = st.form_submit_button("Cadastrar Produto")

# Verificação de erro
if enviar:
    if nome.strip() == "":
        st.warning("Digite o nome do produto!")
    elif preco <= 0:
        st.warning("Digite um preço válido!")
    else:
        banco.cadastrar(nome, categoria, preco)
        st.success("Produto esportivo cadastrado com sucesso!")
