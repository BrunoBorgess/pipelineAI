import streamlit as st
from datetime import datetime, time

def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9,0)) # Horário padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produto", min_value=1, step=1)
    produto = st.selectbox(" Produto", options= ["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

    if st.button("Salvar"):
        data_hora = datetime.combine(data, hora)
        st.write("**Dados da venda:**")
        st.write(f"Email do vendedor:{email}" )
        st.write(f"Data e hora da compra: {data_hora}")
        st.write(f"Valor da venda: R${valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")


if __name__ == "__main__":
    main = main()