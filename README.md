import tkinter as tk
import threading
import random

perguntas = {
    "Matemática": {
    "O que é um número primo?": ["a) Um número divisível por 2", "b) Um número divisível por 3", "c) Um número natural maior que 1 com apenas dois divisores: 1 e ele mesmo", "d) Um número que não pode ser representado no sistema binário"],
    "O que é um polinômio?": ["a) Um número inteiro", "b) Uma expressão algébrica composta por termos que envolvem variáveis elevadas a expoentes inteiros não negativos", "c) Um número fracionário", "d) Um tipo de logaritmo"],
    "Qual é a fórmula da área de um triângulo?": ["a) A = l * w", "b) A = πr²", "c) A = 1/2 * b * h", "d) A = s²"],
    "O que são números irracionais?": ["a) Números que não podem ser representados como frações", "b) Números que são inteiros", "c) Números que são sempre negativos", "d) Números que podem ser escritos na forma a/b, onde 'a' e 'b' são inteiros"],
    "O que é uma equação linear?": ["a) Uma equação com expoentes elevados", "b) Uma equação que envolve raízes quadradas", "c) Uma equação de segundo grau", "d) Uma equação em que cada termo é uma constante ou o produto de uma constante e a primeira potência de uma variável"],
    "Qual é a propriedade distributiva?": ["a) a(b + c) = ab + ac", "b) a(b - c) = ab - ac", "c) a/b = c/d, então ad = bc", "d) a^2 + b^2 = c^2"],
    "O que é a média aritmética?": ["a) A soma de todos os valores dividida pelo número de valores", "b) O valor que ocorre com mais frequência em um conjunto de dados", "c) A diferença entre o maior e o menor valor", "d) A multiplicação de todos os valores"],
    "O que é uma fração equivalente?": ["a) Frações que têm denominadores diferentes", "b) Frações que têm numeradores diferentes", "c) Frações que representam a mesma quantidade", "d) Frações que não podem ser simplificadas"],
    "O que é o Teorema de Pitágoras?": ["a) A soma dos ângulos internos de um triângulo é 180°", "b) A soma dos quadrados dos catetos é igual ao quadrado da hipotenusa em um triângulo retângulo", "c) A soma dos lados de um triângulo é igual a 180°", "d) A soma das áreas dos quadrados dos catetos é igual à área do quadrado da hipotenusa"],
    "O que é um múltiplo comum?": ["a) Um número que é a soma de dois números primos", "b) Um número que é divisível por dois ou mais números diferentes de zero", "c) Um número que não tem divisores comuns com outro número", "d) Um número que é primo"],
    "Qual é a propriedade comutativa da adição?": ["a) a + b = b + a", "b) a - b = b - a", "c) ab = ba", "d) a/b = b/a"],
    "O que é uma razão?": ["a) Uma comparação entre dois números", "b) A soma de dois números", "c) O produto de dois números", "d) A diferença entre dois números"],
    "O que é uma progressão aritmética?": ["a) Uma sequência de números em que a diferença entre termos consecutivos é constante", "b) Uma sequência de números em que a razão entre termos consecutivos é constante", "c) Uma sequência de números em que cada termo é o produto dos anteriores", "d) Uma sequência de números em que a soma dos termos é constante"],
    "Qual é a definição de mediana em um conjunto de dados?": ["a) O número que ocorre com mais frequência", "b) A média aritmética dos dados", "c) O valor do meio quando os dados estão organizados em ordem", "d) A diferença entre o maior e o menor valor"],    
    "O que é uma circunferência?": ["a) A área entre dois pontos em uma curva", "b) A soma das áreas de um polígono", "c) O conjunto de todos os pontos em um plano que estão a uma distância fixa de um ponto fixo chamado centro", "d) O limite de uma sequência infinita"],
    },
    "História": {
"Quem foi o responsável pelo Descobrimento do Brasil em 1500?": ["a) Pedro Álvares Cabral", "b) Cristóvão Colombo", "c) Fernão Mendes Pinto", "d) Vasco da Gama"],
"Qual foi o período em que o Brasil foi uma colônia de Portugal?": ["a) Período Colonial", "b) Período Imperial", "c) Período Republicano", "d) Período Ditatorial"],
"Em que ano foi proclamada a Independência do Brasil?": ["a) 1822", "b) 1500", "c) 1889", "d) 1964"],
"Quem foi o primeiro imperador do Brasil?": ["a) Dom Pedro II", "b) Dom João VI", "c) Dom Pedro I", "d) Dom Manuel I"],
"O que foi a Guerra do Paraguai (1864-1870)?": ["a) Conflito entre Brasil e Paraguai", "b) Revolução Farroupilha", "c) Inconfidência Mineira", "d) Revolta dos Malês"],
"Quem foi o líder da Revolta dos Malês em 1835?": ["a) Zumbi dos Palmares", "b) Luís Gama", "c) Abdias do Nascimento", "d) Manuel Congo"],
"Qual movimento contestou o governo de Getúlio Vargas na década de 1930?": ["a) Revolução de 1930", "b) Revolução Constitucionalista de 1932", "c) Revolta da Armada", "d) Intentona Comunista"],
"O que foi o AI-5 durante o regime militar (1964-1985)?": ["a) Ato Institucional nº 5", "b) Assembleia Internacional de 1965", "c) Acordo Internacional de 5 de abril", "d) Ação Integralista Brasileira"],
"Quem foi o presidente do Brasil durante a Proclamação da República em 1889?": ["a) Floriano Peixoto", "b) Deodoro da Fonseca", "c) Prudente de Morais", "d) Marechal Hermes da Fonseca"],
"O que representou o movimento Tenentista na década de 1920?": ["a) Contestação militar ao governo", "b) Movimento sindicalista", "c) Revolta da Vacina", "d) Greve dos Canudos"],
"Qual foi o objetivo da política de industrialização implementada durante o governo de Juscelino Kubitschek?": ["a) Desenvolvimento da indústria nacional", "b) Aumento das exportações agrícolas", "c) Combate à inflação", "d) Implementação do socialismo"],
"Quem foi o líder da Revolta da Armada em 1893?": ["a) Floriano Peixoto", "b) Deodoro da Fonseca", "c) Almirante Custódio de Melo", "d) Marechal Hermes da Fonseca"],
"Qual foi o nome do plano econômico que marcou o governo de Fernando Collor em 1990?": ["a) Plano Cruzado", "b) Plano Real", "c) Plano Collor", "d) Plano Sarney"],
"O que foi o movimento operário conhecido como Canudos?": ["a) Comunidade utópica no interior da Bahia", "b) Revolta popular contra o governo", "c) Greve geral de trabalhadores", "d) Revolta dos Sertanejos"],
"Quem foi o líder quilombola que resistiu ao sistema escravista no Brasil colonial?": ["a) Zumbi dos Palmares", "b) Chico Rei", "c) Luís Gama", "d) Manuel Congo"],
},
    "Português": {
"Qual é a sílaba tônica da palavra cachorro ?": ["a) ca", "b) cho", "c) ro", "d) cach"],
"Em qual alternativa a palavra está escrita corretamente?": ["a) excesivo", "b) excessivo", "c) ecessivo", "d) exsessivo"],
"Qual é o plural correto de papel?": ["a) papéis", "b) papelões", "c) papelãos", "d) papélis"],
"O que é um sinônimo para a palavra alegre?": ["a) triste", "b) feliz", "c) sério", "d) cansado"],
"Qual é a classe gramatical da palavra correr?": ["a) adjetivo", "b) verbo", "c) substantivo", "d) preposição"],
"Qual é o antônimo de ampliar?": ["a) aumentar", "b) reduzir", "c) manter", "d) melhorar"],
"Em qual alternativa a palavra é um pronome pessoal?": ["a) casa", "b) ele", "c) bonito", "d) correndo"],
"Qual é a conjugação correta do verbo ler na terceira pessoa do singular do presente do indicativo?": ["a) lemos", "b) lê", "c) li", "d) le"],
"O que é um ditongo?": ["a) Encontro de uma vogal com uma semivogal.", "b) Encontro de duas vogais em uma mesma sílaba.", "c) Encontro de duas consoantes em uma mesma sílaba.", "d) Encontro de uma consoante com uma semivogal."],
"Qual é a forma correta de completar a frase: Ele ___ muito bem na prova.?": ["a) foram", "b) fui", "c) éramos", "d) foi"],
"Em qual alternativa a palavra está grafada corretamente?": ["a) disculpa", "b) desculpa", "c) discolpa", "d) desculpah"],
"Qual é o plural de cidadão?": ["a) cidadãos", "b) cidadães", "c) cidadonhos", "d) cidadões"],
"Qual é o sujeito da frase: O pássaro canta na janela.?": ["a) O pássaro", "b) Canta", "c) Na janela", "d) O pássaro canta"],
"O que é um adjetivo?": ["a) Palavra que expressa ação.", "b) Palavra que indica lugar.", "c) Palavra que caracteriza ou qualifica um ser.", "d) Palavra que conecta termos na frase."],
"Qual é a conjugação correta do verbo ter na primeira pessoa do singular do pretérito perfeito do indicativo?": ["a) tive", "b) tenho", "c) tuve", "d) tivemos"],
        
    },
    "Ciências": {
    "Qual é a função das mitocôndrias em uma célula?": ["a) Produção de energia através da fotossíntese.", "b) Armazenamento de nutrientes.", "c) Respiração celular e produção de ATP.", "d) Síntese de proteínas."],
    "Como ocorre a reprodução assexuada em organismos unicelulares?": ["a) Por meio da mitose.", "b) Através da meiose.", "c) Por fecundação.", "d) Pela formação de esporos."],
    "Qual é a diferença entre mitose e meiose?": ["a) A mitose resulta em células geneticamente diferentes, enquanto a meiose produz células geneticamente idênticas.", "b) A mitose produz células haploides, enquanto a meiose produz células diploides.", "c) A mitose é responsável pela reprodução assexuada, enquanto a meiose está envolvida na reprodução sexuada.", "d) A mitose ocorre apenas em células animais, enquanto a meiose ocorre apenas em células vegetais."],
    "O que é a teoria celular e quais são seus princípios fundamentais?": ["a) A teoria celular afirma que todos os organismos são unicelulares.", "b) Os princípios fundamentais incluem a ideia de que a célula é a unidade básica da vida e que todos os seres vivos são compostos por células.", "c) A teoria celular defende que apenas organismos complexos possuem células.", "d) Os princípios fundamentais incluem a ideia de que a célula é incapaz de se reproduzir."],
    "Como as plantas realizam a troca gasosa durante a fotossíntese?": ["a) Através da absorção de oxigênio pelas raízes.", "b) Pela liberação de dióxido de carbono pelos estômatos.", "c) Pela absorção de dióxido de carbono pelas folhas.", "d) Pela liberação de oxigênio durante a fase escura da fotossíntese."],
    "O que são ácidos e bases e como eles se relacionam com o pH?": ["a) Ácidos têm pH maior que 7, enquanto bases têm pH menor que 7.", "b) Ácidos aumentam o pH, enquanto bases diminuem o pH.", "c) Ácidos têm pH menor que 7, enquanto bases têm pH maior que 7.", "d) Ácidos e bases têm sempre o mesmo pH."],
    "Qual é a diferença entre uma reação endotérmica e exotérmica?": ["a) Reações endotérmicas liberam energia, enquanto reações exotérmicas absorvem energia.", "b) Reações endotérmicas absorvem energia, enquanto reações exotérmicas liberam energia.", "c) Ambas liberam energia.", "d) Ambas absorvem energia."],
    "O que é a tabela periódica e como os elementos estão organizados nela?": ["a) A tabela periódica organiza os elementos por ordem de massa atômica.", "b) Os elementos são organizados por ordem de número atômico.", "c) A tabela periódica organiza os elementos por ordem alfabética.", "d) Os elementos são organizados por ordem de volume atômico."],
    "Explique a lei da conservação da massa em reações químicas.": ["a) A massa dos reagentes é sempre maior que a massa dos produtos.", "b) A massa dos produtos é sempre maior que a massa dos reagentes.", "c) A massa total dos reagentes é igual à massa total dos produtos.", "d) A massa total dos produtos é sempre zero."],
    "Como funcionam as ligações iônicas e covalentes entre átomos?": ["a) Ligações iônicas envolvem a compartilhamento de elétrons, enquanto ligações covalentes envolvem a transferência de elétrons.", "b) Ligações iônicas envolvem a transferência de elétrons, enquanto ligações covalentes envolvem o compartilhamento de elétrons.", "c) Ambas as ligações envolvem a transferência de elétrons.", "d) Ambas as ligações envolvem o compartilhamento de elétrons."],
    "O que é a lei da inércia e como ela se aplica aos objetos em movimento?": ["a) A lei da inércia afirma que objetos em movimento permanecem em movimento, enquanto objetos em repouso permanecem em repouso.", "b) A lei da inércia afirma que a velocidade de um objeto é constante.", "c) A lei da inércia afirma que a força é diretamente proporcional à aceleração.", "d) A lei da inércia não se aplica a objetos em movimento."],
    "Explique a diferença entre velocidade e aceleração.": ["a) Velocidade é a taxa de mudança de posição, enquanto aceleração é a taxa de mudança de velocidade.", "b) Velocidade é a taxa de mudança de velocidade, enquanto aceleração é a taxa de mudança de posição.", "c) Velocidade e aceleração são conceitos idênticos.", "d) Velocidade e aceleração são ambos relacionados à posição de um objeto."],
    "Como a energia térmica se propaga e é transferida entre corpos?": ["a) A energia térmica se propaga apenas através de ondas sonoras.", "b) A energia térmica se propaga por condução, convecção e radiação.", "c) A energia térmica é transferida apenas por convecção.", "d) A energia térmica não pode ser transferida entre corpos."],
    "O que são ondas eletromagnéticas e qual é sua importância na física?": ["a) Ondas eletromagnéticas são ondas mecânicas que requerem um meio material para se propagar.", "b) Ondas eletromagnéticas são ondas sonoras.", "c) Ondas eletromagnéticas são ondas que não requerem um meio material para se propagar e incluem luz visível e ondas de rádio.", "d) Ondas eletromagnéticas são exclusivamente ondas de som."],
    "Como a lei da gravidade de Newton descreve a atração entre dois corpos massivos?": ["a) A força gravitacional é diretamente proporcional à massa de um corpo e inversamente proporcional à distância entre eles.", "b) A força gravitacional é independente da massa dos corpos e da distância entre eles.", "c) A força gravitacional é diretamente proporcional à distância entre os corpos e independente de suas massas.", "d) A lei da gravidade de Newton não se aplica a corpos massivos."]    
    },
    "Esporte": {
    "Qual país sediou a Copa do Mundo de Futebol Masculino em 2014?": ["a) Brasil", "b) Alemanha", "c) Rússia", "d) Espanha"],
    "Qual piloto de Fórmula 1 é conhecido como 'Honey Badger'?": ["a) Lewis Hamilton", "b) Sebastian Vettel", "c) Daniel Ricciardo", "d) Fernando Alonso"],
    "Quantas vezes a seleção brasileira de futebol masculino ganhou a medalha de ouro nas Olimpíadas até 2022?": ["a) 1", "b) 2", "c) 3", "d) 4"],
    "Quem é o maior artilheiro da seleção argentina de futebol?": ["a) Lionel Messi", "b) Diego Maradona", "c) Gabriel Batistuta", "d) Hernan Crespo"],
    "Qual é o esporte principal dos Jogos Paralímpicos de Verão?": ["a) Basquete em cadeira de rodas", "b) Goalball", "c) Levantamento de peso", "d) Atletismo"],
    "Qual é o tempo de acréscimo padrão em uma partida de futebol?": ["a) 5 minutos", "b) 10 minutos", "c) Variável", "d) 7 minutos"],
    "Em que esporte a brasileira Marta é uma lenda, sendo eleita seis vezes como a melhor jogadora do mundo?": ["a) Vôlei", "b) Futebol", "c) Natação", "d) Atletismo"],
    "Qual é a distância total percorrida por uma maratona olímpica?": ["a) 26.2 milhas (42.195 km)", "b) 13.1 milhas (21.0975 km)", "c) 10 milhas (16.0934 km)", "d) 30 km"],
    "Quem é o maior vencedor da história da Fórmula 1, com sete títulos mundiais?": ["a) Sebastian Vettel", "b) Lewis Hamilton", "c) Fernando Alonso", "d) Michael Schumacher"],
    "Qual país sediará os Jogos Olímpicos de Verão de 2028?": ["a) França", "b) Austrália", "c) Estados Unidos", "d) Canadá"],
    "Qual é o recorde de mais gols marcados em uma única edição da Copa do Mundo de Futebol Masculino?": ["a) 10 gols", "b) 13 gols", "c) 16 gols", "d) 18 gols"],
    "Em que ano o Brasil sediou os Jogos Olímpicos pela primeira vez?": ["a) 1956", "b) 1964", "c) 2016", "d) 1980"],
    "Quem é considerado o 'Pistoleiro' e é um dos principais atacantes da seleção uruguaia?": ["a) Edinson Cavani", "b) Luis Suárez", "c) Diego Forlán", "d) Abel Hernandez"],
    "Qual é a única seleção africana a vencer a Copa do Mundo de Futebol Masculino?": ["a) Gana", "b) Nigéria", "c) África do Sul", "d) Camarões"],
    "Qual é a nacionalidade do piloto de Fórmula 1 Max Verstappen?": ["a) Holandesa", "b) Belga", "c) Alemã", "d) Francesa"],
    },
    "Perguntatrix": { 
    "O que é a média aritmética?": ["a) A soma de todos os valores dividida pelo número de valores", "b) O valor que ocorre com mais frequência em um conjunto de dados", "c) A diferença entre o maior e o menor valor", "d) A multiplicação de todos os valores"],
    "O que é uma fração equivalente?": ["a) Frações que têm denominadores diferentes", "b) Frações que têm numeradores diferentes", "c) Frações que representam a mesma quantidade", "d) Frações que não podem ser simplificadas"],
    "O que é o Teorema de Pitágoras?": ["a) A soma dos ângulos internos de um triângulo é 180°", "b) A soma dos quadrados dos catetos é igual ao quadrado da hipotenusa em um triângulo retângulo", "c) A soma dos lados de um triângulo é igual a 180°", "d) A soma das áreas dos quadrados dos catetos é igual à área do quadrado da hipotenusa"],
    "Quem foi o presidente do Brasil durante a Proclamação da República em 1889?": ["a) Floriano Peixoto", "b) Deodoro da Fonseca", "c) Prudente de Morais", "d) Marechal Hermes da Fonseca"],
    "O que representou o movimento Tenentista na década de 1920?": ["a) Contestação militar ao governo", "b) Movimento sindicalista", "c) Revolta da Vacina", "d) Greve dos Canudos"],
    "Qual foi o objetivo da política de industrialização implementada durante o governo de Juscelino Kubitschek?": ["a) Desenvolvimento da indústria nacional", "b) Aumento das exportações agrícolas", "c) Combate à inflação", "d) Implementação do socialismo"],
    "Em qual alternativa a palavra está escrita corretamente?": ["a) excesivo", "b) excessivo", "c) ecessivo", "d) exsessivo"],
    "Qual é o plural correto de papel?": ["a) papéis", "b) papelões", "c) papelãos", "d) papélis"],
    "O que é um sinônimo para a palavra alegre?": ["a) triste", "b) feliz", "c) sério", "d) cansado"],
    "O que é a lei da inércia e como ela se aplica aos objetos em movimento?": ["a) A lei da inércia afirma que objetos em movimento permanecem em movimento, enquanto objetos em repouso permanecem em repouso.", "b) A lei da inércia afirma que a velocidade de um objeto é constante.", "c) A lei da inércia afirma que a força é diretamente proporcional à aceleração.", "d) A lei da inércia não se aplica a objetos em movimento."],
    "Explique a diferença entre velocidade e aceleração.": ["a) Velocidade é a taxa de mudança de posição, enquanto aceleração é a taxa de mudança de velocidade.", "b) Velocidade é a taxa de mudança de velocidade, enquanto aceleração é a taxa de mudança de posição.", "c) Velocidade e aceleração são conceitos idênticos.", "d) Velocidade e aceleração são ambos relacionados à posição de um objeto."],
    "Como a energia térmica se propaga e é transferida entre corpos?": ["a) A energia térmica se propaga apenas através de ondas sonoras.", "b) A energia térmica se propaga por condução, convecção e radiação.", "c) A energia térmica é transferida apenas por convecção.", "d) A energia térmica não pode ser transferida entre corpos."],
    "Qual país sediará os Jogos Olímpicos de Verão de 2028?": ["a) França", "b) Austrália", "c) Estados Unidos", "d) Canadá"],
    "Qual é o recorde de mais gols marcados em uma única edição da Copa do Mundo de Futebol Masculino?": ["a) 10 gols", "b) 13 gols", "c) 16 gols", "d) 18 gols"],
    "Em que ano o Brasil sediou os Jogos Olímpicos pela primeira vez?": ["a) 1956", "b) 1964", "c) 2016", "d) 1980"],
    }
}

