import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "ACb48049c3213efc8954ab0f2eabbb3e2b"
# Your Auth Token from twilio.com/console
auth_token  = "63379be50d1cfea9f30ee76e77868aeb"
client = Client(account_sid, auth_token)


# Abrir os arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor(a): {vendedor}, venda: {vendas}')
        message = client.messages.create(
            to="+5517981204938",
            from_="+13203730709",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor(a): {vendedor}, venda: {vendas}')

        print(message.sid)