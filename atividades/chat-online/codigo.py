# hashzap
# botão de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que é enviada (aparece para todo mundo)
    # Nome: Texto de Mensagem

import flet as ft

def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()
    
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: entrou no chat", size=20, italic=True, color=ft.colors.GREEN))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem =ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)

    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(evento):
        if nome_usuario.value != "":
            # fechar o popup
            popup.open = False
            # remover o botão
            pagina.remove(botao_iniciar)
            pagina.remove(texto)
            # adicionar o chat
            pagina.add(chat)
            # texto que o usuário entrou na sala
            pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
            # criar o campo de mensagem do usuário
            pagina.add(ft.Row(
                [campo_mensagem, botao_enviar_mensagem]
            ))
            # criar o botao de enviar a mensagem do usuario
            pagina.update()
        else:
            popup.open = False
            alerta = ft.Text("O CAMPO NOME NÃO PODE FICAR VAZIO")
            pagina.add(alerta)

    nome_usuario = ft.TextField(label="Escreva seu nome", on_submit=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
    )

    def entrar_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main)