respostas = {
    #ciencias
    "Qual é a função das mitocôndrias em uma célula?": "c",
    "Como ocorre a reprodução assexuada em organismos unicelulares?": "a",
    "Qual é a diferença entre mitose e meiose?": "a",
    "O que é a teoria celular e quais são seus princípios fundamentais?": "b",
    "Como as plantas realizam a troca gasosa durante a fotossíntese?": "c",
    "O que são ácidos e bases e como eles se relacionam com o pH?": "c",
    "Qual é a diferença entre uma reação endotérmica e exotérmica?": "b",
    "O que é a tabela periódica e como os elementos estão organizados nela?": "b",
    "Explique a lei da conservação da massa em reações químicas.": "c",
    "Como funcionam as ligações iônicas e covalentes entre átomos?": "b",
    "O que é a lei da inércia e como ela se aplica aos objetos em movimento?": "a",
    "Explique a diferença entre velocidade e aceleração.": "a",
    "Como a energia térmica se propaga e é transferida entre corpos?": "b",
    "O que são ondas eletromagnéticas e qual é sua importância na física?": "c",
    "Como a lei da gravidade de Newton descreve a atração entre dois corpos massivos?": "a",
    #esportes
    "Qual país sediou a Copa do Mundo de Futebol Masculino em 2014?": "b",
    "Qual piloto de Fórmula 1 é conhecido como 'Honey Badger'?": "c",
    "Quantas vezes a seleção brasileira de futebol masculino ganhou a medalha de ouro nas Olimpíadas até 2022?": "b",
    "Quem é o maior artilheiro da seleção argentina de futebol?": "b",
    "Qual é o esporte principal dos Jogos Paralímpicos de Verão?": "a",
    "Quem é o único piloto a conquistar o título mundial de Fórmula 1 com uma equipe italiana desde a década de 1950?": "c",
    "Qual é o tempo de acréscimo padrão em uma partida de futebol?": "c",
    "Quem é conhecido como 'The Special One' no mundo do futebol?": "b",
    "Em que esporte a brasileira Marta é uma lenda, sendo eleita seis vezes como a melhor jogadora do mundo?": "b",
    "Qual é a distância total percorrida por uma maratona olímpica?": "a",
    "Quem é o maior vencedor da história da Fórmula 1, com sete títulos mundiais?": "b",
    "Qual país sediará os Jogos Olímpicos de Verão de 2028?": "c",
    "Qual é o recorde de mais gols marcados em uma única edição da Copa do Mundo de Futebol Masculino?": "c",
    "Quem é o técnico da seleção alemã de futebol masculino em 2023?": "c",
    "Em que ano o Brasil sediou os Jogos Olímpicos pela primeira vez?": "c",
    "Quem é considerado o 'Pistoleiro' e é um dos principais atacantes da seleção uruguaia?": "b",
    "Qual é a única seleção africana a vencer a Copa do Mundo de Futebol Masculino?": "c",
    "Qual é a nacionalidade do piloto de Fórmula 1 Max Verstappen?": "a",
    "Quem é o atual campeão olímpico dos 100 metros rasos masculino?": "c",
    "Qual é o nome do troféu concedido ao vencedor da Fórmula 1 ao final de cada temporada?": "c",
    "Qual país sediou a Copa do Mundo de Futebol Masculino em 2014?": "b",
    "Qual piloto de Fórmula 1 é conhecido como 'Honey Badger'?": "c",
    "Quantas vezes a seleção brasileira de futebol masculino ganhou a medalha de ouro nas Olimpíadas até 2022?": "b",
    "Quem é o maior artilheiro da seleção argentina de futebol?": "b",
    "Qual é o esporte principal dos Jogos Paralímpicos de Verão?": "a",
    #Historia
    "Quem foi o responsável pelo Descobrimento do Brasil em 1500?": "a",
    "Qual foi o período em que o Brasil foi uma colônia de Portugal?": "a",
    "Em que ano foi proclamada a Independência do Brasil?": "a",
    "Quem foi o primeiro imperador do Brasil?": "c",
    "O que foi a Guerra do Paraguai (1864-1870)?": "a",
    "Quem foi o líder da Revolta dos Malês em 1835?": "d",
    "Qual movimento contestou o governo de Getúlio Vargas na década de 1930?": "a",
    "O que foi o AI-5 durante o regime militar (1964-1985)?": "a",
    "Quem foi o presidente do Brasil durante a Proclamação da República em 1889?": "b",
    "O que representou o movimento Tenentista na década de 1920?": "a",
    "Qual foi o objetivo da política de industrialização implementada durante o governo de Juscelino Kubitschek?": "a",
    "Quem foi o líder da Revolta da Armada em 1893?": "c",
    "Qual foi o nome do plano econômico que marcou o governo de Fernando Collor em 1990?": "c",
    "O que foi o movimento operário conhecido como 'Canudos'?": "b",
    "Quem foi o líder quilombola que resistiu ao sistema escravista no Brasil colonial?": "a",
    #Portugues 
    "Qual é a sílaba tônica da palavra 'cachorro'?": "b",
    "Em qual alternativa a palavra está escrita corretamente?": "b",
    "Qual é o plural correto de 'papel'?": "a",
    "O que é um sinônimo para a palavra 'alegre'?": "b",
    "Qual é a classe gramatical da palavra 'correr'?": "b",
    "Qual é o antônimo de 'ampliar'?": "b",
    "Em qual alternativa a palavra é um pronome pessoal?": "b",
    "Qual é a conjugação correta do verbo 'ler' na terceira pessoa do singular do presente do indicativo?": "b",
    "O que é um ditongo?": "a",
    "Qual é a forma correta de completar a frase: 'Ele ___ muito bem na prova.'": "d",
    "Em qual alternativa a palavra está grafada corretamente?": "b",
    "Qual é o plural de 'cidadão'?": "a",
    "Qual é o sujeito da frase: 'O pássaro canta na janela.'?": "a",
    "O que é um adjetivo?": "c",
    "Qual é a conjugação correta do verbo 'ter' na primeira pessoa do singular do pretérito perfeito do indicativo?": "a",
    #Matematica
    "O que é um número primo?": "c",
    "O que é um polinômio?": "b",
    "Qual é a fórmula da área de um triângulo?": "c",
    "O que são números irracionais?": "a",
    "O que é uma equação linear?": "d",
    "Qual é a propriedade distributiva?": "a",
    "O que é a média aritmética?": "a",
    "O que é uma fração equivalente?": "c",
    "O que é o Teorema de Pitágoras?": "b",
    "O que é um múltiplo comum?": "b",
    "Qual é a propriedade comutativa da adição?": "a",
    "O que é uma razão?": "a",
    "O que é uma progressão aritmética?": "a",
    "Qual é a definição de mediana em um conjunto de dados?": "c",
    "O que é uma circunferência?": "c",

}


