# hashzap
# botão de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que é enviada (aparece para todo mundo)
    # Nome: Texto de Mensagem

# biblioteca para abrir o python no app e mostrar na web
import flet as ft

# definindo a função principal do aplicativo
def main(pagina):
    # o que irá mostrar no início do programa
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
        # texto recebe o que foi digitado pelo usuário e usuário recebe o nome do usuário. O tipo dos dados recebe o nome de mensagem.
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    # cria a caixa de mensagem com o label e garante que ao apertar enter, mesmo sem ter clicado no botão irá para a função enviar_mensagem
    campo_mensagem =ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)

    # cria o botão elevado "Enviar" e quando clicar chama a função enviar_mensagem
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
            # cria uma linha com o campo_mensagem e o botao_enviar_mensagem
            pagina.add(ft.Row(
                [campo_mensagem, botao_enviar_mensagem]
            ))
            # criar o botao de enviar a mensagem do usuario
            pagina.update()
        else:
            popup.open = False
            alerta = ft.Text("O CAMPO NOME NÃO PODE FICAR VAZIO")
            pagina.add(alerta)

    # cria um texto de ajuda "Escreva seu nome" e se apertar enter, mesmo sem clicar no botão, irá chamar a função entrar_chat
    nome_usuario = ft.TextField(label="Escreva seu nome", on_submit=entrar_chat)

    # popup recebe um alerta de diálogo
    popup = ft.AlertDialog(
        open = False,
        modal = True,
        # Título do popup
        title = ft.Text("Bem vindo ao Hashzap"),
        # dentro do popup, cria uma caixa de entrada de dados que recebe nome_usuario
        content = nome_usuario,
        # cria o botão elevado "Entrar" e quando clicar nele, chama a função entrar_chat
        actions = [ft.ElevatedButton("Entrar", on_click = entrar_chat)]
    )

    # inicializando a função entrar popup
    def entrar_popup(evento):
        # Criando uma caixa de diálogo para o popup
        pagina.dialog = popup
        # chamando o popup
        popup.open = True
        # atualizando a página
        pagina.update()

    # Cria o botão elevado chamado "Iniciar chat" e quando clicar nele, chama a função entrar_popup
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

# o view=ft.WEB_BROWSER, serve para mostrar no navegador
ft.app(target=main, view=ft.WEB_BROWSER)