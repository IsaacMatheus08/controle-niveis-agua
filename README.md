# 🚰 Controle de Níveis de Água

Programa desenvolvido em Python para monitorar e exibir alertas sobre o nível de água de um reservatório, utilizando cores no terminal para destacar cada situação.

---

## 📋 Descrição

O sistema simula o monitoramento de um reservatório com **5 níveis de água**, do mais baixo ao mais alto. Cada nível possui uma mensagem de alerta e uma cor correspondente, exibidas no terminal com o auxílio da biblioteca **colorama**.

---

## ⚙️ Funcionalidades

- Lista com os 5 níveis do reservatório
- Função responsável por definir a cor conforme o nível informado
- Exibição da situação atual do reservatório com a cor correspondente
- Restauração do estilo padrão do terminal após a exibição

---

## 🎨 Níveis e cores

| Nível | Situação | Cor |
|-------|----------|-----|
| Nível 1 | Muito baixo (crítico) | 🔴 Vermelho |
| Nível 2 | Baixo | 🟡 Amarelo |
| Nível 3 | Médio | 🟢 Verde |
| Nível 4 | Alto | 🩵 Ciano |
| Nível 5 | Muito alto (alerta) | 🔵 Azul |

---

## 🖥️ Como executar

1. Certifique-se de ter o **Python 3** instalado
2. Clone o repositório:
   ```
   git clone https://github.com/IsaacMatheus08/controle-niveis-agua.git
   ```
3. Acesse a pasta do projeto:
   ```
   cd controle-niveis-agua
   ```
4. Instale a biblioteca colorama:
   ```
   pip install colorama
   ```
5. Execute o programa:
   ```
   python app.py
   ```

---

## 💬 Exemplo de saída

```
Nível 3 - Médio
```
> Exibido em verde no terminal, representando o nível atual do reservatório.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- [colorama](https://pypi.org/project/colorama/)

---

## 👤 Autor

Feito por **Isaac Matheus** — Atividade prática do curso **Técnico em Desenvolvimento de Sistemas**.