pontuacao = 0
pergunta_atual = 0
perguntas_selecionadas = []
tempo_por_pergunta = 10  # Defina o tempo limite para cada pergunta em segundos
tempo_restante = tempo_por_pergunta  
timer = None
fullscreen = False 
modo_selecionado = ""  

def iniciar_timer():
    global timer, tempo_restante
    timer = threading.Timer(1, atualizar_tempo)
    timer.start()

def atualizar_tempo():
    global timer, tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        visor_tempo.config(text=f"Tempo restante: {tempo_restante} s")
        iniciar_timer()
    else:
        tempo_expirado()

def tempo_expirado():
    proxima_pergunta()

def mostrar_botao_opcoes():
    for botao in opcoes_botao:
        botao.pack(pady=(20 if fullscreen else 10))  
        visor_tempo.pack(pady=(20 if fullscreen else 10))  
        botao_reiniciar.pack(pady=(20 if fullscreen else 10))  
        botao_reiniciar.pack_forget()

def iniciar_jogo(modo):
    global pontuacao, pergunta_atual, tempo_restante, perguntas_selecionadas, modo_selecionado
    modo_selecionado = modo
    if modo_selecionado:
        pontuacao = 0
        pergunta_atual = 0
        tempo_restante = tempo_por_pergunta
        perguntas_selecionadas = random.sample(list(perguntas[modo_selecionado].keys()), len(perguntas[modo_selecionado]))
        
        
        menu_label.config(text=modo_selecionado.capitalize())

        for botao in botoes_modo:
            botao.pack_forget()  
        for botao in opcoes_botao:
            botao.pack()  
        proxima_pergunta()
        mostrar_botao_opcoes()  
        
