
# Contribuindo para o Projeto

Obrigado por seu interesse em contribuir para o projeto! Abaixo você encontrará um guia rápido sobre como começar e quais são as diretrizes para contribuições, incluindo o processo de contribuição e os padrões de commit.

## Como Contribuir

### 1. Faça um Fork do Repositório

Primeiro, faça um fork do repositório para sua conta pessoal no GitHub. Isso permite que você trabalhe nas suas próprias alterações sem afetar o código principal do projeto.

- Vá até o repositório principal e clique no botão `Fork` no canto superior direito.
- Clone o fork para o seu ambiente local:

  ```bash
  git clone https://github.com/seu-usuario/seu-fork.git
  cd nome-do-projeto
  ```

### 2. Crie uma Branch para sua Contribuição

Sempre crie uma nova branch para sua contribuição. Isso ajuda a manter o histórico de commits organizado e facilita a revisão do código. Nomeie a branch de maneira descritiva de acordo com a funcionalidade ou correção que você está implementando.

```bash
git checkout -b feat-nome-da-feature
```

### 3. Faça Suas Alterações

Implemente suas alterações no projeto. Garanta que você está seguindo os padrões de estilo e que o código está limpo e legível. Também é importante testar suas alterações localmente antes de enviar.

### 4. Realize Commits Claros e Objetivos

Realize commits frequentes e sempre escreva mensagens de commit claras e descritivas. Para manter a consistência no repositório, siga o padrão de commits descrito abaixo.

### 5. Teste Suas Alterações

Certifique-se de que suas alterações não quebram nada e, de preferência, escreva testes para validar sua implementação (se aplicável).

### 6. Envie um Pull Request (PR)

Depois de concluir suas alterações e testar o código, envie um Pull Request (PR) para o repositório original. No PR, explique claramente quais problemas a contribuição resolve e qualquer outro detalhe relevante.

```bash
git push origin feat-nome-da-feature
```

No GitHub, vá até a página do seu fork e clique em `New Pull Request`. 

---

## Diretrizes de Commit

Estamos utilizando o [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) como padrão para mensagens de commit. Esse padrão ajuda a manter o histórico de commits organizado e claro. Aqui estão os principais tipos de commits aceitos:

### Estrutura de uma Mensagem de Commit

```
<tipo>(escopo opcional): descrição breve
```

Exemplo:

```
feat(form): adiciona funcionalidade de consulta de pets
```

### Tipos de Commit Aceitos

- **feat**: Introdução de uma nova funcionalidade.
  - Exemplo: `feat(form): adiciona campo de idade`
  
- **fix**: Correção de bugs.
  - Exemplo: `fix(css): corrige espaçamento entre inputs`
  
- **docs**: Alterações na documentação.
  - Exemplo: `docs(README): adiciona instruções de instalação`
  
- **style**: Alterações que não afetam a lógica do código (ex.: formatação, correções de estilo).
  - Exemplo: `style(form): aplica estilo aos botões`
  
- **refactor**: Refatoração de código sem adicionar novas funcionalidades ou corrigir bugs.
  - Exemplo: `refactor(js): simplifica a função de cadastro`
  
- **test**: Adição ou modificação de testes.
  - Exemplo: `test(api): adiciona teste para rota de consulta`
  
- **chore**: Alterações de tarefas de build, ferramentas ou dependências.
  - Exemplo: `chore: atualiza dependências do projeto`

### Regras para o Escopo
O escopo é opcional, mas pode ser adicionado para detalhar melhor a área afetada. Exemplos de escopos incluem:
- **form**: se estiver alterando algo relacionado ao formulário.
- **css**: se a mudança for relacionada ao CSS.
- **backend**: se a mudança for no código do Flask.

---

## Estilo de Código

Por favor, siga o padrão de estilo do código utilizado no projeto. Utilize ferramentas como o **Flake8** (para Python) para verificar o código antes de realizar um commit.

### Linter (Python)

Você pode rodar um linter para verificar se o código está de acordo com as diretrizes de estilo:

```bash
flake8 app.py
```

---

## Reportando Bugs e Sugerindo Funcionalidades

Se você encontrou um bug ou tem uma sugestão de funcionalidade, abra uma [issue](https://github.com/seu-usuario/seu-repositorio/issues) antes de começar a trabalhar. Isso garante que todos estejam alinhados sobre o que precisa ser feito.

---

Se tiver dúvidas, entre em contato com os mantenedores do projeto. Estamos ansiosos para ver suas contribuições!
