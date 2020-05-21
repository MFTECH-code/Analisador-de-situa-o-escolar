def analyser(media_escola, formato):
    '''
    Média: Qual a média determinada pela escola...
    Formato: Qual o formato: Bimestral ou Trimestral...
    B -> Bimestre
    T -> Trimestre
    
    '''
    if formato == 'B':
        notas1 = list() 
        for bi_1 in range(1, 5):
            nota1 = float(input(f'Digite sua nota no {bi_1}º bimestre: '))
            notas1.append(nota1)
        total1 = sum(notas1)
        media_aluno1 = total1 / 4
        if media_aluno1 >= media_escola:
            return print(f'Sua situação é boa, sua média foi {media_aluno1:.2f}.')
        else:
            return print(f'Infelizmente você não estudou o suficiente... Sua média foi {media_aluno1:.2f}.')
    if formato == 'T':
        notas2 = list()
        for tri_1 in range(1, 4):
            nota2 = float(input(f'Digite sua nota no {tri_1}º trimestre: '))
            notas2.append(nota2)
        total2 = sum(notas2)
        media_aluno2 = total2 / 3
        if media_aluno2 >= media_escola:
            return print(f'Sua situação é boa, sua média foi {media_aluno2:.2f}.')
        else:
            return print(f'Infelizmente você não estudou o suficiente... Sua média foi {media_aluno2:.2f}.')
        
    
            
media_escolar = float(input('Qual a média da sua escola: '))
formato_escola = str(input('Qual o formato que sua escola segue? [BI/TRI]: ')).upper().strip()[0]
analyser(media_escolar, formato_escola)