def reiniciar_jogo():
    iniciar_jogo(modo_selecionado)
    resultado_label.config(text="")
    botao_reiniciar.pack_forget()  

def proxima_pergunta():
    global pergunta_atual, timer, tempo_restante, perguntas_selecionadas
    if timer:
        timer.cancel()  

    if pergunta_atual < len(perguntas_selecionadas):
        pergunta = perguntas_selecionadas[pergunta_atual]
        opcoes = perguntas[modo_selecionado][pergunta]
        pergunta_label.config(text=pergunta, fg='white', bg='navy', font=('Helvetica', 18 if fullscreen else 16))
        for i, opcao in enumerate(opcoes):
            opcoes_botao[i].config(text=opcao, command=lambda i=i: verificar_resposta(i), fg='black', bg='yellow', font=('Helvetica', 16 if fullscreen else 14), height=2, width=30 if fullscreen else 20)
        
        tempo_restante = tempo_por_pergunta
        visor_tempo.config(text=f"Tempo restante: {tempo_restante} s", fg='white', bg='navy', font=('Helvetica', 14 if fullscreen else 12))
        janela.title(f"PERGUNTATRIX - JOGO DE PERGUNTAS E RESPOSTAS")
        iniciar_timer()
        pergunta_atual += 1
    else:
        resultado_label.config(text=f"Sua pontuação final é: {pontuacao}/{len(perguntas_selecionadas)}", fg='white', bg='navy', font=('Helvetica', 16 if fullscreen else 14))
        botao_reiniciar.pack()  # Mostra o botão de reiniciar

