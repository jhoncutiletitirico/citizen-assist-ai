# Citizen Assist AI – Orientação para pessoas idosas (60+)

Global Solution 2026.2 – CitizenTech | Pensamento Computacional e Automação com Python | 1CC

> ⚠️ Este assistente **não é um canal oficial**. Ele apenas resume informações públicas e indica a fonte oficial. Não pede nem guarda dados pessoais.

## Integrantes
| Nome | RM |
|---|---|
| Jhon Cutile Titirico | 571976 |

## Público e problema
**Público:** pessoas idosas (60 anos ou mais) e seus familiares/cuidadores.
**Problema:** direitos como ônibus gratuito, remédio de graça, BPC, Carteira da Pessoa Idosa e Tarifa Social de Energia estão espalhados em vários sites, com linguagem técnica e sujeitos a golpes ("ligação do INSS pedindo dados"). O assistente reúne essas orientações em linguagem simples, mostrando **o que levar, onde ir e a fonte oficial**.

## ODS relacionados
- **ODS 1** – Erradicação da pobreza (acesso a BPC, CadÚnico, Tarifa Social)
- **ODS 3** – Saúde e bem-estar (Cartão SUS, vacinação, Farmácia Popular)
- **ODS 10** – Redução das desigualdades (direitos da pessoa idosa)
- **ODS 11** – Cidades e comunidades sustentáveis (transporte gratuito)

## Como executar
Requer apenas Python 3.10+ (sem bibliotecas externas). Dentro da pasta `citizen-assist-ai`:
```bash
python main.py
```

## Estrutura
```
citizen-assist-ai/
├── main.py                 # menu principal
├── orientacao.py           # classe Orientacao
├── base_conhecimento.py    # classe BaseConhecimento + normalizar() e pontuar()
├── assistente.py           # classe Assistente (atendimento, histórico, indicadores, CSV)
├── testes/teste_simulado.py  # teste de uso simulado (4 perfis, 11 atendimentos)
└── data/
    ├── base_conhecimento.json   # 12 orientações, 4 categorias
    ├── historico.json           # atendimentos registrados
    └── atendimentos.csv         # exportação (csv.DictWriter)
```

### Classes (composição)
```
Assistente (nome, base, historico)
 └── base: BaseConhecimento (caminho, orientacoes)
       └── orientacoes: [Orientacao, Orientacao, ...]
```
| Classe | Métodos principais |
|---|---|
| `Orientacao` | `exibir()` |
| `BaseConhecimento` | `carregar()`, `categorias()`, `por_categoria()`, `pontuar()`, `buscar()` |
| `Assistente` | `perguntar()`, `navegar()`, `registrar()`, `indicadores()`, `exportar_csv()`, `pedir_nota()` |

**Dicionários:** cada registro do JSON, cada atendimento do histórico, a tabela `ACENTOS`.
**Tuplas:** `buscar()` devolve uma lista de tuplas `(pontos, orientacao)`; `categorias()` devolve uma tupla; `CAMPOS` (campos obrigatórios do JSON) é uma tupla.

## Regra de pontuação
1. Pergunta, palavras-chave e título são **normalizados** (minúsculas, sem acentos, sem pontuação).
2. **+3** para cada palavra-chave da orientação que aparece na pergunta.
3. **+1** para cada palavra da pergunta com 4+ letras que aparece no título.
4. **≥ 6 pontos → ALTA**, **3 a 5 → MÉDIA**, **< 3 → "Não encontrei"** (sugere categorias).
5. Mostra a melhor orientação e até 2 alternativas com 3+ pontos (no empate fica a ordem do JSON).

Exemplo: *"Como faço o cartão do SUS?"* → +3 (`cartao do sus`) +3 (`sus`) +1 (`cartao` no título) = **7 pontos, ALTA**.

Ajuste feito: além de `?!.,;:()`, também removemos `/ - " '` na normalização.

## Regras de atendimento implementadas
- Navegação por categorias numeradas com **0 para voltar** em todas as telas.
- Entradas inválidas (letras, vazio, fora da faixa, s/n inválido) **nunca encerram** o programa.
- Pergunta com **8+ dígitos ou "@"** é recusada e **não é registrada**.
- Toda resposta mostra **fonte, data de verificação e aviso** de canal não oficial.
- JSON ausente/corrompido não trava o programa.

