# Gerando o pdf

def gerar_pdf(galera):
    import reportlab.pdfgen

    doc = reportlab.pdfgen.canvas.Canvas('contatos.pdf')
    coluna = 80
    linha = 800
    doc.drawString(coluna, linha, 'Nomes e telefones')

    for nome, telefone in galera.items():
        linha -= 15
        doc.drawString(coluna, linha, nome + ':' + telefone)

        doc.save()