def verificar_resposta(escolha):
    global pontuacao
    resposta_correta = respostas[perguntas_selecionadas[pergunta_atual - 1]]
    if escolha == ord(resposta_correta) - ord('a'):
        pontuacao += 1
    proxima_pergunta()

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    janela.attributes("-fullscreen", fullscreen)
    update_ui()

def update_ui():
    global fullscreen
    menu_label.config(font=('Helvetica', 18 if fullscreen else 16))
    botao_inicio.config(font=('Helvetica', 14 if fullscreen else 12), height=2, width=20)
    pergunta_label.config(font=('Helvetica', 18 if fullscreen else 16))
    for botao in opcoes_botao:
        botao.config(font=('Helvetica', 16 if fullscreen else 14), height=2, width=30 if fullscreen else 20)
    resultado_label.config(font=('Helvetica', 16 if fullscreen else 14))
    visor_tempo.config(font=('Helvetica', 14 if fullscreen else 12))


janela = tk.Tk()
janela.title("PERGUNTATRIX - JOGO DE PERGUNTAS E RESPOSTAS")


janela.configure(bg='navy')  


menu_label = tk.Label(janela, text="Escolha o Modo:", fg='white', bg='navy', font=('Helvetica', 18))
menu_label.pack(pady=20)


botoes_modo = []
for modo in perguntas.keys():
    botao_modo = tk.Button(janela, text=modo, command=lambda modo=modo: iniciar_jogo(modo), fg='black', bg='yellow', font=('Helvetica', 14))
    botao_modo.pack(pady=10)
    botoes_modo.append(botao_modo)


botao_reiniciar = tk.Button(janela, text="Reiniciar Jogo", command=reiniciar_jogo, fg='black', bg='yellow')
botao_reiniciar.pack()
botao_reiniciar.pack_forget()  


pergunta_label = tk.Label(janela, text="", fg='white', bg='navy')
pergunta_label.pack(pady=10)

opcoes_botao = []
for _ in range(4):
    botao = tk.Button(janela, text="", fg='black', bg='yellow')
    botao.pack_forget()  
    opcoes_botao.append(botao)

resultado_label = tk.Label(janela, text="", fg='white', bg='navy')
resultado_label.pack(pady=10)

visor_tempo = tk.Label(janela, text="", fg='white', bg='navy')
visor_tempo.pack(pady=10)

janela.mainloop()

# Perguntatix
