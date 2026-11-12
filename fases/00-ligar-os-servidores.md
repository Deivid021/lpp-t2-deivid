# 🍕 Fase 0 — Ligar os servidores

> **Missão:** deixar o ambiente pronto, descobrir o seu universo e fazer o primeiro teste ficar verde.
> **Recompensa:** 5 XP · distintivo 🔌 *Servidor no ar*

## O que você vai aprender

- Preparar o ambiente de trabalho (Windows + VS Code) e o fluxo com GitHub.
- Entender como o seu universo é gerado a partir da sua matrícula.
- Rodar os testes e ler o placar do trabalho.

## Passo 1 — Crie o seu repositório

1. Na página do repositório do Trabalho 02 (`juniorbsn-ui/lpp-t2`), clique em **Use this template → Create a new repository**.
2. Deixe-o **privado** e compartilhe com o professor (Settings → Collaborators).
3. Clone no seu computador e abra a pasta no **VS Code** (menu *Terminal → New Terminal* abre o terminal já na pasta certa).

## Passo 2 — Confira as ferramentas

Instale o **Python 3.10 ou superior** em python.org (no Windows, marque **Add python.exe to PATH**). No terminal:

```bash
python --version
```

> Linux/Mac: use `python3` no lugar de `python`.

## Passo 3 — Descubra o seu universo

```bash
python iniciar.py
```

Digite a sua matrícula quando pedir. O comando cria, só para você:

- `contexto/` — a história e os dados da **BitFood** (leia o `CONTEXTO.md`);
- `fases/` — os roteiros de cada fase (como este);
- `src/` — os arquivos **onde você vai programar**;
- `testes/` — os testes que dizem se você acertou.

## Passo 4 — Faça o primeiro teste ficar verde

Abra `src/fase0.py` e implemente `boas_vindas`: ela recebe o nome da marca e devolve exatamente `Servidores da <marca> no ar!`.

```python
def boas_vindas(marca):
    return f"Servidores da {marca} no ar!"
```

## Passo 5 — Rode o placar

```bash
python placar.py
```

Você verá o placar com as fases, o seu XP e o que falhou. Fases só destravam quando a anterior está verde.

## Passo 6 — Envie para o GitHub

```bash
git add .
git commit -m "Fase 0: servidores no ar"
git push
```

Faça um commit ao concluir cada fase: o histórico de commits conta a história do seu trabalho.

## Para saber mais

- Regras do jogo: o trabalho é **individual**. Os seus dados e os nomes das suas funções são exclusivos da sua matrícula.
- Se o teste disser que a matrícula não consta na turma, confira o número em `t2.config.json`.

## O que aprendemos

- Como preparar o ambiente e o fluxo `commit` → `push`.
- Que cada aluno tem um universo próprio, gerado de forma determinística pela matrícula.
- Como rodar os testes e ler o placar.
