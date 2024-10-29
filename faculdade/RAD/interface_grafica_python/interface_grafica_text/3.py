import webview

def main():
    # Cria uma janela com a URL especificada
    webview.create_window('Olá, mundo! Este é o primeiro exemplo do PyWebView', 'https://www.google.com/')
    webview.start()

if __name__ == '__main__':
    main()
