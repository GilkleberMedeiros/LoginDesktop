Primeiro dia: 
Um dos primeiros bugs dessa 
versão foi o fato de que quando 
que clicava para mudar da janela
login para a janela signin, eele carregava
a janela signin totalmente vazia e não destruia
a janela login, dizendo que não existia imagens 
e por isso não carregava imagens da nova janela, 
resolvi isso tirando o método de destruição
da função swap e colocando antes da chamada da
função swap dentro de cada janela

Segundo dia: 
Resolvi fazer com que as duas janelas
sempre aparecessem no meio da tela, pois do jeito
que estava antes estava ruim quando trocava muito de
janela utilizei o método winfo_screenwindth() para
pegar a largura da tela e o seu equivalente para
a altura fiz alguns cálculos e configurei
no método geometry. Um pequeno problema que tive
foi que eu utilizei o método screenmmwindth() com
dois ms no meio e ele não me retornava o valor 
certo.

Consertei a janela de signin que estava ainda com
os mesmo campos da janela login.

Criei o método para checar se as entradas estão vazias.

Criei o método que chama os outros métodos para checar se
cada entrada individual está certa.

Adicionei labels dentro do objeto de cada entry para
servirem como aviso caso a entry(entrada) esteja
vazia ou caso não corresponda a outras condições.

Terceiro dia:
Configurei para que as menssagens de aviso sejam exibidas
nas labels.

Configurei para que os entry de senha não mostrassem a 
senha e sim "*" quando o entry.get() não fosse o 
placeholder.

Terminei as métodos que checam cada tipo de entry individual
mente, check_name(), check_email(), check_pass().

Essa versão termina por aqui, agora o que falta é somente 
implementar a integração com o banco de dados.