## Integração com outras disciplinas
- **Energias Renováveis (SERS):** a orientação 9 (Tarifa Social de Energia) foi a base do simulador de energia, que está em outro repositório (`citizen-assist-energia`).
- **Arquitetura de Computadores:** a orientação 12 (atendimento prioritário) tem o mesmo tema da fila virtual feita no ESP32 (Wokwi). Os dois projetos não trocam dados; a ligação é só de tema.

A busca por pontuação continua sendo a parte avaliada nesta disciplina.

## Fontes consultadas
| Orientação | Fonte |
|---|---|
| Cartão SUS | https://www.gov.br/saude/pt-br/composicao/seidigi/meususdigital |
| Farmácia Popular | https://www.gov.br/saude/pt-br/assuntos/noticias/2025/fevereiro/ministerio-da-saude-anuncia-100-de-gratuidade-no-farmacia-popular-e-abre-credenciamento-a-todos-os-municipios-do-pais |
| Vacina da gripe | https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/g/gripe-influenza |
| Ônibus gratuito, estacionamento, prioridade | Estatuto da Pessoa Idosa – https://www.planalto.gov.br/ccivil_03/leis/2003/l10.741.htm |
| Carteira da Pessoa Idosa | https://www.gov.br/pt-br/servicos/adquirir-carteira-do-idoso |
| BPC | https://www.gov.br/inss/pt-br/direitos-e-deveres/beneficios-assistenciais/beneficio-assistencial-a-pessoa-idosa-bpc-loas |
| Cadastro Único | https://www.gov.br/mds/pt-br/acoes-e-programas/cadastro-unico |
| Tarifa Social (Luz do Povo) | https://www.gov.br/mme/pt-br/a-revolucao-brasileira-em-energia-e-mineracao/combate-a-pobreza-energetica-e-inclusao-social/luz-do-povo |
| Prova de vida | https://www.gov.br/inss/pt-br/assuntos/prova-de-vida |
| Disque 100 | https://www.gov.br/mdh/pt-br/ondh |

## Resultado do teste com usuários
> **Atenção: este teste foi SIMULADO.** Não consegui testar com pessoas de fora no prazo. Simulei 4 perfis de usuário (senhora de 72 anos, filha cuidadora, senhor de 66 anos e neto ajudando o avô). Cada perfil é uma sequência de perguntas e respostas digitada automaticamente no `main.py` de verdade, pelo script `testes/teste_simulado.py`. O programa rodou normalmente e gravou o `historico.json` e o `atendimentos.csv`. As notas de facilidade também fazem parte da simulação, então não medem a opinião de uma pessoa real.

| Indicador | Valor |
|---|---|
| Perfis simulados | 4 |
| Atendimentos | 11 |
| Resposta encontrada (%) | 81,8% |
| Taxa de acerto – ajudou (%) | 72,7% |
| Tempo médio para encontrar (s) | 0,0 (as teclas foram digitadas pelo script, então não mede o tempo de uma pessoa) |
| Tentativas por atendimento | 1,00 |
| Facilidade de uso (1 a 5) | 4,25 (simulada) |

O teste também passou por uma opção inválida no menu (`abc`) e por uma pergunta com CPF. O programa pediu de novo e não registrou a pergunta com CPF.

**Dúvidas sem solução:**
- "sou aposentado preciso ir ao banco?" (não encontrou)
- "recebi ligação pedindo senha do banco" (não encontrou)
- "vaga de estacionamento pra idoso" (encontrou a orientação 6, mas o perfil respondeu que não ajudou)

**Melhoria feita a partir do teste:** acrescentei as palavras-chave `ligacao` e `senha do banco` na orientação 11 (golpes e violência contra a pessoa idosa). Antes, "recebi ligação pedindo senha do banco" não encontrava nada; agora encontra a orientação 11 com 6 pontos (confiança ALTA). A dúvida do "aposentado" eu deixei para mostrar a alteração ao vivo no vídeo.

## Limitações
- Busca por palavras: não entende sinônimos que não estejam nas palavras-chave nem erros de digitação.
- Regras locais (ex.: ônibus grátis de 60 a 64 anos) variam por cidade; o assistente só dá a regra nacional.
- As informações podem mudar: sempre confirme na fonte oficial.

## Vídeo técnico
<link do YouTube (não listado), 5 a 8 minutos>
